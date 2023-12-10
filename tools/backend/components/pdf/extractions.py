import os
from io import BytesIO
from typing import List, Dict
from pathlib import Path
from dataclasses import dataclass
import streamlit as st


@dataclass
class GlobalData:
    HEADER = ['id', 'label', 'name', 'contents']
    PPATH = os.getcwd()
    DPATH = Path(f'{PPATH}/data/')

    @classmethod
    def get_benign(cls) -> Dict:
        return {"name": "Benign", "type": 0}

    @classmethod
    def get_malicious(cls) -> Dict:
        return {"name": "Malicious", "type": 1}


def pdf_loader(files: str) -> BytesIO:
    """_summary_

    Parameters
    ----------
    files : Path
        The files sources from st.file_uploader

    Returns
    -------
    BytesIO
        Converting PDF file to byte stream. Performing encoding with One Hot Encoding and n-grams.
    """
    ...
