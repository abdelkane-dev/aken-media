"""Aken short with the animated mascot: frames, voice mix, mascot overlay strip."""
import sys, wave, math
import numpy as np
from PIL import Image, ImageFilter, ImageDraw

ROOT = sys.argv[1]
VIS, MAS, VOICE, OUT = f"{ROOT}/visuals", f"{ROOT}/mascotte", f"{ROOT}/voice/gilles", f"{ROOT}/anim"
FPS, TOTAL, W, H = 30, 23.5, 1080, 1920
STRIP_Y, STRIP_H = 1320, 600

# 1. Background frames: blurred cover + slide at 80 % on top
for index in range(1, 5):
    slide = Image.open(f"{VIS}/out/v3-s{index}.png").convert("RGB")
    cover = slide.resize((W, int(slide.height * W / slide.width))).resize((W, H))
    background = cover.filter(ImageFilter.GaussianBlur(45)).point(lambda value: int(value * 0.4))
    small = slide.resize((864, 1080), Image.LANCZOS)
    mask = Image.new("L", small.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, *small.size), 36, fill=255)
    shadow = Image.new("L", (W, H), 0)
    ImageDraw.Draw(shadow).rounded_rectangle((108, 250, 972, 1350), 40, fill=170)
    background.paste((0, 0, 0), (0, 0), shadow.filter(ImageFilter.GaussianBlur(30)))
    background.paste(small, (108, 230), mask)
    background.save(f"{OUT}/bg{index}.png")

# 2. Voice mix (male placeholder voice) at fixed delays
RATE = 16000
delays = [0.4, 5.6, 13.1, 20.5]
voice = np.zeros(int(TOTAL * RATE))
for number, delay in enumerate(delays, 1):
    with wave.open(f"{VOICE}/s{number}.wav") as source:
        data = np.frombuffer(source.readframes(source.getnframes()), np.int16) / 32768
    start = int(delay * RATE)
    voice[start:start + len(data)] += data[: len(voice) - start]
with wave.open(f"{OUT}/voice.wav", "wb") as target:
    target.setnchannels(1); target.setsampwidth(2); target.setframerate(RATE)
    target.writeframes((np.clip(voice, -1, 1) * 32767).astype(np.int16).tobytes())
hop = RATE // FPS
loudness = np.array([np.sqrt(np.mean(voice[i * hop:(i + 1) * hop] ** 2)) for i in range(int(TOTAL * FPS))])
mouth_open = loudness > 0.035
# hold each mouth state at least 2 frames so it does not flicker
for frame in range(2, len(mouth_open)):
    if mouth_open[frame] != mouth_open[frame - 1] and mouth_open[frame - 1] != mouth_open[frame - 2]:
        mouth_open[frame] = mouth_open[frame - 1]

# 3. Mascot sprites, one common scale
SCALE = 1.06
sprites = {}
for name in ["coucou", "pointe", "pouce", "marche1", "marche2", "bouche-fermee", "bouche-ouverte"]:
    image = Image.open(f"{MAS}/{name}.png").convert("RGBA")
    sprites[name] = image.resize((int(image.width * SCALE), int(image.height * SCALE)), Image.LANCZOS)

def ease(value):
    value = min(max(value, 0), 1)
    return value * value * (3 - 2 * value)

LEFT, RIGHT = 150, 760   # x of the mascot centre
def pose_at(time, frame):
    """Return sprite name, centre x, vertical offset, rotation, scale pop."""
    float_bob = 8 * math.sin(time * 2 * math.pi * 0.8)
    talk = "bouche-ouverte" if mouth_open[frame] else "bouche-fermee"
    if time < 1.6:
        progress = time / 1.6
        step = "marche1" if int(time / 0.2) % 2 == 0 else "marche2"
        return step, -200 + (LEFT + 200) * ease(progress * 1.1), -abs(math.sin(time * math.pi / 0.2)) * 14, 0, 1
    if time < 5.5:
        return talk, LEFT, float_bob, 0, 1
    if time < 9.2:
        pop = 1 + 0.08 * max(0, 1 - (time - 5.5) / 0.25)
        return "pointe", LEFT + 20, float_bob, 0, pop
    if time < 10.6:
        progress = (time - 9.2) / 1.4
        step = "marche1" if int(time / 0.2) % 2 == 0 else "marche2"
        return step, LEFT + (RIGHT - LEFT) * ease(progress), -abs(math.sin(time * math.pi / 0.2)) * 14, 0, 1
    if time < 13.0:
        return talk, RIGHT, float_bob, 0, 1
    if time < 16.6:
        pop = 1 + 0.1 * max(0, 1 - (time - 13.0) / 0.25)
        return "pouce", RIGHT, float_bob, 0, pop
    if time < 20.3:
        return talk, RIGHT, float_bob, 0, 1
    wave_angle = 5 * math.sin((time - 20.3) * 2 * math.pi * 1.6)
    return "coucou", RIGHT, float_bob, wave_angle, 1 + 0.06 * max(0, 1 - (time - 20.3) / 0.25)

out = sys.stdout.buffer
for frame in range(int(TOTAL * FPS)):
    time = frame / FPS
    name, centre_x, offset_y, angle, pop = pose_at(time, frame)
    sprite = sprites[name]
    if pop != 1:
        sprite = sprite.resize((int(sprite.width * pop), int(sprite.height * pop)), Image.BILINEAR)
    if angle:
        sprite = sprite.rotate(angle, resample=Image.BICUBIC, expand=True, center=(sprite.width // 2, sprite.height))
    canvas = Image.new("RGBA", (W, STRIP_H), (0, 0, 0, 0))
    ground = STRIP_H - 18
    shadow = Image.new("RGBA", (W, STRIP_H), (0, 0, 0, 0))
    spread = 110 + offset_y
    ImageDraw.Draw(shadow).ellipse((centre_x - spread, ground - 14, centre_x + spread, ground + 14), fill=(0, 0, 0, 120))
    canvas.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(8)))
    layer = Image.new("RGBA", (W, STRIP_H), (0, 0, 0, 0))
    layer.paste(sprite, (int(centre_x - sprite.width / 2), int(ground - sprite.height + offset_y)))
    canvas.alpha_composite(layer)
    out.write(canvas.tobytes())
