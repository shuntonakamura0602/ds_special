import pandas as pd
import matplotlib.pyplot as plt
url='https://raw.githubusercontent.com/shuntonakamura0602/intro_git/main/savant_data.csv'

df=pd.read_csv(url,header=0)
x = []
for i in range(0,37):
    x.append(i)
wo = []
for i in df['woba']:
    wo.append(i)
babip = []
for i in df['babip']:
    babip.append(i)
plt.title('Relationship between woba and babip')
plt.plot(x,wo,'k-',label='woba')
plt.plot(x,babip,'k:',label='babip')
plt.legend()
plt.savefig('result.png')
plt.show()