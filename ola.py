#firt command
# -*- coding: utf-8 -*-
print("hello")
#multiplicação e exponenciação
print(2*2)
print(2**3)

#módulo de divisão
print(10/3)
#resto da divisão
print("resto",10%3)
#tipos de variaveis
var1 = 1 #int
var2 = 1.1 #float
var3 = "bla bla" #string
var4 = False #boolean
print(var1,var2)
print("----------------")
### Tipos de operadores  relacionais
#mesmo do java
#comandos condicionais
'''
if condicao:
	execução
elif:

else:

'''
if var1 > var2:
	print ("var 2 é maior")

else:
	print("var1 é menor")
## laço de repetição
x = 1
while x < 5:
	print("x",x)
	x = x + 1
	# x +=1
print("----------------")
#lista
lista = [1,2,3,4,5]
lista2 = ["ola", "oi"]
lista3 = ["ola", 0, 1.3, False]

for i in lista3:
	print(i)
print("----------------")
#for ranger
for i in range(10):
	print(i)
print("----------------")
#for de 2 em 2
for i in range(10,20,2):
	print(i)
print("----------------")
## inputs
numero = input("digite um numero: ")
print(numero)
print("digitado", numero)

