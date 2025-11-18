import streamlit as st

def summary():
  container = st.container()
  with container:
    st.title("SEACP - HV"),
    st.divider(),
    st.html(
      """
      <p align="center">
        <a href="https://go-skill-icons.vercel.app/">
          <img
            src="https://go-skill-icons.vercel.app/api/icons?i=googlecolab,python,numpy,scipy,pandas,matplotlib,seaborn,scikitlearn,opencv&theme=dark"
          />
        </a>
      </p>"""),
    st.divider(),
    st.markdown(
      """
      O **S**istema de **E**xtração e **A**nálise de **C**or de **P**ele em **H**umanos **V**irtuais é um sistema criado com o intuito de extrair e 
      analizar dados de imagens de humanos virtuais, com foco na cor da pele. O sistema utiliza técnicas de visão computacional para processar as 
      imagens e extrair informações relevantes sobre a cor da pele. A partir disso, poderemos usar modelos de Inteligencia Artificial para analisar
      esses dados e gerar insights que podem ser úteis em diversas áreas, como saúde, cosméticos, moda, entre outras.
      """
    )
    
    st.markdown("""
      ## Autores
      - João Vitor Rezende Moura -- Estudante
      - Vitor Flávio -- Professor Orientador
    """)
  return container


