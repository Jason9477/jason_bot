ls=[]
with open('country_list.txt','r') as f: 
    for _ in f.readlines():
        n=str(_).split('\n')[0]
        ls.append(n)
print(ls)