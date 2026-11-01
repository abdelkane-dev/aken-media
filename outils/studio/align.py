"""Découpe un texte en sous-titres et les cale sur les passages parlés d'une voix.
Usage : python3 align.py voix.mp3 "texte" > timings.json"""
import sys, json, re, subprocess

def speech_segments(path, noise="-34dB", gap=0.22):
    out = subprocess.run(["ffmpeg", "-i", path, "-af", f"silencedetect=n={noise}:d={gap}", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                               capture_output=True, text=True).stdout)
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", out)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", out)]
    segs, cur = [], 0.0
    for s, e in zip(starts, ends + [dur] * (len(starts) - len(ends))):
        if s - cur > 0.08: segs.append([cur, s])
        cur = e
    if dur - cur > 0.08: segs.append([cur, dur])
    return segs, dur

def chunks(text, max_words=4):
    text = re.sub(r"\s*[«»]\s*", " ", text).replace(" .", ".").replace(" ,", ",")
    text = re.sub(r"\s+", " ", text)
    parts = re.split(r"(?<=[.!?…:;,])\s+", text.strip())
    res = []
    for p in parts:
        w = p.split()
        k = max(1, -(-len(w) // max_words))
        size = -(-len(w) // k)
        for i in range(0, len(w), size):
            res.append(" ".join(w[i:i + size]))
    return res

def align(path, text):
    segs, dur = speech_segments(path)
    cs = chunks(text)
    total_speech = sum(e - s for s, e in segs)
    weights = [max(len(c), 4) for c in cs]
    W = sum(weights)
    # temps « parlé » cumulé → temps réel
    def real(x):
        acc = 0
        for s, e in segs:
            if acc + (e - s) >= x: return s + (x - acc)
            acc += e - s
        return segs[-1][1]
    out, acc = [], 0
    for c, w in zip(cs, weights):
        a = acc / W * total_speech; acc += w; b = acc / W * total_speech
        out.append({"text": c, "start": round(real(a + 0.01), 3), "end": round(real(b), 3)})
    return {"duration": dur, "chunks": out}

if __name__ == "__main__":
    print(json.dumps(align(sys.argv[1], sys.argv[2]), ensure_ascii=False, indent=1))
