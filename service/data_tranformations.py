from __future__ import annotations, print_function
import os
import tarfile
import zipfile
import random
import shutil
import csv
from typing import List
from pathlib import Path
import glob

HEADER = ['id', 'label', 'name','contents']
ID = 0


class MalwarePDFDataset:
    def __init__(self):
        super(MalwarePDFDataset, self).__init__()
        

def extract_tar_file(folder_name: str):
    """Extract the .tar.gz and remove it after

    Parameters
    ----------
    folder_name : str
        The .tar.gz file source path (without extension)
    """
    
    SOURCE_PATH = Path("../source")
    # os.makedirs(SOURCE_PATH, exist_ok=True)
    file_path = SOURCE_PATH / f'{folder_name}.tar.gz'

    if not file_path.exists():
        return f"File not found: {file_path}"
    try:
        file = tarfile.open(file_path)
        file.extractall(SOURCE_PATH)
        file.close()
        os.remove(file_path)
        
        extracted_path = os.listdir(SOURCE_PATH / folder_name)
        
        index = 1
        for filename in extracted_path:
            old_path = SOURCE_PATH / folder_name / filename
            new_path = SOURCE_PATH / folder_name / f"{folder_name}_{index}.zip"
            os.rename(old_path, new_path)
            index += 1
        return f"Extraction {folder_name}.tar.gz completed successfully"
    
    except Exception as e:
        return f"An error occurred: {str(e)}"     
    

def zip_extract(folder_path: str):
    """Extract the zip file in one time and Delete the files afterwards

    Parameters
    ----------
    folder_path : str
        The target folder path

    Returns
    -------
    str
        Completing the extractions and return a message
    """
    
    # Create the target folder if it doesn't exist
    SOURCE_PATH = Path(f"../source/{folder_path}")
    
    if not SOURCE_PATH.is_dir():
        os.mkdir(SOURCE_PATH)

    # TODO: Extract the Benign PDF files
    for filename in os.listdir(SOURCE_PATH):
        if filename.endswith(".zip"):
            zip_file_path = SOURCE_PATH / filename  # Full path to the ZIP file
            # TODO: Splitting the zip file name with its extensions as folder name
            sub_folder = SOURCE_PATH / os.path.splitext(os.path.basename(filename))[0]
            if not sub_folder.is_dir():
                try:
                    # TODO: Extract all the pdf files and move to initialized folder
                    with zipfile.ZipFile(zip_file_path, 'r') as zip:
                        zip.extractall(path=sub_folder)
                    
                    # Delete the zip file after extraction
                    os.remove(zip_file_path)
                
                # Handle bad zip files
                except zipfile.BadZipfile as e:
                    print("BAD ZIP: " + str(zip_file_path))
                    try:
                        os.remove(zip_file_path)
                    except OSError as e:
                        if e.errno != errno.ENOENT:
                            raise
    
    length_dir = len(os.listdir(SOURCE_PATH))                    
    message = f"The {SOURCE_PATH} zip files successfully extracted. The length of directories: {length_dir}"
    
    return SOURCE_PATH, length_dir, message
        
    
def spliting_data(source_folder, split_ratio=0.8):
    """_summary_

    Parameters
    ----------
    source_folder : _type_
        _description_
    split_ratio : float, optional
        _description_, by default 0.8

    Returns
    -------
    _type_
        _description_
    """
    
    DEST_PATH = Path(f"../data/{source_folder}")
    SOURCE_PATH = Path(f"../source/{source_folder}")

    train_dir = DEST_PATH / 'train'
    test_dir = DEST_PATH / 'test'
    
    os.makedirs(train_dir, exist_ok=True)  # Create train_dir if it doesn't exist
    os.makedirs(test_dir, exist_ok=True)   # Create test_dir if it doesn't exist
        
    for folder in os.listdir(SOURCE_PATH):
        folder_path = os.path.join(SOURCE_PATH, folder)  # Full path to the subfolder

        # Check if it's a directory
        if os.path.isdir(folder_path):
            # Get the list of files in the folder
            files = os.listdir(folder_path)

            # Split the files into train and test sets
            train_files = files[:int(len(files) * split_ratio)]
            test_files = files[int(len(files) * split_ratio):]

            # Copy the train files to the train directory
            for file in train_files:
                src_file_path = os.path.join(folder_path, file)
                dst_file_path = os.path.join(train_dir, file)
                shutil.copy(src_file_path, dst_file_path)

            # Copy the test files to the test directory
            for file in test_files:
                src_file_path = os.path.join(folder_path, file)
                dst_file_path = os.path.join(test_dir, file)
                shutil.copy(src_file_path, dst_file_path)
            
    shutil.rmtree(SOURCE_PATH)  # Remove the source folder after splitting
    
    return f"Splitting {source_folder} is completed"

        
def get_file_byte_string(file):
    """Converting PDF file to byte stream. Performing encoding with One Hot Encoding and n-grams.

    Parameters
    ----------
    file : _type_
        _description_

    Returns
    -------
    bytes
        Resulting 
    """
    curr_file = open(file, "rb")
    data = curr_file.read()
    data_str = str(data)
    data_delim = ' '.join(data_str[i:i+4] for i in range(0, len(data_str), 4))
    data_bytes = bytes(data_delim, 'utf-8')
    curr_file.close()
    return data_bytes
                
def create_row(filetype, file, writer):
    """Generate the da

    Parameters
    ----------
    filetype : _type_
        _description_
    file : _type_
        _description_
    writer : _type_
        _description_
    """
    global ID
    file_data = []
    file_data.append(id)
    file_data.append(filetype)
    file_data.append(os.path.basename(os.path.normpath(file)))
    bytecode = get_file_byte_string(file)
    file_data.append(bytecode)
    writer.writerow(file_data)
    file_data.clear()
    ID += 1
        
    
def csv_generator(file_name: str) -> None:
    """_summary_

    Parameters
    ----------
    file_name : str
        _description_

    Returns
    -------
    _type_
        _description_
    """
    
    # Specify the column name
    HEADER = ['id', 'label', 'name','contents']
    
    with open('testing.csv', 'a+') as testing_csv:
        writer = csv.writer(testing_csv)
        writer.writerow(HEADER)
        #benign first
        for benign_file in os.listdir(os.path.join('Testing', 'Benign')):
            #put all this into "do_list_creation(filetype, file) function"
            create_row(0, os.path.join('Testing', 'Benign', benign_file), writer)
        #now malicious
        for malicious_file in os.listdir(os.path.join('Testing', 'Malicious')):
            create_row(1, os.path.join('Testing', 'Malicious', malicious_file), writer)
            
    with open('training.csv', 'a+') as training_csv:
        writer = csv.writer(training_csv)
        writer.writerow(HEADER)
        #benign
        for benign_file in os.listdir(os.path.join('Training', 'Benign')):
            create_row(0, os.path.join('Training', 'Benign', benign_file), writer)
        #now malicious
        for malicious_file in os.listdir(os.path.join('Training', 'Malicious')):
            create_row(1, os.path.join('Training', 'Malicious', malicious_file), writer)
    
    return "Succesfully Completed"
    
if __name__ == "__main__":
    
    # DATA_PATH = Path("../data")
    # if not os.path.exists(DATA_PATH):
    #     os.mkdir(DATA_PATH)
    
    BENIGN: str = "Benign"
    MALICIOUS: str = "Malicious"
    
    # benign_extract = extract_tar_file(BENIGN)
    # print(benign_extract)
    # malicious_extract = extract_tar_file(MALICIOUS)
    # print(malicious_extract)
    
    # benign_zip_extract = zip_extract(BENIGN)
    # print(benign_zip_extract)
    # malicious_zip_extract = zip_extract(MALICIOUS)
    # print(malicious_zip_extract)
    
    # split_benign = spliting_data(source_folder = BENIGN, split_ratio=0.8)
    # print(split_benign)
    # split_malicious = spliting_data(source_folder = MALICIOUS, split_ratio=0.8)
    # print(split_malicious)
    
    