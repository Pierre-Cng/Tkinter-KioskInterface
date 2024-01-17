'''
import threading 
import time 
from queue import Queue

q = Queue()

class Class1:
    def func(self):
            for i in range(100):
                data = q.get()
                print(data)

class Class2:
    def __init__(self):
            self.data = 0

    def func(self):
            for i in range(100):
                  q.put(self.data)
                  self.data +=1

obj2 = Class2()       
obj1 = Class1()
thread2 = threading.Thread(target=obj2.func)
thread1 = threading.Thread(target=obj1.func)
thread2.start()
thread1.start()
print('standard:', obj2.data)
print([x for x in range(100)])
'''
import math 
from matplotlib import pyplot as plt 
data = []
signals = {}
selected_signals = ['Channel1.Message1.signal2']
'''
for x in range(20):
    data.append(f'Channel1.Message1.signal2, {x}, {math.cos(x)}')

for item in data:
    signal, x, y = item.strip().split(',')
    print(signal)
    if signal not in signals:
        signals[signal] = {'name': signal, 'x':[], 'y':[]}
    signals[signal]['x'].append(x)
    signals[signal]['y'].append(y)
'''
'''
for signal in signals:
    if signal in selected_signals:
        plt.plot(signals[signal]['x'], signals[signal]['y'], label=signal)
'''

fig1, ax = plt.subplots()
for x in range(200):
    data.append((x, math.sin(x)))
x, y = zip(*data)
print(x, y)
ax.plot(x, y)
plt.show()
