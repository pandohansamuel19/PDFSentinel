import os
import logging
import time
from pathlib import Path
from typing import List, Dict
from dataclasses import dataclass
from io import BytesIO, StringIO
from enum import Enum
from uuid import UUID

import streamlit as st
import pandas as pd
from pandas import DataFrame, Series

from tools.backend.database.supabase_conn import SupabaseConnection, UserDB
from tools.pages import about, flow_control, history, paper_resources, welcome
from tools.pdf_transform.pdf_transform import DataTransformations

# Page Config
st.set_page_config(
    page_title="tf_transformers_malicious_pdf",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded",
)


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


def model_consumption(model_type: str, content_data: str) -> List[str]:
    """Listening saved model from database and consume for predictions

    Returns
    -------
    List[str]
        Will return Benign or Malicious
    """

    ...


def send_interations_data(
    id: UUID, initial_date: str, files_name: str, pdf_status: GlobalData
) -> str:
    """Will send generated data from user interactions to database
    """
    ...


def main() -> None:
    columns_1, columns_2 = st.columns(2)
    pdf_status = []

    st.title("😈 tf_transformers_malicious_pdf")
    st.markdown("This how we can detect the PDF are `Benign` or `Malicious` with Transformers Encoders implementations with TensorFlow")
    st.markdown("## Upload and Detect")
    with st.expander("Choose your way to upload the Suspected PDF file"):
        file_upload, link_upload = st.tabs(
            ["Upload PDF Here", "Upload PDF Link"])

        # TODO: user can uploading the suspected pdf here
        with file_upload:
            uploaded_file = st.file_uploader(
                "Choose the suspecting PDF files", type="pdf")
            if uploaded_file is not None:
                if uploaded_file.type == "application/pdf":
                    return

            st.button("Detect", type="primary", key=1)
            if st.button:
                decision = "Benign"
                # with st.spinner('Wait for it...'):
                #     time.sleep(5)
                if decision == "Benign":
                    st.success('THIS PDF FILE ARE BENIGN', icon="✅")
                elif decision == "Malicious":
                    st.error('THIS PDF FILE ARE MALICIOUS', icon="🚨")

        with link_upload:
            # Store the initial value of widgets in session state
            # st.text_input(
            #     "Placeholder for the other text input widget",
            #     "This is a placeholder",
            #     key="placeholder",
            # )

            # if "visibility" not in st.session_state:
            #     st.session_state.visibility = "visible"
            #     st.session_state.disabled = False

            text_input = st.text_input(
                "Enter some text 👇",
                # label_visibility=st.session_state.visibility,
                # disabled=st.session_state.disabled,
                # placeholder=st.session_state.placeholder,
            )

            if text_input:
                # TODO: Processing the PDF and Detect the Suspected File
                pdf_extractions = pdf_loader(text_input)
                return

            st.button("Detect", type="primary", key=2)
            if st.button:
                decision = "Benign"
                # with st.spinner('Wait for it...'):
                #     time.sleep(5)
                if decision == "Benign":
                    st.success('THIS PDF FILE ARE BENIGN', icon="✅")
                elif decision == "Malicious":
                    st.error('THIS PDF FILE ARE MALICIOUS', icon="🚨")
