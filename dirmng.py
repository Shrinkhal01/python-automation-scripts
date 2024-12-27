import os
import shutil

# Define the Downloads folder path
downloads_folder = os.path.expanduser("~/Downloads")

# Define the file type categories and their respective folders
file_categories = {
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv"],
    "Archives": [".zip", ".tar", ".gz", ".7z", ".rar"],
    "Code": [".py", ".java", ".c", ".cpp", ".js", ".html", ".css", ".sh"],
    "Others": []  # Files that don't match any category
}

# Create category folders if they don't exist
for category in file_categories.keys():
    category_path = os.path.join(downloads_folder, category)
    os.makedirs(category_path, exist_ok=True)

# Function to move a file to its respective category folder
def move_file(file_name, category_folder):
    src = os.path.join(downloads_folder, file_name)
    dest = os.path.join(category_folder, file_name)
    shutil.move(src, dest)

# Organize the files
for file_name in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, file_name)
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(file_name)[1].lower()
        moved = False
        
        # Check which category the file belongs to
        for category, extensions in file_categories.items():
            if file_extension in extensions:
                move_file(file_name, os.path.join(downloads_folder, category))
                moved = True
                break
        
        # If no category matches, move the file to "Others"
        if not moved:
            move_file(file_name, os.path.join(downloads_folder, "Others"))

print("Downloads folder organized successfully!")
