# Image Augmentation Script

This Python script performs various random augmentations on `.png` images . It uses the `albumentations` library to apply transformations like brightness/contrast adjustments, horizontal flipping, rotation, scaling, and adding Gaussian noise to the images.

## Features
- **Random Brightness/Contrast**: Adjusts the brightness and contrast of the image.
- **Horizontal Flip**: Flips the image horizontally.
- **Rotation**: Rotates the image randomly within a specified limit.
- **Random Scaling**: Scales the image by a random factor.
- **Gaussian Noise**: Adds noise to the image for data augmentation.

## Usage
1. Set the `input_dir` to the directory containing your `.png` images.
2. Set the `output_dir` where you want the augmented images to be saved.
3. Set `num_augmentations` to specify how many augmented versions of each image you want.

```bash
python aug_images.py
