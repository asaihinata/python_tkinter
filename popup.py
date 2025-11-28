import tkinter as tk
from manyfunction import *
from tkinter import _get_temp_root,_destroy_temp_root
class Dialog:
 command=None
 def __init__(self,master=None,**kwargs):
  if not master:master=kwargs.get("parent")
  self.master,self.kwargs=master,kwargs
 def show(self,**kwargs):
  for k,v in kwargs.items():self.kwargs[k]=v
  master=self.master
  if not master:master=_get_temp_root()
  try:s=master.tk.call(self.command,*master._options(self.kwargs))
  finally:_destroy_temp_root(master)
  return s
class Message(Dialog):command="tk_messageBox"
def _show(title=None,message=None,_icon=None,_type=None,**kwargs):
 if _icon and "icon" not in kwargs:kwargs["icon"]=_icon
 if _type and "type" not in kwargs:kwargs["type"]=_type
 if title:kwargs["title"]=title
 if message:kwargs["message"]=message
 res=Message(**kwargs).show()
 if isinstance(res,bool):return "yes" if res else "no"
 return str(res)
def showinfo(title=None,message=None,**kwargs):return _show(title,message,"info","ok",**kwargs)
def showwarning(title=None,message=None,**kwargs):return _show(title,message,"warning","ok",**kwargs)
def showerror(title=None,message=None,**kwargs):return _show(title,message,"error","ok",**kwargs)
def askquestion(title=None,message=None,**kwargs):return _show(title,message,"question","yesno",**kwargs)
def askokcancel(title=None,message=None,**kwargs):return _show(title,message,"question","okcancel",**kwargs)=="ok"
def askyesno(title=None,message=None,**kwargs):return _show(title,message,"question","yesno",**kwargs)=="yes"
def askyesnocancel(title=None,message=None,**kwargs):
 s=str(_show(title,message,"question","yesnocancel",**kwargs))
 return None if s=="cancel" else s=="yes"
def askretrycancel(title=None,message=None,**kwargs):return _show(title,message,"warning","retrycancel",**kwargs)=="retry"
class popups:
 def __init__(self,**kwargs):
  self.title=kwargs.get("title","Information")
  self.message=kwargs.get("message","Information message")
  self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "info"
  root=tk.Tk()
  root.withdraw()
  root.iconbitmap(self.icon)
  self.retul=showinfo(title=self.title,message=self.message,icon=self.icon)
  root.destroy()
class popupw:
 def __init__(self,**kwargs):
  self.title=kwargs.get("title","Warning")
  self.message=kwargs.get("message","Warning message")
  self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "warning"
  root=tk.Tk()
  root.withdraw()
  self.retul=showwarning(title=self.title,message=self.message,icon=self.icon)
  root.destroy()
class popupwyn:
 def __init__(self,**kwargs):
  self.title=kwargs.get("title","Warning")
  self.message=kwargs.get("message","Warning message")
  self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "warning"
  root=tk.Tk()
  root.withdraw()
  self.retul=showwarning(title=self.title,message=self.message,icon=self.icon,type="yesno")
  root.destroy()
class popupe:
 def __init__(self,**kwargs):
  self.title=kwargs.get("title","Error")
  self.message=kwargs.get("message","Error message")
  self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "error"
  root=tk.Tk()
  root.withdraw()
  self.retul=showerror(title=self.title,message=self.message,icon=self.icon)
  root.destroy()
class popupq:
 def __init__(self,**kwargs):
  self.title=kwargs.get("title","Question")
  self.message=kwargs.get("message","Question message")
  self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "question"
  root=tk.Tk()
  root.withdraw()
  self.retul=askquestion(title=self.title,message=self.message,icon=self.icon)
  root.destroy()
class popupoc:
 def __init__(self,**kwargs):
  self.title=kwargs.get("title","Question")
  self.message=kwargs.get("message","Question message")
  self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "question"
  root=tk.Tk()
  root.withdraw()
  self.retul=askokcancel(title=self.title,message=self.message,icon=self.icon)
  root.destroy()
class popupyn:
 def __init__(self,**kwargs):
  self.title=kwargs.get("title","Question")
  self.message=kwargs.get("message","Question message")
  self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "question"
  root=tk.Tk()
  root.withdraw()
  self.retul=askyesno(title=self.title,message=self.message,icon=self.icon)
  root.destroy()
class popupync:
 def __init__(self,**kwargs):
  self.title=kwargs.get("title","Question")
  self.message=kwargs.get("message","Question message")
  self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "question"
  root=tk.Tk()
  root.withdraw()
  self.retul=askyesnocancel(title=self.title,message=self.message,icon=self.icon)
  root.destroy()
class popuptry:
 def __init__(self,**kwargs):
  self.title=kwargs.get("title","Question")
  self.message=kwargs.get("message","Question message")
  self.icon=kwargs.get("icon") if kwargs.get("icon") in icon_list else "question"
  root=tk.Tk()
  root.withdraw()
  self.retul=askretrycancel(title=self.title,message=self.message,icon=self.icon)
  root.destroy()