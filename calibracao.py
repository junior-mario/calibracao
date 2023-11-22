

# Realiza a calibração para determinar a area que será utilizada pra detectar o veiculo
# Para executar o streamlit utilize o seguinte comando streamlit run calibracao.py


import cv2
import streamlit as st
import numpy as np
from PIL import Image


def brighten_image(image, amount):
    img_bright = cv2.convertScaleAbs(image, beta=amount)
    return img_bright

#FUNCAO PARA CRIAR RETANGULO
#recebe X e Y 

def retangulo(imagem, x, y, xh, yh):
    #desenha o retângulo com borda verde 
    x = int(x)
    verde = (0, 255, 0)  
    #(x,y) (x+h, y+h)
    img_retangulo = cv2.rectangle(imagem, (x, y), (xh, yh), verde, 3)
    #cv2.imshow("Canvas", imagem)
    return img_retangulo



def desenha_linha_1(imagem, x, yh=1080):
    #desenha linha
    x = int(x)
    azul = (255, 0, 0) 
    #(x,y) (x+h, y+h)
    y = 5
    xh = x
    img_linha_1 = cv2.line(imagem, (x, y), (xh, yh), azul, 3)
    #cv2.imshow("Canvas", imagem)
    return img_linha_1


def desenha_linha_2(imagem, x, yh=1080):
    #desenha linha  
    x = int(x)
    azul = (0, 0, 255) 
    #(x,y) (x+h, y+h)
    y = 5
    xh = x
    img_linha_2 = cv2.line(imagem, (x, y), (xh, yh), azul, 3)
    #cv2.imshow("Canvas", imagem)
    return img_linha_2


def convert(variavel):
    string = str(variavel)
    return string


def blur_image(image, amount):
    blur_img = cv2.GaussianBlur(image, (11, 11), amount)
    return blur_img


def enhance_details(img):
    hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
    return hdr


def reduzir_imagem(img):
    hdr = cv2.resize(img, (0,0), fx=0.4, fy=0.4) # diminiu a imagem da mask e reproducao
    return hdr

def main_loop():

    st.title("Calibração de mascara")
    #st.subheader("This app allows you to play with Image filters!")

    #blur_rate = st.sidebar.slider("Blurring", min_value=0.5, max_value=3.5)
    #brightness_amount = st.sidebar.slider("Brightness", min_value=-50, max_value=50, value=0)
    apply_enhancement_filter = st.sidebar.checkbox('Enhance Details')
    apply_reduction = st.sidebar.checkbox('Redimencioar 40%')

    # Cria os slidebar na lateral da pagina
    st.sidebar.write('**Dimensão do Retangulo:** ')
    eixo_x = st.sidebar.slider("Eixo X", min_value=20, max_value=1980, value=222)
    eixo_xh = st.sidebar.slider("Tamanho X", min_value=20, max_value=1980, value=1375)
    eixo_y = st.sidebar.slider("Eixo Y", min_value=25, max_value=1080, value=193)
    eixo_yh = st.sidebar.slider("Tamanho Y", min_value=20, max_value=1080, value=907)




    st.sidebar.write('**Dimensão das Linhas:** ')
    st.sidebar.write('*Linha 1:* ')
    eixo_x_linha_1 = st.sidebar.slider("Eixo X Linha 1", min_value=20, max_value=1980, value=736)
    #eixo_xh_linha_1 = st.sidebar.slider("Tamanho X Linha 1", min_value=2, max_value=1980)
    #eixo_y_linha_1 = st.sidebar.slider("Eixo Y Linha 1", min_value=25, max_value=1980)
    #eixo_yh_linha_1 = st.sidebar.slider("Tamanho Y Linha 1", min_value=20, max_value=1080)
    st.sidebar.write('*Linha 2:* ')
    eixo_x_linha_2 = st.sidebar.slider("Eixo X Linha 2", min_value=20, max_value=1980, value=1021)

    
    # Exibi o texto na tela #
    st.write('**Dimensão da mascara:** ')   
    st.write('x:', eixo_x, ' x+h:', eixo_xh)
    st.write('y:', eixo_y, ' y+h:', eixo_yh)
    #st.write ('roi = frame [', eixo_x,    ']')
    resultado = 'roi = frame [' + str(eixo_y) +':'+str(eixo_yh)+','+ str(eixo_x) +':'+ str(eixo_xh)+']'
    



    st.write('**Dimensão das Linhas:** ')
    st.write('**Linha 1:** ', eixo_x_linha_1,)  
    st.write('**Linha 2:** ', eixo_x_linha_2,)  


    # Exibi o texto na tela #  





    st.code(resultado, language='python') # trecho do codigo para copiar


    # Realiza o upload da imagem
    image_file = st.file_uploader("Envio da imagem", type=['jpg', 'png', 'jpeg'])
    if not image_file:
        return None

    original_image = Image.open(image_file)
    original_image = np.array(original_image)

    #processed_image = blur_image(original_image, blur_rate)
    #processed_image = brighten_image(processed_image, brightness_amount)


    # Editado a imagem  desenhando o retangulo na imagem
    processed_image = retangulo(original_image, eixo_x, eixo_y, eixo_xh, eixo_yh)
    processed_image = desenha_linha_1(original_image, eixo_x_linha_1)
    processed_image = desenha_linha_2(original_image, eixo_x_linha_2)


    if apply_enhancement_filter:
        processed_image = enhance_details(processed_image)

    if apply_reduction:
        imagem_reduzida = reduzir_imagem(original_image)

    #st.text("Original Image vs Processed Image")
    #st.image([original_image, processed_image])
    st.image([processed_image]) # Exibe a imagem na tela
    #st.image([imagem_reduzida]) # Exibe a imagem na tela


if __name__ == '__main__':
    main_loop()