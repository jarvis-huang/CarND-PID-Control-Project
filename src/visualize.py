import numpy as np
import matplotlib.pyplot as plt

build_folder = '../build/'

f1 = build_folder+'cte_p.txt'
f2 = build_folder+'cte_pd.txt'

f3 = build_folder+'cte_bias_pd.txt'
f4 = build_folder+'cte_bias_pid.txt'

cte_p = np.array([])
with open(f1) as f:
    for line in f:
        cte_p = np.append(cte_p, float(line))

cte_pd = np.array([])
with open(f2) as f:
    for line in f:
        cte_pd = np.append(cte_pd, float(line))

cte_bias_pd = np.array([])
with open(f3) as f:
    for line in f:
        cte_bias_pd = np.append(cte_bias_pd, float(line))

cte_bias_pid = np.array([])
with open(f4) as f:
    for line in f:
        cte_bias_pid = np.append(cte_bias_pid, float(line))
                
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
ax1.plot(cte_p, 'r', label='P controller')
ax1.plot(cte_pd, 'g', label='PD controller')
ax1.set_title('CTE under no bias')
plt.sca(ax1)
plt.legend(loc="upper left")
ax2.plot(cte_bias_pd, 'r', label='PD controller')
ax2.plot(cte_bias_pid, 'g', label='PID controller')
ax2.set_title('CTE under steering bias')
plt.sca(ax2)
plt.legend(loc="upper left")
plt.show()

