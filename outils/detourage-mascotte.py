import sys, numpy as np
from PIL import Image
from scipy import ndimage
src, dst = sys.argv[1], sys.argv[2]
im = np.array(Image.open(src).convert("RGBA")).astype(np.int16)
rgb, a = im[..., :3], im[..., 3]
trans = a < 20
dist = ndimage.distance_transform_edt(~trans)
mn = rgb.min(-1); sat = rgb.max(-1) - mn
whiteish = (mn > 200) & (sat < 30)
cand = whiteish & (dist < 22) & ~trans
# garder seulement le blanc relié à l'extérieur
lab, _ = ndimage.label(cand | trans)
outside = set(np.unique(lab[trans])) - {0}
border = np.isin(lab, list(outside)) & cand
newa = a.copy(); newa[border] = 0
# adoucir le bord (1 px)
m = newa > 0
m = ndimage.binary_erosion(m, iterations=1)
soft = ndimage.gaussian_filter(m.astype(float), 0.8) * 255
out = im.copy(); out[..., 3] = np.minimum(newa, soft).astype(np.int16)
# recadrer
ys, xs = np.where(out[..., 3] > 10)
out = out[ys.min():ys.max()+1, xs.min():xs.max()+1]
Image.fromarray(out.astype(np.uint8)).save(dst)
