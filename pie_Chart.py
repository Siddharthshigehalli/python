import matplotlib.pyplot as plt

labels = 'A', 'B','C'
selsctions = [70, 2, 30]
colors = ['r', 'p', 'b']

  plt.pie(selection, labels=labels, colors=colors
          stratangle=60,
          explode = (0, 0, 0),
          autopct = '%1.2f%%')


plt.axis('equal')
plt.title('Population')
plt.show()
