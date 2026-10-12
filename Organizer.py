from pathlib import Path
import os


lib_path = Path(os.path.dirname(os.path.abspath(__file__))) #gets the current location of the python script

#creates a path for the following folders (Text, Pictures, PDF, Word, Excel, Other) in the same location as the Python script
text_path = Path(lib_path / "Text") 
images_path = Path(lib_path / "Pictures")
pdf_path = Path(lib_path / "PDF")
word_path = Path(lib_path / "Word")
excel_path = Path(lib_path / "Excel")
other_path = Path(lib_path / "Other")

#a file-type dictionary that contains the corresponding folder to file extensions
file_type = {
    "Text": (".txt",),
    "Images": (".jpg", ".png", ".jpeg"),
    "PDF": (".pdf",),
    "Word": (".doc", ".docx"),
    "Excel": (".xls", ".xlsx")
}

#checks first if the paths for the folders don't exit yet
if (not text_path.exists() or 
    not images_path.exists() or 
    not pdf_path.exists() or 
    not word_path.exists() or 
    not excel_path.exists() or 
    not other_path.exists()):

    #if yes, it creates the folders in the same location 
    text_path.mkdir(exist_ok=True, parents=True)
    images_path.mkdir(exist_ok=True, parents=True)
    pdf_path.mkdir(exist_ok=True, parents=True)
    word_path.mkdir(exist_ok=True, parents=True)
    excel_path.mkdir(exist_ok=True, parents=True)
    other_path.mkdir(exist_ok=True, parents=True)


#iteration for each file in the directory
for file in lib_path.iterdir():
    #if the file is a directory, it skips to the next iteration
    if file.is_dir():
        continue
    #it then checks the file in question its extension and moves it to the corresponding folder based on the file-type dictionary
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
