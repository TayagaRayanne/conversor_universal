from conversor.conversor_temperatura import conversorTemperatura
from conversor.conversor_moeda import conversorMoeda
from conversor.conversor_medida import conversorMedida
from conversor.conversor_tempo import conversorTempo

# Função principal que exibe o menu principal e direciona para os submenus
def menu_principal():
    while True:
        print("\n====== Menu Principal ======")
        print("1 - Conversor de temperatura ")
        print("2 - Conversor de moeda ")
        print("3 - Conversor de medidas ")
        print("4 - Conversor de tempo ")
        print("5 - Sair")
        opcao = input("Escolha uma opção (1-5): ")
        
        # Direciona para o menu de temperatura
        if opcao == '1':
            menu_temperatura()
        # Direciona para o menu de moeda
        elif opcao == '2':
            menu_moeda()
        # Direciona para o menu de medidas
        elif opcao == '3':
            menu_medidas()
        # Direciona para o menu de tempo
        elif opcao == '4':
            menu_tempo()
        # Sai do programa
        elif opcao == '5':
            print("Saindo do programa...")
            break
        # Caso o usuário digite uma opção inválida
        else:
            print("Opção inválida, tente novamente!")

# Menu de conversão de temperatura
def menu_temperatura():
    print("\n====== Menu de Conversão de Temperatura ======")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    opcao = input("Escolha uma opção (1 ou 2): ")
    conversor = conversorTemperatura()  # Instancia o conversor de temperatura
       
    if opcao == '1':
        celsius = float(input("Digite a temperatura em Celsius: "))  # Recebe valor em Celsius
        fahrenheit = conversor.celsius_para_fahrenheit(celsius)      # Converte para Fahrenheit
        print(f"{celsius}°C é igual a {fahrenheit}°F.")
    elif opcao == '2':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))  # Recebe valor em Fahrenheit
        celsius = conversor.fahrenheit_para_celsius(fahrenheit)           # Converte para Celsius
        print(f"{fahrenheit}°F é igual a {celsius}°C.")
    else:
        print("Opção inválida, tente novamente!")

# Menu de conversão de moeda
def menu_moeda():
    print("\n====== Menu de Conversão de Moeda ======")
    print("1 - Real para Dólar")
    print("2 - Dólar para Real")
    opcao = input("Escolha uma opção (1 ou 2): ")
    conversor = conversorMoeda()  # Instancia o conversor de moeda
    
    if opcao == '1':
        valor = float(input("Digite o valor em Reais: "))  # Recebe valor em reais
        resultado = conversor.real_para_dolar(valor)       # Converte para dólar
        print(f"R${valor:.2f} é igual a ${resultado:.2f}.")
    elif opcao == '2':
        valor = float(input("Digite o valor em Dólares: "))  # Recebe valor em dólares
        resultado = conversor.dolar_para_real(valor)         # Converte para reais
        print(f"${valor:.2f} é igual a R${resultado:.2f}.")
    else:
        print("Opção inválida, tente novamente!")

# Menu de conversão de medidas
def menu_medidas():
    print("\n====== Menu de Conversão de Medidas ======")
    print("1 - Metros para Quilômetros")
    print("2 - Quilômetros para Metros")
    opcao = input("Escolha uma opção (1 ou 2): ")
    conversor = conversorMedida()  # Instancia o conversor de medidas
    
    if opcao == '1':
        metros = float(input("Digite o valor em metros: "))           # Recebe valor em metros
        quilometros = conversor.metros_para_quilometros(metros)       # Converte para quilômetros
        print(f"{metros} metros é igual a {quilometros} quilômetros.")
    elif opcao == '2':
        quilometros = float(input("Digite o valor em quilômetros: ")) # Recebe valor em quilômetros
        metros = conversor.quilometros_para_metros(quilometros)      # Converte para metros
        print(f"{quilometros} quilômetros é igual a {metros} metros.")
    else:
        print("Opção inválida, tente novamente!") 

# Menu de conversão de tempo
def menu_tempo():
    print("\n====== Menu de Conversão de Tempo ======")
    print("1 - Segundos para Minutos")
    print("2 - Minutos para Segundos")
    opcao = input("Escolha uma opção (1 ou 2): ")
    conversor = conversorTempo()  # Instancia o conversor de tempo
    
    if opcao == '1':
        segundos = float(input("Digite o valor em segundos: "))      # Recebe valor em segundos
        minutos = conversor.segundos_para_minutos(segundos)          # Converte para minutos
        print(f"{segundos:.2f} segundos é igual a {minutos:.2f} minutos.")
    elif opcao == '2':
        minutos = float(input("Digite o valor em minutos: "))        # Recebe valor em minutos
        segundos = conversor.minutos_para_segundos(minutos)          # Converte para segundos
        print(f"{minutos:.2f} minutos é igual a {segundos:.2f} segundos.")
    else:
        print("Opção inválida, tente novamente!")      

# Inicia o programa chamando o menu principal
if __name__ == "__main__":
    menu_principal()

