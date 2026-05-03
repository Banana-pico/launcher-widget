from PIL import Image
import sys

src = sys.argv[1]
dst = sys.argv[2]

img = Image.open(src).convert('RGBA')
sizes = [256, 128, 64, 48, 32, 16]
imgs = [img.resize((s, s), Image.LANCZOS) for s in sizes]
imgs[0].save(dst, format='ICO', sizes=[(s, s) for s in sizes], append_images=imgs[1:])
print('ICO saved:', dst)
