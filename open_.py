import os

def open_file(file_path):
    try:
        os.startfile(file_path)
    except OSError as e:
        print(f"Error: {e}")
