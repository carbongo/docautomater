# docautomater

Automated document creation software that streamlines the process based on a provided list, utilizing customizable templates.

## Requirements

- Python 3.6+
- [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)

## Installation
1. Clone the repository
2. Install the requirements
3. Run `python3 docautomater.py`

## Usage
1. Create a list of people you want to create documents for in an Excel file, with each person a new line. The first column should be the name of the person, and the second column should be the name of the document you want to create for them.
2. Create a template for each document you want to create. The template should be a Word document with the text you want to be the same for each person. For example, if you want to create a document for each person that says "Hello, [name]!", then your template should be a Word document with the text "Hello, [name]!".
3. Run the program and select the Excel file and the Word document as a template.
4. The program will create a new Word document for each person in the list, with the text from the template and the name of the person inserted in the appropriate places.