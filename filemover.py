import os
import shutil
import argparse

source_folder = "./source_documents"
ignore_folder = "./ignore"
target_folder = "./loaded_documents"
desired_file_count = 30000  # Set your desired file count here

def count_files(folder_path):
    return len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])

def move_files(source_path, target_path, file_count):
    files_to_move = os.listdir(source_path)[:file_count]
    for file_name in files_to_move:
        source_file = os.path.join(source_path, file_name)
        target_file = os.path.join(target_path, file_name)
        shutil.move(source_file, target_file)
        #print(f"Moved {file_name} to {target_path}")

def fill_to_desired_count():
    source_file_count = count_files(source_folder)
    if source_file_count < desired_file_count:
        move_file_count = desired_file_count - source_file_count
        move_files(ignore_folder, source_folder, move_file_count)
    elif source_file_count > desired_file_count:
        move_file_count = source_file_count - desired_file_count
        move_files(source_folder, ignore_folder, move_file_count)
    print(f"Current file count in root folder: {count_files(source_folder)}")

def move_all_files():
    source_file_count = count_files(source_folder)
    move_files(source_folder, target_folder, source_file_count)
    print(f"Moved all files to destination folder. Total files moved: {source_file_count}")

parser = argparse.ArgumentParser(description="Monitor and manage files in folders.")
parser.add_argument("--done", action="store_true", help="Move all files to the destination folder.")
args = parser.parse_args()

if args.done:
    move_all_files()
else:
    fill_to_desired_count()
