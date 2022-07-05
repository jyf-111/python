from cProfile import label
import matplotlib.pyplot as plt

print(plt.style.available)
input_value = [1,2,3,4,5]
squares = [1,4,9,16,25]

fig,ax = plt.subplots() # fig整张 ax小图

ax.plot(input_value,squares,linewidth=3)
ax.set_title("平方数",fontsize=24)
ax.set_xlabel("值",fontsize=14)
ax.set_ylabel("值得平方",fontsize=14)
ax.tick_params(axis='both',labelsize=14) # 刻度
plt.style.use('bmh')

plt.show()