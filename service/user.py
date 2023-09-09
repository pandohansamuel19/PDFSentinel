import streamlit
from supabase import (
    StorageException,
    SupabaseAuthClient,
    SupabaseRealtimeClient,
    SupabaseStorageClient
)
from utils import SupabaseConnection

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
