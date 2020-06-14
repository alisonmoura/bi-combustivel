# BI Combustível

Projeto do Grupo 2 do Trabalho Prático da matéria Sistemas de Apoio à Desição - FACOM/UFMS

## Integrantes
- Alison Iuri Oghino de Moura
- Geovanna Santiago de Souza
- Kelli Regina Mesa de Sousa Martins
- Mariana Narita Masunaga Nara Mendes Benitez

## Setup do Projeto

>Certifique-se que você tenha o `python3` e o `pip3` instalado no seu ambiente, disponível para execução em Interface de Comando de Linha (CLI).

Instale as dependências do projeto com o comando abaixo (execute-o no terminal na pasta do projeto):

```
pip3 install -r requirements.txt
```

## Run do Projeto

> ATENÇÃO: O processo é *time-consuming* e computacionalmente intenso, pois gera um merge de cerca de 809 mil itens em um CSV. Última execução em um CPU i3/4G RAM em aproximadamente 15211 segundos.

Execute no terminal

```
python3 index.py
```


## Estrutura do Projeto

`index.py`: arquivo principal que realiza o processo de ETL, pega todos os arquivos .csv da pasta `datasets` junta e limpa todos os dados em uma planilha única: `etl.csv`, que é armazenada na pasta `output`.

`datasets`: Pasta que contém o conjunto de dataset (.csv) para o BI. Por questões de otimização de armazenamento, todos os arquivos com extensão `.csv` são ingnorados pelo git. Somente está sendo vercionado o arquivo `datasets.zip`

`output`: Pasta onde os resultados são armazenados. Por questões de otimização de armazenamento, todos os arquivos com extensão `.csv` são ingnorados pelo git. Somente está sendo vercionado o arquivo `etl.zip`

`tests`: pasta com arquivos com testes de algoritmos.