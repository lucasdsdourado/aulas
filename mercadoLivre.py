import requests
from bs4 import BeautifulSoup

# Abrindo um arquivo txt para escrever os dados
file = open('produtos.txt', 'a', encoding='utf-8')

for i in range(1,48*6,48):
    pag=i
    # URL da página que queremos extrair
    if i == 1:
        pag=0
    url = f'https://lista.mercadolivre.com.br/informatica/tablets-acessorios/tablets/xiaomi/xiaomi-pad_Desde_{i}_NoIndex_True'

    # Cabeçalhos para simular um navegador
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
    }

    # Fazendo a requisição GET
    response = requests.get(url, headers=headers)

    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Parsing do conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrando todos os elementos que contêm os produtos
        products = soup.find_all('li', class_='ui-search-layout__item')

        # Iterando sobre os produtos encontrados
        for product in products:
            # Extraindo o nome do produto
            name_tag = product.find('a', class_='')
            name = name_tag.get_text().strip() if name_tag else 'Nome não encontrado'

            # Extraindo o preço do produto
            price_tag = product.find('span', class_='andes-money-amount__fraction')
            price = price_tag.get_text().strip() if price_tag else 'Preço não encontrado'

            # Extraindo o link do produto
            link_tag = product.find('a', class_='')
            link = link_tag['href'] if link_tag else 'Link não encontrado'

            # Escrevendo no arquivo
            file.write(f'{name};{price};{link}\n')

        print('Dados extraídos com sucesso e salvos em produtos.txt')
    else:
        print(f'Erro ao acessar a página. Status code: {response.status_code}')
