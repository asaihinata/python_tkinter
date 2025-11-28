import tkinter as tk,numpy as np,japanize_matplotlib
from manyfunction import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator,LogLocator,AutoLocator
from matplotlib.dates import AutoDateLocator,DateFormatter
graph_color=["#4477AA","#EE7733","#228833","#AA66CC","#77AADD","#FFA94D","#55AA55","#CC3311","#CC99FF","#FF8888","#444444","#888888","#332288","#88ccee","#44aa99","#117733","#999933","#ddcc77","#cc6677","#882255","#aa4499","#dddddd"]
class GraphWidget(tk.Frame):
 def __init__(self,master,kwargs):
  super().__init__(master)
  self.bg=parsecolor(kwargs.get("bg",THEMES["bg6"]))# グラフ上
  self.fg=parsecolor(kwargs.get("bg",THEMES["fg1"]))# グラフ上の文字色
  self.font_mpl=FontProperties(fname="")
  self.size=self._size(kwargs.get("size",(500,450)))# 表示させるサイズ
  self.width=self.size[0]
  self.height=self.size[1]
  self.fig=Figure(figsize=(self.width/100,self.height/100),dpi=100,facecolor=self.bg)
  self.ax=self.fig.add_subplot(111)
  self.canvas=FigureCanvasTkAgg(self.fig,master=self)
  self.canvas.get_tk_widget().pack(fill="both",expand=True)
  self.canvas.draw()
 def _size(self,sizes=(500,450)):
  if isinstance(sizes,(tuple,list)) and len(list(sizes))==2:
   if isinstance(sizes[0],(int,float)) and isinstance(sizes[1],(int,float)):return tuple(sizes)
   else:
    if not isinstance(sizes[0],(int,float)):sizes[0]=500
    if not isinstance(sizes[1],(int,float)):sizes[1]=450
    return sizes
  else:return (500,450)