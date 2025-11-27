"""
Use demo
from manyfunction import *
clear()
from mylibral import *
layout=[
[sgg.Text(text="textウィジェット1",key="text_key1")],
[sgg.Text(text="textウィジェット2",key="text_key2"),sgg.Text(text="textウィジェット3",key="text_key3")],
]
win=sgg.window(title="demo code",layout=layout,scroll_y=True,maxmine=True)
win.run()
"""
from new_element import *
from popup import *
def counts():
 sgg.count+=1
 return sgg.count
class sgg:
 count=0
 @staticmethod
 def Menu(**kwargs):return{"count":counts(),"type":"Menu",**kwargs}
 @staticmethod
 def Menubutton(**kwargs):return{"count":counts(),"type":"Menubutton",**kwargs}
 @staticmethod
 def Text(**kwargs):return{"count":counts(),"type":"Text",**kwargs}
 @staticmethod
 def Link(**kwargs):return{"count":counts(),"type":"Link",**kwargs}
 @staticmethod
 def Images(**kwargs):return{"count":counts(),"type":"Images",**kwargs}
 @staticmethod
 def Button(**kwargs):return{"count":counts(),"type":"Button",**kwargs}
 @staticmethod
 def Input(**kwargs):return{"count":counts(),"type":"Input",**kwargs}
 @staticmethod
 def Multiline(**kwargs):return{"count":counts(),"type":"Multiline",**kwargs}
 @staticmethod
 def Table(**kwargs):return{"count":counts(),"type":"Table",**kwargs}
 @staticmethod
 def Tree(**kwargs):return{"count":counts(),"type":"Tree",**kwargs}
 @staticmethod
 def Listbox(**kwargs):return{"count":counts(),"type":"Listbox",**kwargs}
 @staticmethod
 def Combobox(**kwargs):return{"count":counts(),"type":"Combobox",**kwargs}
 @staticmethod
 def Radio(**kwargs):return{"count":counts(),"type":"Radio",**kwargs}
 @staticmethod
 def Checkbox(**kwargs):return{"count":counts(),"type":"Checkbox",**kwargs}
 @staticmethod
 def Frames(**kwargs):return{"count":counts(),"type":"Frames",**kwargs}
 @staticmethod
 def Column(**kwargs):return{"count":counts(),"type":"Column",**kwargs}
 @staticmethod
 def Slidebar(**kwargs):return{"count":counts(),"type":"Slidebar",**kwargs}
 @staticmethod
 def InputNumber(**kwargs):return{"count":counts(),"type":"InputNumber",**kwargs}
 @staticmethod
 def FileLoad(**kwargs):return{"count":counts(),"type":"FileLoad",**kwargs}
 @staticmethod
 def FolderLoad(**kwargs):return{"count":counts(),"type":"FolderLoad",**kwargs}
 @staticmethod
 def Calendars(**kwargs):return{"count":counts(),"type":"Calendars",**kwargs}
 @staticmethod
 def InputDate(**kwargs):return{"count":counts(),"type":"InputDate",**kwargs}
 @staticmethod
 def Colorbtn(**kwargs):return{"count":counts(),"type":"Colorbtn",**kwargs}
 @staticmethod
 def Tab(**kwargs):return{"count":counts(),"type":"Tab",**kwargs}
 @staticmethod
 def Progressbar(**kwargs):return{"count":counts(),"type":"Progressbar",**kwargs}
 @classmethod
 def Popup(**kwargs):return popups(**kwargs)
 @classmethod
 def Popupwarning(cls,**kwargs):return popupw(**kwargs)
 @classmethod
 def Popuperror(cls,**kwargs):return popupe(**kwargs)
 @classmethod
 def Popupyesno(cls,**kwargs):return popupq(**kwargs)
 @classmethod
 def Popupokcancel(cls,**kwargs):return popupoc(**kwargs)
 @classmethod
 def Popupyesno(cls,**kwargs):return popupyn(**kwargs)
 @classmethod
 def Popupyesnocancel(cls,**kwargs):return popupync(**kwargs)
 @classmethod
 def Popuptrycancel(cls,**kwargs):return popuptry(**kwargs)
 @classmethod
 def window(cls,**kwargs):return SubWindowController(kwargs) if kwargs.get("type")=="toplevel" else WindowController(kwargs)
 def formatlist():
  for i in fotmat_list:print(f"{i}:{fotmat_list[i]}")