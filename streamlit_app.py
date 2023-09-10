import os
import logging
from pathlib import Path
from typing import List, Self
from dataclasses import dataclass
from io import BytesIO, StringIO
from enum import Enum

import streamlit as st
import pandas as pd
from pandas import DataFrame, Series

from service.custom_model import Transformer
from service.supabase_conn import SupabaseConnection, UserDB

# Page Config
st.set_page_config(
    page_title="DeepDetect",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

@st.cache_data
def pdf_loader(files: Path) -> BytesIO:
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

def model_consumption() -> List[str]:
    """Listening saved model from database and consume for predictions

    Returns
    -------
    List[str]
        Will return Benign or Malicious
    """
    ...
    
def send_interations_data():
    """Will send generated data from user interactions to database
    """
    ...


def main() -> None:
    st.title("😈 tf_transformers_malicious_pdf")
    st.markdown("This how we can detect the PDF are `Benign` or `Malicious` with Transformers Encoders implementations with TensorFlow")
    
    columns_1, columns_2 = st.columns(2)
    pdf_status = []
    with columns_1:
        uploaded_file = st.file_uploader("Choose the suspecting PDF files", type="pdf")
        if uploaded_file is not None:
            if uploaded_file.type == "application/pdf":
                pass
                
        
    with columns_2:
        st.markdown("## Your PDF Status")
        # *! This
        # for this moment give the ui if pdf are benign or malicious
        

if __name__ == '__main__':
    main()