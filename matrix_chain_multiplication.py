import random
import sys
import time
import matplotlib.pyplot as plt

#Brute-Force_recursive 
def MatrixChainOrder0(p,n): 
  s = [[0] * n for _ in range(n)]  
  def matrix_chain_recursive(i, j):
    if i == j:
      return 0
    _min = sys.maxsize
    for k in range(i, j):
      cost = matrix_chain_recursive(i, k) + matrix_chain_recursive(k + 1, j) + (p[i-1] * p[k] * p[j])
      if cost < _min:
        _min = cost
        s[i][j] = k 
    return _min
  min_scalar_multiplications = matrix_chain_recursive(1, n-1)
  return min_scalar_multiplications, s

#Dynamic Programming
def matrixChainOrder1(p,n):
	m = [[0 for _ in range(n)] for _ in range(n)]
	s = [[0 for _ in range(n)] for _ in range(n)]
	for i in range(1, n):
		m[i][i] = 0
	for L in range(2, n):
		for i in range(1, n - L + 1):
			j = i + L - 1
			m[i][j] = sys.maxsize
			for k in range(i, j):
				tempCost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
				if (tempCost < m[i][j]):
					m[i][j] = tempCost
					s[i][j] = k
	return m[1][n-1], s

t_recursive = []
t_dynamic = []
for t in range(2,17):
	P = [random.randint(1,30) for _ in range(t)]
	n = len(P)
 
	t_start = time.time()
	m1,s1 = MatrixChainOrder0(P, n)
	t_end = time.time()
	t_recursive.append(t_end-t_start)
 
	t_start = time.time()
	m2,s2 = matrixChainOrder1(P, n)
	t_end = time.time()
	t_dynamic.append(t_end-t_start)

x = [i for i in range(2,17)]
plt.xlabel("Input_size")
plt.ylabel("Execution time")
plt.plot(x, t_recursive, 'r')
plt.plot(x, t_dynamic, 'b')
plt.legend(['Brute-Force_Recursive','Dynamic Programming'])
plt.show()
