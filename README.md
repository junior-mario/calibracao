


# Delimitação de ROI 

Este micro projeto foi criado para facilitar a delimitação de um ROI em uma imagem em projetos com Opencv.

&nbsp;
## 🔥 Introdução

Tem por finalidade facilitar a criação de um ROI para uma imagem, permitindo selecionar a área de interesse
baseado em uma foto ou de um frame do video que será utilizado.
A versão 1.0 permite a criação do ROI e mais 2 linhas na vertical, com o intuito de utiliza-las para detecção de objetos.

&nbsp;
### ⚙️ Pré-requisitos

Para realizar a instalação dos requisitos basta instala-los utilizando o comando abaixo.
Obs: como o projeto foi feito para ser hospedado no stremlit é utilizado a biblioteca: opencv-python-headless

```
pip install -r requirements. txt
```

&nbsp;
### 🔨 Deploy Aplicação no Streamlit

Está aplicação utilizou o seguinte tutorial para o deploy.

[Deploy](https://www.alura.com.br/artigos/streamlit-compartilhando-sua-aplicacao-de-dados-sem-dor-de-cabeca)


&nbsp;
## 🛠️ Executando localmente

Se desejar executar localmente pode utilizar o seguinte comando após instalar os pré-requisitos.

```
streamlit run calibracao.py
```

&nbsp;
## 📦 Tecnologias usadas:


 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
 ![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)


&nbsp;
## 👷 Autores

* **Mario** - *desenvolvimento* - [Mario](https://github.com/junior-mario)

&nbsp;
## 📄 Licença

Esse projeto está sob a licença MIT - acesse os detalhes [LICENSE.md](https://github.com/junior-mario/calibracao/blob/main/LICENSE).


&nbsp;
## 💭 FAQ - Perguntas frequentes

#### Estou tendo problemas para executar operaçãoes na imagem

Altere a biblioteca ***opencv-python-headless*** para ***opencv-python==4.8.1.78*** no arquivo requirements.txt


