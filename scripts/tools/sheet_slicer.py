from PIL import Image
import os

fname = "32_pixel_ground.png"
dims = (32, 32)
if not os.path.exists(f"../../art/{fname[:-4]}"):
    os.mkdir(f"../../art/{fname[:-4]}")

sheet = Image.open(f"../../art/{fname}")

for y in range(int(sheet.size[1] / dims[1])):
    for x in range(int(sheet.size[0] / dims[0])):
        if y < sheet.size[0] / dims[0]:
            tile = sheet.crop((y * dims[1], x * dims[0], y * dims[1] + dims[1], x * dims[0] + dims[0]))
            tile.save(f"../../art/{fname[:-4]}/{x}_{y}.png")
