import image
import random # import for random builtin function

def main():
  # Load an image from somewhere online
  pic1 = image.Pic('http://www.sbu.edu/images/default-source/alumni/show-your-spirit-zoom-backgrounds/campus-in-summer.jpg')
  pic2 = image.Pic('http://www.sbu.edu/images/default-source/alumni/show-your-spirit-zoom-backgrounds/campus-in-summer.jpg')
  pic3 = image.Pic('http://www.sbu.edu/images/default-source/alumni/show-your-spirit-zoom-backgrounds/campus-in-summer.jpg')
  pic4 = image.Pic('http://www.sbu.edu/images/default-source/alumni/show-your-spirit-zoom-backgrounds/campus-in-summer.jpg')
  pic5 = image.Pic('http://www.sbu.edu/images/default-source/alumni/show-your-spirit-zoom-backgrounds/campus-in-summer.jpg')
  pic6 = image.Pic('http://www.sbu.edu/images/default-source/alumni/show-your-spirit-zoom-backgrounds/campus-in-summer.jpg')
  pic7 = image.Pic('http://www.sbu.edu/images/default-source/alumni/show-your-spirit-zoom-backgrounds/campus-in-summer.jpg')
  # Modify our image
  print("Modifying image... ")
  boost_red(pic1)
  invert(pic2)
  grey_scale(pic3)
  grainy(pic4)
  selected_invert(pic5, 100, 100, 200, 200)
  mirror_image(pic6)
  blur(pic7, 3)
  print("Done modifying image")
  print("-------------------")
  # Save the image
  pic1.save_image("myImage-red.jpg")
  pic2.save_image("myImage-inverted.jpg")
  pic3.save_image("myImage-grey.jpg")
  pic4.save_image("myImage-grainy.jpg")
  pic5.save_image("myImage-selected-invert.jpg")
  pic6.save_image("myImage-mirror.jpg")
  pic7.save_image("myImage-blur.jpg")

# BOOST THE RED - DON'T DELETE
# This is ONE example of a function that changes a picture.
# You will create several other functions that look similar to this.
def boost_red(pic):
  # Go through each row and column
  for row in range(pic.height):
    for col in range(pic.width):
      # Gets a pixel at row/col
      pixel = pic.pixels[row][col]

      # Get the RGB values of this pixel
      red = pixel.red
      green = pixel.green
      blue = pixel.blue

      # Resave them by altering the red
      pixel.red = red + 100
      pixel.green = green
      pixel.blue = blue

      # Finally, reset the pixel stored at that spot
      pic.pixels[row][col] = pixel

def invert(pic):
  """
    Arguments:
      pic: The image to be modified
    Modifies:
      By removing RGB value from 255
  """
  # Go through each row and column
  for row in range(pic.height):
    for col in range(pic.width):
      # Gets a pixel at row/col
      pixel = pic.pixels[row][col]

      # Get the RGB values of this pixel
      red = pixel.red
      green = pixel.green
      blue = pixel.blue

      # Resave them by inverting
      pixel.red = 255 - red
      pixel.green = 255 - green
      pixel.blue = 255 - blue

      # Finally, reset the pixel stored at that spot
      pic.pixels[row][col] = pixel

def grey_scale(pic):
  """
    Arguments:
      pic: The image to be modified
    Modifies:
      The image with the average values of three RGB channels
  """
  # Go through each row and column
  for row in range(pic.height):
    for col in range(pic.width):
      # Gets a pixel at row/col
      pixel = pic.pixels[row][col]

      # Get the RGB values of this pixel
      red = pixel.red
      green = pixel.green
      blue = pixel.blue

      # Average the three RGB values and cast as int
      average_rgb = int((red + green + blue) / 3)

      # Resave them with the average
      pixel.red = average_rgb
      pixel.green = average_rgb
      pixel.blue = average_rgb

      # Finally, reset the pixel stored at that spot
      pic.pixels[row][col] = pixel

def grainy(pic):
  """
    Arguments:
      pic: The image to be modified
    Modifies:
      The image with the randomly to boost red, green, or blue by 100.
  """
  # Go through each row and column
  for row in range(pic.height):
    for col in range(pic.width):
      # Gets a pixel at row/col
      pixel = pic.pixels[row][col]

      # Get the RGB values of this pixel
      red = pixel.red
      green = pixel.green
      blue = pixel.blue

      # Use builtin choice function to choose a random RGB
      boost_color = random.choice([red, green, blue])

      if boost_color == red:
        pixel.red = min(pixel.red + 100, 255)  # Make sure pixel doesn't go over 255
      elif boost_color == green:
        pixel.green = min(pixel.green + 100, 255)
      elif boost_color == blue:
        pixel.blue = min(pixel.blue + 100, 255)

      # Finally, reset the pixel stored at that spot
      pic.pixels[row][col] = pixel

def selected_invert(pic, row1, col1, row2, col2):
  """
      Arguments:
        pic: The image to be modified
        row1, col1: The top-left coordinates of the rectangle to modify
        row2, col2: The bottom-right coordinates of the rectangle to modify
      Modifies:
        Inverts the colors of pixels within the specified rectangular region only
  """
  # Go through each pixel within the defined rectangle
  for row in range(row1, row2):
    for col in range(col1, col2):
      # Gets a pixel at row/col
      pixel = pic.pixels[row][col]

      # Get the RGB values of this pixel
      red = pixel.red
      green = pixel.green
      blue = pixel.blue

      # Resave them by inverting
      pixel.red = 255 - red
      pixel.green = 255 - green
      pixel.blue = 255 - blue

      # Finally, reset the pixel stored at that spot
      pic.pixels[row][col] = pixel

def mirror_image(pic):
  """
      Mirrors the right half of the image onto the left half.
      Arguments:
        pic: The image to modify by mirroring the right half onto the left half
      """
  # Assign width and height of the image to vars
  width = pic.width
  height = pic.height

  # Loop through each pixel in the right half of the image
  for row in range(height):
    for col in range(width // 2, width):  # Only go through right half of the image
      # Get the pixel on the right side
      right_pixel = pic.pixels[row][col]

      # Calculate the mirrored x-position on the left side
      mirrored_col = width - col - 1 # -1 makes sure all pixels are mirrored

      # Set the left side pixel to have the same RGB values as the right side
      pic.pixels[row][mirrored_col].red = right_pixel.red
      pic.pixels[row][mirrored_col].green = right_pixel.green
      pic.pixels[row][mirrored_col].blue = right_pixel.blue

def blur(pic, window):
  """
      Blurs the image horizontally by averaging the RGB values of each pixel with its
      next neighbors.

      Arguments:
        pic: The image to modify
        window: The number of pixels to include in the averaging for the blur effect
      """
  height = pic.height
  width = pic.width

  # Iterate over each row
  for row in range(height):
    # Only go up to width - window to avoid going out of bounds
    for col in range(width - window + 1):
      # Initialize sums for red, green, and blue
      red_sum = 0
      green_sum = 0
      blue_sum = 0

      # Sum up the RGB values within the window
      for i in range(window):
        pixel = pic.pixels[row][col + i] # Access each pixel in the window
        red_sum += pixel.red
        green_sum += pixel.green
        blue_sum += pixel.blue

      # Calculate the average RGB values and cast is as int
      new_red = int(red_sum / window)
      new_green = int(green_sum / window)
      new_blue = int(blue_sum / window)

      # Apply the averaged color to the current pixel
      pic.pixels[row][col].red = new_red
      pic.pixels[row][col].green = new_green
      pic.pixels[row][col].blue = new_blue

main()
