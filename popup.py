import tkinter as tk,tkinter.messagebox as me
from manyfunction import *
class Popupi:
 def __init__(self,**kwargs):
  self.title=kwargs.get("title","Information")
  self.message=kwargs.get("message","Information message")
  self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "info"
  root=tk.Tk()
  root.withdraw()
  self.retul=me.showinfo(title=self.title,message=self.message,icon=self.icon)
  root.destroy()
 @classmethod
 def p(cls,kwargs):return cls(**kwargs).retul
class Popupw:
 def __init__(self,**kwargs):
  self.title=kwargs.get("title","Warning")
  self.message=kwargs.get("message","Warning message")
  self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "warning"
  root=tk.Tk()
  root.withdraw()
  self.retul=me.showwarning(title=self.title,message=self.message,icon=self.icon)
  root.destroy()
 @classmethod
 def p(cls,kwargs):return cls(**kwargs).retul
class Popupe:
 def __init__(self,**kwargs):
  self.title=kwargs.get("title","Error")
  self.message=kwargs.get("message","Error message")
  self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "error"
  root=tk.Tk()
  root.withdraw()
  self.retul=me.showerror(title=self.title,message=self.message,icon=self.icon)
  root.destroy()
 @classmethod
 def p(cls,kwargs):return cls(**kwargs).retul
class Popupq:
 def __init__(self,**kwargs):
  self.title=kwargs.get("title","Question")
  self.message=kwargs.get("message","Question message")
  self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "question"
  root=tk.Tk()
  root.withdraw()
  self.retul=me.askquestion(title=self.title,message=self.message,icon=self.icon)
  root.destroy()
 @classmethod
 def p(cls,kwargs):return cls(**kwargs).retul
class Popupoc:
 def __init__(self,**kwargs):
  self.title=kwargs.get("title","Question")
  self.message=kwargs.get("message","Question message")
  self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "question"
  root=tk.Tk()
  root.withdraw()
  self.retul=me.askokcancel(title=self.title,message=self.message,icon=self.icon)
  root.destroy()
 @classmethod
 def p(cls,kwargs):return cls(**kwargs).retul
class Popupyn:
 def __init__(self,**kwargs):
  self.title=kwargs.get("title","Question")
  self.message=kwargs.get("message","Question message")
  self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "question"
  root=tk.Tk()
  root.withdraw()
  self.retul=me.askyesno(title=self.title,message=self.message,icon=self.icon)
  root.destroy()
 @classmethod
 def p(cls,kwargs):return cls(**kwargs).retul
class Popupync:
 def __init__(self,**kwargs):
  self.title=kwargs.get("title","Question")
  self.message=kwargs.get("message","Question message")
  self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "question"
  root=tk.Tk()
  root.withdraw()
  self.retul=me.askyesnocancel(title=self.title,message=self.message,icon=self.icon)
  root.destroy()
 @classmethod
 def p(cls,kwargs):return cls(**kwargs).retul
class Popuptry:
 def __init__(self,**kwargs):
  self.title=kwargs.get("title","Question")
  self.message=kwargs.get("message","Question message")
  self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "question"
  root=tk.Tk()
  root.withdraw()
  self.retul=me.askretrycancel(title=self.title,message=self.message,icon=self.icon)
  root.destroy()
 @classmethod
 def p(cls,kwargs):return cls(**kwargs).retul