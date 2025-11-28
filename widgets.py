from manyfunction import *
import pyautogui as p,tkinter.font as tkFont
winsize=list(p.size())
class fonts(tkFont.Font):
 def __init__(self,master,family="Meiryo",size=14,weight="normal",slant="roman",overstrike=False,underline=False):super().__init__(master,family=family,size=size,weight=weight,slant=slant,overstrike=overstrike,underline=underline)
class __Widget__:# 全体用
 def _exec_funcs(funcs=None):# exec関数(listかcallable)
  if isinstance(funcs,list):
   for f in funcs:
    try:f() if callable(f) else None
    except:pass
  elif callable(funcs):
   try:funcs()
   except:pass
  else:return None
 def _size(kwargs,autos=(None,None)):
  size=list(kwargs.get("size",autos))
  return (nums(size[0],autos[0]),nums(size[1],autos[1])) if size and isinstance(size,list) and len(size)==2 else autos
 def window_maxandmin_size(master,maxsize,minsize):
  if isinstance(minsize,(tuple,list)) and isinstance(maxsize,(tuple,list)):
   maxsize,minsize=list(maxsize),list(minsize)
   if maxsize[0]<minsize[0]:
    a=maxsize[0]
    maxsize[0]=minsize[0]
    minsize[0]=a
   if maxsize[1]<minsize[1]:
    a=maxsize[1]
    maxsize[1]=minsize[1]
    minsize[1]=a
   if winsize[0]<minsize[0]:minsize[0]=winsize[0]
   if winsize[1]<minsize[1]:minsize[1]=winsize[1]
   if winsize[0]<maxsize[0]:maxsize[0]=winsize[0]
   if winsize[1]<maxsize[1]:maxsize[1]=winsize[1]
   master.maxsize(maxsize[0],maxsize[1])
   master.minsize(minsize[0],minsize[1])
  elif isinstance(maxsize,(list,tuple)):
   maxsize=list(maxsize)
   if winsize[0]<maxsize[0]:maxsize[0]=winsize[0]
   if winsize[1]<maxsize[1]:maxsize[1]=winsize[1]
   master.maxsize(maxsize[0],maxsize[1])
  elif isinstance(minsize,(list,tuple)):
   minsize=list(minsize)
   if winsize[0]<minsize[0]:minsize[0]=winsize[0]
   if winsize[1]<minsize[1]:minsize[1]=winsize[1]
   master.minsize(minsize[0],minsize[1])