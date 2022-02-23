import matplotlib.pyplot as plt
import warnings
warnings.simplefilter('ignore')

import numpy as np
import pandas as pd
data = pd.DataFrame()
np.random.seed(0)
data['身長'] = np.random.normal(170,5,100)
data['クラス'] = ['a','b','c','d'] * 25
data['成績'] = [ 2, 5, 4, 1, 4, 3, 4, 2, 4, 5] * 10
data['体重'] = np.random.normal(60,3,100)

print(data.head())

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.hist(data['身長'])
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(data['体重'])
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(data['身長'],data['体重'])
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(data['身長'],data['体重'])
m,c =np.polyfit(data['身長'],data['体重'],1)
ax.plot(data['身長'],m*data['身長'] + c)
fig.suptitle('Regression-line')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

for class_type in data['クラス'].unique():
    ax.plot(data.loc[data['クラス'] == class_type, '身長'].values,label=class_type)
    ax.legend(loc='upper right')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

for class_type in data['クラス'].unique():
  ax.hist(data.loc[data['クラス'] == class_type, '身長'].values,label=class_type,alpha=0.2,bins = 20 )
ax.legend(loc='upper right')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.hist(data['身長'])
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
ax.set_xlabel('X', fontsize=15)
ax.set_ylabel('Y', fontsize=15)
ax.set_ylim(0, 30)
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
fig.suptitle('title')
ax1.set_title('1')
ax1.hist(data['身長'])
ax2.set_title('2')
ax2.hist(data['クラス'])
ax3.set_title('3')
ax3.hist(data['成績'])
ax4.set_title('4')
ax4.hist(data['体重'])
fig.subplots_adjust(wspace=0.5, hspace=0.5)
plt.show()