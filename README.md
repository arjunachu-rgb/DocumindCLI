# DocuMind CLI – Document Data Extractor

## 1. Project Overview

DocuMind CLI is a Python command-line application that extracts text and data from different file formats and converts the extracted content into CSV or JSON files.

It supports PDF documents, images, text files, and Excel spreadsheets.

## 2. Features

- Extract text from PDF files.
- Extract text from images using OCR.
- Read text files.
- Extract tabular data from Excel files.
- Display extracted data in the terminal.
- Export extracted data to CSV and JSON formats.
- Handle missing files and unsupported file formats.

## 3. Technologies and Libraries

- **Python:** Main programming language.
- **argparse:** Handles command-line arguments.
- **os:** Handles file paths and file operations.
- **pdfplumber:** Extracts text from PDF files.
- **Pillow:** Opens and processes images.
- **pytesseract:** Extracts text from images using OCR.
- **pandas:** Processes tabular data and creates CSV files.
- **openpyxl:** Supports reading Excel `.xlsx` files.
- **tabulate:** Displays data in a readable terminal table.
- **json:** Writes extracted data to JSON files.

**External requirement:** Tesseract OCR must be installed separately for image text extraction.

## 4. Project Structure

```text
DocumindCLI/
├── Documind.py
├── summarizer.py
├── READ ME.md
├── requirement.txt
├── Result/
└── src/
    ├── parser.py
    ├── display.py
    ├── extractor/
    │   ├── extract_pdf.py
    │   ├── extract_image.py
    │   ├── extract_text.py
    │   └── extract_xlsx.py
    └── convert/
        ├── convert_csv.py
        └── convert_json.py
```

## 5. Installation

Install the required Python libraries by running:

```bash
pip install -r requirement.txt
```

Make sure Python and Tesseract OCR are installed on your system.

## 6. How to Run

Open a terminal in the project folder.

### Convert a file to JSON

```bash
python Documind.py -i sample.pdf -f json
```

### Convert a file to CSV

```bash
python Documind.py -i sample.xlsx -f csv
```

Replace `sample.pdf` or `sample.xlsx` with the path to your input file.

### Supported input formats

- PDF: `.pdf`
- Images: `.png`, `.jpg`, `.jpeg`, `.bmp`, `.tiff`
- Text: `.txt`
- Excel: `.xlsx`, `.xls`

### Supported output formats

- CSV: `.csv`
- JSON: `.json`

If the output format is not specified, JSON is selected by default.

## 7. Output

The extracted data is displayed in the terminal and the converted output file is saved in the `Result/` folder.

## 8. Error Handling

DocuMind CLI checks whether the input file exists and reports unsupported file formats.

## 9. Future Improvements

- Improve table extraction from images.
- Support input files provided through URLs.
- Add document summarization.
- Improve structured data extraction.


## About the Developer

**Name:** Arjun S. S.  
**Degree:** B.E. Computer Science and Engineering  
**Graduation Year:** 2027

### Developer Information
- **GitHub:** [My GitHub Profile](https://github.com/arjunachu-rgb)
- **Project:** DocuMind CLI
- **Programming Language:** Python

### Contact
For questions, suggestions, or collaboration, feel free to connect with me through GitHub.

---

*Developed as a mini project to explore document processing and data extraction using Python.*
