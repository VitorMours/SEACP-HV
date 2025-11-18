import streamlit as st 


def image_capture_code():
    container = st.container()
    with container:
        st.markdown("""
            ### Captura e Processamento de Imagem
            
            Temos que o primeiro passo de entendimento do nosso algorito, é a captura e processamento da imagem que é feito pelo opencv, já que 
            ele vai ser o "motor" principal de processamento de imagem dentro do nosso sistema. Com isso, temos que a captura da imagem pode ser 
            feita de diversas formas, seja por upload, câmera ou outras formas, e após a captura, temos que o processamento da imagem é feito por 
            meio do upload de file que temos na nossa aplicação web, que é feita por meio do streamlit, e poderá ser usado na outra parte do 
            nosso projeto.
            
            Com isso, temos que a captura vai ser responsável por converter a imagem para o modelo correto e necessário para que o funcionamento 
            do projeto se dê de forma correta, e esse modelo é o BGR (Blue, Green, Red), que é o modelo padrão do OpenCV para representação 
            de imagens coloridas.
            
            
        """)


    return container