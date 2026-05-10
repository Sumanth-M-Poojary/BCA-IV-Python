from PIL import Image, ImageDraw, ImageFont
import textwrap

# Text to convert to handwriting
txt = "hello tnssdmnm jdskjksjdkjksdhnmn dskjsdkjksdj dsjjhsd nkjsdkjksdjkjsdkdsjksdkjkdsjkjdssskkjskdjkdsjkdsj"

# Image settings
img_width = 1200
img_height = 400
background_color = "white"
text_color = "black"

# Create a blank image
image = Image.new("RGB", (img_width, img_height), background_color)
draw = ImageDraw.Draw(image)

# Try to use a handwriting-style font, fallback to default
try:
    # You can download handwriting fonts and place them in the same directory
    # For example: "Caveat-Bold.ttf" or "LuckiestGuy.ttf"
    font = ImageFont.truetype("arial.ttf", 20)
except:
    # Fallback to default font
    font = ImageFont.load_default()

# Text wrapping
margin = 20
max_width = img_width - 2 * margin
wrapped_text = textwrap.fill(txt, width=60)

# Draw text on image
draw.text((margin, margin), wrapped_text, fill=text_color, font=font)

# Save the image
image.save("handwrite_output.png")
print("Handwritten text saved as 'handwrite_output.png'")


