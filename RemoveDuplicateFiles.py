import os
import hashlib

def file_hash(path, block_size=65536):
    hasher = hashlib.md5()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            hasher.update(block)
    return hasher.hexdigest()

def remove_duplicates(folder):
    hashes = {}
    for root, _, files in os.walk(folder):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                h = file_hash(file_path)
                if h in hashes:
                    print(f"Removing duplicate: {file_path}")
                    os.remove(file_path)
                else:
                    hashes[h] = file_path
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    folder = input("Enter folder path to remove duplicates: ").strip()
    if os.path.isdir(folder):
        remove_duplicates(folder)
    else:
        print("Invalid folder path.")