import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox

fig,ax = plt.subplots()
x_values = range(100)
y_values = [x**2 for x in x_values]

# ax.scatter(x_values,y_values,s=20,c=(0,0.8,0))
ax.scatter(x_values,y_values,s=20,c=y_values,cmap=plt.cm.Blues) # colormap

ax.set_title("平方数",fontsize=24)

ax.axis([0,110,0,11000]) # 轴范围

plt.savefig('matplotlib/squares_plot.png',bbox_inches='tight') # bbox_inches裁剪掉多余空白

plt.show()
