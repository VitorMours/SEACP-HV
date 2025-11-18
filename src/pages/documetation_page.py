import tempfile
import io
import os
import streamlit as st 
from src.blocks import documetation_info
from src.blocks import documetation_tech_context
from src.blocks import documetation_code_example
def create_documetation_page():
    documetation_info.summary()
    documetation_tech_context.libraries_context()
    documetation_code_example.image_capture_code()
    st.divider()
    st.markdown("### Upload de Arquivo")
    file_uploaded = st.file_uploader("Upload the human file",
        accept_multiple_files=False                 
                    
    )
    
    if file_uploaded is not None:
        os.makedirs("src/media/uploads", exist_ok=True)
        file_path = os.path.join("src/media/uploads", file_uploaded.name)
        with open(file_path, "wb") as f:
            f.write(file_uploaded.getbuffer())
        
        st.success(f"Arquivo salvo temporariamente em: {file_path}")