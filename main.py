#
#              Made by Happy
#
import os
import re
import zipfile
import random

def extract_numbers_from_filename(filename):
    # Extract numbers from the filename using regular expression
    match = re.search(r'\d+', filename)
    if match:
        return int(match.group())
    return None
def extract_numbers_from_randomized_zip(zip_file_path, target_filename_pattern):
    numbers = []
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        for file_info in zip_ref.infolist():
            if re.match(target_filename_pattern, file_info.filename):
                # Extract numbers from the target file's name
                numbers.extend(re.findall(r'\d+', file_info.filename))
    return numbers
def scan_folder_for_files(folder_path, file_pattern, target_filename_pattern):
    file_numbers = []
    zip_file_numbers = []
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if re.match(file_pattern, file_name):
                # Extract numbers from the file name
                numbers = extract_numbers_from_filename(file_name)
                if numbers is not None:
                    file_numbers.append(numbers)
                if file_name.endswith('.zip'):
                    zip_file_path = os.path.join(root, file_name)
                    numbers_from_zip = extract_numbers_from_randomized_zip(zip_file_path, target_filename_pattern)
                    zip_file_numbers.extend(numbers_from_zip)

    return file_numbers, zip_file_numbers
folder_path = input("Enter the path to the UMA folder: ")
file_pattern = r'\d+_uma'
target_filename_pattern = r'\d+_sf'
file_numbers, zip_file_numbers = scan_folder_for_files(folder_path, file_pattern, target_filename_pattern)
for i in range(len(file_numbers)):
    os.system("start \" \" http://localhost:4322/uma20/api/v2/pdf/" + str(file_numbers[i]) + "/" + str(zip_file_numbers[i]) + "_sf")
