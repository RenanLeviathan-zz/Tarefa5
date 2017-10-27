# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:09:36 2017

@author: Israël e Renan
"""
class Grafo:
    def __init__(self,vertices,inicial):
        self.lista={}
        self.marc=[]
        self.queue=[]
        self.marc.append(inicial)
        self.queue.append(inicial)
        for i in vertices:
            v=[x for x in input("adjacentes a {}\n".format(i)).split()]
            self.lista[i]=v
    
    def mostrar(self):
        for i in self.lista:
            print(i)
    
    def busca_largura(self):
        exp=[]
        while self.queue != []:
            v=self.queue[0]
            self.queue=self.queue[1:]
            for w in self.lista[v]:
                if w not in self.marc:
                    exp.append((v,w))
                    self.queue.append(w)
                    self.marc.append(w)
                else:
                    if ((v,w) not in exp) and ((w,v) not in exp):
                        exp.append((v,w))
        return exp
                    
vertices=[x for x in input("Vértices do grafo").split()]
inicial=input("Vértice inicial:")
g=Grafo(vertices,inicial)
exp=g.busca_largura()
print([i for i in exp])