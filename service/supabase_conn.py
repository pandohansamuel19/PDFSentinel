from __future__ import annotations, print_function
import streamlit
from streamlit import secrets
from abc import ABC, abstractmethod
from typing import List, Protocol
from supabase import Client, create_client
from supabase import (
    StorageException,
    SupabaseAuthClient,
    SupabaseRealtimeClient,
    SupabaseStorageClient
)


class SupabaseConnection(ABC):
    def __init__(self):
        super(SupabaseConnection, self).__init__()
        self._url = secrets["supabase"]["SB_URL"]
        self._key = secrets["supabase"]["SB_KEY"]
        
        
    @abstractmethod
    def connect(self) -> None:
        """Connect to Supabase by using SDK

        Returns
        -------
        conn
            will generate jwt token if succesfully connected
        """
        conn: Client = create_client(self._url, self._key)
        return conn
    
    @abstractmethod
    def disconnect(self) -> None:
        ...
    
    @abstractmethod
    def initialize_DB(self) -> None:
        # TODO: if connect intialize to existing DB
        ...

class UserDB(SupabaseConnection):
    def __init__(self):
        super(UserDB, self).__init__()
        
    def get_unique_model(self):
        ...
        
    def delete_unique_model(self):
        ...
        
    def download_data(self):
        ...
        
    def upload_unique_data(self):
        ...
