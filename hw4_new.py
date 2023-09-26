# marianar@andrew.cmu.edu 
# anqiyang@andrew.cmu.edu 
# potungk@andrew.cmu.edu

from datetime import datetime
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import FormatStrFormatter
import pandas as pd

# part A

# code for modifying 2019 data

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

# code for modifying and output 2022 data

input = open('daily-treasury-rates2022.csv', encoding='utf-8')

daily_yield_curves = []
cnt = 0
for i in input.readlines():

    replaced = i.replace('"', '').replace('\n', '')
    replaced_lst = replaced.split(',')
    # print(replaced_lst)
    if cnt == 0:
        column = replaced_lst
        column.pop(4)
    else:
        for j in range(len(replaced_lst)):
            if j == 0:
                replaced_lst[j] = datetime.strptime(replaced_lst[j], '%m/%d/%Y').date().strftime('%m/%d/%y')
            if j != 0 and j != 4:
                replaced_lst[j] = float(replaced_lst[j])
        replaced_lst.pop(4)
        daily_yield_curves.insert(-cnt, replaced_lst)

    cnt += 1

daily_yield_curves.insert(0, column)

output = open('daily_yield_curves_2022.txt', 'wt')
for i in daily_yield_curves:
    frmt_row = f"{i[0]: <10} {i[1]: <5} {i[2]: <5} {i[3]: <5} {i[4]: <5} {i[5]: <5} {i[6]: <5} {i[7]: <5} {i[8]: <5} {i[9]: <5} {i[10]: <5} {i[11]: <5} {i[12]: <5}\n"
    output.write(frmt_row)

output.close()

# part B
# transform data
data = daily_yield_curves
x = []
z = []

Y = np.array([[1, 2, 3, 6, 12, 24, 36, 60, 84, 120, 240, 360]]).transpose()
for i in range(1,len(data[1:])):
    x.append((datetime.strptime(data[i][0], '%m/%d/%y') - datetime.strptime(data[1][0], '%m/%d/%y')).days)
    z.append(data[i][1:])

X = np.array([x])
Z = np.array(z).transpose()

# print(X.shape, Y.shape, Z.shape)

# plot_surface
fig = plt.figure(figsize=(8, 10))
ax = fig.add_subplot(1, 1, 1, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set(xlabel='trading days since 01/03/22', ylabel='months to maturity', zlabel='rate')
ax.zaxis.set_major_formatter(FormatStrFormatter('%.1f'))
fig.colorbar(surf, ax=ax, shrink=1, aspect=4, anchor=(0.2, 0.35), fraction=0.08)
fig.show()

# plot_wireframe
fig = plt.figure(figsize=(8, 10))
ax = fig.add_subplot(1, 1, 1, projection='3d')
surf = ax.plot_wireframe(X, Y, Z, cmap=cm.coolwarm)
ax.set(xlabel='trading days since 01/03/22', ylabel='months to maturity', zlabel='rate')
ax.zaxis.set_major_formatter(FormatStrFormatter('%.1f'))
#fig.colorbar(surf, ax=ax, shrink=1, aspect=4, anchor=(0.2, 0.35), fraction=0.08)
plt.show()



# part C
# Extract dates and bond maturities from the first sub-list
dates = [item[0] for item in daily_yield_curves[1:]]
#dates = [datetime.strptime(item[0], '%m/%d/%y').date() for item in daily_yield_curves[1:]]
bond_maturities = daily_yield_curves[0][1:]

# Extract interest rate values for the DataFrame
interest_rates = [[float(rate) for rate in item[1:]] for item in daily_yield_curves[1:]]
yield_curve_df = pd.DataFrame(interest_rates, columns=bond_maturities, index=dates)
yield_curve_df

# plot 1
yield_curve_df.plot(title="Interest Rate Time Series, 2022")
plt.show()
# plot 2 - transpose plot 1
yield_curve_df.T.plot(title="Interest Rate Time Series, 2022", xlabel="Maturity", ylabel="Yield %")
plt.show()

#plot 3 - 20 days interval
# Extract every 20th trading day
selected_trading_days = yield_curve_df[::20]
# # Transpose the DataFrame and select only the desired trading days
by_day_yield_curve_df = selected_trading_days.T

# Display the resulting DataFrame
by_day_yield_curve_df=by_day_yield_curve_df.rename(index = {'1 Mo':1, '2 Mo':2, '3 Mo':3, '6 Mo':6, '1 Yr':12, '2 Yr':24, '3 Yr':36, '5 Yr':60, '7 Yr':84, '10 Yr':120, '20 Yr':240, '30 Yr':360})
by_day_yield_curve_df.plot(title='2022 Yield Curves, 20 Day Interval').legend(loc=4)
plt.show()
plt.show()