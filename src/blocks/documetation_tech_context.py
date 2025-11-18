import streamlit as st 


def libraries_context():
    container = st.container()
    with container:
        st.markdown("""
            ### Tecnologias Utilizadas
            
            Temos que diversas tecnologias foram usadas dentro do desenvolvimento desse sistema, e elas tiveram suas funcionalidades específicas 
            em cada um dos casos, e esses casos serão levemente e brevemente pontuados a seguir, de forma a elucidar o papel de cada uma dessas tecnologias.
            
            - **Python**: Linguagem de programação do desenvolvimento.
            - **Google Colab**: Ambiente para desenvolvimento e testes iniciais.
            - **OpenCV**: Biblioteca de VC para processamento de imagens e extração de características.
            - **NumPy**: Biblioteca para manipulação e análise de dados.
            - **Pandas**: Biblioteca para manipulação e análise de dados tabulares.
            - **Matplotlib e Seaborn**: Bibliotecas de visualização de dados.
            - **Scikit-learn**: Biblioteca de aprendizado de máquina para construir e avaliar modelos preditivos.
                      
            Tendo em vista essas necessidades, essas tecnologias foram escolhidas por serem amplamente utilizadas na comunidade de ciência de dados e visão computacional,
            possuindo uma vasta gama de funcionalidades e uma comunidade ativa que contribui para o desenvolvimento contínuo dessas ferramentas.
            Com isso, temos a necessidade de importar e preparar essas ferramentas, como será mostrado a seguir:
            
            ```python
            import cv2
            import numpy as np
            import pandas as pd
            import scipy
            import matplotlib.pyplot as plt
            import seaborn as sns
            import sklearn
            import skimage
            ``` 
        """)


    return container