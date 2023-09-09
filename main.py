import os
import sys
import logging
from pathlib import Path
from abc import ABC, abstractmethod
from typing import List, Self
from dataclasses import dataclass
from enum import Enum
from email import message

import streamlit as st
import pandas as pd
from pandas import DataFrame, Series
# import tensorflow as tf

# Page Config
st.set_page_config(
    page_title="DeepDetect",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main() -> None:
    st.write("Here's our first attempt at using data to create a table:")
    st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

if __name__ == '__main__':
    main()