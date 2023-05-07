import os
import argparse
import textract
from PyPDF2 import PdfReader

def parse_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    raw_text = ''
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            raw_text += text
    
    return raw_text

def parse_pdf_textract(pdf_path):
    text = textract.process(pdf_path)
    return text

if __name__=="__main__":
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Extract text from a PDF file and save it to a text file')
    parser.add_argument('pdf_path', type=str, help='Path of the PDF file to extract text from')
    parser.add_argument('dest_dir', type=str, help='Path of the directory to save the text file to')

    parser.add_argument(
        "--textract",
        dest="use_textract",
        # type=bool,
        action="store_true",
        help="Whether or not to use textract",
        # required=False,
        # default=False,
    )

    # Parse the arguments
    args = parser.parse_args()

    # Call the parse_pdf function
    if args.use_textract:
        raw_text = parse_pdf_textract(args.pdf_path)
    else:
        raw_text = parse_pdf(args.pdf_path)

    out_fname = os.path.splitext(os.path.basename(args.pdf_path))[0] + '.txt'

    with open(os.path.join(args.dest_dir, out_fname), 'w') as f:
        f.write(raw_text)
        print(f'Output saved to {args.dest_dir}')