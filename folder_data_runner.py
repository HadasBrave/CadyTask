from tkinter import filedialog
import tkinter as tk
from pathlib import Path
from extract_data import ExtrctData


class FolderDataRunner:
    def __init__(self):
        self.data = ExtrctData()
        self.operating_range = self.data.operating_range

    def ask_directory(self):
        try:
            # ask for the folder directory
            self.root = tk.Tk()
            self.root.withdraw()
            self.folder_selected = filedialog.askdirectory()
        except Exception as e:
            print(f"Error processing: {str(e)}")

    def process_directory(self):
        # convert directoty from string to Path
        direction_path = Path(self.folder_selected)
        # select all the txt files in the directory
        txt_files = list(direction_path.glob("*.txt"))

        if not txt_files:
            print(f"No text files found in {self.folder_selected}")
            return
        # run get_operating_ranges() on all the files
        for file_path in txt_files:
            try:
                self.data.get_operating_ranges(file_path)
            except Exception as e:
                print(f"Error processing {file_path.name}: {str(e)}")