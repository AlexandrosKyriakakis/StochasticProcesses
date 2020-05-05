import numpy as np  # numerical computations library. We will call it np in our code
import matplotlib.pyplot as plt 
import sympy as sp
"""
# αν έχω μια λίστα 
mylist = [1,2,3,4,5] 
# και θέλω να κάνω την λίστα expolist =  2^mylist[i] για κάθε i που ανηκει στη λιστα mylist
#μπορώ να κάνω map (όπως στην ML):
mylist = list(map(lambda i: 2**i, mylist))
print(mylist)
# Αλλά μπορεις να το κάνεις και με generator που ειναι αυτό που μου αρέσει πολύ
mylist = [2**x for x in mylist]
print (mylist)
"""
x = np.arange(-10,10,0.0001)
y = -x**3 + (2*x**2)/3 + (5*x)/18 + 1/18

plt.subplot()
plt.plot(x,y)
plt.grid()
#plt.show()
#np.set_printoptions(precision=5)
p = 2/3
a = np.array([[1/2,1/2],[1/4,3/4]])
#print(a.dot(a))
#print(a.dot(a))
#print((np.sqrt(3)+1)/6)
#b = np.array([[1,1,1],[1,(np.sqrt(3)-1)/6,(np.sqrt(3)+1)/6],[1,((np.sqrt(3)-1)/6)**2,((np.sqrt(3)+1)/6)**2]])
#print(np.linalg.inv(b).dot([[1],[0],[1/2]]))
#a = np.array([[1,1,1],[1,(-1/6)*(1 + 1.j),(-1/6)*(1 - 1.j)],[1,((-1/6)*(1 + 1.j))**2,((-1/6)*(1 - 1.j))**2]], dtype=complex)
#c = np.array([[1.,0,0],[0,0.9999,0.0001],[0,0.0001,0.9999]])
N = 10000000000
c = 0
for x in range(1,N+1):
    c += 1/(4**x)

print (c)

a = sp.Matrix(a)
#print(a.jordan_form())
b = np.array([1,1,1])
b = sp.Matrix(b)

#print(np.linalg.eigvals([[0,1/2,1/2],[1/3,1/3,1/3],[0,2/3,1/3]]))
#print(np.roots([-1, 2/3, 5/18, 1/18]))