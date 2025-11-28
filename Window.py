from manyfunction import *
from element import *
from widgets import __Widget__
from popup import *
import pyautogui as p
winsize=list(p.size())
class WindowController:
 def __init__(self,kwargs):
  self.count=0
  self.loadfun=kwargs.get("load")
  self.title=kwargs.get("title","window")
  self.layout=kwargs.get("layout",[[]])
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.bg=parsecolor(kwargs.get("bg",THEMES["bg1"]))
  self.font=kwargs.get("font",THEMES["font"])
  self.scroll_y=bols(kwargs.get("scroll_y"),False)
  self.scroll_x=bols(kwargs.get("scroll_x"),False)
  self.root=tk.Tk()# root ウィンドウ
  self.root.title(self.title)
  self.root.protocol("WM_DELETE_WINDOW",self._on_window_close)
  self.root.tk_setPalette(background=self.bg)
  self.size=kwargs.get("size",(None,None))
  self.maxmine=bols(kwargs.get("maxmine"),False)
  self.max_size=kwargs.get("maxsizes")
  self.min_size=kwargs.get("minsizes")
  __Widget__.window_maxandmin_size(self.root,self.max_size,self.min_size)
  if self.maxmine:self.maxwin()# 画面の最大化の設定
  self.location=kwargs.get("location",(0,0))
  self.maxsize=winsize# 画面の最大サイズ
  self.widgets={}# key->widget
  self.closed=False
  self._close_result=None
  self.canvas=None# スクロールサポート:必要に応じてキャンバス/フレームラッパーを作成する
  parent=self.root
  if self.scroll_y or self.scroll_x:
   self.canvas=tk.Canvas(self.root,bg=self.bg,highlightthickness=0)
   self._inner_frame=tk.Frame(self.canvas,bg=self.bg)
   self.canvas.create_window((0,0),window=self._inner_frame,anchor="nw")
   self._inner_frame.bind("<Configure>",lambda e:self.canvas.configure(scrollregion=self.canvas.bbox("all")))
   if self.scroll_y:
    ybar=tk.Scrollbar(self.root,orient="vertical",command=self.canvas.yview)
    self.canvas.configure(yscrollcommand=ybar.set)
    ybar.pack(side="right",fill="y")
   if self.scroll_x:
    xbar=tk.Scrollbar(self.root,orient="horizontal",command=self.canvas.xview)
    self.canvas.configure(xscrollcommand=xbar.set)
    xbar.pack(side="bottom",fill="x")
   self.canvas.pack(fill="both",expand=True)
   parent=self._inner_frame
  if self.size!=(None,None):# sizeとlocation
   w,h=self.size
   x,y=self.location
   try:self.root.geometry(f"{int(w)}x{int(h)}+{int(x)}+{int(y)}")
   except:self.root.geometry(f"+{int(x)}+{int(y)}")
  else:
   x,y=self.location
   try:self.root.geometry(f"+{int(x)}+{int(y)}")
   except:pass
  if self.layout:self._build_layout(self.layout,parent)# layoutを作る
 def scroll_to(self,key):
  w,y=self.widgets.get(key),0
  if not self.canvas or not w:return
  self.root.update_idletasks()
  try:y=self.canvas.canvasy(w.winfo_rooty()-self.canvas.winfo_rooty())
  except:return None
  scroll_region=self.canvas.bbox("all")
  if not scroll_region:return None
  total_height=scroll_region[3]-scroll_region[1]
  if total_height<=0:return None
  self.canvas.yview_moveto(y/total_height)
 def _build_layout(self,layout,parent,bgcolor=None):
  for row in layout:
   bg=(bgcolor or self.bg)
   row_frame=tk.Frame(parent,bg=bg)
   row_frame.pack(fill="x",padx=5,pady=5)
   for kwargs in row:self._create_element(kwargs,row_frame,bg)
 def _create_element(self,kwargs,parent,bgs=None):# widget作成
  t,widget=kwargs.get("type"),None
  kwargs["back_bg"]=bgs
  self.count+=1
  if t=="Menu":widget=Menu(parent,kwargs)
  elif t=="Menubutton":widget=Menubutton(parent,kwargs)
  elif t=="Text":widget=Text(parent,kwargs)
  elif t=="Link":widget=Link(parent,kwargs)
  elif t=="Images":widget=Images(parent,kwargs)
  elif t=="Button":widget=Button(parent,kwargs)
  elif t=="Input":widget=Input(parent,kwargs)
  elif t=="Multiline":widget=Multiline(parent,kwargs)
  elif t=="Listbox":widget=Listbox(parent,kwargs)
  elif t=="Combobox":widget=Combobox(parent,kwargs)
  elif t=="InputNumber":widget=InputNumber(parent,kwargs)
  elif t=="Radio":widget=Radio(parent,kwargs)
  elif t=="Checkbox":widget=Checkbox(parent,kwargs)
  elif t=="FileLoad":widget=FileLoad(parent,kwargs)
  elif t=="FolderLoad":widget=FolderLoad(parent,kwargs)
  elif t=="Colorbtn":widget=Colorbtn(parent,kwargs)
  elif t=="Progressbar":widget=Progressbar(parent,kwargs)
  elif t=="Tab":
   widget=Tab(parent,kwargs)# Tabウィジェットの生成
   for tab in kwargs.get("tabs",[]):
    if not isinstance(tab,(list,tuple)) or len(tab)==0:continue
    frame=tk.Frame(widget.nb,bg=widget.bg)
    widget.add_tab(tab[0],frame)
    if 1<len(tab) and isinstance(tab[1],list):
     try:self._build_layout(tab[1],frame,kwargs.get("bg"))
     except Exception as e:print("Tabレイアウト構築エラー:",e)
  elif t=="Frames":# Frame
   widget=Frames(parent,kwargs)
   if kwargs.get("layout"):self._build_layout(kwargs.get("layout"),widget,kwargs.get("bg"))
  elif t=="Column":
   widget=Column(parent,kwargs)
   if kwargs.get("layout"):self._build_layout(kwargs.get("layout"),widget,kwargs.get("bg"))
  elif t=="Table":widget=Table(parent,kwargs)
  elif t=="Tree":widget=Tree(parent,kwargs)
  elif t=="Slidebar":widget=Slidebar(parent,kwargs)
  elif t=="Calendars":widget=Calendars(parent,kwargs)
  elif t=="InputDate":widget=InputDate(parent,kwargs)
  else:widget=tk.Label(parent,text=f"Unknown element:{t}")
  if widget:# packとregister
   if t=="Menu":self.root.config(menu=widget)
   else:widget.pack(side="left",padx=5,pady=5)
   if kwargs.get("key"):self.widgets[kwargs["key"]]=widget
   else:self.widgets[f"widget{self.count}"]=widget
 def get(self,key):return self.widgets.get(key)# ウィジェット取得
 def get_title(self):
  try:return self.title
  except Exception as e:return f"Title get error:{e}"
 def set_title(self,new_title):
  try:
   self.title=new_title
   self.root.title(new_title)
  except Exception as e:print(f"Title change error:{e}")
 def winclose(self):return "winclose"# 閉じるメッセージ
 def _on_window_close(self):
  self._close_result="winclose"
  self.closed=True
  try:self.root.destroy()
  except Exception as e:print(f"close error:{e}")
 def close(self):self.root.quit()
 def maxwin(self):# ウィンドウを最大化
  try:self.root.state("zoomed")
  except:pass
 def minwin(self):# ウィンドウを最小化
  try:self.root.iconify()
  except:pass
 def run(self):# メインループ実行
  if self.loadfun:__Widget__._exec_funcs(self.loadfun)
  if self.canvas:self.root.after(100,self._update_region)
  self.root.mainloop()
 def _update_region(self):
  try:self.canvas.configure(scrollregion=self.canvas.bbox("all"))
  except:pass
class SubWindowController:
 def __init__(self,kwargs):
  self.parent=kwargs.get("parent")
  if self.parent and hasattr(self.parent,"root"):self.master=self.parent.root
  else:self.master=None
  self.takefocus=bols(kwargs.get("takefocus"))
  self.root=tk.Toplevel(self.master,takefocus=self.takefocus)
  self.count=0
  self.loadfun=kwargs.get("load")
  self.title=kwargs.get("title","Sub Window")
  self.layout=kwargs.get("layout",[[]])
  self.size=kwargs.get("size",(None,None))
  self.max_size=kwargs.get("maxsizes")
  self.min_size=kwargs.get("minsizes")
  __Widget__.window_maxandmin_size(self.root,self.max_size,self.min_size)
  self.location=kwargs.get("location",(0,0))
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.bg=parsecolor(kwargs.get("bg",THEMES["bg1"]))
  self.font=kwargs.get("font",THEMES["font"])
  self.scroll_y=bols(kwargs.get("scroll_y"),False)
  self.scroll_x=bols(kwargs.get("scroll_x"),False)
  self.root.title(self.title)
  self.root.tk_setPalette(background=self.bg)
  self.closed=False
  self._close_result=None
  self.widgets={}
  self.getele=None
  self.elename=None
  parent=self.root
  if self.scroll_y or self.scroll_x:
   self.canvas=tk.Canvas(self.root,bg=self.bg,highlightthickness=0)
   self._inner_frame=tk.Frame(self.canvas,bg=self.bg)
   self.canvas.create_window((0,0),window=self._inner_frame,anchor="nw")
   self._inner_frame.bind("<Configure>",lambda e:self.canvas.configure(scrollregion=self.canvas.bbox("all")))
   if self.scroll_y:
    ybar=tk.Scrollbar(self.root,orient="vertical",command=self.canvas.yview)
    self.canvas.configure(yscrollcommand=ybar.set)
    ybar.pack(side="right",fill="y")
   if self.scroll_x:
    xbar=tk.Scrollbar(self.root,orient="horizontal",command=self.canvas.xview)
    self.canvas.configure(xscrollcommand=xbar.set)
    xbar.pack(side="bottom",fill="x")
   self.canvas.pack(fill="both",expand=True)
   parent=self._inner_frame
  if self.size!=(None,None):
   w,h=self.size
   x,y=self.location
   try:self.root.geometry(f"{int(w)}x{int(h)}+{int(x)}+{int(y)}")
   except:self.root.geometry(f"+{int(x)}+{int(y)}")
  else:
   x,y=self.location
   try:self.root.geometry(f"+{int(x)}+{int(y)}")
   except:pass
  if self.layout:self._build_layout(self.layout,parent)
  self.root.protocol("WM_DELETE_WINDOW",self._on_window_close)
 def _build_layout(self,layout,parent,bgcolor=None):
  for row in layout:
   bg=(bgcolor or self.bg)
   row_frame=tk.Frame(parent,bg=bg)
   row_frame.pack(fill="x",padx=5,pady=5)
   for kwargs in row:self._create_element(kwargs,row_frame,bg)
 def _create_element(self,kwargs,parent,bgs=None):# widget作成
  t,widget=kwargs["type"],None
  kwargs["back_bg"]=bgs
  self.count+=1
  if t=="Menu":widget=Menu(parent,kwargs)
  elif t=="Menubutton":widget=Menubutton(parent,kwargs)
  elif t=="Text":widget=Text(parent,kwargs)
  elif t=="Link":widget=Link(parent,kwargs)
  elif t=="Images":widget=Images(parent,kwargs)
  elif t=="Button":widget=Button(parent,kwargs)
  elif t=="Input":widget=Input(parent,kwargs)
  elif t=="Multiline":widget=Multiline(parent,kwargs)
  elif t=="Listbox":widget=Listbox(parent,kwargs)
  elif t=="Combobox":widget=Combobox(parent,kwargs)
  elif t=="Progressbar":widget=Progressbar(parent,kwargs)
  elif t=="InputNumber":widget=InputNumber(parent,kwargs)
  elif t=="Radio":widget=Radio(parent,kwargs)
  elif t=="Checkbox":widget=Checkbox(parent,kwargs)
  elif t=="FileLoad":widget=FileLoad(parent,kwargs)
  elif t=="FolderLoad":widget=FolderLoad(parent,kwargs)
  elif t=="Frames":# Frame
   widget=Frames(parent,kwargs)
   if kwargs.get("layout"):self._build_layout(kwargs.get("layout"),widget,kwargs.get("bg"))
  elif t=="Column":
   widget=Column(parent,kwargs)
   if kwargs.get("layout"):self._build_layout(kwargs.get("layout"),widget,kwargs.get("bg"))
  elif t=="Table":widget=Table(parent,kwargs)
  elif t=="Tree":widget=Tree(parent,kwargs)
  elif t=="Slidebar":widget=Slidebar(parent,kwargs)
  elif t=="Calendars":widget=Calendars(parent,kwargs)
  elif t=="InputDate":widget=InputDate(parent,kwargs)
  elif t=="Colorbtn":widget=Colorbtn(parent,kwargs)
  elif t=="Tab":
   widget=Tab(parent,kwargs)# Tabウィジェットの生成
   for tab in kwargs.get("tabs",[]):
    if not isinstance(tab,(list,tuple)) or len(tab)==0:continue
    frame=tk.Frame(widget.nb,bg=widget.bg)
    widget.add_tab(tab[0],frame)
    if 1<len(tab) and isinstance(tab[1],list):
     try:self._build_layout(tab[1],frame,kwargs.get("bg"))
     except Exception as e:print("Tabレイアウト構築エラー:",e)
  else:widget=tk.Label(parent,text=f"Unknown element:{t}")# 該当なし
  if widget:# packとregister
   if t=="Menu":self.root.config(menu=widget)
   else:widget.pack(side="left",padx=5,pady=5)
   if kwargs.get("key"):self.widgets[kwargs.get("key")]=widget
   else:self.widgets[f"widget{self.count}"]=widget
 def get(self,key):return self.widgets[key]# ウィジェット取得
 def maxwin(self):# ウィンドウを最大化
  try:self.root.state("zoomed")
  except:pass
 def minwin(self):# ウィンドウを最小化
  try:self.root.iconify()
  except:pass
 def _on_window_close(self):# 閉じる処理（メインを閉じない）
  self.closed=True
  try:self.root.destroy()
  except:pass
 def close(self):self.root.quit()
 def run(self):# 実行
  if self.loadfun:__Widget__._exec_funcs(self.loadfun)
  if hasattr(self,"canvas"):self.root.after(100,self._update_region)
  self.root.mainloop()
 def _update_region(self):
  try:self.canvas.configure(scrollregion=self.canvas.bbox("all"))
  except:pass
 def scroll_to(self,key):
  w=self.widgets.get(key)
  if not w or not hasattr(self,"canvas") or self.canvas==None:pass
  self.root.update_idletasks()
  try:cy=self.canvas.canvasy(w.winfo_rooty()-self.canvas.winfo_rooty())
  except:return None
  scroll_region=self.canvas.bbox("all")
  if not scroll_region:return None
  total_height=scroll_region[3]-scroll_region[1]
  if total_height<=0:return None
  self.canvas.yview_moveto(cy/total_height)