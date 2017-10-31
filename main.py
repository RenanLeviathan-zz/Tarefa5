# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:09:36 2017

@author: Israël e Renan
"""
class Grafo:
  def __init__(self,grafo,inicial):
    self.lista={}
    self.lista=grafo
    self.marc=[]
    self.queue=[]
    self.marc.append(inicial)
    self.queue.append(inicial)

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
          print("aresta de retorno:",(v,w))
          if ((v,w) not in exp) and ((w,v) not in exp):
            exp.append((v,w))
    return exp
                
grafo={
  'a':['b','c'],
  'b':['a','c','d','f'],
  'c':['a','b','d','e'],
  'd':['b','c','e','f'],
  'e':['c','d','f'],
  'f':['b','d','e']
  }
inicial=input("Vértice inicial:")
g=Grafo(grafo,inicial)
exp=g.busca_largura()
print([i for i in exp])
