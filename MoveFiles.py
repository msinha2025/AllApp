import os
import shutil
from datetime import datetime
import platform

def get_default_downloads():
    if platform.system() == "Windows":
        return os.path.join(os.environ["USERPROFILE"], "Downloads")
    else:
        return os.path.expanduser("~/Downloads")

def organise_files(source_dir, target_dir):
    if not os.path.exists(source_dir):
        print(f"Source folder not found: {source_dir}")
        return

    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if os.path.isfile(file_path):
            mtime = os.path.getmtime(file_path)
            date = datetime.fromtimestamp(mtime)
            year = str(date.year)
            month = f"{date.month:02d}"
            day = f"{date.day:02d}"

            dest_dir = os.path.join(target_dir, year, month, day)
            os.makedirs(dest_dir, exist_ok=True)

            dest_path = os.path.join(dest_dir, filename)
            shutil.move(file_path, dest_path)
            print(f"Moved: {filename} -> {dest_dir}")

def main():
    default_source = get_default_downloads()
    source_dir = input(f"Enter source folder path [{default_source}]: ").strip() or default_source
    target_dir = input("Enter target folder path [~/OrganisedFiles]: ").strip() or os.path.expanduser("~/OrganisedFiles")
    organise_files(source_dir, target_dir)

if __name__ == "__main__":
    main()