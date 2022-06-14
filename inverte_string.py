#Escreva um programa que inverta os caracteres de um string.
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;



def inverte_string(string):
  invertida = ""
  for i in string:
    invertida= i +invertida
  return invertida


if __name__ == "__main__":
    string = input("Digite a string que deseja inverter: ")
    print(f'A string invertida é: {inverte_string(string)}')