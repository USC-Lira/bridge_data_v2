import os
import shutil
import argparse

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        # Check if 'images0' exists in the current directory and delete it
        images0_path = os.path.join(root, 'images0')
        if 'images0' in dirs and 'images1' in dirs:
            print(f"Deleting folder: {images0_path}")
            shutil.rmtree(images0_path)
        
        # Check if 'images1' exists and rename it to 'images0'
        images1_path = os.path.join(root, 'images1')
        if 'images1' in dirs and not os.path.exists(images0_path):
            new_name_path = os.path.join(root, 'images0')
            print(f"Renaming folder: {images1_path} to {new_name_path}")
            shutil.move(images1_path, new_name_path)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process directories by deleting "images0" and renaming "images1" to "images0".')
    parser.add_argument('directory', type=str, help='Path to the directory to process')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Process the specified directory
    process_directory(args.directory)

if __name__ == '__main__':
    main()

