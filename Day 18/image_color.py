# import statement
import colorgram

# stores colors in rgb format
rgb_colors = []

# extracts 30 colors from the image named 'image.jpg'
colors = colorgram.extract('image.jpg', 30)

# stores each color in the list
for color in colors:
    rgb_colors.append(color.rgb)

# extracting only the r, g and b values
rgb_colors = [(r, g, b) for r, g, b in rgb_colors]
