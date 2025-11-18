import streamlit as st
from src.blocks import documetation_code_example, project_math_example

def create_code_page():
    st.title("Exemplos de Código")
    
    tab1, tab2 = st.tabs(["Exemplo de Código", "Exemplo de Matemática"])
    
    with tab1:
        if hasattr(documetation_code_example, 'show_code'):
            documetation_code_example.show_code()
        else:
            st.info("Seção de código em desenvolvimento")
    
    with tab2:
        if hasattr(project_math_example, 'show_math'):
            project_math_example.show_math()
        else:
            st.info("Seção de matemática em desenvolvimento")
