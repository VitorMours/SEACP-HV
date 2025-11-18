import streamlit as st 
from src.blocks import documetation_info
from src.blocks import documetation_tech_context

def create_documetation_page():
    documetation_info.summary()
    documetation_tech_context.libraries_context()
    
    st.divider()
    st.markdown("### Upload de Arquivo")
    st.file_uploader("Upload the human file")