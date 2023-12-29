from matplotlib import pyplot as plt 

figure, ax = plt.subplots()

with open('data.txt', 'r') as file:
    for line in file:
        values = [int(val) for val in line.split(',')]
        x, y = values[0], values[1]
        ax.plot(x, y, 'b.')
plt.show()