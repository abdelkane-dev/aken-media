import sys, wave, math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
MAS, VOIX = sys.argv[1], sys.argv[2]
FPS, W, H = 30, 1080, 1920
with wave.open(VOIX) as s:
    v = np.frombuffer(s.readframes(s.getnframes()), np.int16) / 32768; R = s.getframerate()
TOTAL = len(v) / R + 1.2
hop = R // FPS; N = int(TOTAL * FPS)
loud = np.array([np.sqrt(np.mean(v[i*hop:(i+1)*hop]**2)) if i*hop < len(v) else 0 for i in range(N)])
loud = np.convolve(loud, np.ones(3)/3, 'same')
thr = max(0.02, np.percentile(loud[loud > 0.005], 40)) if (loud > 0.005).any() else 0.03
mouth = loud > thr
for f in range(2, N):
    if mouth[f] != mouth[f-1] and mouth[f-1] != mouth[f-2]: mouth[f] = mouth[f-1]
S = 2.15
sp = {n: (lambda im: im.resize((int(im.width*S), int(im.height*S)), Image.LANCZOS))(Image.open(f"{MAS}/{n}.png").convert("RGBA"))
      for n in ["bouche-fermee", "bouche-ouverte", "coucou"]}
# fond Aken : noir + halo orange
yy, xx = np.mgrid[0:H, 0:W]
d = np.sqrt((xx-W/2)**2 + ((yy-1250)*0.8)**2) / 900
glow = np.clip(1-d, 0, 1)**2
bg = np.zeros((H, W, 3)); bg[:] = (10, 10, 10)
bg += glow[..., None] * np.array([255, 90, 0]) * 0.45
bgi = Image.fromarray(bg.clip(0, 255).astype(np.uint8)).convert("RGBA")
dr = ImageDraw.Draw(bgi)
def ease(t): t = min(max(t, 0), 1); return t*t*(3-2*t)
out = sys.stdout.buffer
talk_end = len(v) / R
for f in range(N):
    t = f / FPS
    frame = bgi.copy()
    breathe = 1 + 0.012 * math.sin(t * 2 * math.pi * 0.35)
    sway = 1.6 * math.sin(t * 2 * math.pi * 0.45) + (1.2 * math.sin(t * 2*math.pi*2.1) if mouth[f] else 0)
    bob = 6 * math.sin(t * 2 * math.pi * 0.7)
    intro = ease(t / 0.45)
    if t < talk_end:
        a = sp["bouche-ouverte" if mouth[f] else "bouche-fermee"]; b = None; mix = 0
    else:
        a = sp["bouche-fermee"]; b = sp["coucou"]; mix = ease((t - talk_end) / 0.3)
    def place(img, alpha, extra_rot=0):
        im = img.resize((int(img.width * breathe), int(img.height * (breathe + 0.006 * math.sin(t*2*math.pi*0.35)))), Image.BILINEAR)
        im = im.rotate(sway + extra_rot, resample=Image.BICUBIC, expand=True, center=(im.width//2, im.height))
        if alpha < 1:
            al = im.getchannel("A").point(lambda p: int(p * alpha)); im.putalpha(al)
        x = W//2 - im.width//2; y = int(H - 120 - im.height + bob + (1 - intro) * 500)
        frame.alpha_composite(im, (x, max(y, -im.height)))
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).ellipse((W//2-260, H-150, W//2+260, H-95), fill=(0, 0, 0, 150))
    frame.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
    if mix < 1: place(a, 1 - mix if b else 1)
    if b is not None and mix > 0: place(b, mix, 4 * math.sin((t - talk_end) * 2 * math.pi * 1.8))
    out.write(frame.convert("RGB").tobytes())
print(TOTAL, file=sys.stderr)
