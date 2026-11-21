import sys
word=['L','E','B','R','O','S']
find=input()
for idx,val in enumerate(word):
    if find in val:
        print(idx) 
        sys.exit()
print("None")
        