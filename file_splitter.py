import os
import pandas as pd
import uuid
import csv
import sys

class FileSettings:
    def __init__(self, file_name, row_size=1000):
        self.file_name = file_name
        self.row_size = row_size

class FileSplitter:
    def __init__(self, file_settings):
        if not isinstance(file_settings, FileSettings):
            raise ValueError("Please pass a correct instance of FileSettings")

        self.file_settings = file_settings

        if not os.path.exists(self.file_settings.file_name):
            raise FileNotFoundError(f"File '{self.file_settings.file_name}' not found!")

        # Detect delimiter
        self.delimiter = self.detect_delimiter()

        # Read only header first
        try:
            with open(self.file_settings.file_name, "r", encoding="utf-8", errors="replace") as f:
                reader = csv.reader(f, delimiter=self.delimiter)
                self.headers = next(reader)  # Read first row as headers
        except Exception as e:
            raise ValueError(f"Error reading CSV file: {e}")

    def detect_delimiter(self):
        """Detects the delimiter of the CSV file automatically."""
        with open(self.file_settings.file_name, "r", encoding="utf-8", errors="replace") as f:
            first_line = f.readline()
            if ";" in first_line:
                return ";"
            elif "\t" in first_line:
                return "\t"
            else:
                return ","

    def run(self, directory="output_chunks"):
        os.makedirs(directory, exist_ok=True)
        counter = 1

        # Set a very high field size limit
        csv.field_size_limit(sys.maxsize)  # Set to maximum size

        # Read CSV line by line to prevent memory issues
        with open(self.file_settings.file_name, "r", encoding="utf-8", errors="replace") as infile:
            reader = csv.reader(infile, delimiter=self.delimiter)
            next(reader)  # Skip header row

            buffer = []
            for row in reader:
                if len(row) != len(self.headers):  # Skip malformed rows
                    continue

                buffer.append(row)

                if len(buffer) >= self.file_settings.row_size:
                    file_name = f"{directory}/{self.file_settings.file_name.split('.')[0]}_part_{counter}_{uuid.uuid4().hex}.csv"
                    
                    # Write chunk to file
                    with open(file_name, "w", encoding="utf-8", newline="") as outfile:
                        writer = csv.writer(outfile, delimiter=self.delimiter)
                        writer.writerow(self.headers)  # Write header
                        writer.writerows(buffer)  # Write chunk data
                    
                    print(f"Saved {file_name}")
                    counter += 1
                    buffer = []

        print("File splitting completed successfully.")

def main():
    try:
        file_name = "sample1.csv"  # Change to your actual file
        row_size = 500000  # Adjust row size based on RAM

        helper = FileSplitter(FileSettings(file_name=file_name, row_size=row_size))
        helper.run()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
