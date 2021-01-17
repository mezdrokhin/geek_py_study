import json
with open("file7.txt", 'r', encoding='utf-8') as f7:
    content = f7.readlines()
good=[]
d1={}
for el in content:
    st=el.split(' ')
    pr=int(st[2])-int(st[3])
    d1[st[0]] = pr
    if pr>0:
        good.append(pr)
d1["average_profit"]=sum(good)/len(good)
print(d1)
with open("file7_js.json", "w") as f7j:
    json.dump(d1, f7j)