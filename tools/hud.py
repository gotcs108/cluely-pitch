from PIL import Image, ImageDraw, ImageFont, ImageFilter

im = Image.open("plate.png").convert("RGB")
W, H = im.size
print("plate size:", W, H)

FONT = "C:/Windows/Fonts/consolab.ttf"   # Consolas Bold
size = int(W * 0.072)
font = ImageFont.truetype(FONT, size)

LINES = ["> DO NOT EXPLAIN", "  THE GLASSES"]
GREEN = (122, 255, 138)

pad = int(W * 0.055)
lh = int(size * 1.28)
block_h = lh * len(LINES)
y0 = int(H * 0.70)

# subtle dark scrim so the text survives the busy asphalt
scrim = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(scrim)
top = y0 - int(size * 0.7)
bot = y0 + block_h + int(size * 0.7)
for i, y in enumerate(range(top, bot)):
    a = int(105 * min(1.0, min(y - top, bot - y) / (size * 1.4)))
    sd.line([(0, y), (int(W * 0.86), y)], fill=(0, 0, 0, a))
scrim = scrim.filter(ImageFilter.GaussianBlur(14))
im = Image.alpha_composite(im.convert("RGBA"), scrim)

# glow pass
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
for i, ln in enumerate(LINES):
    gd.text((pad, y0 + i * lh), ln, font=font, fill=GREEN + (255,))
glow = glow.filter(ImageFilter.GaussianBlur(int(size * 0.30)))
im = Image.alpha_composite(im, glow)
im = Image.alpha_composite(im, glow)

# crisp pass, slightly translucent so it reads as a lens overlay
sharp = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(sharp)
for i, ln in enumerate(LINES):
    d.text((pad, y0 + i * lh), ln, font=font, fill=GREEN + (240,))
# blinking cursor block
cw = d.textlength("M", font=font)
last_w = d.textlength(LINES[-1], font=font)
d.rectangle(
    [pad + last_w + cw * 0.25, y0 + (len(LINES) - 1) * lh + size * 0.12,
     pad + last_w + cw * 1.05, y0 + (len(LINES) - 1) * lh + size * 1.02],
    fill=GREEN + (200,),
)
im = Image.alpha_composite(im, sharp).convert("RGB")

im.save("thumbnail.png")
im.resize((200, int(200 * H / W)), Image.LANCZOS).save("thumbnail_200px.png")
print("wrote thumbnail.png + thumbnail_200px.png")
