
x = input("Please enter the first data block")
y = input("Please enter the second data block")
def xor(x,y):
 result=""
 if len(x) == len(y):
# x = 1001 ,  y = 1010 
# x XOR y = 0011
    for i in range (len(x)):
     if x[i] == y[i] :
      result = result + "0"
     else: 
      result = result + "1"
 else:
  print("The two data blocks must have equal lengths")
 return result

print(f"{x} xor {y} = ",xor(x,y))