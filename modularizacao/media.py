from statistics import *
#mean(lista)
#median(lista)
#mode(lista)

def media(lista):
	tam = len(lista)
	return sum(lista)/tam

def mediana(lista):
	lista_ordenada= sorted(lista)
	tam = len(lista_ordenada)
	if tam % 2 == 0:
		mediana = (lista_ordenada[int(tam/2)] + lista_ordenada[int((len/2)+1)])/2
	elif tam % 2 == 1:
		mediana = lista_ordenada[int(tam/2)]
	return mediana
def moda(lista):
	#usar dicionario
	lista_dicionario = {}
	for elemento in lista:
		if elemento not in lista_dicionario:
			lista_dicionario[elemento] = 1
		else:
		 	lista_dicionario[elemento] +=1
	maior = max(lista_dicionario.values()) # valores da lista

	for i in lista_dicionario:
		if lista_dicionario[i] == maior:
			moda = i
	return moda
