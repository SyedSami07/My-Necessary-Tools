import os

prefix = "real_video_"
extensions = (".mp4", ".mov", ".mkv", ".avi")

files = sorted([f for f in os.listdir() if f.lower().endswith(extensions)])

for i, filename in enumerate(files, start=68):
    new_name = f"{prefix}{i:02}{os.path.splitext(filename)[1]}"
    os.rename(filename, new_name)
    print(filename, " -> ", new_name)