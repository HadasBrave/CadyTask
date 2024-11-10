from folder_data_runner import FolderDataRunner

def main():
    runner = FolderDataRunner()
    runner.ask_directory()
    runner.process_directory()

if __name__ == "__main__":
    main()


