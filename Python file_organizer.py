import os
import shutil

FILE_CATEGORIES = {
    "Images": [".jpeg", ".gif", ".jpg", ".png", ".bmp", ".tiff"],
    "Videos": [".mp4", ".mkv", ".avi", ".flv", ".mov"],
    "Documents": [".doc", ".pdf", ".txt", ".docx", ".xls", ".ppt", ".pptx", ".xlsx"],  # Fixed comma
    "Audio": [".mp3", ".aac", ".wav", ".flac", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Data": [".csv", ".json", ".xml"],
    "Others": []
}


def organize_files(directory):
    """Organizes files in the given dir based on their file type"""
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    for category in FILE_CATEGORIES:
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isdir(file_path):
            continue

        file_moved = False

        for category, extensions in FILE_CATEGORIES.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(directory, category, filename))
                file_moved = True
                break

        if not file_moved:
            shutil.move(file_path, os.path.join(directory, "Others", filename))

if __name__ == "__main__":
    directory_to_organize = input("Enter the directory path to organize: ")
    organize_files(directory_to_organize)
