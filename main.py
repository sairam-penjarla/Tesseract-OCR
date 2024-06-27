import argparse
import pytesseract
import os
import random
from PIL import Image
import shutil

def extract_text(image_path):
  """Extracts text from an image using pytesseract.

  Args:
      image_path (str): Path to the image file.

  Returns:
      str: The extracted text from the image.
  """

  # Check if inputs and outputs folders exist
  if not os.path.exists("inputs"):
    os.makedirs("inputs")
  if not os.path.exists("outputs"):
    os.makedirs("outputs")

  # Move image to inputs folder (optional, can be modified based on your needs)
  if not image_path.startswith("inputs/"):
    shutil.move(image_path, os.path.join("inputs", os.path.basename(image_path)))
    image_path = os.path.join("inputs", os.path.basename(image_path))

  try:
    # Read the image
    img = Image.open(image_path)
  except FileNotFoundError:
    print(f"Error: Image file '{image_path}' not found.")
    return

  # Extract text using pytesseract
  extracted_text = pytesseract.image_to_string(img)

  # Generate a random filename to avoid conflicts (optional)
  output_filename = f"output_{random.randint(1000, 9999)}.txt"
  output_path = os.path.join("outputs", output_filename)

  # Save the extracted text to a file
  with open(output_path, "w") as f:
    f.write(extracted_text)

  print(f"Text extracted and saved to: {output_path}")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Image Text Extraction Tool")
    parser.add_argument("--image_path", required=True, help="Path to the image file")
    args = parser.parse_args()

    # Call the extract_text function
    extract_text(args.image_path)