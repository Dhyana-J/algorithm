from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement

data = ['A','B','C','D']

result = list(permutations(data,2))
result2 = list(combinations(data,2))
result3 = list(product(data,repeat=2)) #permutation + 원소 중복
result4 = list(combinations_with_replacement(data,2)) #combination + 원소 중복

print('============')
print((result))
print('============')
print((result2))
print('============')
print((result3))
print('============')
print((result4))