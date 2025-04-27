import os
import cv2
from PIL import Image
import shutil

def convert_to_jpg(input_path, output_path):
    """Convert image to JPG format"""
    try:
        # Read the image
        img = cv2.imread(input_path)
        if img is None:
            print(f"Could not read image: {input_path}")
            return False
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Save as JPG
        cv2.imwrite(output_path, img, [cv2.IMWRITE_JPEG_QUALITY, 95])
        return True
    except Exception as e:
        print(f"Error converting {input_path}: {str(e)}")
        return False

def process_images():
    # Create images2 directory if it doesn't exist
    output_dir = "images2"
    os.makedirs(output_dir, exist_ok=True)
    
    # Create person-specific directories
    jim_dir = os.path.join(output_dir, "Jim")
    lebron_dir = os.path.join(output_dir, "Lebron")
    os.makedirs(jim_dir, exist_ok=True)
    os.makedirs(lebron_dir, exist_ok=True)
    
    # Supported image extensions
    extensions = ('.jpg', '.jpeg', '.png', '.webp')
    
    # Get all files in current directory
    current_dir = os.getcwd()
    files = [f for f in os.listdir(current_dir) if f.lower().endswith(extensions)]
    
    # Process each image
    for file in files:
        input_path = os.path.join(current_dir, file)
        filename = os.path.splitext(file)[0]  # Get filename without extension
        
        # Determine output directory based on filename
        if filename.lower().startswith('jim'):
            output_subdir = jim_dir
        elif filename.lower().startswith('lebron'):
            output_subdir = lebron_dir
        else:
            output_subdir = output_dir
        
        # Create output path with .jpg extension
        output_path = os.path.join(output_subdir, f"{filename}.jpg")
        
        # Convert and move the image
        if convert_to_jpg(input_path, output_path):
            print(f"Successfully converted and moved: {file} -> {output_path}")
        else:
            print(f"Failed to convert: {file}")

if __name__ == "__main__":
    print("Starting image conversion and organization...")
    process_images()
    print("Process completed!")
