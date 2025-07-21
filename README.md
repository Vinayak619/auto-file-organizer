# 🗂️ Auto File Organizer

A simple Python script that helps you keep your folders clean and organized by automatically sorting files into categorized directories like **Images**, **Documents**, **Videos**, **Music**, and **Others** based on file extensions.

---

## 🚀 Features

- Sorts all files in a directory into respective folders
- Supports common file types (JPG, PNG, PDF, MP3, MP4, etc.)
- Uses `tqdm` progress bar for better user feedback
- Automatically creates folders if they don’t exist
- Easy to use – just run and organize with a single command

---

## 📁 Categories Handled

- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, etc.
- **Documents**: `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`, etc.
- **Videos**: `.mp4`, `.mkv`, `.avi`, `.mov`, etc.
- **Music**: `.mp3`, `.wav`, `.aac`, `.flac`, etc.
- **Others**: Any unrecognized file types

---

## 🧠 How It Works

1. You provide the path to the folder you want to organize.
2. The script scans all files in that folder.
3. It determines the category of each file based on its extension.
4. It creates corresponding folders (if needed) and moves files accordingly.
5. A `tqdm` progress bar shows file-sorting status.

---

## 🛠️ Requirements

- Python 3.x
- [`tqdm`](https://pypi.org/project/tqdm/)

To install tqdm:

```bash
pip install tqdm
