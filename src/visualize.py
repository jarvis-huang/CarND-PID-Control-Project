import numpy as np
import matplotlib.pyplot as plt

build_folder = '../build/'

'''
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
'''

'''
f1 = build_folder+'cte_p_0.15.txt'
f2 = build_folder+'cte_p_0.3.txt'

cte_small = np.array([])
with open(f1) as f:
    for line in f:
        cte_small = np.append(cte_small, float(line))

cte_large = np.array([])
with open(f2) as f:
    for line in f:
        cte_large = np.append(cte_large, float(line))

plt.plot(cte_small, 'r', label='P=0.15')
plt.plot(cte_large, 'g', label='P=0.3')
plt.title('CTE of P controller')
plt.legend(loc="upper left")
plt.show()
'''

'''
f1 = build_folder+'cte_d_0.2.txt'
f2 = build_folder+'cte_d_0.8.txt'

cte_d_small = np.array([])
with open(f1) as f:
    for line in f:
        cte_d_small = np.append(cte_d_small, float(line))

cte_d_large = np.array([])
with open(f2) as f:
    for line in f:
        cte_d_large = np.append(cte_d_large, float(line))

plt.plot(cte_d_small, 'r', label='D=0.2')
plt.plot(cte_d_large, 'g', label='D=0.8')
plt.title('CTE of PD controller')
plt.legend(loc="upper right")
plt.show()
'''

f0 = build_folder+'cte_i_0.txt'
f1 = build_folder+'cte_i_0.003.txt'
f2 = build_folder+'cte_i_0.008.txt'

cte_i_zero = np.array([])
with open(f0) as f:
    for line in f:
        cte_i_zero = np.append(cte_i_zero, float(line))
        
cte_i_small = np.array([])
with open(f1) as f:
    for line in f:
        cte_i_small = np.append(cte_i_small, float(line))

cte_i_large = np.array([])
with open(f2) as f:
    for line in f:
        cte_i_large = np.append(cte_i_large, float(line))

plt.plot(cte_i_zero, 'b', label='I=0')
plt.plot(cte_i_small, 'r', label='I=0.003')
plt.plot(cte_i_large, 'g', label='I=0.008')
plt.title('CTE of PID controller')
plt.legend(loc="upper left")
plt.show()

