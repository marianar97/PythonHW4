# HW4
## PART A - Mariana
## PART B - Sophia
## PART C - Angela

from datetime import datetime
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import FormatStrFormatter


##### PART A 

###code for modifying 2019 data

# input = open('/Users/sophiakuo/Documents/23F-Python/Assignments/HW4/daily-treasury-rates2019.csv',encoding='utf-8')

# daily_yield_curves = []
# cnt=0
# for i in input.readlines():
    
#     replaced = i.replace('"','').replace('\n','')
#     replaced_lst = replaced.split(',')
#     #print(replaced_lst)
#     if cnt==0:
#         column = replaced_lst
#     else:
#         for j in range(len(replaced_lst)):
#             if j==0:
#                 replaced_lst[j] = datetime.strptime(replaced_lst[j], '%m/%d/%Y').date().strftime('%m/%d/%y')
#             if j!=0:
#                 replaced_lst[j] = float(replaced_lst[j])
#         daily_yield_curves.insert(-cnt,replaced_lst)
#     cnt+=1
    
# daily_yield_curves.insert(0,column)
# #daily_yield_curves

###code for modifying and output 2022 data

input = open('/Users/sophiakuo/Documents/23F-Python/Assignments/HW4/daily-treasury-rates2022.csv',encoding='utf-8')


daily_yield_curves = []
cnt=0
for i in input.readlines():
    
    replaced = i.replace('"','').replace('\n','')
    replaced_lst = replaced.split(',')
    #print(replaced_lst)
    if cnt==0:
        column=replaced_lst
        column.pop(4)
    else:
        for j in range(len(replaced_lst)):
            if j==0:
                replaced_lst[j] = datetime.strptime(replaced_lst[j], '%m/%d/%Y').date().strftime('%m/%d/%y')
            if j!=0 and j!=4:
                replaced_lst[j] = float(replaced_lst[j])
        replaced_lst.pop(4)
        daily_yield_curves.insert(-cnt,replaced_lst)

    cnt+=1
    
daily_yield_curves.insert(0,column)

output = open('/Users/sophiakuo/Documents/23F-Python/Assignments/HW4/daily_yield_curves_2022.txt','wt')
for i in daily_yield_curves:
    frmt_row = f"{i[0]: <10} {i[1]: <5} {i[2]: <5} {i[3]: <5} {i[4]: <5} {i[5]: <5} {i[6]: <5} {i[7]: <5} {i[8]: <5} {i[9]: <5} {i[10]: <5} {i[11]: <5} {i[12]: <5}\n"
    output.write(frmt_row)

output.close()


##### PART B

### transform data
data = daily_yield_curves
x=[]
z=[]

for i in range(len(data)):
    if i==0:
        Y=np.array([[1, 2, 3, 6, 12, 24, 36, 60, 84, 120, 240, 360]]).transpose()
    else:
        x.append((datetime.strptime(data[i][0], '%m/%d/%y') - datetime.strptime(data[1][0], '%m/%d/%y')).days)  
        z.append(data[i][1:])

X=np.array([x])
Z=np.array(z).transpose()

#print(X.shape, Y.shape, Z.shape)

### plot_surface
fig = plt.figure(figsize=(8, 10))
ax = fig.add_subplot(1, 1, 1, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set(xlabel='trading days since 01/03/22', ylabel='months to maturity', zlabel='rate')
ax.zaxis.set_major_formatter(FormatStrFormatter('%.1f'))
fig.colorbar(surf, ax = ax, shrink = 1, aspect = 4 , anchor =(0.2,0.35),fraction=0.08) 
fig.show()


### plot_wireframe
fig = plt.figure(figsize=(8, 10))
ax = fig.add_subplot(1, 1, 1, projection='3d')
surf = ax.plot_wireframe (X, Y, Z, cmap=cm.coolwarm)
ax.set(xlabel='trading days since 01/03/22', ylabel='months to maturity', zlabel='rate')
ax.zaxis.set_major_formatter(FormatStrFormatter('%.1f'))
fig.colorbar(surf, ax = ax, shrink = 1, aspect = 4 , anchor =(0.2,0.35),fraction=0.08) 
plt.show()