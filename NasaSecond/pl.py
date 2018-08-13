import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
alphs, cds, cls = [], [], []
for ii in glob.glob('aoa_*'):
   f, ax = plt.subplots()
   plt.subplots_adjust(right=.8, hspace=1)
   ax2 = ax.twinx()
   dat = pd.read_csv('./%s'%ii, header=None, sep=r'\s+')[1000:]
   dat.columns = ['time', 'Cd', 'Cl']
   dat = dat.sort('time').iloc[25:]
   alphs.append(float((ii.split('_')[1].strip('aoa').strip('.dat'))))
   cds.append(np.mean(dat.Cd[dat.time > 6]))
   cls.append(np.mean(dat.Cl[dat.time > 6]))
   ax.plot(dat.time, dat.Cd, c='green')
   ax2.plot(dat.time, dat.Cl, c='pink')
   ax.set_ylabel('Cd', color='green')
   ax2.set_ylabel('Cl',color= 'pink')
   f.savefig('timehist%f.pdf'%alphs[-1])
   #plt.show() ; hey
   plt.clf() 
   
f, ax = plt.subplots()
ax2 = ax.twinx()

shapes = ['^', 'p', '*']
for ii, jj in enumerate([80, 120, 180]):
   dat = pd.read_csv('../grit%i.dat'%jj, sep=r'\s+', header=None)
   dat.columns = ['alpha', 'Cl', 'Cd']
   ax.plot(dat.alpha, dat.Cd * 1e4, marker=shapes[ii], c='purple', label='Observed, Grit=%i'%jj)
   ax2.plot(dat.alpha, dat.Cl, marker=shapes[ii], c='green', label='Observed, Grit=%i'%jj)


ax.scatter(alphs, cds, c='purple', marker='x', label='Nalu', s=10)
ax2.scatter(alphs, cls, c='green', marker='x', s=10)
ax.set_ylabel('Cd', color='purple')
ax2.set_ylabel('Cl',color= 'green')
ax.set_xlabel("AOA (degrees)")
ax.legend()
plt.tight_layout()
plt.savefig('NACA_Nalu_vs_Wind_tunnel_data.pdf')
plt.clf()

f, ax = plt.subplots()
ax2 = ax.twinx()

shapes = ['^', 'p', '*']
for ii, jj in enumerate([80, 120, 180]):
   dat = pd.read_csv('../grit%i.dat'%jj, sep=r'\s+', header=None)
   dat.columns = ['alpha', 'Cl', 'Cd']
   ax.plot(dat.alpha, dat.Cd * 1e4, marker=shapes[ii], c='purple', label='Observed, Grit=%i'%jj)
   ax2.plot(dat.alpha, dat.Cl, marker=shapes[ii], c='green', label='Observed, Grit=%i'%jj)


ax.scatter(alphs, cds, c='purple', marker='x', label='Nalu', s=10)
ax2.scatter(alphs, cls, c='green', marker='x', s=10)
ax.set_ylabel('Cd', color='purple')
ax2.set_ylabel('Cl',color= 'green')
ax.set_xlabel("AOA (degrees)")
ax.legend()
ax.set_xlim(17, 21)
plt.tight_layout()
plt.savefig('zoom.pdf')
plt.clf()
