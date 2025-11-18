import streamlit as st 
from src.pages import main_page, documetation_page, code_page

def create_app():
    pg = st.navigation([
        st.Page(main_page.create_main_page, title="Home"),
        st.Page(documetation_page.create_documetation_page, title="Documentação"),
        st.Page(code_page.create_code_page, title="Código")
    ])
    pg.run()

if __name__ == "__main__":
    create_app()