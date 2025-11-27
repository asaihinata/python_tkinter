import tkinter as tk,tkinter.messagebox as me
from manyfunction import *
def popups():
 class popups:
  def __init__(self,**kwargs):
   self.title=kwargs.get("title","Information")
   self.message=kwargs.get("message","Information message")
   self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "info"
   root=tk.Tk()
   root.withdraw()
   self.retul=me.showinfo(title=self.title,message=self.message,icon=self.icon)
   root.destroy()
 return popups().retul
def popupw():
 class popupw:
  def __init__(self,**kwargs):
   self.title=kwargs.get("title","Warning")
   self.message=kwargs.get("message","Warning message")
   self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "warning"
   root=tk.Tk()
   root.withdraw()
   self.retul=me.showwarning(title=self.title,message=self.message,icon=self.icon)
   root.destroy()
 return popupw().retul
def popupe():
 class popupe:
  def __init__(self,**kwargs):
   self.title=kwargs.get("title","Error")
   self.message=kwargs.get("message","Error message")
   self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "error"
   root=tk.Tk()
   root.withdraw()
   self.retul=me.showerror(title=self.title,message=self.message,icon=self.icon)
   root.destroy()
 return popupe().retul
def popupq():
 class popupq:
  def __init__(self,**kwargs):
   self.title=kwargs.get("title","Question")
   self.message=kwargs.get("message","Question message")
   self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "question"
   root=tk.Tk()
   root.withdraw()
   self.retul=me.askquestion(title=self.title,message=self.message,icon=self.icon)
   root.destroy()
 return popupq().retul
def popupoc():
 class popupoc:
  def __init__(self,**kwargs):
   self.title=kwargs.get("title","Question")
   self.message=kwargs.get("message","Question message")
   self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "question"
   root=tk.Tk()
   root.withdraw()
   self.retul=me.askokcancel(title=self.title,message=self.message,icon=self.icon)
   root.destroy().retul
 return popupoc()
def popupyn():
 class popupyn:
  def __init__(self,**kwargs):
   self.title=kwargs.get("title","Question")
   self.message=kwargs.get("message","Question message")
   self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "question"
   root=tk.Tk()
   root.withdraw()
   self.retul=me.askyesno(title=self.title,message=self.message,icon=self.icon)
   root.destroy()
 return popupyn().retul
def popupync():
 class popupync:
  def __init__(self,**kwargs):
   self.title=kwargs.get("title","Question")
   self.message=kwargs.get("message","Question message")
   self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "question"
   root=tk.Tk()
   root.withdraw()
   self.retul=me.askyesnocancel(title=self.title,message=self.message,icon=self.icon)
   root.destroy()
 return popupync().retul
def popuptry():
 class popuptry:
  def __init__(self,**kwargs):
   self.title=kwargs.get("title","Question")
   self.message=kwargs.get("message","Question message")
   self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "question"
   root=tk.Tk()
   root.withdraw()
   self.retul=me.askretrycancel(title=self.title,message=self.message,icon=self.icon)
   root.destroy()
 return popuptry().retul