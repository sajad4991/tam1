a = input("har chi dos dari az keybordet vard kon : ")
b = len(a)
for i in range(b+1):
    if a[i] == '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' :
        print("string have numbers")
        break        
    else :
         print("a")
