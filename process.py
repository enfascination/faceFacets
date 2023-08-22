#from chatgpt 3.5
from PIL import Image
import os
import csv

#definitions
def splitImagesInHalf(image):
    # Get the dimensions of the original image
    width, height = image.size

    # Split the image vertically into left and right halves
    left_half = image.crop((0, 0, width // 2, height))
    right_half = image.crop((width // 2, 0, width, height))

    # Create a new canvas for arranging the split images
    new_canvas = Image.new("RGBA", (2400, 1600), (255, 255, 255, 0))

    # Arrange the split images on the canvas
    new_canvas.paste(left_half, (0, 0))
    new_canvas.paste(right_half, (width // 2, 0))
    new_canvas.paste(right_half, (width // 2 + width // 2, 0))
    new_canvas.paste(left_half, (width // 2 + 2*width // 2, 0))

    return new_canvas

def splitImages(image, x):
    # Get the dimensions of the original image
    width, height = image.size

    # Split the image vertically into left and right halves
    left_half = image.crop((0, 0, x, height))
    right_half = image.crop((x, 0, width, height))

    # Create a new canvas for arranging the split images
    new_canvas = Image.new("RGBA", (2400, 1600), (255, 255, 255, 0))

    # Arrange the split images on the canvas
    new_canvas.paste(left_half, (0, 0))
    new_canvas.paste(right_half, (x, 0))
    new_canvas.paste(right_half, (width, 0))
    new_canvas.paste(left_half, (width + (width-x), 0))

    return new_canvas

def doubleHalves(image, x):
    # Get the dimensions of the original image
    width, height = image.size

    # Split the image vertically into left and right halves
    left_half = image.crop((0, 0, x, height))
    right_half = image.crop((x, 0, width, height))

    # Flip the second left and right image halves horizontally
    flipped_left_half = left_half.transpose(Image.FLIP_LEFT_RIGHT)
    flipped_right_half = right_half.transpose(Image.FLIP_LEFT_RIGHT)

    # Create a new canvas for arranging the split images
    new_canvas = Image.new("RGBA", (2400, 1600), (255, 255, 255, 0))

    # Arrange the split images on the canvas
    new_canvas.paste(left_half, (0, 0))
    new_canvas.paste(flipped_left_half, (x, 0))
    new_canvas.paste(flipped_right_half, (2*x, 0))
    new_canvas.paste(right_half, (width + x, 0))

    return new_canvas


source_directory = "./"
input_directory = "./input/"
output_directory = "./output/"
hints_file = "halves_sample.csv"

# process files of choice, with user computed halfpoints
half_points = []
with open(os.path.join(source_directory, hints_file)) as filecsv:
    for line in filecsv:
        el = line.strip().split(", ")
        el[1] = int(el[1])
        half_points.append( el )
half_points = dict(half_points)
filelist = half_points.keys()


# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Iterate through each file in the input directory
#for filename in os.listdir(input_directory):
for filename in filelist:
    if filename.lower().endswith(".jpg"):
        input_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, "resize_" + os.path.splitext(filename)[0] + ".png")

        # Open the image
        image = Image.open(input_path)
        old_width, old_height = image.size

        # Resize the image while maintaining aspect ratio
        new_width = 1200
        new_height = int(new_width * image.height / image.width)
        resized_image = image.resize((new_width, new_height))

        # # Create a new canvas
        # new_canvas = Image.new("RGBA", (2400, 1600), (255, 255, 255, 0))
        # # Paste the resized image onto the canvas
        # new_canvas.paste(split_image, (0, 0, new_width, new_height))

        # Inside the loop where you process images
        # After resizing the image, call the splitImages function
        half = round(half_points[filename]/old_width * new_width)
        new_canvas = doubleHalves(resized_image, half)

        # Save the final image as PNG
        new_canvas.save(output_path, "PNG")

        print(f"Processed: {filename}")

print("Done processing all files.")
