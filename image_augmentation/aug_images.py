import albumentations as A
import cv2
import os
from tqdm import tqdm

# Define augmentation pipeline
transform = A.Compose([
    A.RandomBrightnessContrast(p=0.5),
    A.HorizontalFlip(p=0.5),
    A.Rotate(limit=30, p=0.5),
    A.RandomScale(scale_limit=0.1, p=0.5),
    A.GaussNoise(p=0.5)
])

def augment_images(input_dir, output_dir, num_augmentations=5):
    print(f"Input directory: {input_dir}")
    print(f"Output directory: {output_dir}")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    # Iterate through all images
    image_count = 0
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.png'):
            image_count += 1
            image_path = os.path.join(input_dir, filename)
            print(f"Processing image: {image_path}")
            
            image = cv2.imread(image_path)
            if image is None:
                print(f"Failed to read image: {image_path}")
                continue
            
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Perform augmentation
            for i in range(num_augmentations):
                augmented = transform(image=image)
                augmented_image = augmented['image']
                
                # Save augmented image
                output_filename = f"{os.path.splitext(filename)[0]}_aug_{i}.png"
                output_path = os.path.join(output_dir, output_filename)
                cv2.imwrite(output_path, cv2.cvtColor(augmented_image, cv2.COLOR_RGB2BGR))
                print(f"Saved augmented image: {output_path}")

    print(f"Processed {image_count} images")
    print(f"Augmentation complete. Augmented images saved in {output_dir}")

# Usage
input_dir = '.'  # Current directory
output_dir = 'augmented-images'
num_augmentations = 5

augment_images(input_dir, output_dir, num_augmentations)