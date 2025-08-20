# 📦 7z Extractor (Python)

This repository provides a simple Python script to extract `.7z` archive files.
It uses the [py7zr](https://pypi.org/project/py7zr/) library to unpack archives into a target folder.

---

## 🚀 Features

* Extracts `.7z` archive files
* Automatically creates the output folder if it doesn’t exist
* Minimal and easy-to-understand Python code

---

## 🛠 Requirements

* Python 3.7+
* [py7zr](https://pypi.org/project/py7zr/)

---

## ⚡ Installation

Install the dependency:

```bash
pip install py7zr
```

---

## 📂 Usage

To extract `archive.7z` into a folder called `output_folder`:

```python
from pathlib import Path
import py7zr

src = Path("archive.7z")               # Input archive file
out_dir = Path("output_folder")      # Output folder
out_dir.mkdir(exist_ok=True)

with py7zr.SevenZipFile(src, mode='r') as archive:
    archive.extractall(path=out_dir)
```

---

## 🔍 Example

If `archive.7z` contains `example.txt`, after running the script you will get:

```
output_folder/
└── example.txt
```

---

## ❗ Notes

* Extraction may take a while for large archives.
* Ensure you have enough free disk space (the extracted size is often 2–3x larger than the archive).
* If the archive is password-protected:

  ```python
  with py7zr.SevenZipFile(src, 'r', password='YOUR_PASSWORD') as archive:
      archive.extractall(path=out_dir)
  ```

---

