import matplotlib.pyplot as plt
import matplotlib

#--------comments' time--------
#中文样式
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.size']=10
#数据
x=[0,1,2,3,4,5,6]
y=[29,55,33,45,40,15,3]
#y值
for i in range(0,7):
    plt.text(x[i]-0.1,y[i]+0.5,y[i])
#标题
plt.title('评论时间',size=20)
#x,y标签
plt.ylabel('评论条数')
plt.xlabel('时间')
#x轴下标
plt.xticks((0,1,2,3,4,5,6),('7-13之前','7-13','7-14','7-15','7-16','7-17','7-18'))
#柱状图
plt.bar(x,y,width=0.8)

plt.show()

#--------stars table--------
matplotlib.rcParams['font.size']=15
#数据
labels='一星','两星','三星','四星','五星'
sizes=[8,21,40,57,91]
explode=[0,0,0,0,0.1]
colors='skyblue','plum','darkgrey','sandybrown','greenyellow'
#饼图 pctdistance:百分比的text离圆心的距离
plt.pie(sizes,labels=labels,autopct='%1.1f%%',explode=explode,colors=colors,pctdistance=0.7,shadow=True)

plt.show()

#--------catagories--------
#数据
labels=['幽默搞笑','影视','未分类','科技','心灵鸡汤','军事','美食','动漫','文化','文学','其他']
sizes=[12,199,148,10,50,35,84,28,58,32,60]
colors=['darksalmon','c','orange','palegreen','dodgerblue','plum','khaki','mediumpurple','lightblue','hotpink','silver']
#饼图
plt.pie(sizes,labels=labels,autopct='%1.1f%%',pctdistance=0.7,colors=colors)
plt.show()

#--------sentiment of comments--------
#数据
labels=['positive','neutral','negative']
sizes=[87,23,102]
explode=[0,0,0.1]
#饼图
plt.pie(sizes,labels=labels,explode=explode,autopct='%1.1f%%')
plt.show()
