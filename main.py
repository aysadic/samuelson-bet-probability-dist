import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

np.random.seed(1923)
coin = np.array([0,1])
sums = []

trial = 100
noPeople = 30000
people = np.zeros(noPeople)
profit = 200
loss = 100

for i in range(noPeople):
    for j in range(trial):
        roll = np.random.choice(coin)
        if roll == 1:
            people[i] += profit
        elif roll == 0:
            people[i] -= loss

print(people)
print(len(people))
print(min(people))
print(max(people))

ax = sns.displot(people, kde=True)
ax.set(xlabel='Kazanç [TL]', ylabel='Kişi Sayısı')
plt.show()


