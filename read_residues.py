# _*_ coding: utf-8 _*_
# @Author   : Qingbo Jiao
# @Time     : 2023/4/10 12:55
# @FileName : read_residues.py
file = []
with open('5988pocket.pdb','r') as f:
    lines = f.readlines()
    for line in lines:
        temp = []
        l = line.split()
        temp.append(l[3])
        temp.append(l[4])
        file.append(temp)
# file = np.array(file)
res = []
for i in file:
    if i not in res:
        res.append(i)
print(res)
print(len(res))
# save Pocket5988.csv
import pandas as pd

df = pd.DataFrame(res, columns=['Residue','Location'])
df.to_csv('Pocket5988.csv', index=False)
