from PyPDF2 import PdfReader, PdfWriter
import os

def extract_pages(input_path, output_path, start_page, end_page):
    """
    Extracts a range of pages from a PDF and saves them to a new file.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"The file '{input_path}' does not exist.")

    reader = PdfReader(input_path)
    writer = PdfWriter()

    num_pages = len(reader.pages)
    if start_page < 1 or end_page > num_pages or start_page > end_page:
        raise ValueError(f"Invalid page range. This file contains {num_pages} pages.")

    for i in range(start_page - 1, end_page):  # 0-based index
        writer.add_page(reader.pages[i])

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "wb") as f:
        writer.write(f)
