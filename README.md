# DocAutomater

DocAutomater is an automated document creation software that streamlines the process based on a provided list, utilizing customizable templates.

## Installation

1. Download the latest release from the [releases page](https://github.com/carbongo/docautomater/releases).
2. Open the `.exe` file (Windows) or `.app` file (Mac).

## Usage

### Input

- A table file (either `.csv` or `.xlsx`) containing the data to be inserted into the document. An example is included in the repository.
- A `.docx` document file containing the text to be modified. An example is included in the repository.

### Output

- A new `.docx` document file for each row in the table file. The new files will have the same text as the original document file, but with keywords replaced by the data from the table file.

### Steps

1. Create a list of people you want to create documents for in an Excel file, with each person a new line. The first column should be the name of the person, and the rest of the columns should be the data you want to insert into the document.
2. Create a template for each document you want to create. The template should be a Word document with the text you want to be the same for each person. For example, if you want to create a document for each person that says "Hello, [name]!", then your template should be a Word document with the text "Hello, [name]!".
3. Run the program and select the Excel file and the Word document as a template.
4. The program will create a new Word document for each person in the list, with the text from the template and the name of the person inserted in the appropriate places.

## Development

1. Clone the repository.
2. Install the requirements.
3. Run `python3 docautomater.py`.

## Requirements

- Python 3.x
- PySimpleGUI: For creating the GUI.
- pandas: For reading the table file (either `.csv` or `.xlsx`).
- python-docx: For reading and modifying the `.docx` document file.
- openpyxl: For reading `.xlsx` expanding pandas.

## FAQ

### Why is the program not working?

- Make sure you have the latest version of Python installed.
- Make sure you have installed all the requirements.
- Make sure you have selected the correct files.
- Make sure the table file is in the correct format.
- Make sure the template file is in the correct format.
- Make sure the template file contains the keywords you want to replace.
- Make sure the template file contains the keywords in special symbols, e.g. `%name%`, in order to avoid mixing up with regular words.
- Make sure the table file contains the column names in the first row.
