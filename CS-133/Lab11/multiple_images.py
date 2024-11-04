import image

def main():
  # A list of face images that are available
  # Face images of men
  men_face_files = ["alex.jpg", "alexander.jpg", "alfred.jpg", "ambroz.jpg"]
  # Face images of women
  women_face_files = ["zelmira.jpg","zita.jpg", "zlata.jpg", "zlatica.jpg", "zora.jpg"]
  base_url = "http://raw.githubusercontent.com/cs-133-01-22fa/faces/main/"

  # Load a list of pics
  men_face_pics = []
  for face_path in men_face_files:
    men_face_pics.append(image.Pic(base_url + face_path))

  women_face_pics = []
  for face_path in women_face_files:
    women_face_pics.append(image.Pic(base_url + face_path))

  print("Modifying images... ")
  average_pics(men_face_pics)
  average_pics(women_face_pics)
  # Save the image
  men_face_pics[0].save_image("average_men.jpg")
  women_face_pics[0].save_image("average_women.jpg")
  print("Done modifying images")
  print("-------------------")

def average_pics(faces):
  """
    Takes a list of face images and modifies the first
    image in the list to be the average of the entire list.
  """
  # We want to modify the first face, so save it in a variable
  first_face = faces[0]

  # Get the number of images to calculate the average
  num_faces = len(faces)

  # Iterate over each pixel location
  for row in range(first_face.height):
    for col in range(first_face.width):
      # Initialize sums for red, green, and blue
      red_sum = 0
      green_sum = 0
      blue_sum = 0

      # Accumulate RGB values from each image at the current pixel location
      for face in faces:
        pixel = face.pixels[row][col]
        red_sum += pixel.red
        green_sum += pixel.green
        blue_sum += pixel.blue

      # Calculate the average RGB values
      avg_red = int(red_sum / num_faces)
      avg_green = int(green_sum / num_faces)
      avg_blue = int(blue_sum / num_faces)

      # Apply the averaged RGB values to the first image
      first_face.pixels[row][col].red = avg_red
      first_face.pixels[row][col].green = avg_green
      first_face.pixels[row][col].blue = avg_blue


main()
