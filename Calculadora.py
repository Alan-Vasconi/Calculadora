import time
nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
telefone = int(input('Digite o seu telefone sem nenhum simbolo apenas números:'))

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Tel: {telefone}')
print()

desejo = input('Você deseja usar a Calculadora? ')

if desejo =='Não': 
    print('Programa encerrado')
    exit()
    
if desejo =='Sim':
    print('======== Selecione o seu sinal ========')
    print('1 - +')
    print('2 - -')
    print('3 - /')
    print('4 - *')
    print('5 - **')

if desejo =='sim':
    print('======== Selecione o seu sinal ========')
    print('1 - +')
    print('2 - -')
    print('3 - /')
    print('4 - *')
    print('5 - **')

if desejo =='SIM':
    print('======== Selecione o seu sinal ========')
    print('1 - +')
    print('2 - -')
    print('3 - /')
    print('4 - *')
    print('5 - **')

calculo = input('======== Qual operação você deseja: ')

print()


if calculo =='1':
    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o segundo valor: '))
    resultado1 = float(valor1 + valor2)
    print(resultado1)

if calculo =='2':
    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o segundo valor: '))
    resultado2 = float(valor1 - valor2)
    print(resultado2)

if calculo =='3':
    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o segundo valor: '))
    resultado3 = float(valor1 / valor2)
    print(resultado3)

if calculo =='4':
    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o segundo valor: '))
    resultado4 = float(valor1 * valor2)
    print(resultado4)

if calculo =='5':
    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o valor para elevar: '))
    resultado5 = float(valor1 ** valor2)
    print(resultado5)
