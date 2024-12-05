import os
import random
from PIL import Image

def sample_resize_and_save_by_subfolder(input_dir, output_dir, n, new_size=(128, 128)):
    """
    Randomly samples n images from each subdirectory in the input_dir, resizes them,
    converts them to PNG format, and saves them in corresponding subfolders in the output_dir.

    Parameters:
        input_dir (str): Path to the main directory containing subfolders.
        output_dir (str): Path to the output directory to save processed images.
        n (int): Number of images to sample from each subfolder.
        new_size (tuple): New size to resize images (width, height).
    """
    # Supported image extensions
    valid_extensions = (".jpg", ".jpeg", ".png")

    # Loop through each subdirectory in the input directory
    for folder in os.listdir(input_dir):
        folder_path = os.path.join(input_dir, folder)

        # Ensure the path is a directory
        if os.path.isdir(folder_path):
            # List all valid image files in the current folder
            files = [f for f in os.listdir(folder_path) if f.lower().endswith(valid_extensions)]

            print(folder_path)
            if not files:
                print("here")
                
            # Sample n files randomly
            sampled_files = random.sample(files, min(n, len(files)))

            # Create a corresponding subfolder in the output directory
            output_subfolder = os.path.join(output_dir, folder)
            os.makedirs(output_subfolder, exist_ok=True)

            # Process and save sampled files
            for file in sampled_files:
                src = os.path.join(folder_path, file)
                dst = os.path.join(output_subfolder, f"{os.path.splitext(file)[0]}.png")

                try:
                    # Open, resize, convert to PNG, and save the image
                    with Image.open(src) as img:
                        resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
                        resized_img.save(dst, format="PNG")
                        print(f"Saved: {dst}")
                except Exception as e:
                    print(f"Error processing {file} in folder {folder}: {e}")

# Parameters
input_directory = "archive/test"  # Replace with the path to your main folder
output_directory = "archive_small/test"  # Replace with the path to your output folder
num_images = 50  # Replace with the number of images to sample from each folder
resize_dimensions = (128, 128)  # Replace with the desired resize dimensions (width, height)

# Run the function
sample_resize_and_save_by_subfolder(input_directory, output_directory, num_images, resize_dimensions)