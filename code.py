mp=dict()
f = open("input.txt", "r")
lines= f.readlines()
for x in lines:
    line = x.strip()
    data = line.split(':')
    mp[data[0]] = int(data[1].strip())

n=len(mp)
tmp=[]

print("Number of employees:")
k=int(input())
print()

tmp_keys=list(mp.keys())
tmp_val=list(mp.values())
tmp_val.sort()

res=float('inf')
for i in range(n-k+1):
    curr=tmp_val[i+k-1]-tmp_val[i]
    if curr < res:
        res=curr
        start = i
        end = i+k       

sorted_dict=dict(sorted(mp.items(), key=lambda item: item[1]))
goody = sorted_dict.keys()
result = list(goody)[start:end]

print("Here the goodies that are selected for distribution are:")
for x in result:
    print(x,":",mp[x])
print()

print('And the difference between the chosen goodie with highest price and the lowest price is',res)