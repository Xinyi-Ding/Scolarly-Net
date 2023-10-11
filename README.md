# Analysis Prototype for Formative Assessment

## Summary of functionality
### Main functionality:
1. This code can read the metadata of the paper from an Excel file (index.xlsx), such as the name of the paper, the path to the PDF file, and so on.
2. This code can connect to a SQLite database (test_db.sqlite) and define three tables: papers (information about papers), entities (information about entities), and papers_have_entities (information about the association of papers with entities).
3. This code can convert PDF files to DOCX files.
4. This code can analysis the text of the paper into entities and the entity information was stored as a JSON file and save the entities in the SQLite.
5. This code provide a command line interface that allows the user to enter queries to retrieve entity-related papers from SQLite database.

### User Diagram

![User_Diagram](image/PSD.png)

The user starts the code in a command line terminal. The code starts execution, loading the configuration and database connection. If it is the first run or if there are new articles in the papers folder, the code will use pdf2docx, spaCy library to analyse the articles and the analysed article entities information will be saved in the SQLite database. After that the code will wait for the user to enter the query command in the command line. When the code receives the user's input, it parses the query command and generates a SQL command to retrieve the relevant information from the SQLite database, The code displays the results of the query in a readable form on the command line terminal, showing the papers that match the query condition. The user can continue to enter new query commands, or enter "q" to exit the code. If the user chooses to exit, the code ends execution.

## Dependence
### Python
This code was made by Python, and need using Python3 to run. The later [Section](#setup-conda) supply the instruction about installing conda to work with Python.

### Used Library
#### Built-In Library
1. json: this is a built-in library for Python to process data in JSON format. In this prototype code, It is used to store information about text and entities in JSON format in a file. 
2. os: this is a built-in library for Python that provides features to interact with the operating system, such as file and directory management.
3. sqlite3: this is a built-in library for Python to interact with SQLite databases. In this code, it is used to connect to SQLite databases, execute SQL queries, and manage database tables.

#### Third-party Library
1. pdf3docx: this is python library for converting PDF files to DOCX format. It allows to extract the contents of a PDF document into a DOCX file in Microsoft Word. In this code it is used to convert research paper in PDF format to DOCX format for subsequent processing of text and entities.
2. docx: this is part of the Python-docx library, which is used to create and manipulate Microsoft Word DOCX files. It is used to read and process converted DOCX format research paper files.
3. simplify_docx: this is a Python library for simplifying and extracting text content from DOCX files, removing special characters, etc. it used to extract the text in DOCX files and convert it to JSON format for further processing and storage.
4. spacy: this is a natural language processing library that provides a rich set of NLP features, including text processing, entity recognition, text classification, and more. Its website is https://spacy.io/. it is used to load English NLP models for entity recognition of text in DOCX files.
5. openpyxl: this is a Python library for reading and writing Excel files (.xlsx format). For this code, it is used to load the meta data for the research paper from Excel file.
6. prompt_toolkit: this is a Python library for building interactive command line interfaces, providing features such as auto-completion and history. Using this in this code can allow user to enter query commands without directly write SQL query commands.

## Instruction
### Running Instruction
``` bash
git clone https://git.ecdf.ed.ac.uk/psd2324/Carlson-Johnson
cd Carlson-Johnson
tar -xf papers.tar.gz
python prototype.py
```

### Setup Python Environment
#### Setup Conda
The instruction for installing conda from Anaconda:\
1. Open [Anaconda Download](https://www.anaconda.com/download) page and choose the package that suitable for your computer system. If you use the anaconda graphical installer, please fllow their installisation steps and ignore the steps below.
2. If you want to use the Commond line installer for Linux and Mac, download the *****.sh installer.
3. Run the following commond in your terminal:
```bash
cd the_path_your_download_sh
chmod +x *****.sh
./*****.sh
```
4. When you meet this please Enter Yes:
```text
Do you accept the license terms? [yes|no]
[no] >>>
```
5. When you meet this please Press Enter:
```text
[home/you/miniconda3] >>>
```
6. When you meet this please Enter Yes to setup conda in bash.
```text
installation finished.
Do you wish the installer to initialize Miniconda3 in your /home/you/.bashrc ? [yes|no]
[no] >>>
```
7. There are some useful conda commond:
```bash
# to create a conda environment
conda create -n env_name
# to activate a conda environment
conda activate env_name
# to quit a conda environment
conda deactivate
# to install a package in environment
conda install package_name
pip install package_name
```
#### Setup Requirement
If using conda:
```bash
conda create -n PSD python==3.9.0
conda activate PSD
pip install -r requirement.txt
```
If using python virtual environment:
```bash
mkdir my_project_venv
python3 -m venv my_project_venv
source my_project_venv/bin/activate
pip install -r requirement.txt
```
#### Common Setup Environment Error
When run the prototype.py, it might show:
```text
RuntimeError: cannot find builtin font with name 'Arial'
```
Solution: Go to your anaconda3’s installed package folder, find the path Anaconda3/envs/pdf2docx/Lib/site-packages/pdf2docx/common/constrants.py. Change 
DEFAULT_FONT_NAME = ‘Arial’ to ‘helv’. This is link to the official [#issue](https://github.com/dothinking/pdf2docx/issues/216) from pdf2docx in GitHub.











