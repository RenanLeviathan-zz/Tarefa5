class Grafo:
  def __init__(self,grafo,inicial):
    self.lista={}
    self.lista=grafo
    self.marc=[]
    self.queue=[]
    self.exp=[]
    self.history=""
    self.marc.append(inicial)
    self.queue.append(inicial)

  def get(self):
    return self.lista  
  
  def get_history(self):
    return self.history
  
  def busca_largura(self):
    while self.queue != []:
      v=self.queue[0]
      self.queue=self.queue[1:]
      for w in self.lista[v]:
        if w not in self.marc:
          self.exp.append((v,w))
          self.queue.append(w)
          self.marc.append(w)
          self.history+="Aresta de busca: ({},{})\n".format(v,w)
        else:
          if ((v,w) not in self.exp) and ((w,v) not in self.exp):
            self.history+="aresta de retorno: ({},{})\n".format(v,w)
            self.exp.append((v,w))
              