# PDF to Image Converter

This script converts each page of a PDF file into high-resolution images. It uses the `pdf2image` library to extract each page as an image, which is useful when working with PDFs that need to be processed as images (e.g., for OCR, analysis, etc.).

## Features
- **Convert PDF Pages to Images**: Converts each page of a PDF file to a separate image.
- **High Resolution**: The images are saved at a resolution of 300 DPI to ensure high quality.
- **Output Folder**: Saves each page as a `.png` image in the specified output directory.

## Usage
1. Set the `pdf_path` to the location of your PDF file.
2. Set the `output_folder` where the images will be saved.
3. Run the script, and it will create PNG images for each page in the output folder.

```bash
python pdf_to_image.py