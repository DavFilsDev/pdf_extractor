import argparse
import os
from extractor.core import extract_pages

def main():
    parser = argparse.ArgumentParser(
        description="Extract a range of pages from a PDF file inside the input/ folder."
    )

    parser.add_argument(
        "-f", "--file", required=True,
        help="Name of the PDF file inside the 'input/' folder"
    )
    parser.add_argument(
        "-s", "--start", type=int, required=True,
        help="Start page number (1-based)"
    )
    parser.add_argument(
        "-e", "--end", type=int, required=True,
        help="End page number (inclusive, 1-based)"
    )

    args = parser.parse_args()

    input_dir = "input"
    output_dir = "output"

    input_path = os.path.join(input_dir, args.file)
    base_name = os.path.splitext(args.file)[0]
    output_filename = f"{base_name}_pages_{args.start}_to_{args.end}.pdf"
    output_path = os.path.join(output_dir, output_filename)

    try:
        extract_pages(input_path, output_path, args.start, args.end)
        print(f"✅ Successfully saved extracted pages to: {output_path}")
    except Exception as e:
        print(f"❌ Error: {e}")
