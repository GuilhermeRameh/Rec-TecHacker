# import requests
# from bs4 import BeautifulSoup

# # Faz a requisição HTTP para a página
# url = 'https://pt.wikipedia.org/wiki/Lista_de_instituições_de_ensino_superior_do_Brasil'
# response = requests.get(url)

# # Verifica se a requisição foi bem-sucedida
# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Localizar o elemento com a classe do texto que indica o tipo de faculdade
#     # texto_indicador = soup.find_all(class_="mw-headline")
#     texto_indicador = soup.find_all("dt")
#     # Verificar se o texto indica que a lista é de faculdades públicas ou privadas
#     if texto_indicador:
#         for palavra in texto_indicador:
#             if "Públicas" in palavra:
#                 # A lista é de faculdades públicas
#                 print(palavra.find_next("li"))


