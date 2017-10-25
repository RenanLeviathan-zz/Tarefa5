# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:09:36 2017

@author: Israël e Renan
"""
#modulo de lista de adjacências
def lista_adj(vertices):
    lista={}
    for i in vertices:
        v=[int(x) for x in input("adjacentes a {}\n".format(i)).split()]
        lista[i]=v
    return lista
        
def mostrar_lista(lista):
    for i in lista:
        print(i)
        
def aresta_explorada(l,marc):
    exp=[]
    for i in l.keys():
        if i not in marc:
            print("marca {}".format(i))
            marc.append(i)
        partida=i
        for w in l[partida]:
            if w not in marc:
                print("marca {}".format(w))
                marc.append(w)
            if (w in l[partida]) and (((partida,w) not in exp) and ((w,partida) not in exp)): 
                print("explora a aresta ({},{})".format(partida,w))
                exp.append((partida,w))
                partida=w
    return exp
                    
                
            
vertices=[int(x) for x in input("Vértices do grafo").split()]
lista=lista_adj(vertices)
marcados=[]#lista dos vértices marcados
exp=aresta_explorada(lista,marcados)
print(lista)
print([i for i in exp])