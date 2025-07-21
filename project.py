# Auto File Organizer
import os
import shutil
from tqdm import tqdm

def main():
    directory = input("Enter the path to the folder to organize: ").strip()
    if not os.path.exists(directory):
        print("Invalid path!")
        return
    files = file_list(directory)
    if not files:
        print("No files to organize.")
        return
    move_file(files, directory)
    print("\n✅ All files organized successfully!")


def file_list(directory):
    files = []
    for entry in os.listdir(directory): # looping through files
        full_path = os.path.join(directory, entry)
        if os.path.isfile(full_path):
            files.append(full_path)
    return files


def category(filename):
    extension = os.path.splitext(filename)[1].lower()  # extract files extenstion
    categories = {
        '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images',
        '.mp3': 'Music', '.wav': 'Music',
        '.mp4': 'Videos', '.mkv': 'Videos',
        '.pdf': 'Documents', '.docx': 'Documents', '.txt': 'Documents',
        '.zip': 'Archives', '.rar': 'Archives',
    }
    
    return categories.get(extension, 'Others')


def move_file(file_list, directory):
    for file in tqdm(file_list, desc="Organizing"):
        cat = category(file)
        target_dir = os.path.join(directory, cat)
        
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)   # create folder
        shutil.move(file, os.path.join(target_dir, os.path.basename(file)))



if __name__ == "__main__":
    main()