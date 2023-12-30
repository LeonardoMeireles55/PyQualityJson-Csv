import requests
import json


def post_results():
    endpoint_url = "http://localhost:8080/bio/sendValues"

    # Caminho para o arquivo JSON na raiz
    json_file_path = "./outfiles/integra_400.json"  # Substitua "nome_do_arquivo.json" pelo seu arquivo

    # Carregar dados do arquivo JSON
    with open(json_file_path, 'r') as file:
        data_to_send = json.load(file)

    # Configurar cabeçalhos para indicar que você está enviando dados JSON
    headers = {'Content-Type': 'application/json'}

    # Fazer a solicitação POST com os dados JSON
    response = requests.post(endpoint_url, json=data_to_send, headers=headers)

    # Verificar o status da resposta
    if response.status_code == 200:
        print("POST bem-sucedido")
    else:
        print(f"Falha no POST. Código de status: {response.status_code}")
        print(f"Resposta do servidor: {response.text}")


# Chamar a função para enviar a solicitação POST
post_results()
