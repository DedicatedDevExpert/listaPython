# Definindo a função de conversão
"""def celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Definindo a função resultado
def resultado(res):
     # a variavel fahrenheit envia o valor e recebe o resultado
    fahrenheit = celsius_para_fahrenheit(res)  # Chama a função de conversão
    print(f"{res}°C = {fahrenheit}°F")  # Imprime o resultado


# Chamando a função resultado com um valor específico
resultado(20)"""


# outra maneira


# Definindo a função de conversão
def celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Definindo a função resultado
def resultado(*temperaturas_celsius):

    # aqui temperaturas_celsius pega os valores de resultado() e vai emviando um por um para temp que depoies envia para (temp)
    for temp in temperaturas_celsius:
        # Chama a função de conversão para cada temperatura
        fahrenheit = celsius_para_fahrenheit(temp)
        # Imprime o resultado
        print(f"{temp}°C = {fahrenheit}°F")


# Chamando a função resultado com várias temperaturas
resultado(0, 20, 37, 27, 15)
