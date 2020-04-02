import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


x = [1, 1, 1, 5, 6, 18, 47, 98, 191, 359, 670, 947, 1236, 1529,
     1872, 2433, 3629, 5698, 7402, 9217, 10827, 13531, 15679]
y = ['10 MART 2020', '11 MART 2020', '12 MART 2020', '13 MART 2020', '14 MART 2020', '15 MART 2020', '16 MART 2020', '17 MART 2020', '18 MART 2020', '19 MART 2020', '20 MART 2020', '21 MART 2020',
     '22 MART 2020', '23 MART 2020', '24 MART 2020', '25 MART 2020', '26 MART 2020', '27 MART 2020', '28 MART 2020', '29 MART 2020', '30 MART 2020', '31 MART 2020', '1 NİSAN 2020']

plt.plot(y,x,"o--r")

plt.title("Türkiye corona virüs tablosu")

plt.xlabel("Tarih")

plt.show()

"""

x = np.linspace(0,2,200)

plt.plot(x,x,label="linear")
plt.plot(x,x**2,label="linear")
plt.plot(x,x**3,label="linear")

"""
