import argparse
import os

from src.extractor.extract_pdf import extract_pdf
from src.extractor.extract_image import extract_image
from src.extractor.extract_text import extract_text
from src.extractor.extract_xlsx import extract_xlsx
from src.display import display_table


def create_parser():
    parser = argparse.ArgumentParser(description="DocuMind CLI - Text,xlsx,png,pdf to csv,json")
    parser.add_argument("-i", "--input",required=True,help="Path to the input file (TXT, PDF, image, or Excel)")
    parser.add_argument("-f", "--format",choices=["csv", "json"],default="json",help="Output format")
    return parser

def parse_file(file_path):
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return extract_pdf(file_path)

    elif extension in [".png", ".jpg", ".jpeg", ".bmp", ".tiff"]:
        return extract_image(file_path)

    elif extension == ".txt":
        return extract_text(file_path)

    elif extension in [".xlsx", ".xls"]:
        return extract_xlsx(file_path)

    else:
        raise ValueError(
            "Unsupported file format: " + extension
        )

