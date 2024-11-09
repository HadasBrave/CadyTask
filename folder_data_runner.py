from tkinter import filedialog
from tkinter import *
from pathlib import Path
from extract_data import ExtrctData

class FolderDataRunner:
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()
        self.folder_selected = filedialog.askdirectory()
        self.data = ExtrctData()
        self.process_directory()
        self.operating_range = self.data.operating_range

    def process_directory(self):
        direction_path = Path(self.folder_selected)
        txt_files = list(direction_path.glob("*.txt"))

        if not txt_files:
            print(f"No text files found in {self.folder_selected}")
            return

        for file_path in txt_files:
            try:
                self.data.get_operating_ranges(file_path)
            except Exception as e:
                print(f"Error processing {file_path.name}: {str(e)}")