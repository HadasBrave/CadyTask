# Datasheet Range Extractor
A Python tool that extracts operating voltage and temperature ranges from electronic component datasheets using regular expressions.
## Overview
This tool processes text files containing datasheet information and extracts:

- Voltage ranges (min and max values)
- Temperature ranges (min and max values)

The system uses regular expressions to identify and parse these values, handling various formats and notations.
## Prerequisites

- Python 3.6 or higher
- tkinter (usually comes with Python installation)

## Installation

1. **Clone the repository**:
```bash
clone [your-repository-url]
 ```

2. *Navigate to the project directory**:
```bash
cd [project-directory]
 ```


## Usage
### Method 1: Run as Main Script
```bash
python main.py
 ```
This will:

1. Open a file dialog for folder selection
2. Process all .txt files in the selected folder
3. Print the extracted ranges

### Method 2: Import in Your Code
```bash
from folder_data_runner import FolderDataRunner

# Initialize the runner
folder_runner = FolderDataRunner()

# Select folder via dialog
folder_runner.ask_directory()

# Process all .txt files in the selected folder
folder_runner.process_directory()

# Access the extracted ranges
print(folder_runner.operating_range)
 ```
### File Processing
The system processes text files using two main classes:

- **ExtractData**: Handles the actual extraction of voltage and temperature ranges
- **FolderDataRunner**: Manages folder selection and batch processing of files

### Output Format
The extracted data is stored in the operating_range list as dictionaries with the following structure:
```bash
[
    {
        'voltage': {'min': float_value, 'max': float_value},
        'temperature': {'min': float_value, 'max': float_value}
    },
    # One entry per processed file
]
 ```
## Notes

- The system assumes voltage values are followed by V and temperature values by °C in the datasheet files.
- The voltage pattern matches formats like "3.3V to 5V"
- The temperature pattern matches various formats including negative values and different minus signs (- or –)
- If multiple ranges are found in a file, they must be identical or the system will return None for that range
- Files must be in .txt format
- The system handles different variations of temperature degree symbols (° or ⁰)

## Error Handling
The system includes comprehensive error handling:

- File reading errors are caught and reported
- Processing errors for individual files won't stop the entire batch
- Invalid format errors are handled gracefully
