# 📄 pdf_extractor

A simple command-line tool to extract specific pages from a PDF file and save them into a new file.  
Great for quick page trimming without opening a heavy PDF editor.

---

## 🚀 Features

- 📥 Input files stored in an `input/` folder
- 📤 Outputs automatically saved in an `output/` folder (created if it doesn’t exist)
- ✅ Validates page ranges and file existence
- ⚙️ Simple CLI interface
- 🧪 Includes a sample PDF to test right away

---

## 🛠️ Installation

First, clone the repository and install the required packages:

```bash
git clone https://github.com/DavFilsDev/pdf_extractor.git
cd pdf_extractor
pip install -r requirements.txt
````

---

## 📁 Folder Structure

```
pdf_extractor/
│
├── extractor/           # Contains core PDF extraction logic
│   └── __init__.py
│   └── core.py
├── input/               # Place your input PDF files here
│   └── test_file.pdf    # A sample file to test extraction
├── output/              # Will be created automatically if missing
├── cli.py               # Command-line interface
├── main.py              # Entry point for the program
├── README.md            # All informations about the project
└── requirements.txt     # All dependancies used in the project
```

## 🧪 Usage

To extract pages from a PDF file located in the `input/` folder:

```bash
python main.py -f test_file.pdf -s 1 -e 2
```

This command will extract **pages 1 to 2** from the file `input/test_file.pdf` and create a new file:

```
output/test_file_pages_1_to_2.pdf
```


## ⚙️ CLI Arguments

| Argument        | Description                                        |
| --------------- | -------------------------------------------------- |
| `-f`, `--file`  | PDF filename to extract from (must be in `input/`) |
| `-s`, `--start` | Start page number (1-based index)                  |
| `-e`, `--end`   | End page number (inclusive)                        |

s
## 📦 Requirements

* Python 3.7+
* PyPDF2

Install dependencies with:

```bash
pip install -r requirements.txt
```

## 🎯 Example

Assuming `input/test_file.pdf` has more than 3 pages:

```bash
python main.py -f test_file.pdf -s 2 -e 4
```

Creates a new file in the `output/` folder:
`output/test_file_pages.pdf_2_to_4.pdf`

## 📄 First Use Test

A sample file named `test_file.pdf` is already provided in the `input/` folder.
Try this to test your setup immediately:

```bash
python main.py -f test_file.pdf -s 1 -e 2
```

## 🧭 Coming Soon

* Ability to specify a **custom output filename** using `--output` or `-o`.
Example (future use):

```bash
python main.py -f test_file.pdf -s 1 -e 3 -o my_summary.pdf
```

If this argument is not provided, the output filename will follow the default pattern:

```
output/test_file_pages_1_to_3.pdf
```

## 📝 License

MIT License.

## 👨‍💻 Author

**F. M. David Fils RATIANDRAIBE**  
🔗 [@DavFilsDev on GitHub](https://github.com/DavFilsDev)
