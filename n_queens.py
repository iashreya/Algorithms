#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[262]:


class N_Queens:
    def __init__(self, n):
        self.n = n
        self.arr = np.zeros(n**2).reshape(n,n)
        self.queens = []
        self.safe = []
        
    def safe_cells(self):
        for x,y in self.queens:
            self.arr[x,y]=2
            hor = [(x,i) for i in range(self.n) if self.arr[x,i]==0]
            ver = [(i,y) for i in range(self.n) if self.arr[i,y]==0]
            left_diag = [(i,j) for i,j in zip(range(x,-1,-1),range(y,-1,-1)) if self.arr[i,j]==0]+[(i,j) for i,j in zip(range(x,self.n,1),range(y,self.n,1)) if self.arr[i,j]==0]
            right_diag = [(i,j) for i,j in zip(range(x,self.n,1),range(y,-1,-1)) if self.arr[i,j]==0]+[(i,j) for i,j in zip(range(x,-1,-1),range(y,self.n,1)) if self.arr[i,j]==0]
            for i in hor+ver+left_diag+right_diag:
                self.arr[i]=1
        self.safe = [(i,j) for i in range(self.n) for j in range(self.n) if self.arr[i,j]==0]
    

    def solveNQ(self,i,j):
        if (i,j) not in self.safe:
            return False
        else:
            self.queens.append((i,j))
            self.safe_cells()
            if len(self.queens)==self.n:
                return True
            if len(self.safe)==0:
                if len(self.queens)==self.n:
                    return True
                else:
                    return False
            else:
                self.solveNQ(self.safe[0][0],self.safe[0][1])
        if len(self.queens)==self.n:
            return True
        else:
            return False
        
        
    def solve(self):
        self.safe_cells()
        initial_state = self.safe.copy()
        for i,j in self.safe:
            self.arr[i,j]=2
            if self.solveNQ(i,j)==True:
                print(self.queens)
                for i in range(self.n):
                    for j in range(self.n):
                        if self.arr[i,j]!=2:
                            self.arr[i,j]=0
                print(self.arr)
                return True
            self.safe = initial_state.copy()
            self.queens = []
            self.arr = np.zeros(self.n*self.n).reshape(self.n, self.n)
        return False
        


# In[267]:


n = N_Queens(6)


# In[268]:


n.solve()


# In[ ]:





# In[ ]:




