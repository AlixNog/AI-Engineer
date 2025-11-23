# Projeto: Extração de dados de Nota Fiscal (PDF) com LLM

Este projeto recebe como entrada um arquivo _.pdf_ que representa uma nota fiscal e retorna os seguintes dados no formato JSON
  - Descrição dos produtos/serviços  
  - Valor total dos produtos  
  - Número da DANFE (formato `xxx.xxx.xxx`)  
  - Data de emissão  
  - Valor total da nota  
  - CNPJ do prestador  

## Pré-requisitos

- Python versão 3 ou superior
- Bibliotecas listadas no arquivo `requirements.txt`
- - Podem ser facilmente instaladas com o comando ```pip install -r requirements.txt```
- Chave de API do Groq salva como variável de ambiente
- - A variável, obrigatorialmente, tem que se chamar `GROQ_API_KEY`
  - Veja um [pequeno tutorial aqui](https://www.autodesk.com/br/support/technical/article/caas/sfdcarticles/sfdcarticles/PTB/How-to-set-an-environment-variable.html) sobre como configurar variáveis de ambiente em diferentes sistemas operacionais

## Funcionamento

O script recebe um único argumento. Este argumento, necessariamente, deverá conter o caminho relativo ou absoluto para um arquivo _.pdf_ contendo uma nota fiscal em Português.

Para rodar o script, utilize o comando `python src/projeto.py <arquivo.pdf>`
  - Tenha certeza de enviar o arquivo _.pdf_. Caso contrário, o _script_ não irá funcionar

O _script_:
1. Recebe arquivo _.pdf_ via linha de comando
2. Extrai o texto utilizando a biblioteca _pypdf_
3. Envia o texto para um agente configurado com o modelo: 'groq:llama-3.3-70b-versatile'
4. Extrai diversas informações pré-solicitadas e as imprime na tela como um arquivo JSON
   
O _script_ pode ser facilmente alterado para salvar o JSON em formato texto alterando as últimas linhas da função _main_