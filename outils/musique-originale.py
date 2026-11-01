"""Original royalty-free track for Aken videos: modern, upbeat, 112 BPM, A minor.
Pure numpy synthesis, no samples, no third-party audio. Output: 44.1 kHz stereo WAV."""
import sys
import wave
import numpy as np

RATE = 44100
BPM = 112
BEAT = 60 / BPM
BAR = 4 * BEAT
BARS = int(sys.argv[2]) if len(sys.argv) > 2 else 12
LENGTH = int(BARS * BAR * RATE) + RATE
rng = np.random.default_rng(7)

left = np.zeros(LENGTH)
right = np.zeros(LENGTH)
kick_env = np.zeros(LENGTH)  # used for sidechain ducking


def midi(note):
    return 440.0 * 2 ** ((note - 69) / 12)


def place(signal, start_s, pan=0.0, gain=1.0):
    start = int(start_s * RATE)
    end = min(LENGTH, start + len(signal))
    chunk = signal[: end - start] * gain
    left[start:end] += chunk * (1 - max(pan, 0))
    right[start:end] += chunk * (1 + min(pan, 0))


def envelope(length_s, attack=0.005, decay=0.2):
    n = int(length_s * RATE)
    t = np.arange(n) / RATE
    env = np.minimum(1, t / attack) * np.exp(-t / decay)
    return env


def saw(freq, length_s, detunes=(0,)):
    t = np.arange(int(length_s * RATE)) / RATE
    out = np.zeros_like(t)
    for cents in detunes:
        f = freq * 2 ** (cents / 1200)
        phase = rng.random()
        out += 2 * ((t * f + phase) % 1) - 1
    return out / len(detunes)


def lowpass(signal, width):
    kernel = np.ones(width) / width
    return np.convolve(signal, kernel, mode="same")


def kick(start_s):
    n = int(0.45 * RATE)
    t = np.arange(n) / RATE
    freq = 45 + 95 * np.exp(-t * 28)
    phase = 2 * np.pi * np.cumsum(freq) / RATE
    body = np.sin(phase) * np.exp(-t * 7)
    click = rng.standard_normal(n) * np.exp(-t * 400) * 0.25
    place(body + click, start_s, gain=1.0)
    s = int(start_s * RATE)
    e = min(LENGTH, s + int(0.35 * RATE))
    kick_env[s:e] = np.maximum(kick_env[s:e], np.exp(-np.arange(e - s) / RATE * 9))


def clap(start_s):
    n = int(0.25 * RATE)
    t = np.arange(n) / RATE
    noise = rng.standard_normal(n)
    noise = np.diff(noise, prepend=0)  # crude high-pass
    env = np.exp(-t * 22) + 0.6 * np.exp(-np.maximum(t - 0.012, 0) * 30) * (t > 0.012)
    place(lowpass(noise, 3) * env * 0.14, start_s, pan=0.1)


def hat(start_s, gain):
    n = int(0.06 * RATE)
    t = np.arange(n) / RATE
    noise = np.diff(np.diff(rng.standard_normal(n), prepend=0), prepend=0)
    place(noise * np.exp(-t * 120) * 0.035 * gain, start_s, pan=-0.3)


def riser(start_s, length_s):
    n = int(length_s * RATE)
    t = np.linspace(0, 1, n)
    noise = np.diff(rng.standard_normal(n), prepend=0)
    place(lowpass(noise, 4) * t ** 3 * 0.06, start_s)


# A minor progression: Am - F - C - G (roots and triads)
progression = [(57, [69, 72, 76]), (53, [65, 69, 72]), (48, [64, 67, 72]), (55, [67, 71, 74])]
pentatonic = [69, 72, 74, 76, 79, 81]
arp_pattern = [0, 2, 4, 3, 5, 4, 2, 3]

for bar in range(BARS):
    start = bar * BAR
    root, chord = progression[bar % 4]
    intro = bar < 2
    outro = bar == BARS - 1

    # Warm sustained pad under everything
    pad = sum(saw(midi(note - 12), BAR, detunes=(-9, 0, 8)) for note in chord) / 3
    pad_env = np.minimum(1, np.arange(len(pad)) / (0.25 * RATE)) * np.minimum(1, (len(pad) - np.arange(len(pad))) / (0.3 * RATE))
    place(lowpass(pad, 24) * pad_env, start, gain=0.2)

    # Chord stabs: syncopated (on 1, the "and" of 2, and 4)
    for beat_pos in (0, 1.5, 3):
        length = BEAT * 0.9
        stab = sum(saw(midi(note), length, detunes=(-12, 0, 11)) for note in chord) / 3
        stab = lowpass(stab, 6 if intro else 3) * envelope(length, 0.004, 0.18)
        place(stab, start + beat_pos * BEAT, pan=0.25 if beat_pos == 1.5 else -0.15, gain=0.42)

    if not intro:
        # Four-on-the-floor kick, claps on 2 and 4, eighth-note hats
        for beat in range(4):
            kick(start + beat * BEAT)
        for beat in (1, 3):
            clap(start + beat * BEAT)
        for eighth in range(8):
            hat(start + eighth * BEAT / 2, 1.0 if eighth % 2 else 0.5)

        # Off-beat bass on eighths
        for eighth in range(8):
            if eighth % 2 == 1 or eighth == 0:
                length = BEAT / 2 * 0.85
                note = root - 12 + (12 if eighth == 7 else 0)
                bass = saw(midi(note), length, detunes=(-5, 5))
                bass = lowpass(bass, 18) * envelope(length, 0.003, 0.12)
                place(bass, start + eighth * BEAT / 2, gain=0.62)

    # Pluck arpeggio from bar 5 for energy
    if bar >= 4 and not outro:
        for step, index in enumerate(arp_pattern):
            length = BEAT / 2
            note = pentatonic[index]
            t = np.arange(int(length * RATE)) / RATE
            pluck = (np.sign(np.sin(2 * np.pi * midi(note) * t)) * 0.5 + np.sin(2 * np.pi * midi(note) * t)) * np.exp(-t * 14)
            place(lowpass(pluck, 4), start + step * BEAT / 2, pan=0.35 if step % 2 else -0.35, gain=0.2)

# Risers into the drop (bar 3) and into the arpeggio section (bar 5)
riser(2 * BAR - BAR, BAR)
riser(4 * BAR - BAR / 2, BAR / 2)

# Sidechain ducking of everything except the kick feel
duck = 1 - 0.55 * kick_env
left *= duck
right *= duck
# Re-add a clean kick layer by approximating: kick energy already placed before ducking

# Fade in/out, normalise, soft clip
total = int(BARS * BAR * RATE)
fade = np.ones(LENGTH)
fade[: int(0.3 * RATE)] = np.linspace(0, 1, int(0.3 * RATE))
fade[total - int(1.2 * RATE): total] = np.linspace(1, 0, int(1.2 * RATE))
fade[total:] = 0
left *= fade
right *= fade
peak = max(np.abs(left).max(), np.abs(right).max())
left = np.tanh(left / peak * 1.3) * 0.89
right = np.tanh(right / peak * 1.3) * 0.89

stereo = np.stack([left[:total], right[:total]], axis=1)
pcm = (stereo * 32767).astype(np.int16)
with wave.open(sys.argv[1], "wb") as output:
    output.setnchannels(2)
    output.setsampwidth(2)
    output.setframerate(RATE)
    output.writeframes(pcm.tobytes())
print(f"{BARS} bars, {total / RATE:.1f} s")
