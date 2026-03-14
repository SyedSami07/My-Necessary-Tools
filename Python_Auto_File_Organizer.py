import os
import shutil

folder_path = input("Enter folder path to organize: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Archives": [".zip", ".rar", ".7z"],
    "Audio": [".mp3", ".wav"],
    "Programs": [".exe", ".msi"]
}

for folder in file_types:
    os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

os.makedirs(os.path.join(folder_path, "Others"), exist_ok=True)

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        moved = False
        ext = os.path.splitext(file)[1].lower()

        for folder, extensions in file_types.items():
            if ext in extensions:
                shutil.move(file_path, os.path.join(folder_path, folder, file))
                moved = True
                break

        if not moved:
            shutil.move(file_path, os.path.join(folder_path, "Others", file))

print("Files organized successfully!")