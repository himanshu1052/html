from sketchpy import canvas
import cv2
import turtle

# Provide the full path to the SVG file
svg_file_path = "C:\\path\\to\\happy dusshera.svg"

# Load the SVG file using sketchpy
obj = canvas.sketch_from_svg(svg_file_path)

# Open the image you want to resize
image_path = "path_to_your_image.jpg"  # Provide the path to your image file

# Set the new size (width, height)
new_size = (400, 300)  # Replace with the desired width and height

# Open the image using OpenCV
image = cv2.imread(image_path)

if image is not None:
    # Resize the image
    resized_image = cv2.resize(image, new_size)

    # Save the resized image with the same file name and path, overwriting the original
    cv2.imwrite(image_path, resized_image)
else:
    print("Image not found or cannot be opened.")

t = turtle.Turtle()

t.penup()
t.goto(-60, -290)
t.pendown()
t.pencolor("#ff6600")
t.write("Happy Dussehra", align="center", font=("Arial", 50, "bold"))
obj.draw()
t.hideturtle()
turtle.done()
