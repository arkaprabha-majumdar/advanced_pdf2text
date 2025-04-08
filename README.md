# advanced_pdf2text

## Overview
Most traditional PDF-to-text tools follow one of two approaches:
1. Extract the embedded text layer directly from the PDF.
2. Extract images from the PDF, without converting them to text.

This project takes a different approach.

## What it does
`advanced_pdf2text` converts PDF pages into images and then applies OCR (Optical Character Recognition) to extract text from those images. 

This allows us to capture *all* the text in a document — including text inside diagrams, charts, schematics, or mechanical drawings — which typical PDF readers would miss.

## Why is this useful?
This is especially powerful when processing technical documents or scanned PDFs where valuable information may only exist within images. The extracted text can then be passed downstream into NLP pipelines (like Langchain), enriching the context and enabling better insights from otherwise inaccessible data.

## Notes
- Modern paid tools like Microsoft Document Intelligence provide similar functionality.
- This project is free and open-source.

## Usage
pdf → images → OCR → text
