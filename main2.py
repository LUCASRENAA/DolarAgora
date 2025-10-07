import requests
import json

url = 'https://www.mercadobitcoin.net/api/BTC/ticker/'

try:
    response = requests.get(url)
    response.raise_for_status() 
    data = response.json()
    ultimo_preco = data['ticker']['last']
    
    print(f"O último preço do Bitcoin no Mercado Bitcoin é: R$ {float(ultimo_preco):.2f}")

except requests.exceptions.RequestException as e:
    print(f"Erro ao acessar a API: {e}")