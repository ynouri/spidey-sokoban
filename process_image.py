#!/usr/bin/env python3
"""Process Spidey image to remove white background"""

from PIL import Image

# Load the image
img = Image.open('assets/spin.jpeg')

# Convert to RGBA
img = img.convert('RGBA')

# Get pixel data
pixels = img.load()

# Remove white background (make it transparent)
width, height = img.size
for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        # If pixel is close to white, make it transparent
        if r > 240 and g > 240 and b > 240:
            pixels[x, y] = (r, g, b, 0)

# Save as PNG
img.save('assets/spin.png')
print("Processed spin.png created successfully!")
print(f"Image size: {width}x{height}")
