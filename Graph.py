import tkinter as tk,numpy as np,japanize_matplotlib
from manyfunction import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
clear()
def numdexy(x,y):
 lenx,leny=len(x),len(y)
 if lenx!=leny and lenx<leny:y=[y[i] for i in range(0,lenx,1)]
 if lenx!=leny and leny<lenx:x=[x[i] for i in range(0,leny,1)]
 return(x,y)
class GraphWidget(tk.Frame):
 def __init__(self,master,kwargs):
  super().__init__(master)
  self.size=self._size(kwargs.get("size"))
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.graph_bg=parsecolor(kwargs.get("bg",THEMES["bg6"]))
  self.graph_grid=parsecolor(kwargs.get("graph_grid","#b7b7b7"))
  self.grid_xy=bols(kwargs.get("grid_xy"),True)
  self.grid_x=bols(kwargs.get("grid_x"),False)
  self.grid_y=bols(kwargs.get("grid_y"),False)
  self.x_ma_step=num0(kwargs.get("xa_step"),None)
  self.y_ma_step=num0(kwargs.get("ya_step"),None)
  self.x_mi_step=num0(kwargs.get("yi_step"),None)
  self.y_mi_step=num0(kwargs.get("yi_step"),None)
  y_verwrit=kwargs.get("y_verwrit")
  self.y_verwrit=y_verwrit if y_verwrit in ("horizontal","vertical") else "vertical"
  self.fig=Figure(figsize=(self.size[0]/100,self.size[1]/100),dpi=100,facecolor=self.graph_bg)
  self.ax=self.fig.add_subplot(111)
  self._apply_theme_colors()
  self.canvas=FigureCanvasTkAgg(self.fig,master=self)
  self.canvas.get_tk_widget().pack(fill="both",expand=True)
  self.canvas.draw()
 def _size(self,sizes=(500,400)):
  if isinstance(sizes,(tuple,list)) and len(list(sizes))==2:
   if isinstance(sizes[0],(int,float)) and isinstance(sizes[1],(int,float)):return tuple(sizes)
   else:
    if not isinstance(sizes[0],(int,float)):sizes[0]=500
    if not isinstance(sizes[1],(int,float)):sizes[1]=400
    return sizes
  else:return (500,400)
 def _apply_theme_colors(self):
  self.ax.set_facecolor(self.graph_bg)
  self.ax.tick_params(colors=self.fg)
  self.ax.title.set_color(self.fg)
  self.ax.xaxis.label.set_color(self.fg)
  self.ax.yaxis.label.set_color(self.fg)
  self._apply_grid()
 def _apply_grid(self):
  if self.grid_xy:self.ax.grid(True,color=self.graph_grid,linestyle="--",alpha=0.6)
  else:
   self.ax.grid(False)
   if self.grid_x:self.ax.xaxis.grid(True,color=self.graph_grid,linestyle="--",alpha=0.6)
   if self.grid_y:self.ax.yaxis.grid(True,color=self.graph_grid,linestyle="--",alpha=0.6)
 def _apply_labels(self,title,xlabel,ylabel):
  self.ax.set_title(title,color=self.fg)
  self.ax.set_xlabel(xlabel,color=self.fg)
  self.ax.set_ylabel(ylabel,color=self.fg,rotation=self.y_verwrit)
  self._apply_grid()
 def clear(self):
  self.ax.clear()
  self._apply_theme_colors()
class LineGraph(GraphWidget):
 def __init__(self,master,kwargs):
  super().__init__(master,kwargs)
  self.xlist=kwargs.get("xlist")
  self.ylist=kwargs.get("ylist")
  self.label=strs(kwargs.get("label"))
  self.title=strs(kwargs.get("title"))
  self.xlabel=strs(kwargs.get("xlabel"))
  self.ylabel=strs(kwargs.get("ylabel"))
  self.color=parsecolor(kwargs.get("color"))
  self.marker=markers(kwargs.get("marker","o"))
  self.markersize=num0(kwargs.get("markersize"),10)
  self.markerbg=parsecolor(kwargs.get("markerbg"))
  self.markerbgcolor=parsecolor(kwargs.get("markerbgcolor"))
  linestyle=lines(kwargs.get("linestyle"))
  self.linestyle=linestyle if linestyle in linestyle_list else "-"
  self.linewidth=num0(kwargs.get("linewidth"),2)
  self.alpha=range_num(num0s(kwargs.get("alpha"),1),0,1,1)
  if self.xlist!=None and self.ylist!=None:
   self.plot(x=self.xlist,y=self.ylist,title=self.title,xlabel=self.xlabel,ylabel=self.ylabel,color=self.color,marker=self.marker,linewidth=self.linewidth,linestyle=self.linestyle,markersize=self.markersize,alpha=self.alpha,markerfacecolor=self.markerbg,markeredgecolor=self.markerbgcolor)
 def plot(self,x,y,title="",xlabel="",ylabel="",color=None,marker="o",linewidth=2,linestyle="-",markersize=10,alpha=1,markerfacecolor=None,markeredgecolor=None):
  self.clear()
  (x,y)=numdexy(x,y)
  self.ax.plot(np.array(x),np.array(y),marker=marker,color=color,linewidth=linewidth,markersize=markersize,linestyle=linestyle,alpha=alpha,markeredgecolor=markeredgecolor,markerfacecolor=markerfacecolor)
  self._apply_labels(title,xlabel,ylabel)
  self.canvas.draw()
class BarGraph(GraphWidget):
 def __init__(self,master,kwargs):
  super().__init__(master,kwargs)
  self.xlist=kwargs.get("xlist")
  self.ylist=kwargs.get("ylist")
  self.label=strs(kwargs.get("label"))
  self.title=strs(kwargs.get("title"))
  self.xlabel=strs(kwargs.get("xlabel"))
  self.ylabel=strs(kwargs.get("ylabel"))
  self.color=parsecolor(kwargs.get("color"))
  self.border=parsecolor(kwargs.get("bg"))# edgecolor
  self.linewidth=num0(kwargs.get("linewidth"),2)
  self.alpha=range_num(num0s(kwargs.get("alpha"),1),0,1,1)
  self.width=range_num(num0s(kwargs.get("width"),1),0,1,1)
  align=kwargs.get("align")
  self.align=align if align in ("center","edge") else "center"
  if self.xlist!=None and self.ylist!=None:self.plot(x=self.xlist,y=self.ylist,title=self.title,label=self.label,xlabel=self.xlabel,ylabel=self.ylabel,color=self.color,linewidth=self.linewidth,alpha=self.alpha,width=self.width,border=self.border,align=self.align)
 def plot(self,x,y,title="",label=None,xlabel="",ylabel="",color=None,linewidth=2,alpha=1,width=0.8,border=None,align="center"):
  self.clear()
  (x,y)=numdexy(x,y)
  self.ax.bar(np.array(x),np.array(y),label=label,color=color,linewidth=linewidth,alpha=alpha,width=width,edgecolor=border,align=align)
  self._apply_labels(title,xlabel,ylabel)
  self.canvas.draw()
class Scatter(GraphWidget):
 def __init__(self,master,kwargs):
  super().__init__(master,kwargs)
  self.xlist=kwargs.get("xlist")
  self.ylist=kwargs.get("ylist")
  self.label=strs(kwargs.get("label"))
  self.title=strs(kwargs.get("title"))
  self.xlabel=strs(kwargs.get("xlabel"))
  self.ylabel=strs(kwargs.get("ylabel"))
  self.c=parsecolor(kwargs.get("color"))
  self.marker=markers(kwargs.get("marker","o"))
  self.markerborder=parsecolor(kwargs.get("markerbg"))
  self.s=num1s(kwargs.get("markersize"),10)
  self.alpha=range_num(num0s(kwargs.get("alpha"),1),0,1,1)
  self.linewidth=num0(kwargs.get("linewidth"),2)
  if self.xlist!=None and self.ylist!=None:
   self.plot(self.xlist,self.ylist,title=self.title,xlabel=self.xlabel,ylabel=self.ylabel,color=self.c,marker=self.marker,linewidth=self.linewidth,alpha=self.alpha,markerborder=self.markerborder)
 def plot(self,x,y,title="",xlabel="",ylabel="",color=None,marker="o",linewidth=2,alpha=1,markerborder=None):
  self.clear()
  (x,y)=numdexy(x,y)
  self.ax.scatter(np.array(x),np.array(y),marker=marker,alpha=alpha,linewidth=linewidth,c=color,edgecolors=markerborder)
  self._apply_labels(title,xlabel,ylabel)
  self.canvas.draw()
class Pie(GraphWidget):
 def __init__(self,master,kwargs):
  super().__init__(master,kwargs)
  self.date=kwargs.get("date")
  self.label=strs(kwargs.get("label"))
  self.title=strs(kwargs.get("title"))
  self.startangle=nums(kwargs.get("startangle"),0)
  self.shadow=bols(kwargs.get("shadow"),False)
  self.counterclock=bols(kwargs.get("counterclock"),True)
  if self.date!=None:self.plot(date=self.date,title=self.title,startangle=self.startangle,shadow=self.shadow,counterclock=self.counterclock)
 def plot(self,date,title="",startangle=0,shadow=False,counterclock=True):
  self.clear()
  self.ax.pie(np.array(date),labels=None,startangle=startangle,shadow=shadow,counterclock=counterclock)
  self.ax.set_title(title,color=self.fg)
  self._apply_grid()
  self.canvas.draw()