import requests
import os
import time

def layout():
    print("#####################")
    print(" ### Consulta CEP ###")
    print("#####################")
    print()


def entrada_de_dados():
    os.system('clear')

    layout()
    cep_input = input('Digite um CEP para a consulta: ')
    if len(cep_input) !=8:
        print('Cep invalido! Tente Novamente!')
        time.sleep(1.5)
        entrada_de_dados()
    requisicão_rest(cep_input)
    

def requisicão_rest(cep_informado):
    request = requests.get(f'http://viacep.com.br/ws/{cep_informado}/json')

    dados_do_cep = request.json()

    if 'erro' in dados_do_cep:
        print(f'CEP invalido! Tente novamente!')
        time.sleep(1.5)
        entrada_de_dados()
    else:
        retorno_da_requisicao_rest(dados_do_cep)

def retorno_da_requisica    o_rest(dados_do_cep):
        print('==> CEP Encontrado! <==')
        print(f"CEP: {dados_do_cep['cep']}")
        print(f"Estado: {dados_do_cep['uf']}")
        print(f"Cidade: {dados_do_cep['localidade']}")
        ops = int(input('Deseja uma nova consulta?\n 1-Sim. 2- Sair\n'))
        if ops == 1:
            entrada_de_dados()
        else:
            exit()


if __name__ == "__main__":
    entrada_de_dados()