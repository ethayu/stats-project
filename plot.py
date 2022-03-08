import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab

data = pd.read_csv('data.csv')
data.dropna(inplace=True)
data = data[data.age != 0]
data.plot.scatter(x='age', y='ACS')
m, b = np.polyfit(data.age, data.ACS, 1)
plt.plot(data.age, m*data.age + b, 'r-')
pylab.gcf().canvas.manager.set_window_title('Age vs ACS')
#plt.savefig('Age_vs_ACS.png', dpi=1200)
pylab.show()

data = data[data.earnings != 0]
data.plot.scatter(x='earnings', y='ACS')
m, b = np.polyfit(data.earnings, data.ACS, 1)
plt.plot(data.earnings, m*data.earnings + b, 'r-')
pylab.gcf().canvas.manager.set_window_title('Earnings vs ACS')
#plt.savefig('Earnings_vs_ACS.png', dpi=1200)
pylab.show()
