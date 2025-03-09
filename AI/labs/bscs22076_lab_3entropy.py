import numpy as np
from collections import Counter
from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt

def loaddataset():
  data=np.array([[2,5,0],[3,6,0],[5,6,1],[6,5,1],[8,7,1],[]])
  X,y=data[:,:-1],data[:,-1]
  
def entropy(y):
 total=len(y)
 count=Counter(y)
 entropy=-sum((c/total)*np.log2(c/total) for c in count.values())
 return entropy


def bestsplit(X,y):
 best_feat=None
 best_thresh=None
 best_ent=float('inf')
 n=X.shape[0]
 for i in range(X.shape[1]):
  unique_vals=np.unique(X[:,i])
  for val in unique_vals:
   left_mask=X[:,i]<=val
   right_mask=X[:,i]>val
   if np.sum(left_mask)==0 or np.sum(right_mask)==0:
    continue
   left_labels=y[left_mask]
   right_labels=y[right_mask]
   left_ent=entropy(left_labels)
   right_ent=entropy(right_labels)
   w_ent=(np.sum(left_mask)/n)*left_ent+(np.sum(right_mask)/n)*right_ent
   if w_ent<best_ent:
    best_ent=w_ent
    best_feat=i
    best_thresh=val
 return best_feat,best_thresh

class decisiontree:
 def __init__(self,maxdepth=5):
  self.maxdepth=maxdepth
  self.tree=None
 def fit(self,x,y,depth=0):
  if len(set(y))==1:return y[0]
  if depth==self.maxdepth:
   cnt=Counter(y)
   return cnt.most_common(1)[0][0]
  feat,thr=bestsplit(x,y)
  if feat is None:
   cnt=Counter(y)
   return cnt.most_common(1)[0][0]
  leftmask=x[:,feat]<=thr
  rightmask=~leftmask
  leftx=x[leftmask]
  lefty=y[leftmask]
  rightx=x[rightmask]
  righty=y[rightmask]
  lefttree=self.fit(leftx,lefty,depth+1)
  righttree=self.fit(rightx,righty,depth+1)
  return {'feature':feat,'threshold':thr,'left':lefttree,'right':righttree}
 def train(self,x,y):
  self.tree=self.fit(x,y)
 def predsample(self,node,xi):
  if not isinstance(node,dict):return node
  f=node['feature']
  t=node['threshold']
  if xi[f]<=t:
   return self.predsample(node['left'],xi)
  else:
   return self.predsample(node['right'],xi)
 def predict(self,x):
  return np.array([self.predsample(self.tree,xi) for xi in x])

def drawtree(node,graph=None,parent=None,edgelabel=''):
 if graph is None:graph=nx.DiGraph()
 lbl=("f"+str(node['feature'])+"<="+str(node['threshold'])) if isinstance(node,dict) else ("class:"+str(node))
 nid=len(graph.nodes)
 graph.add_node(nid,label=lbl)
 if parent is not None:
  graph.add_edge(parent,nid,label=edgelabel)
 if isinstance(node,dict):
  drawtree(node['left'],graph,nid,"yes")
  drawtree(node['right'],graph,nid,"no")
 return graph

def plottree(tree):
 g=drawtree(tree)
 pos=nx.spring_layout(g)
 labs=nx.get_node_attributes(g,"label")
 elabs=nx.get_edge_attributes(g,"label")
 plt.figure(figsize=(10,6))
 nx.draw(g,pos,with_labels=True,labels=labs,node_size=3000,node_color="lightblue")
 nx.draw_networkx_edge_labels(g,pos,edge_labels=elabs)
 plt.show()

if __name__=="__main__":
 data=np.array([[2,5,0],[3,6,0],[5,6,1],[6,5,1],[8,7,1],[1,4,0],[4,6,1],[7,8,1],[2,6,0],[5,5,1]])
 x,y=data[:,:-1],data[:,-1]
 dt=decisiontree(maxdepth=10)
 dt.train(x,y)
 print("predictions:",dt.predict(x))
 plottree(dt.tree)

  
  
  