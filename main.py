# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:09:36 2017
Busca em largura
@author: Israël e Renan
"""
from Graph import *
from tkinter import *
from random import *
class Main:
  def __init__(self,master=None,graph=None,pos=None):
    self.widget1 = Frame(master,width=600,height=500)
    ini=input("Vértice inicial da busca:\n")
    self.graph=Grafo(graph,ini)
    self.widget1.pack()
    self.canvas=Canvas(self.widget1,width=500,height=500)
    self.canvas.pack(side=RIGHT)
    self.graph.busca_largura()
    seed(7)
    pares=[]
    #organiza os pares
    for i in self.graph.get():
      for j in self.graph.get()[i]:
        if ((i,j) not in pares) and ((j,i) not in pares):
          pares.append((i,j))
    for p in pares:
      #primeiro vértice do par
      self.canvas.create_oval(pos[p[0]][0]-10,pos[p[0]][1]-10,pos[p[0]][0]+10,pos[p[0]][1]+10,fill="blue")
      self.canvas.create_text(pos[p[0]][0],pos[p[0]][1],text=p[0],fill="white")
      #segundo vértice do par
      self.canvas.create_oval(pos[p[1]][0]-10,pos[p[1]][1]-10,pos[p[1]][0]+10,pos[p[1]][1]+10,fill="blue")
      self.canvas.create_text(pos[p[1]][0],pos[p[1]][1],text=p[1],fill="white")
      #criando linhas
      self.canvas.create_line(pos[p[0]][0],pos[p[0]][1],pos[p[1]][0],pos[p[1]][1])
    self.msg=Label(self.widget1,text=self.graph.get_history())
    self.msg.pack(side=LEFT)  

grafo={
  'a':['b','c'],
  'b':['a','c','d','f'],
  'c':['a','b','d','e'],
  'd':['b','c','e','f'],
  'e':['c','d','f'],
  'f':['b','d','e']
  }
pos={
'a':(10,100),
'b':(110,100),
'c':(10,200),
'd':(110,150),
'e':(210,200),
'f':(210,100)
}
#visualização do grafo
root=Tk()
Main(root,grafo,pos)
root.title("Busca em Largura")
root.mainloop()