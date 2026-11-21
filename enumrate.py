l=[2,342,52,7543]

# index=0
# for item in l:
#   print(f"the item number at index {index} is {item}")
#   index+=1

# this can bhi simplify using enumerate func

for index,item in enumerate(l):
  print(f"the item number at index {index} is {item}")


l2=[1,2,3,4,5,6,7,8,9]

for i, index in enumerate(l2):
  if(i==2 or i==4 or i==6):
    print("item")