from __future__ import annotations, print_function
import os
import tarfile
import zipfile
import random
import shutil
import csv
from typing import List
from pathlib import Path

HEADER = ['id', 'label', 'name','contents']
ID = 0


class MalwarePDFDataset:
    def __init__(self):
        super(MalwarePDFDataset, self).__init__()
        

    def extract_tar_file(self, file_name: str):
        """Extract the .tar.gz and remove it after

        Parameters
        ----------
        file_name : str
            The .tar.gz file source path
        """
        FILE_PATH = Path("data/")
        file = tarfile.open(FILE_PATH / f'{file_name}.tar.gz')
        file.extractall(FILE_PATH / f'{file_name}')
        file.close()
        os.remove(FILE_PATH / f'{file_name}.tar.gz')

    def zip_extract(self, folder_path: Path):
        """Extract the zip file in one time

        Parameters
        ----------
        folder_path : Path
            The target folder path

        Returns
        -------
        int
            Completing the extractions and return the sum of files in the folder
        """
        index += 1
        # TODO: Extract the Benign PDF files
        for filename in os.listdir(folder_path):
            if filename.endswith(".zip"):
                zip_file_path = folder_path / filename  # Full path to the ZIP file
                # TODO: Splitting the zip file name with its extensions as folder name
                benign_folder = os.path.splitext(os.path.basename(filename))[0] + index
                if not os.path.isdir(benign_folder):
                    try:
                        # TODO: Extract all the pdf files and move to initialized folder
                        zip = zipfile.ZipFile(zip_file_path, 'r')
                        os.mkdir(benign_folder)
                        zip.extractall(path=benign_folder)
                    # Handle bad zip files
                    except zipfile.BadZipfile as e:
                        print("BAD ZIP: " + str(zip_file_path))
                        try:
                            os.remove(zip_file_path)
                        except OSError as e:
                            if e.errno != errno.ENOENT:
                                raise
        index += 1
        return len(os.listdir(folder_path))
        
    
    def spliting_data(self, source: Path, destination: Path, train_split: int) -> None:
        """Manually spliting the data to training and testing folders

        Parameters
        ----------
        source : Path
            The base pdf folder target
        destination : Path
            The randomize pdf file spread to specific folder
        train_split : int
            The train split percentage
        """
        for file_name in random.sample(os.listdir(source), train_split):
            shutil.move(os.path.join(source, file_name), destination)

        for file in os.listdir(source):
            os.rename(os.path.join(source, file), os.path.join(destination, file))

        return "Splitting and Renaming from {} to {} are completed".format(
            source, destination
        )
        
    def get_file_byte_string(self, file):
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
                
    def create_row(self, filetype, file, writer):
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
        bytecode = self.get_file_byte_string(file)
        file_data.append(bytecode)
        writer.writerow(file_data)
        file_data.clear()
        ID += 1
        
    
    def csv_generator(self, file_name: str) -> None:
        """Generate csv files for containing PDF fileto Byte Stream data
        """
        with open('testing.csv', 'a+') as testing_csv:
            writer = csv.writer(testing_csv)
            writer.writerow(HEADER)
            #benign first
            for benign_file in os.listdir(os.path.join('Testing', 'Benign')):
                #put all this into "do_list_creation(filetype, file) function"
                self.create_row(0, os.path.join('Testing', 'Benign', benign_file), writer)
            #now malicious
            for malicious_file in os.listdir(os.path.join('Testing', 'Malicious')):
                self.create_row(1, os.path.join('Testing', 'Malicious', malicious_file), writer)
    
    
if __name__ == "__main__":
    ...