

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


def convert(variavel):
    string = str(variavel)
    return string


def blur_image(image, amount):
    blur_img = cv2.GaussianBlur(image, (11, 11), amount)
    return blur_img


def enhance_details(img):
    hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
    return hdr


def main_loop():

    st.title("Calibração de mascara")
    #st.subheader("This app allows you to play with Image filters!")

    #blur_rate = st.sidebar.slider("Blurring", min_value=0.5, max_value=3.5)
    #brightness_amount = st.sidebar.slider("Brightness", min_value=-50, max_value=50, value=0)
    apply_enhancement_filter = st.sidebar.checkbox('Enhance Details')

    # Editado
    eixo_x = st.sidebar.slider("Eixo X", min_value=20, max_value=1980)
    eixo_xh = st.sidebar.slider("Tamanho X", min_value=20, max_value=1980)
    eixo_y = st.sidebar.slider("Eixo Y", min_value=20, max_value=1080)
    eixo_yh = st.sidebar.slider("Tamanho Y", min_value=20, max_value=1080)

    

    st.write('**Dimensão da mascara:** ')   
    st.write('x:', eixo_x, ' x+h:', eixo_xh)
    st.write('y:', eixo_y, ' y+h:', eixo_yh)
    
    st.write ('roi = frame [', eixo_x,    ']')
    resultado = 'roi = frame [' + str(eixo_y) +':'+str(eixo_yh)+','+ str(eixo_x) +':'+ str(eixo_xh)+']'
      

    st.code(resultado, language='python')

    image_file = st.file_uploader("Envio da imagem", type=['jpg', 'png', 'jpeg'])
    if not image_file:
        return None

    original_image = Image.open(image_file)
    original_image = np.array(original_image)

    #processed_image = blur_image(original_image, blur_rate)
    #processed_image = brighten_image(processed_image, brightness_amount)

    # Editado
    processed_image = retangulo(original_image, eixo_x, eixo_y, eixo_xh, eixo_yh)


    if apply_enhancement_filter:
        processed_image = enhance_details(processed_image)

    #st.text("Original Image vs Processed Image")
    #st.image([original_image, processed_image])
    st.image([processed_image])


if __name__ == '__main__':
    main_loop()