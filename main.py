import hashlib
import tkinter as tk
from tkinter import filedialog
import os


def analyze_file(file_path):
    try:
        # Calculate MD5 hash of the file
        md5_hash = hashlib.md5()
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                md5_hash.update(chunk)
        file_hash = md5_hash.hexdigest()

        # Get file metadata
        file_metadata = {
            'Name': os.path.basename(file_path),
            'Path': file_path,
            'Size': os.path.getsize(file_path),
            'MD5 Hash': file_hash
        }

        print("File Metadata:")
        for key, value in file_metadata.items():
            print(f"{key}: {value}")
        print("")

    except Exception as e:
        print(f"Error analyzing file {file_path}: {e}")


def choose_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    directory_path = filedialog.askdirectory(title="Choose Directory")
    if directory_path:
        analyze_directory(directory_path)


def analyze_directory(directory_path):
    try:
        # Traverse the directory and analyze each file
        for root, _, files in os.walk(directory_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                analyze_file(file_path)

    except Exception as e:
        print(f"Error analyzing directory {directory_path}: {e}")


def main():
    choose_directory()


if __name__ == "__main__":
    main()