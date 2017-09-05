print(int("11",15))
    
s = input()
s = s.strip()
#if(int(s)==0):
#    break
f = list(map(int,s.split(" ")))
a = p2n(f)-1
k = math.sqrt(a)
ff = []
for x in pr:
    if(x>k):
        break
    c = 0
    while(a%x==0):
        c += 1
        a //= x
    if(c>0):
        ff.append([x,c])   
        
if(a!=1):
    ff.append([a,1])

ff.sort(key=lambda x: (x[0]*-1))

for x in ff:
    print(x[0],x[1],end = " ")
print("")




#a = [1, 3, 5]
#a[1:2] = [x + 2 for x in a[1:2]]
#print(a)
# f[0]  f[1]   w = w.replace("  ","")


#m = int("00111",2) & int("11111",2)
#print(bin(m))  


#z = list(filter(lambda x: x==1, f))
#f = list(map(int,f))
#print(sum(f))

# f = sorted(f, key=lambda x: (x%10, x*-1))
# list(filter(lambda x: '*' not in x, f))

# f = list(map(int,s.split(" "))) " "
# f[0]  f[1]
# print("")

#def gcd(m, n):
#    if(m%n==0):
#        return n
#    else:
#        return gcd(n, m%n)