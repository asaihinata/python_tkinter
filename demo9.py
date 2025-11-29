from manyfunction import *
clear()
from mylibral import *
x1=[1,2,3]
y1=[1,2,3]
layout=[
[sgg.Text(text="折り線グラフ")],
[sgg.LineGraph(xlist=x1,ylist=y1,title="タイトル",xlabel="xlabel",ylabel="ylabel")],
[sgg.Text(text="棒グラフ")],
[sgg.BarGraph(xlist=x1,ylist=y1,title="タイトル",xlabel="xlabel",ylabel="ylabel",width=0.5)],
[sgg.Text(text="散布図")],
[sgg.Scatter(xlist=x1,ylist=y1,title="タイトル",xlabel="xlabel",ylabel="ylabel")],
[sgg.Text(text="円グラフ")],
[sgg.Pie(date=x1,title="タイトル")]
]
win=sgg.window(title="mylibral ウィジェット デモ",layout=layout,scroll_x=True,scroll_y=True,maxmine=True)
win.run()