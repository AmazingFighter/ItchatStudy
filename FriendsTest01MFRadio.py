# -*-coding: utf-8 -*-
__author__ = 'wangyang'
import itchat
import numpy as np
import matplotlib.pyplot as plt

itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)[0:]
male = female = other = 0
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
total = len(friends[1:])

M = float(male) / total * 100
F = float(female) / total * 100
O = float(other) / total * 100
print u"男性好友：%.2f%%" % M
print u"女性好友：%.2f%%" % F
print u"其他：%.2f%%" % O

fig = plt.figure(figsize=(7,21))
fig.subplots_adjust(top=0.8)
colors = ['red','yellow','blue']
ax1 = fig.add_subplot(211)
x = [M,F,O]
labels = ['male','female','other']
ax1.pie(x,labels=labels,autopct='%1.2f%%',colors = colors)
ax1.set_title('Gender Ratio of My Friends')

ax2 = fig.add_subplot(212)
x1 = np.arange(1,4)
y1 = [male,female,other]
ax2.bar(x1,y1,color = colors)
plt.xticks(x1,('male','female','other'))
ax2.set_title('Gender Distribution Histogram')


plt.savefig('MF.png',format = 'png')
plt.show()
