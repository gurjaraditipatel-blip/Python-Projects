from functools import reduce

#map example
l=[1,2,3,4,5]

square=lambda x: x*x

sqList=map(square,l)
print(list(sqList))

# with using for loop
sqList2=[]
for i in l:
  square2=lambda i: i*i
  sqList2.append(square2(i))
print(sqList2)

# FILTER example
def even(n):
  if(n%2==0):
    return True
  return False

onlyEven=filter(even,l)
print(list(onlyEven))


# Reduce example
def sum(a,b):
  return a+b

mul=lambda x,y:x*y

print(reduce(sum,l))
print(reduce(mul,l))

L=[12,34,56,87,999,654,4343]

def greater(a,b):
  if a>b:
    return a
  return b

print(reduce(greater,L))