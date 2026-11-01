"""Fabrique une vidéo Aken : page animée + sous-titres + voix + musique.
Spécifications dans specs.py ; usage : python3 build.py <nom>"""
import json, os, subprocess, sys
from align import align
HERE = os.path.dirname(os.path.abspath(__file__))
SEM = os.path.join(HERE, "../../brouillons/semaine")
OUT = os.path.join(SEM, "videos"); os.makedirs(OUT, exist_ok=True)
BUILD = os.path.join(HERE, "build"); os.makedirs(BUILD, exist_ok=True)
TAIL = 2.2  # carton de fin

ORBS = """<div class="bg"></div>
<div class="orb" style="width:900px;height:900px;left:-300px;top:200px;background:#FF3D00"></div>
<div class="orb" style="width:800px;height:800px;right:-320px;top:1000px;background:#FFAA00;opacity:.35"></div>"""

END = """<div class="scene" data-start="{s}" data-end="99" style="background:#0A0A0A">
 <div class="orb" style="width:1000px;height:1000px;left:40px;top:500px;background:#FF5A00;opacity:.45"></div>
 <img src="logo.png" style="position:absolute;left:190px;top:620px;width:700px" data-anim="pop" data-at="0">
 <div class="center h" style="top:930px;font-size:58px;white-space:nowrap" data-anim="up" data-at=".25">Devis gratuit sur WhatsApp</div>
 <div class="center" style="top:1050px" data-anim="up" data-at=".4"><span class="pill gbg" style="font-size:54px;padding:22px 44px;color:#0A0A0A;font-family:Montserrat;font-weight:900">+223 93 78 99 16</span></div>
 <div class="center" style="top:1200px;font-size:34px;color:rgba(255,255,255,.7)" data-anim="fade" data-at=".6">Sites · Boutiques en ligne · Applications · Logiciels</div>
</div>"""

def page(conf, body, transparent=False):
    return f"""<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="engine.css"></head>
<body>{'<style>#cap{top:250px;font-size:70px}</style>' if transparent else ''}<div id="stage">{'' if transparent else ORBS}{body}<div id="cap"></div><div id="bar" class="gbg"></div></div>
<script>window.CONF={json.dumps(conf, ensure_ascii=False)};</script><script src="engine.js"></script></body></html>"""

def run(cmd): subprocess.run(cmd, check=True)

def mix(voice, music, dur, out_audio, music_db=-17, voice_delay=0.0):
    run(["ffmpeg", "-y", "-v", "error", "-i", voice, "-stream_loop", "-1", "-i", music, "-filter_complex",
         f"[0:a]adelay={int(voice_delay*1000)}|{int(voice_delay*1000)},apad,atrim=0:{dur},aformat=channel_layouts=stereo,asplit=2[v][sc];"
         f"[1:a]atrim=0:{dur},volume={music_db}dB,afade=t=in:d=0.6,afade=t=out:st={dur-1.2}:d=1.2[m];"
         f"[m][sc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=300[md];"
         f"[v][md]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]",
         "-map", "[a]", "-ar", "48000", "-c:a", "aac", "-b:a", "192k", out_audio])

def make(name, voice, text, music, scenes, avatar=None, music_db=-17, photo=False):
    al = align(voice, text)
    vdur = al["duration"]
    dur = round(vdur + TAIL, 2)
    chunks = al["chunks"]
    def T(i):  # début du sous-titre i
        return chunks[min(i, len(chunks) - 1)]["start"] if i >= 0 else 0
    def W(word):  # début du premier sous-titre contenant ce mot
        for c in chunks:
            if word.lower() in c["text"].lower(): return c["start"]
        raise KeyError(word)
    if isinstance(scenes, list):  # diaporama photo : [(mot, html), ...]
        starts = [0 if i == 0 else W(k) - 0.1 for i, (k, _) in enumerate(scenes)] + [vdur + 0.15]
        body = "".join(f'<div class="scene photo" data-start="{starts[i]:.2f}" data-end="{starts[i+1]:.2f}">{h}</div>' for i, (_, h) in enumerate(scenes))
    else:
        body = scenes(T, vdur)
    body += END.format(s=vdur + 0.15)
    conf = {"duration": dur, "chunks": chunks, "nocap": photo}
    html = os.path.join(HERE, f"_{name}.html")
    open(html, "w").write(page(conf, body, transparent=bool(avatar)))
    audio = os.path.join(BUILD, f"{name}.m4a")
    mix(voice, music, dur, audio, music_db)
    final = os.path.join(OUT, f"{name}.mp4")
    if avatar:
        ov = os.path.join(BUILD, f"{name}_ov.mov")
        run(["node", os.path.join(HERE, "render.js"), html, ov, "30", str(dur), "alpha"])
        run(["ffmpeg", "-y", "-v", "error", "-i", avatar, "-i", ov, "-i", audio, "-filter_complex",
             f"[0:v]fps=30,crop=972:1716:58:170,scale=1080:1907,pad=1080:1920:0:0:0x0e0e0e,tpad=stop_mode=clone:stop_duration={TAIL+1}[av];"
             f"[av][1:v]overlay=0:0:shortest=1,format=yuv420p[v]",
             "-map", "[v]", "-map", "2:a", "-t", str(dur), "-c:v", "libx264", "-preset", "medium", "-crf", "19",
             "-c:a", "copy", "-movflags", "+faststart", final])
    else:
        vid = os.path.join(BUILD, f"{name}_v.mp4")
        run(["node", os.path.join(HERE, "render.js"), html, vid, "30", str(dur)])
        run(["ffmpeg", "-y", "-v", "error", "-i", vid, "-i", audio, "-map", "0:v", "-map", "1:a", "-c:v", "copy",
             "-c:a", "copy", "-shortest", "-movflags", "+faststart", final])
    print(final, dur)
    return final

if __name__ == "__main__":
    import specs
    for n in sys.argv[1:]:
        make(n, **specs.SPECS[n])
