import json
import urllib.request

# Solicitar ao usuário o CEP
CEP = input('Digite o CEP')

#Construir na URL de consulta
url = f"https://viacep.com.br/ws{CEP}/json/"

try:
    # Fazer a requisição
    response = urllib.request.urlopen(url) 
    
    #Ler o  conteudo da resposta
    data = response.read().decode('utf-8')

    # Teste...
    print(data)
except Exception as e:
    print(f"Erro: {e}")