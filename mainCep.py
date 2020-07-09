import requests

def main():
    print("#####################")
    print(" ### Consulta CEP ###")
    print("#####################")
    print()

    n_ten = 0
    
    cep_input = ''
    while len(cep_input) !=8 and len(cep_input) < 8:
        if n_ten > 0:
            cep_input = input('Erro!! Digite um CEP valido : ')
        else:
            cep_input = input('Digite um CEP para a consulta: ')
        n_ten += 1
    request = requests.get(f'http://viacep.com.br/ws/{cep_input}/json')

    address_data = request.json()

    if 'erro' in address_data:
        print(f'CEP invalido')
    else:
        print('==> CEP Encontrado! <==')
        print(f"CEP: {address_data['cep']}")
        print(f"Estado: {address_data['uf']}")
    
    ops = int(input('Deseja uma nova consulta?\n 1-Sim. 2- Sair\n'))
    if ops == 1:
        main()
    else:
        exit()

    

if __name__ == "__main__":
    main()