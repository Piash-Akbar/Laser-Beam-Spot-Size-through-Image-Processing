import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/oo_columns.csv')

steps = np.array(df.steps)
intensity = np.array(df['N_values'])

plt.plot(steps,intensity)
plt.title('')
plt.xlabel('steps')
plt.ylabel('pixel value')
plt.savefig('./zz.png')