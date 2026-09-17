from pathlib import Path
import os

lib_path = Path(os.path.dirname(os.path.abspath(__file__)))
print(lib_path)
text_path = Path(lib_path / "Text")
images_path = Path(lib_path / "Pictures")
pdf_path = Path(lib_path / "PDF")
word_path = Path(lib_path / "Word")
excel_path = Path(lib_path / "Excel")
other_path = Path(lib_path / "Other")


file_type = {
    "Text": (".txt",),
    "Images": (".jpg", ".png", ".jpeg"),
    "PDF": (".pdf",),
    "Word": (".doc", ".docx"),
    "Excel": (".xls", ".xlsx")
}

text_path.mkdir(exist_ok=True, parents=True)
images_path.mkdir(exist_ok=True, parents=True)
pdf_path.mkdir(exist_ok=True, parents=True)
word_path.mkdir(exist_ok=True, parents=True)
excel_path.mkdir(exist_ok=True, parents=True)
other_path.mkdir(exist_ok=True, parents=True)

for file in lib_path.iterdir():
    if file.is_dir():
        continue
    if(file.suffix in file_type["Text"]):
        os.rename(lib_path/file, text_path/file.name)
    elif(file.suffix in file_type["Images"]):
        os.rename(lib_path/file, images_path/file.name)
    elif(file.suffix in file_type["PDF"]):
        os.rename(lib_path/file, pdf_path/file.name)
    elif(file.suffix in file_type["Word"]):
        os.rename(lib_path/file, word_path/file.name)
    elif(file.suffix in file_type["Excel"]):
        os.rename(lib_path/file, excel_path/file.name)
    else:
        os.rename(lib_path/file, other_path/file.name)

print("File organized successfully!")