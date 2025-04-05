from pdf2image import convert_from_path
import os

# PDF file location
pdf_path = "image.pdf"

# Get the PDF filename without extension
pdf_filename = os.path.splitext(os.path.basename(pdf_path))[0]

# Output folder for images
output_folder = "converted_images"
os.makedirs(output_folder, exist_ok=True)

# Convert PDF to images with 300 DPI (high resolution)
images = convert_from_path(pdf_path, dpi=300)

# Save each page as a PNG file with unique names
for i, image in enumerate(images):
    image_path = os.path.join(output_folder, f"{pdf_filename}_page_{i + 1}.png")
    image.save(image_path, "PNG")

print(f"Conversion complete! {len(images)} page(s) saved in '{output_folder}'")
