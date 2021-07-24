#Seleciona o tipo da imagem
FROM python:3.9.5

#Pasta do projeto a qual o docker vai ler os arquivos
WORKDIR /code

#Copia o arquivo de dependia da raiz do diretorio
COPY requirements.txt . 

#instala as depências
RUN pip install -r requirements.txt
    