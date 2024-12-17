import os
from pathlib import Path
import shutil

#we can change directory for a file using this
#os.chdir("")

#how to rename files in Python

for file in os.listdir():
    f = Path(file)

    #split into base name and extension 
    name,ext = f.stem, f.suffix

    splitted = name.split("-")
    splitted = [s.strip() for s in splitted]
    new_name = f"{splitted[3].zfill(2)}-{splitted[1]}-{splitted[2]}-{splitted[0]}{ext}"
    f.rename(new_name)

#how to make a new path
Path("data").mkdir(exist_ok=True)
# or 
if not os.path.exists("data"):
    os.mkdir("data")

shutil.move('source', 'destination')

#this is the template to clean up the desktop 


# audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
#          ".alac", ".amr", ".ape", ".au", ".dss",
#          ".flac", ".flv", ".m4a", ".m4b", ".m4p",
#          ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
#          ".opus", ".qcp", ".tta", ".voc", ".wav",
#          ".wma", ".wv")

# video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
#          ".mp4", ".m4p", ".m4v", ".mxf")

# img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
#        ".gif", ".webp", ".svg", ".apng", ".avif")

# def is_audio(file):
#     return os.path.splitext(file)[1] in audio

# def is_video(file):
#     return os.path.splitext(file)[1] in video

# def is_image(file):
#     return os.path.splitext(file)[1] in img

# def is_screenshot(file):
#     name, ext = os.path.splitext(file)
#     return (ext in img) and "screenshot" in name.lower()

# os.chdir("/Users/patrick/Desktop")

# for file in os.listdir():
#     if is_audio(file):
#         shutil.move(file, "Users/patrick/Documents/audio")
#     elif is_video(file):
#         shutil.move(file, "Users/patrick/Documents/video")
#     elif is_image(file):
#         if is_screenshot(file):
#             shutil.move(file, "Users/patrick/Documents/screenshots")
#         else:
#             shutil.move(file, "Users/patrick/Documents/images")
#     else:
#         shutil.move(file, "Users/patrick/Documents")