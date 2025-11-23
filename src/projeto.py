from pydantic_ai import Agent
from pathlib import Path
import pypdf
import sys

def extract_text_from_pdf(reader):
    ''''
    Extrai e retorna o texto completo de um objeto leitor de PDF.
    Argumentos:
        reader (pypdf.PdfReader): O objeto leitor de PDF.
    Retorna:
        str: O texto extraído do PDF.
    '''
    full_text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:  # Ensure there is text to add
            full_text += page_text + "\n"
    return full_text

def main():
    # Obtem o caminho do PDF a partir dos argumentos da linha de comando
    if len(sys.argv) > 1:
        pdf_name = sys.argv[1]
    else:
        print("Modo de uso: python src/projeto.py <path_to_pdf>")
        return
    
    # Inicializa o agente do Groq
    agent = Agent('groq:llama-3.3-70b-versatile')

    # Lê e extrai o texto do PDF (OCR)
    pdf_path = Path(pdf_name)
    if not pdf_path.is_file():
        print(f"O arquivo {pdf_path} não foi encontrado.")
        return
    reader = pypdf.PdfReader(pdf_path)
    full_text = extract_text_from_pdf(reader)

    # Executa o agente com o texto extraído
    result = agent.run_sync(
        [
            'Segue o texto de uma nota fiscal de serviço eletroônica emitida no Brasil. Extraia as seguintes informações e apresente em formato de um arquivo JSON: Descricao dos produtos/serviços, valor total dos produtos, DANFE número (uma string no formato xxx.xxx.xxx), data de emissão, valor total da nota, CNPJ do prestador. Retorne somente o JSON e nenhum texto a mais',
            full_text
        ]
    )
    
    # Imprime os resultados no terminal
    print(result.output)

main()