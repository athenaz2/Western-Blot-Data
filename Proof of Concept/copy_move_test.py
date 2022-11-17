# Copy region and paste onto another area
# Referenced https://www.adamsmith.haus/python/examples/3039/pil-copy-a-region-of-an-image-to-another-area 

from PIL import Image

file_path = "SCC25DDP_BMI1.jpg"
orig_img = Image.open("images_separated/" + file_path, "r")
# Coordinates: left, top, right, bottom
region = orig_img.crop((130, 245, 250, 270))
orig_img.paste(region, (130, 270, 250, 295))

orig_img.save("images_manipulated/" + file_path)