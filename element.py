import tkinter as tk,os,tkcalendar as tkc,webbrowser
from manyfunction import *
from pathlib import Path
from tkinter import ttk,colorchooser,filedialog
from PIL import Image,ImageTk
from datetime import datetime,date
from widgets import __Widget__ as wi,fonts
class Text(tk.Label):
 def __init__(self,master,kwargs):
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.back_bg=kwargs.get("back_bg")
  self.bg=parsecolor(kwargs.get("bg",self.back_bg or THEMES["bg1"]))
  self.underline=False if kwargs.get("underline","normal")=="normal" else True
  self.weight=kwargs.get("weight") if kwargs.get("weight") in ["normal","bold"] else "normal"
  self.slant=kwargs.get("slant") if kwargs.get("slant") in ["roman","italic"] else "roman"
  self.overstrike=False if kwargs.get("overstrike","normal")=="normal" else True
  self.font_family=kwargs.get("font_family","Meiryo")
  self.font_size=num0(kwargs.get("font_size"),14)
  self.font=kwargs.get("font",fonts(master,self.font_family,self.font_size,self.weight,self.slant,self.overstrike,self.underline))
  self.justify=kwargs.get("justify") if kwargs.get("justify") in ["right","center","left"] else "left"
  self.wraplength=num0(kwargs.get("wraplength"))
  self.cursor=kwargs.get("cursor")
  self.takefocus=bols(kwargs.get("takefocus"))
  self.borderwidth=num0(kwargs.get("bd"))
  self.relief=kwargs.get("relief") if kwargs.get("relief") in relief_list else "flat"
  self.padx=num0(kwargs.get("padx"))
  self.pady=num0(kwargs.get("pady"))
  self.anchor=kwargs.get("anchor","w") if get_dict(anchor_dict,kwargs.get("anchor","right"))[1] in anchor_list else "w"
  self.activeforeground=parsecolor(kwargs.get("activefg"))
  self.activebackground=parsecolor(kwargs.get("activebg"))
  self.highlightthickness=num0(kwargs.get("highlightthickness"))
  self.highlightcolor=parsecolor(kwargs.get("highlightfg"))
  self.highlightbackground=parsecolor(kwargs.get("highlightbg"))
  self.text=kwargs.get("text","")
  self.size=wi._size(kwargs)
  self.width=self.size[0]
  self.height=self.size[1]
  super().__init__(master,takefocus=self.takefocus,borderwidth=self.borderwidth,highlightcolor=self.highlightcolor,highlightbackground=self.highlightbackground,highlightthickness=self.highlightthickness,activeforeground=self.activeforeground,activebackground=self.activebackground,anchor=self.anchor,pady=self.pady,padx=self.padx,relief=self.relief,wraplength=self.wraplength,cursor=self.cursor,text=self.text,bg=self.bg,fg=self.fg,font=self.font,width=self.width,height=self.height,justify=self.justify)
 def get_text(self):return self.text
 def set_text(self,txt):
  if txt:
   self.text=txt
   self.config(text=txt)
 def get_bg(self):return self.bg
 def set_bg(self,nbg):
  if nbg and isinstance(nbg,str):
   self.bg=nbg
   self.config(bg=nbg)
 def get_fg(self):return self.fg
 def set_fg(self,nfg):
  if nfg and isinstance(nfg,str):
   self.fg=nfg
   self.config(fg=nfg)
 def get_font(self):return self.font
 def set_font(self,nfont):
  if nfont and isinstance(nfont,tuple):
   self.font=nfont
   self.config(font=nfont)
 def _delta(self):self.destroy()
class Button(tk.Button):
 def __init__(self,master,kwargs):
  self.funcs=kwargs.get("function")
  self.text=kwargs.get("text","")
  self.size=wi._size(kwargs)
  self.width=self.size[0]
  self.height=self.size[1]
  self.bg=parsecolor(kwargs.get("bg",THEMES["bg2"]))
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.button_underline=False if kwargs.get("underline","normal")=="normal" else True
  self.button_weight=kwargs.get("weight") if kwargs.get("weight") in ["normal","bold"] else "normal"
  self.button_slant=kwargs.get("slant") if kwargs.get("slant") in ["roman","italic"] else "roman"
  self.button_overstrike=False if kwargs.get("overstrike","normal")=="normal" else True
  self.button_fontfamily=kwargs.get("font_family","Meiryo")
  self.button_fontsize=num0(kwargs.get("font_size"),10)
  self.font=kwargs.get("font",fonts(master,self.button_fontfamily,self.button_fontsize,self.button_weight,self.button_slant,self.button_overstrike,self.button_underline))
  self.justify=kwargs.get("justify") if kwargs.get("justify") in ["right","center","left"] else "left"
  self.wraplength=num0(kwargs.get("wraplength"))
  self.cursor=kwargs.get("cursor")
  self.takefocus=bols(kwargs.get("takefocus"))
  self.borderwidth=num0(kwargs.get("bd"))
  self.relief=kwargs.get("relief") if kwargs.get("relief") in relief_list else "flat"
  self.padx=num0(kwargs.get("padx"))
  self.pady=num0(kwargs.get("pady"))
  self.anchor=kwargs.get("anchor","center") if get_dict(anchor_dict,kwargs.get("anchor","center"))[1] in anchor_list else "center"
  self.activeforeground=parsecolor(kwargs.get("activefg"))
  self.activebackground=parsecolor(kwargs.get("activebg"))
  self.highlightthickness=num0(kwargs.get("highlightthickness"))
  self.highlightcolor=parsecolor(kwargs.get("highlightfg"))
  self.highlightbackground=parsecolor(kwargs.get("highlightbg"))
  super().__init__(master,takefocus=self.takefocus,highlightcolor=self.highlightcolor,highlightbackground=self.highlightbackground,highlightthickness=self.highlightthickness,activeforeground=self.activeforeground,activebackground=self.activebackground,anchor=self.anchor,pady=self.pady,padx=self.padx,relief=self.relief,wraplength=self.wraplength,cursor=self.cursor,text=self.text,bg=self.bg,fg=self.fg,font=self.font,command=lambda f=self.funcs:wi._exec_funcs(f),width=self.width,height=self.height)
 def get_text(self):return self.text
 def set_text(self,txt):
  if txt:
   self.text=txt
   self.config(text=txt)
  else:return None
 def get_bg(self):return self.bg
 def set_bg(self,nbg):
  if nbg and isinstance(nbg,str):
   self.bg=nbg
   self.config(bg=nbg)
  else:return None
 def get_fg(self):return self.fg
 def set_fg(self,nfg):
  if nfg and isinstance(nfg,str):
   self.fg=nfg
   self.config(button_fg=nfg)
  else:return None
 def get_font(self):return self.font
 def set_font(self,nfont):
  if nfont and isinstance(nfont,tuple):
   self.font=nfont
   self.config(button_font=nfont)
  else:return None
 def _delta(self):self.destroy()
class FolderLoad(tk.Button):
 def __init__(self,master,kwargs):
  self.foldersaves=None
  self.bg=parsecolor(kwargs.get("bg",THEMES["bg2"]))
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.button_underline=False if kwargs.get("underline","normal")=="normal" else True
  self.button_weight=kwargs.get("weight") if kwargs.get("weight") in ["normal","bold"] else "normal"
  self.button_slant=kwargs.get("slant") if kwargs.get("slant") in ["roman","italic"] else "roman"
  self.button_overstrike=False if kwargs.get("overstrike","normal")=="normal" else True
  self.button_fontfamily=kwargs.get("font_family","Meiryo")
  self.button_fontsize=num0(kwargs.get("font_size"),10)
  self.font=kwargs.get("font",fonts(master,self.button_fontfamily,self.button_fontsize,self.button_weight,self.button_slant,self.button_overstrike,self.button_underline))
  self.justify=kwargs.get("justify") if kwargs.get("justify") in ["right","center","left"] else "left"
  self.wraplength=num0(kwargs.get("wraplength"))
  self.cursor=kwargs.get("cursor")
  self.takefocus=bols(kwargs.get("takefocus"))
  self.borderwidth=num0(kwargs.get("bd"))
  self.relief=kwargs.get("relief") if kwargs.get("relief") in relief_list else "flat"
  self.padx=num0(kwargs.get("padx"))
  self.pady=num0(kwargs.get("pady"))
  self.anchor=kwargs.get("anchor","center") if get_dict(anchor_dict,kwargs.get("anchor","center"))[1] in anchor_list else "center"
  self.activeforeground=parsecolor(kwargs.get("activefg"))
  self.activebackground=parsecolor(kwargs.get("activebg"))
  self.highlightthickness=num0(kwargs.get("highlightthickness"))
  self.highlightcolor=parsecolor(kwargs.get("highlightfg"))
  self.highlightbackground=parsecolor(kwargs.get("highlightbg"))
  self.text=kwargs.get("text","select Folder")
  self.size=wi._size(kwargs)
  self.width=self.size[0]
  self.height=self.size[1]
  self.title=kwargs.get("title","select Folder")
  super().__init__(master,takefocus=self.takefocus,highlightcolor=self.highlightcolor,highlightbackground=self.highlightbackground,highlightthickness=self.highlightthickness,activeforeground=self.activeforeground,activebackground=self.activebackground,anchor=self.anchor,pady=self.pady,padx=self.padx,relief=self.relief,wraplength=self.wraplength,cursor=self.cursor,text=self.text,bg=self.bg,fg=self.fg,font=self.font,width=self.width,height=self.height,command=self._choosefolder)
 def _choosefolder(self):self.foldersaves=filedialog.askdirectory(title=self.title,initialdir=os.getcwd())
 def _choose_pas(self):return self.foldersaves
 def get_title(self):return self.title
 def set_title(self,titles):self.title=titles
 def get_text(self):return self.text
 def set_text(self,txt):
  if txt:
   self.text=txt
   self.config(text=txt)
  else:return None
 def get_bg(self):return self.bg
 def set_bg(self,nbg):
  if nbg and isinstance(nbg,str):
   self.bg=nbg
   self.config(bg=nbg)
  else:return None
 def get_fg(self):return self.fg
 def set_fg(self,nfg):
  if nfg and isinstance(nfg,str):
   self.fg=nfg
   self.config(button_fg=nfg)
  else:return None
 def get_font(self):return self.font
 def set_font(self,nfont):
  if nfont and isinstance(nfont,tuple):
   self.font=nfont
   self.config(button_font=nfont)
  else:return None
 def _delta(self):self.destroy()
class FileLoad(tk.Button):
 def __init__(self,master,kwargs):
  self.filesaves=None
  self.bg=parsecolor(kwargs.get("bg",THEMES["bg2"]))
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.button_underline=False if kwargs.get("underline","normal")=="normal" else True
  self.button_weight=kwargs.get("weight") if kwargs.get("weight") in ["normal","bold"] else "normal"
  self.button_slant=kwargs.get("slant") if kwargs.get("slant") in ["roman","italic"] else "roman"
  self.button_overstrike=False if kwargs.get("overstrike","normal")=="normal" else True
  self.button_fontfamily=kwargs.get("font_family","Meiryo")
  self.button_fontsize=num0(kwargs.get("font_size"),10)
  self.font=kwargs.get("font",fonts(master,self.button_fontfamily,self.button_fontsize,self.button_weight,self.button_slant,self.button_overstrike,self.button_underline))
  self.justify=kwargs.get("justify") if kwargs.get("justify") in ["right","center","left"] else "left"
  self.wraplength=num0(kwargs.get("wraplength"))
  self.cursor=kwargs.get("cursor")
  self.takefocus=bols(kwargs.get("takefocus"))
  self.borderwidth=num0(kwargs.get("bd"))
  self.relief=kwargs.get("relief") if kwargs.get("relief") in relief_list else "flat"
  self.padx=num0(kwargs.get("padx"))
  self.pady=num0(kwargs.get("pady"))
  self.anchor=kwargs.get("anchor","center") if get_dict(anchor_dict,kwargs.get("anchor","center"))[1] in anchor_list else "center"
  self.activeforeground=parsecolor(kwargs.get("activefg"))
  self.activebackground=parsecolor(kwargs.get("activebg"))
  self.highlightthickness=num0(kwargs.get("highlightthickness"))
  self.highlightcolor=parsecolor(kwargs.get("highlightfg"))
  self.highlightbackground=parsecolor(kwargs.get("highlightbg"))
  self.text=kwargs.get("text","select File")
  self.size=wi._size(kwargs)
  self.width=self.size[0]
  self.height=self.size[1]
  self.title=kwargs.get("title","select File")
  super().__init__(master,takefocus=self.takefocus,highlightcolor=self.highlightcolor,highlightbackground=self.highlightbackground,highlightthickness=self.highlightthickness,activeforeground=self.activeforeground,activebackground=self.activebackground,anchor=self.anchor,pady=self.pady,padx=self.padx,relief=self.relief,wraplength=self.wraplength,cursor=self.cursor,text=self.text,bg=self.bg,fg=self.fg,font=self.font,width=self.width,height=self.height,command=self._choosefile)
 def _choosefile(self):self.filesaves=filedialog.askopenfilename(title=self.title,initialdir=os.getcwd())
 def _choose_pas(self):return self.filesaves
 def get_title(self):return self.title
 def set_title(self,titles):self.title=titles
 def get_text(self):return self.text
 def set_text(self,txt):
  if txt:
   self.text=txt
   self.config(text=txt)
  else:return None
 def get_bg(self):return self.bg
 def set_bg(self,nbg):
  if nbg and isinstance(nbg,str):
   self.bg=nbg
   self.config(bg=nbg)
  else:return None
 def get_fg(self):return self.fg
 def set_fg(self,nfg):
  if nfg and isinstance(nfg,str):
   self.fg=nfg
   self.config(button_fg=nfg)
  else:return None
 def get_font(self):return self.font
 def set_font(self,nfont):
  if nfont and isinstance(nfont,tuple):
   self.font=nfont
   self.config(button_font=nfont)
  else:return None
 def _delta(self):self.destroy()
class Colorbtn(tk.Button):
 def __init__(self,master,kwargs):
  self.selectcolor=None
  self.bg=parsecolor(kwargs.get("bg",THEMES["bg2"]))
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.button_underline=False if kwargs.get("underline","normal")=="normal" else True
  self.button_weight=kwargs.get("weight") if kwargs.get("weight") in ["normal","bold"] else "normal"
  self.button_slant=kwargs.get("slant") if kwargs.get("slant") in ["roman","italic"] else "roman"
  self.button_overstrike=False if kwargs.get("overstrike","normal")=="normal" else True
  self.button_fontfamily=kwargs.get("font_family","Meiryo")
  self.button_fontsize=num0(kwargs.get("font_size"),10)
  self.font=kwargs.get("font",fonts(master,self.button_fontfamily,self.button_fontsize,self.button_weight,self.button_slant,self.button_overstrike,self.button_underline))
  self.justify=kwargs.get("justify") if kwargs.get("justify") in ["right","center","left"] else "left"
  self.wraplength=num0(kwargs.get("wraplength"))
  self.cursor=kwargs.get("cursor")
  self.takefocus=bols(kwargs.get("takefocus"))
  self.borderwidth=num0(kwargs.get("bd"))
  self.relief=kwargs.get("relief") if kwargs.get("relief") in relief_list else "flat"
  self.padx=num0(kwargs.get("padx"))
  self.pady=num0(kwargs.get("pady"))
  self.anchor=kwargs.get("anchor","center") if get_dict(anchor_dict,kwargs.get("anchor","center"))[1] in anchor_list else "center"
  self.activeforeground=parsecolor(kwargs.get("activefg"))
  self.activebackground=parsecolor(kwargs.get("activebg"))
  self.highlightthickness=num0(kwargs.get("highlightthickness"))
  self.highlightcolor=parsecolor(kwargs.get("highlightfg"))
  self.highlightbackground=parsecolor(kwargs.get("highlightbg"))
  self.text=kwargs.get("text","select color")
  self.color=kwargs.get("color",None)
  self.size=wi._size(kwargs)
  self.width=self.size[0]
  self.height=self.size[1]
  self.title=kwargs.get("title","select color")
  super().__init__(master,takefocus=self.takefocus,highlightcolor=self.highlightcolor,highlightbackground=self.highlightbackground,highlightthickness=self.highlightthickness,activeforeground=self.activeforeground,activebackground=self.activebackground,anchor=self.anchor,pady=self.pady,padx=self.padx,relief=self.relief,wraplength=self.wraplength,cursor=self.cursor,text=self.text,bg=self.bg,fg=self.fg,font=self.font,width=self.width,height=self.height,command=self.color_change)
 def color_change(self):self.selectcolor=colorchooser.askcolor(color=self.color,title=self.title)
 def _choose_color(self):return self.selectcolor
 def get_title(self):return self.title
 def set_title(self,titles):self.title=titles
 def get_text(self):return self.text
 def set_text(self,txt):
  if txt:
   self.text=txt
   self.config(text=txt)
  else:return None
 def get_bg(self):return self.bg
 def set_bg(self,nbg):
  if nbg and isinstance(nbg,str):
   self.bg=nbg
   self.config(bg=nbg)
  else:return None
 def get_fg(self):return self.fg
 def set_fg(self,nfg):
  if nfg and isinstance(nfg,str):
   self.fg=nfg
   self.config(button_fg=nfg)
  else:return None
 def get_font(self):return self.font
 def set_font(self,nfont):
  if nfont and isinstance(nfont,tuple):
   self.font=nfont
   self.config(button_font=nfont)
  else:return None
 def _delta(self):self.destroy()
class Input(tk.Frame):
 def __init__(self,master,kwargs):
  super().__init__(master)
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.bg=parsecolor(kwargs.get("bg",THEMES["bg3"]))
  self.entry_underline=False if kwargs.get("underline","normal")=="normal" else True
  self.entry_weight=kwargs.get("weight") if kwargs.get("weight") in ["normal","bold"] else "normal"
  self.entry_slant=kwargs.get("slant") if kwargs.get("slant") in ["roman","italic"] else "roman"
  self.entry_overstrike=False if kwargs.get("overstrike","normal")=="normal" else True
  self.entry_fontfamily=kwargs.get("font_family","Meiryo")
  self.entry_fontsize=num0(kwargs.get("font_size"),10)
  self.font=kwargs.get("font",fonts(master,self.entry_fontfamily,self.entry_fontsize,self.entry_weight,self.entry_slant,self.entry_overstrike,self.entry_underline))
  self.justify=kwargs.get("justify") if kwargs.get("justify") in ["right","center","left"] else "left"
  self.wraplength=num0(kwargs.get("wraplength"))
  self.cursor=kwargs.get("cursor")
  self.takefocus=bols(kwargs.get("takefocus"))
  self.borderwidth=num0(kwargs.get("bd"))
  self.relief=kwargs.get("relief") if kwargs.get("relief") in relief_list else "flat"
  self.activeforeground=parsecolor(kwargs.get("activefg"))
  self.activebackground=parsecolor(kwargs.get("activebg"))
  self.highlightthickness=num0(kwargs.get("highlightthickness"))
  self.highlightcolor=parsecolor(kwargs.get("highlightfg"))
  self.highlightbackground=parsecolor(kwargs.get("highlightbg"))
  self.width=num0(kwargs.get("width"),20)
  self.text=kwargs.get("text","")
  self.show=kwargs.get("show")
  self.insertbackground=parsecolor(kwargs.get("insertbg",self.fg))
  self.insertwidth=num0(kwargs.get("insertwidth"),2)
  self.scroll_x=bols(kwargs.get("scroll_x"),False)
  self.input=tk.Entry(self,takefocus=self.takefocus,highlightcolor=self.highlightcolor,highlightbackground=self.highlightbackground,highlightthickness=self.highlightthickness,activeforeground=self.activeforeground,activebackground=self.activebackground,relief=self.relief,cursor=self.cursor,insertwidth=self.insertwidth,insertbackground=self.insertbackground,bg=self.bg,fg=self.fg,font=self.font,width=self.width,justify=self.justify,show=self.show)
  self.input.grid(row=0,column=0,sticky="nsew")
  if self.scroll_x:
   self.xscrollbar=ttk.Scrollbar(self,orient="horizontal",command=self.input.xview)
   self.input.configure(xscrollcommand=self.xscrollbar.set)
   self.xscrollbar.grid(row=1,column=0,sticky="ew")
  if self.text!=None:self.inserts(self.text,place="end")
 def inserts(self,text="",place="end"):self.input.insert(place,text)
 def get_text(self):return self.input.get()
 def select_judge(self):return self.input.select_present()
 def select_cansel(self):self.input.select_clear()
 def all_delta(self):self.input.delete(0,"end")
 def _delta(self):self.destroy()
class Multiline(tk.Frame):
 def __init__(self,master,kwargs):
  super().__init__(master)
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.bg=parsecolor(kwargs.get("bg",THEMES["bg3"]))
  self.entry_underline=False if kwargs.get("underline","normal")=="normal" else True
  self.entry_weight=kwargs.get("weight") if kwargs.get("weight") in ["normal","bold"] else "normal"
  self.entry_slant=kwargs.get("slant") if kwargs.get("slant") in ["roman","italic"] else "roman"
  self.entry_overstrike=False if kwargs.get("overstrike","normal")=="normal" else True
  self.entry_fontfamily=kwargs.get("font_family","Meiryo")
  self.entry_fontsize=num0(kwargs.get("font_size"),10)
  self.font=kwargs.get("font",fonts(master,self.entry_fontfamily,self.entry_fontsize,self.entry_weight,self.entry_slant,self.entry_overstrike,self.entry_underline))
  self.justify=kwargs.get("justify") if kwargs.get("justify") in ["right","center","left"] else "left"
  self.padx=num0(kwargs.get("padx"))
  self.pady=num0(kwargs.get("pady"))
  self.wraplength=num0(kwargs.get("wraplength"))
  self.cursor=kwargs.get("cursor")
  self.takefocus=bols(kwargs.get("takefocus"))
  self.borderwidth=num0(kwargs.get("bd"))
  self.relief=kwargs.get("relief") if kwargs.get("relief") in relief_list else "flat"
  self.activeforeground=parsecolor(kwargs.get("activefg"))
  self.activebackground=parsecolor(kwargs.get("activebg"))
  self.highlightthickness=num0(kwargs.get("highlightthickness"))
  self.highlightcolor=parsecolor(kwargs.get("highlightfg"))
  self.highlightbackground=parsecolor(kwargs.get("highlightbg"))
  self.size=wi._size(kwargs,(20,5))
  self.width=self.size[0]
  self.height=self.size[1]
  self.text=kwargs.get("text","")
  self.state=bols(kwargs.get("state",True),True)
  self.wrap=kwargs.get("wrap") if kwargs.get("wrap") in ["none","word","char"] else "none"
  self.justify=kwargs.get("justify") if kwargs.get("justify","left") in ["left","center","right"] else "left"
  self.insertbackground=parsecolor(kwargs.get("insertbg",self.fg))
  self.insertwidth=num0(kwargs.get("insertwidth"),2)
  self.scroll_y=bols(kwargs.get("scroll_y"),False)
  self.scroll_x=bols(kwargs.get("scroll_x"),False)
  self.mul=tk.Text(self,takefocus=self.takefocus,insertbackground=self.insertbackground,insertwidth=self.insertwidth,padx=self.padx,pady=self.pady,highlightcolor=self.highlightcolor,highlightbackground=self.highlightbackground,highlightthickness=self.highlightthickness,activeforeground=self.activeforeground,activebackground=self.activebackground,relief=self.relief,cursor=self.cursor,bg=self.bg,fg=self.fg,font=self.font,width=self.width,height=self.height,justify=self.justify,state="normal" if self.state else "disabled",wrap=self.wrap)
  self.mul.grid(row=0,column=0,sticky="nsew")
  if self.scroll_y:
   self.yscrollbar=ttk.Scrollbar(self,orient="vertical",command=self.mul.yview)
   self.mul.configure(yscrollcommand=self.yscrollbar.set)
   self.yscrollbar.grid(row=0,column=1,sticky="ns")
  if self.scroll_x:
   self.xscrollbar=ttk.Scrollbar(self,orient="horizontal",command=self.mul.xview)
   self.mul.configure(xscrollcommand=self.xscrollbar.set)
   self.xscrollbar.grid(row=1,column=0,sticky="ew")
  if self.text!=None and isinstance(self.text,(str,int,float)):self.inserts(self.text,place="end")
  elif self.text!=None and isinstance(self.text,(list,tuple)):
   savetext=""
   for i,item in enumerate(list(self.text)):savetext+=f"{item}" if i==len(list(self.text))-1 else f"{item}\n"
   self.text=savetext
   self.inserts(savetext,place="end")
 def inserts(self,text="",place="end"):self.mul.insert(place,text)
 def get_text(self):return self.mul.get(1.0,"end-1c")
 def all_delta(self):self.mul.delete(1.0,"end")
 def _delta(self):self.mul.destroy()
class InputNumber(tk.Spinbox):
 def __init__(self,master,kwargs):
  self.bg=parsecolor(kwargs.get("bg",THEMES["bg3"]))
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.entry_underline=False if kwargs.get("underline","normal")=="normal" else True
  self.entry_weight=kwargs.get("weight") if kwargs.get("weight") in ["normal","bold"] else "normal"
  self.entry_slant=kwargs.get("slant") if kwargs.get("slant") in ["roman","italic"] else "roman"
  self.entry_overstrike=False if kwargs.get("overstrike","normal")=="normal" else True
  self.entry_fontfamily=kwargs.get("font_family","Meiryo")
  self.entry_fontsize=num0(kwargs.get("font_size"),10)
  self.font=kwargs.get("font",fonts(master,self.entry_fontfamily,self.entry_fontsize,self.entry_weight,self.entry_slant,self.entry_overstrike,self.entry_underline))
  self.justify=kwargs.get("justify") if kwargs.get("justify") in ["right","center","left"] else "left"
  self.wraplength=num0(kwargs.get("wraplength"))
  self.cursor=kwargs.get("cursor")
  self.takefocus=bols(kwargs.get("takefocus"))
  self.borderwidth=num0(kwargs.get("bd"))
  self.relief=kwargs.get("relief") if kwargs.get("relief") in relief_list else "flat"
  self.activeforeground=parsecolor(kwargs.get("activefg"))
  self.activebackground=parsecolor(kwargs.get("activebg"))
  self.highlightthickness=num0(kwargs.get("highlightthickness"))
  self.highlightcolor=parsecolor(kwargs.get("highlightfg"))
  self.highlightbackground=parsecolor(kwargs.get("highlightbg"))
  self.min=nums(kwargs.get("min"),0)
  self.max=nums(kwargs.get("max"),100)
  self.increment=num0(kwargs.get("step"),1)
  self.wrap=bols(kwargs.get("wrap"),False)
  self.width=num0(kwargs.get("width"),20)
  self.justify=kwargs.get("justify") if kwargs.get("justify") in ["left","center","right"] else "left"
  self.values=kwargs.get("values")
  self.insertbackground=parsecolor(kwargs.get("insertbg",self.fg))
  self.insertwidth=num0(kwargs.get("insertwidth"),2)
  if isinstance(self.values,(list,tuple)):
   super().__init__(master,takefocus=self.takefocus,highlightcolor=self.highlightcolor,highlightbackground=self.highlightbackground,highlightthickness=self.highlightthickness,activeforeground=self.activeforeground,activebackground=self.activebackground,relief=self.relief,cursor=self.cursor,textvariable=tk.StringVar(value=self.values[0]),values=self.values,bg=self.bg,fg=self.fg,font=self.font,justify=self.justify,wrap=self.wrap,width=self.width)
  else:
   super().__init__(master,takefocus=self.takefocus,insertbackground=self.insertbackground,insertwidth=self.insertwidth,highlightcolor=self.highlightcolor,highlightbackground=self.highlightbackground,highlightthickness=self.highlightthickness,activeforeground=self.activeforeground,activebackground=self.activebackground,relief=self.relief,cursor=self.cursor,from_=self.min,to=self.max,increment=self.increment,bg=self.bg,fg=self.fg,font=self.font,justify=self.justify,wrap=self.wrap,width=self.width)
 def _get(self):return self.get()
 def _delta(self):self.destroy()
class Combobox(ttk.Combobox):
 def __init__(self,master,kwargs):
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.back_bg=kwargs.get("back_bg")
  self.bg=parsecolor(kwargs.get("bg",self.back_bg or THEMES["bg1"]))
  self.entry_underline=False if kwargs.get("underline","normal")=="normal" else True
  self.entry_weight=kwargs.get("weight") if kwargs.get("weight") in ["normal","bold"] else "normal"
  self.entry_slant=kwargs.get("slant") if kwargs.get("slant") in ["roman","italic"] else "roman"
  self.entry_overstrike=False if kwargs.get("overstrike","normal")=="normal" else True
  self.entry_fontfamily=kwargs.get("font_family","Meiryo")
  self.entry_fontsize=num0(kwargs.get("font_size"),10)
  self.font=kwargs.get("font",fonts(master,self.entry_fontfamily,self.entry_fontsize,self.entry_weight,self.entry_slant,self.entry_overstrike,self.entry_underline))
  self.justify=kwargs.get("justify") if kwargs.get("justify") in ["right","center","left"] else "left"
  self.wraplength=num0(kwargs.get("wraplength"))
  self.cursor=kwargs.get("cursor")
  self.takefocus=bols(kwargs.get("takefocus"))
  self.borderwidth=num0(kwargs.get("bd"))
  self.relief=kwargs.get("relief") if kwargs.get("relief") in relief_list else "flat"
  self.padx=num0(kwargs.get("padx"))
  self.pady=num0(kwargs.get("pady"))
  self.activeforeground=parsecolor(kwargs.get("activefg"))
  self.activebackground=parsecolor(kwargs.get("activebg"))
  self.values=kwargs.get("values",[])
  self.default=kwargs.get("default","")
  self.states=kwargs.get("state","readonly")
  self.funcs=kwargs.get("function")
  style=ttk.Style()
  self.stylename=f"Custom{kwargs.get("count")}.TCombobox"
  style.configure(self.stylename,foreground=self.fg,background=self.bg,fieldbackground=self.bg,font=self.font)
  super().__init__(master,takefocus=self.takefocus,activeforeground=self.activeforeground,activebackground=self.activebackground,cursor=self.cursor,values=self.values,state=self.states,font=self.font,style=self.stylename)
  if self.default:self.set(self.default)
  self.bind("<<ComboboxSelected>>",lambda e,f=self.funcs:wi._exec_funcs(f))
 def get_value(self):return self.get()
 def set_value(self,val):self.set(val)
 def clear(self):self.set("")
 def _delta(self):self.destroy()
class Listbox(tk.Frame):
 def __init__(self,master,kwargs):
  super().__init__(master)
  self.values=kwargs.get("values",[]) if type(kwargs.get("values",[])) in [list,tuple] else []
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.bg=parsecolor(kwargs.get("bg",THEMES["bg3"]))
  self.selectforeground=parsecolor(kwargs.get("selectfg",THEMES["fg1"]))
  self.selectbackground=parsecolor(kwargs.get("selectbg",THEMES["bg5"]))
  self.entry_underline=False if kwargs.get("underline","normal")=="normal" else True
  self.entry_weight=kwargs.get("weight") if kwargs.get("weight") in ["normal","bold"] else "normal"
  self.entry_slant=kwargs.get("slant") if kwargs.get("slant") in ["roman","italic"] else "roman"
  self.entry_overstrike=False if kwargs.get("overstrike","normal")=="normal" else True
  self.entry_fontfamily=kwargs.get("font_family","Meiryo")
  self.entry_fontsize=num0(kwargs.get("font_size"),10)
  self.font=kwargs.get("font",fonts(master,self.entry_fontfamily,self.entry_fontsize,self.entry_weight,self.entry_slant,self.entry_overstrike,self.entry_underline))
  self.justify=kwargs.get("justify") if kwargs.get("justify") in ["right","center","left"] else "left"
  self.cursor=kwargs.get("cursor")
  self.exportselection=bols(kwargs.get("exportselection",False),False)
  self.takefocus=bols(kwargs.get("takefocus"))
  self.borderwidth=num0(kwargs.get("bd"))
  self.relief=kwargs.get("relief") if kwargs.get("relief") in relief_list else "flat"
  self.activeforeground=parsecolor(kwargs.get("activefg"))
  self.activebackground=parsecolor(kwargs.get("activebg"))
  self.highlightthickness=num0(kwargs.get("highlightthickness"))
  self.highlightcolor=parsecolor(kwargs.get("highlightfg"))
  self.highlightbackground=parsecolor(kwargs.get("highlightbg"))
  self.selectmode=kwargs.get("selectmode") if kwargs.get("selectmode") in ["browse","single","multiple","extended"] else "browse"
  self.width=kwargs.get("width",20)
  self.height=kwargs.get("hieght",min(max(len(self.values),1),5))
  self.state=bols(kwargs.get("state"))# Trueなら選択可能
  self.scroll_y=bols(kwargs.get("scroll_y"),False)
  self.scroll_x=bols(kwargs.get("scroll_x"),False)
  self.listbox=tk.Listbox(self,exportselection=self.exportselection,selectforeground=self.selectforeground,selectbackground=self.selectbackground,highlightcolor=self.highlightcolor,highlightbackground=self.highlightbackground,highlightthickness=self.highlightthickness,activeforeground=self.activeforeground,activebackground=self.activebackground,relief=self.relief,cursor=self.cursor,listvariable=tk.StringVar(value=self.values),bg=self.bg,fg=self.fg,font=self.font,selectmode=self.selectmode,width=self.width,height=self.height,justify=self.justify,state="normal" if self.state else "disabled")
  self.listbox.grid(row=0,column=0,sticky="nsew")
  self.selectval=nums(kwargs.get("select"))
  self.select_set(self.selectval)
  if self.scroll_y:
   self.yscrollbar=ttk.Scrollbar(self,orient="vertical",command=self.listbox.yview)
   self.listbox.configure(yscrollcommand=self.yscrollbar.set)
   self.yscrollbar.grid(row=0,column=1,sticky="ns")
  if self.scroll_x:
   self.xscrollbar=ttk.Scrollbar(self,orient="horizontal",command=self.listbox.xview)
   self.listbox.configure(xscrollcommand=self.xscrollbar.set)
   self.xscrollbar.grid(row=1,column=0,sticky="ew")
 def select_set(self,val):
  if isinstance(val,int):
   if val<0:val=0
   elif len(self.values)<val:val=len(self.values)-1
   self.listbox.selection_set(val)
 def apend(self,lists=[],place="end"):
  if type(lists) in [list,tuple]:
   for i in lists:self.listbox.insert(place,i)
 def clear(self):self.listbox.delete(0,"end")
 def dele(self,*index):
  if isinstance(index,tuple):
   for i in list(index):
    i=nums(i)
    if i==None or (i<0 or self.lens()<i):continue
    self.listbox.delete(i)
 def lens(self):return self.listbox.size()
 def select(self):return self.listbox.curselection()
 def select_val(self):
  val=list(self.listbox.curselection())
  lists=[]
  if len(val)==1:return self.values[val[0]]
  elif len(val)==0:return None
  for i in val:lists.append(self.values[i])
  return lists
 def indexs(self,num):self.listbox.index(range_num(int(num),1,self.lens(),1))
 def listset(self,lists):
  if type(lists) in [list,tuple]:
   self.clear()
   self.apend(lists,"end")
 def _delta(self):self.listbox.destroy()
class Radio(tk.Radiobutton):
 groups,count={},0
 def __init__(self,master,kwargs):
  Radio.count+=1
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.back_bg=kwargs.get("back_bg")
  self.bg=parsecolor(kwargs.get("bg",self.back_bg or THEMES["bg1"]))
  self.underline=False if kwargs.get("underline","normal")=="normal" else True
  self.weight=kwargs.get("weight") if kwargs.get("weight") in ["normal","bold"] else "normal"
  self.slant=kwargs.get("slant") if kwargs.get("slant") in ["roman","italic"] else "roman"
  self.overstrike=False if kwargs.get("overstrike","normal")=="normal" else True
  self.font_family=kwargs.get("font_family","Meiryo")
  self.font_size=num0(kwargs.get("font_size"),14)
  self.font=kwargs.get("font",fonts(master,self.font_family,self.font_size,self.weight,self.slant,self.overstrike,self.underline))
  self.justify=kwargs.get("justify") if kwargs.get("justify") in ["right","center","left"] else "left"
  self.wraplength=num0(kwargs.get("wraplength"))
  self.cursor=kwargs.get("cursor")
  self.takefocus=bols(kwargs.get("takefocus"))
  self.borderwidth=num0(kwargs.get("bd"))
  self.relief=kwargs.get("relief") if kwargs.get("relief") in relief_list else "flat"
  self.padx=num0(kwargs.get("padx"))
  self.pady=num0(kwargs.get("pady"))
  self.anchor=kwargs.get("anchor","w") if get_dict(anchor_dict,kwargs.get("anchor","right"))[1] in anchor_list else "w"
  self.activeforeground=parsecolor(kwargs.get("activefg"))
  self.activebackground=parsecolor(kwargs.get("activebg"))
  self.highlightthickness=num0(kwargs.get("highlightthickness"))
  self.highlightcolor=parsecolor(kwargs.get("highlightfg"))
  self.highlightbackground=parsecolor(kwargs.get("highlightbg"))
  self.group=kwargs.get("group","default")
  self.text=kwargs.get("text","")
  self.value=kwargs.get("value",f"{self.text}{Radio.count}")
  self.funcs=kwargs.get("function")
  self.default=kwargs.get("default")
  if self.group not in Radio.groups:Radio.groups[self.group]={"var":tk.StringVar(),"has_default":False}
  group_data=Radio.groups[self.group]
  self.variable=group_data["var"]
  super().__init__(master,takefocus=self.takefocus,highlightcolor=self.highlightcolor,highlightbackground=self.highlightbackground,highlightthickness=self.highlightthickness,activeforeground=self.activeforeground,activebackground=self.activebackground,anchor=self.anchor,pady=self.pady,padx=self.padx,relief=self.relief,wraplength=self.wraplength,cursor=self.cursor,text=self.text,value=self.value,variable=self.variable,bg=self.bg,fg=self.fg,font=self.font,command=lambda f=self.funcs:wi._exec_funcs(f))
  if self.default:
   self.variable.set(self.value)
   group_data["has_default"]=True
  if not group_data["has_default"]:
   self.variable.set(self.value)
   group_data["has_default"]=True
 def get_text(self):return self.text
 def set_text(self,txt):
  if txt:
   self.text=txt
   self.config(text=txt)
  else:return None
 def get_bg(self):return self.bg
 def set_bg(self,nbg):
  if nbg and isinstance(nbg,str):
   self.bg=nbg
   self.config(bg=nbg)
  else:return None
 def get_fg(self):return self.fg
 def set_fg(self,nfg):
  if nfg and isinstance(nfg,str):
   self.fg=nfg
   self.config(fg=nfg)
  else:return None
 def get_font(self):return self.font
 def set_font(self,nfont):
  if nfont and isinstance(nfont,tuple):
   self.font=nfont
   self.config(font=nfont)
  else:return None
 def _delta(self):self.destroy()
class Checkbox(tk.Checkbutton):
 def __init__(self,master,kwargs):
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.back_bg=kwargs.get("back_bg")
  self.bg=parsecolor(kwargs.get("bg",self.back_bg or THEMES["bg1"]))
  self.underline=False if kwargs.get("underline","normal")=="normal" else True
  self.weight=kwargs.get("weight") if kwargs.get("weight") in ["normal","bold"] else "normal"
  self.slant=kwargs.get("slant") if kwargs.get("slant") in ["roman","italic"] else "roman"
  self.overstrike=False if kwargs.get("overstrike","normal")=="normal" else True
  self.font_family=kwargs.get("font_family","Meiryo")
  self.font_size=num0(kwargs.get("font_size"),14)
  self.font=kwargs.get("font",fonts(master,self.font_family,self.font_size,self.weight,self.slant,self.overstrike,self.underline))
  self.justify=kwargs.get("justify") if kwargs.get("justify") in ["right","center","left"] else "left"
  self.wraplength=num0(kwargs.get("wraplength"))
  self.cursor=kwargs.get("cursor")
  self.takefocus=bols(kwargs.get("takefocus"))
  self.borderwidth=num0(kwargs.get("bd"))
  self.relief=kwargs.get("relief") if kwargs.get("relief") in relief_list else "flat"
  self.padx=num0(kwargs.get("padx"))
  self.pady=num0(kwargs.get("pady"))
  self.anchor=kwargs.get("anchor","w") if get_dict(anchor_dict,kwargs.get("anchor","right"))[1] in anchor_list else "w"
  self.activeforeground=parsecolor(kwargs.get("activefg"))
  self.activebackground=parsecolor(kwargs.get("activebg"))
  self.highlightthickness=num0(kwargs.get("highlightthickness"))
  self.highlightcolor=parsecolor(kwargs.get("highlightfg"))
  self.highlightbackground=parsecolor(kwargs.get("highlightbg"))
  self.text=kwargs.get("text","")
  self.funcs=kwargs.get("function")
  self.default=bols(kwargs.get("default"),False)
  self.variable=tk.BooleanVar()
  super().__init__(master,takefocus=self.takefocus,highlightcolor=self.highlightcolor,highlightbackground=self.highlightbackground,highlightthickness=self.highlightthickness,activeforeground=self.activeforeground,activebackground=self.activebackground,anchor=self.anchor,pady=self.pady,padx=self.padx,relief=self.relief,wraplength=self.wraplength,cursor=self.cursor,text=self.text,variable=self.variable,bg=self.bg,fg=self.fg,font=self.font,command=lambda f=self.funcs:wi._exec_funcs(f))
  if self.default:
   self.select()
   self.variable.set(True)
  else:
   self.deselect()
   self.variable.set(False)
 def get_value(self):return self.variable.get()
 def set_value(self,value:bool):
  if isinstance(value,bool):self.variable.set(value)
 def _delta(self):self.destroy()
class Tree(tk.Frame):
 def __init__(self,master,kwargs):
  super().__init__(master)
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.header_fg=parsecolor(kwargs.get("header_fg",THEMES["fg1"]))
  self.bg=parsecolor(kwargs.get("bg",THEMES["bg2"]))
  self.header_bg=parsecolor(kwargs.get("header_bg",THEMES["bg4"]))
  self.rowheight=kwargs.get("rowheight",50)
  self.values=kwargs.get("values",[])
  self.header=kwargs.get("header",[])
  self.side_header=kwargs.get("side_header","")
  self.onclick=kwargs.get("function")
  self.scroll_y=bols(kwargs.get("scroll_y"),False)
  self.scroll_x=bols(kwargs.get("scroll_x"),False)
  self.sums=1
  self.maxcols=1 if self._calc_max_columns(self.values)<1 else self._calc_max_columns(self.values)
  cols=[f"col{i}" for i in range(1,self.maxcols+1)]
  self.tree=ttk.Treeview(self,columns=cols,show="tree" if self.header==[] else "tree headings")
  if self.header!=[] and len(self.header)<self.maxcols:
   for i in range(self.maxcols-len(self.header)):self.header.append("")
  self.tree.heading("#0",text=self.side_header)
  self.tree.column("#0",width=200,anchor="w")
  for i,c in enumerate(cols):
   self.tree.heading(c,text="" if self.header==[] else self.header[i])
   self.tree.column(c,width=120,anchor="w")
  self.tree.grid(row=0,column=0,sticky="nsew")
  style=ttk.Style()
  self.stylename=f"Tree{kwargs.get("count")}.Treeview"
  self.header_underline=False if kwargs.get("header_underline","normal")=="normal" else True
  self.header_weight=kwargs.get("header_weight") if kwargs.get("header_weight") in ["normal","bold"] else "normal"
  self.header_slant=kwargs.get("header_slant") if kwargs.get("header_slant") in ["roman","italic"] else "roman"
  self.header_overstrike=False if kwargs.get("header_overstrike","normal")=="normal" else True
  self.header_font_family=kwargs.get("header_fontfamily","Meiryo")
  self.header_font_size=num0(kwargs.get("header_fontsize"),14)
  self.header_font=kwargs.get("font",fonts(self.tree,self.header_font_family,self.header_font_size,self.header_weight,self.header_slant,self.header_overstrike,self.header_underline))
  style.configure(style=f"{self.stylename}.Heading",background=self.header_bg,foreground=self.header_fg,font=self.header_font)
  self.tree.configure(style=f"{self.stylename}.Heading")
  self.underline=False if kwargs.get("underline","normal")=="normal" else True
  self.weight=kwargs.get("weight") if kwargs.get("weight") in ["normal","bold"] else "normal"
  self.slant=kwargs.get("slant") if kwargs.get("slant") in ["roman","italic"] else "roman"
  self.overstrike=False if kwargs.get("overstrike","normal")=="normal" else True
  self.font_family=kwargs.get("font_family","Meiryo")
  self.font_size=num0(kwargs.get("font_size"),14)
  self.font=kwargs.get("font",fonts(self.tree,self.font_family,self.font_size,self.weight,self.slant,self.overstrike,self.underline))
  style.configure(style=self.stylename,background=self.bg,foreground=self.fg,fieldbackground=self.bg,font=self.font,rowheight=self.rowheight)
  self.tree.configure(style=self.stylename)
  if self.scroll_y:
   ybar=ttk.Scrollbar(self,orient="vertical",command=self.tree.yview)
   self.tree.configure(yscrollcommand=ybar.set)
   ybar.grid(row=0,column=1,sticky="ns")
  if self.scroll_x:
   xbar=ttk.Scrollbar(self,orient="horizontal",command=self.tree.xview)
   self.tree.configure(xscrollcommand=xbar.set)
   xbar.grid(row=1,column=0,sticky="ew")
  self.grid_rowconfigure(0,weight=1)
  self.grid_columnconfigure(0,weight=1)
  self.tree.bind("<<TreeviewSelect>>",self._on_select)
  self._build_from_values(self.values)
  self.tree.config(height=min(num0(self.sums,1),15))
 def _calc_max_columns(self,vals):
  maxc,i=0,0
  L=len(vals)
  while i<L:
   v=vals[i]
   if isinstance(v,str) and i+1<L and isinstance(vals[i+1],list):
     c=self._maxlen_in_list(vals[i+1])
     if maxc<c:maxc=c
     i+=2
   else:i+=1
  return maxc
 def _maxlen_in_list(self,lst):
  maxc=0
  strings=[x for x in lst if not isinstance(x,list)]
  if maxc<len(strings):maxc=len(strings)
  for x in lst:
   if isinstance(x,list):
    c=self._maxlen_in_list(x)
    if maxc<c:maxc=c
  return maxc
 def _flatten_strings(self,lst):
  out=[]
  for x in lst:
   if isinstance(x,list):out.extend(self._flatten_strings(x))
   else:out.append(x)
  return out
 def _build_from_values(self,vals):
  i,L=0,len(vals)
  while i<L:
   item=vals[i]
   if isinstance(item,str) and i+1<L and isinstance(vals[i+1],list):
     self._process_data_list(self.tree.insert("","end",text=item,values=("")*self.maxcols),item,vals[i+1])
     self.sums+=2
     i+=2
   else:
    self.sums+=1
    i+=1
 def _process_data_list(self,parent_id,parent_text,data_list):
  summary_values=[x for x in data_list if not isinstance(x,list)]
  summary_id=self.tree.insert(parent_id,tk.END,text=parent_text,values=(tuple((str(x) for x in summary_values[:self.maxcols]))+tuple("" for _ in range(max(0,self.maxcols-len(summary_values))))))
  for idx,x in enumerate(data_list):
   if isinstance(x,list):
    k=idx-1
    while k<=0 and isinstance(data_list[k],list):k-=1
    label=data_list[k] if 0<=k and isinstance(data_list[k],str) else ""
    if any(isinstance(s,list) for s in x):
     nested_summary_values=[s for s in x if not isinstance(s,list)]
     for y in x:
      if isinstance(y,list):self._process_data_list(self.tree.insert(summary_id,tk.END,text=label,values=tuple((str(s) for s in nested_summary_values[:self.maxcols]))+tuple("" for _ in range(max(0,self.maxcols-len(nested_summary_values))))),label,y)
    else:self.tree.insert(summary_id,tk.END,text=label,values=tuple((str(s) for s in x[:self.maxcols]))+tuple("" for _ in range(max(0,self.maxcols-len(x)))))
 def _on_select(self,event):
  if not self.onclick:return
  try:
   sel=self.tree.selection()
   if sel:self.onclick(self,sel[0])
  except:pass
 def expand(self,iid):self.tree.item(iid,open=True)
 def collapse(self,iid):self.tree.item(iid,open=False)
 def get_path(self,iid):
  parts,cur=[],iid
  while cur:
   txt=self.tree.item(cur,"text")
   if txt: parts.append(txt)
   cur=self.tree.parent(cur)
  parts.reverse()
  return "/".join(parts)
 def _delta(self):self.tree.destroy()
 def add_node(self,parent_iid,text,data_list=None):
  pid=self.tree.insert(parent_iid,tk.END,text=text,values=("")*self.maxcols)
  if isinstance(data_list,list):self._process_data_list(pid,text,data_list)
  return pid
 def delete_node(self,iid):self.tree.delete(iid)
 def clear_width(self):
  columns=self.tree["columns"]
  self.update_idletasks()
  if 0<len(columns):
   for col in columns:self.tree.column(col,width=int(self.tree.winfo_width()/len(columns)))
class Table(tk.Frame):
 def __init__(self,master,kwargs):
  super().__init__(master)
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.header_fg=parsecolor(kwargs.get("header_fg",THEMES["fg1"]))
  self.bg=parsecolor(kwargs.get("bg",THEMES["bg2"]))
  self.header_bg=parsecolor(kwargs.get("header_bg",THEMES["bg4"]))
  self.cursor=kwargs.get("cursor")
  self.takefocus=bols(kwargs.get("takefocus"))
  self.padding=kwargs.get("padding",0)
  self.values=kwargs.get("values",[])
  self.header=kwargs.get("header",[])
  self.colwidth=kwargs.get("colwidth",120)
  self.scroll_y=bols(kwargs.get("scroll_y"),False)
  self.scroll_x=bols(kwargs.get("scroll_x"),False)
  self.height=kwargs.get("height",max(len(self.values),1))
  self.rowheight=kwargs.get("rowheight",50)
  self.rowheader=kwargs.get("rowheader",[])
  style=ttk.Style()
  self.stylename=f"Table{kwargs.get("count")}.Treeview"
  self.tree=ttk.Treeview(self,show="headings",style=self.stylename,height=self.height,takefocus=self.takefocus)
  self.header_underline=False if kwargs.get("header_underline","normal")=="normal" else True
  self.header_weight=kwargs.get("header_weight") if kwargs.get("header_weight") in ["normal","bold"] else "normal"
  self.header_slant=kwargs.get("header_slant") if kwargs.get("header_slant") in ["roman","italic"] else "roman"
  self.header_overstrike=False if kwargs.get("header_overstrike","normal")=="normal" else True
  self.header_font_family=kwargs.get("header_fontfamily","Meiryo")
  self.header_font_size=num0(kwargs.get("header_fontsize"),14)
  self.header_font=kwargs.get("font",fonts(self.tree,self.header_font_family,self.header_font_size,self.header_weight,self.header_slant,self.header_overstrike,self.header_underline))
  style.configure(style=f"{self.stylename}.Heading",background=self.header_bg,foreground=self.header_fg,font=self.header_font)
  self.tree.configure(style=f"{self.stylename}.Heading")
  self.underline=False if kwargs.get("underline","normal")=="normal" else True
  self.weight=kwargs.get("weight") if kwargs.get("weight") in ["normal","bold"] else "normal"
  self.slant=kwargs.get("slant") if kwargs.get("slant") in ["roman","italic"] else "roman"
  self.overstrike=False if kwargs.get("overstrike","normal")=="normal" else True
  self.font_family=kwargs.get("font_family","Meiryo")
  self.font_size=num0(kwargs.get("font_size"),14)
  self.font=kwargs.get("font",fonts(self.tree,family=self.font_family,size=self.font_size,weight=self.weight,slant=self.slant,overstrike=self.overstrike,underline=self.underline))
  style.configure(style=self.stylename,background=self.bg,foreground=self.fg,fieldbackground=self.bg,font=self.font,rowheight=self.rowheight)
  self.tree.configure(style=self.stylename)
  columns=[]
  if self.rowheader:columns.append("rowheader")
  if self.header:columns+=self.header
  else:
   if 0<len(self.values):columns+=["col_"+str(i) for i in range(len(self.values[0]))]
  self.tree["columns"]=columns
  for col in columns:
   self.tree.heading(col,text=(" " if self.rowheader else "行")if col=="rowheader" else col if self.header else "")
   self.tree.column(col,anchor="center",width=100)
  self.tree.tag_configure("rowheader_tag",background=self.header_bg,foreground=self.header_fg)
  if self.rowheader:
   for i,row in enumerate(self.values):self.tree.item(self.tree.insert("","end",values=[self.rowheader[i] if i<len(self.rowheader) else ""]+row),tags=("rowheader_tag",))
  else:
   for row in self.values:self.tree.insert("","end",values=row)
  self.tree.grid(row=0,column=0,sticky="nsew")
  if self.scroll_y:
   self.yscrollbar=ttk.Scrollbar(self,orient="vertical",command=self.tree.yview)
   self.tree.configure(yscrollcommand=self.yscrollbar.set)
   self.yscrollbar.grid(row=0,column=1,sticky="ns")
  if self.scroll_x:
   self.xscrollbar=ttk.Scrollbar(self,orient="horizontal",command=self.tree.xview)
   self.tree.configure(xscrollcommand=self.xscrollbar.set)
   self.xscrollbar.grid(row=1,column=0,sticky="ew")
  self.grid_rowconfigure(0,weight=1)
  self.grid_columnconfigure(0,weight=1)
 def clear_width(self,total_width=None):
  columns=self.tree["columns"]
  if total_width==None:
   self.update_idletasks()
   total_width=self.tree.winfo_width()
  if 0<len(columns):
   for col in columns:self.tree.column(col,width=int(total_width/len(columns)))
 def _delta(self):self.tree.destroy()
class Slidebar(tk.Scale):
 def __init__(self,master,kwargs):
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.back_bg=kwargs.get("back_bg")
  self.bg=parsecolor(kwargs.get("bg",self.back_bg or THEMES["bg1"]))
  self.underline=False if kwargs.get("underline","normal")=="normal" else True
  self.weight=kwargs.get("weight") if kwargs.get("weight") in ["normal","bold"] else "normal"
  self.slant=kwargs.get("slant") if kwargs.get("slant") in ["roman","italic"] else "roman"
  self.overstrike=False if kwargs.get("overstrike","normal")=="normal" else True
  self.font_family=kwargs.get("font_family","Meiryo")
  self.font_size=num0(kwargs.get("font_size"),14)
  self.font=kwargs.get("font",fonts(master,self.font_family,self.font_size,self.weight,self.slant,self.overstrike,self.underline))
  self.justify=kwargs.get("justify") if kwargs.get("justify") in ["right","center","left"] else "left"
  self.wraplength=num0(kwargs.get("wraplength"))
  self.cursor=kwargs.get("cursor")
  self.takefocus=bols(kwargs.get("takefocus"))
  self.borderwidth=num0(kwargs.get("bd"))
  self.relief=kwargs.get("relief") if kwargs.get("relief") in relief_list else "flat"
  self.activeforeground=parsecolor(kwargs.get("activefg"))
  self.activebackground=parsecolor(kwargs.get("activebg"))
  self.highlightthickness=num0(kwargs.get("highlightthickness"))
  self.highlightcolor=parsecolor(kwargs.get("highlightfg"))
  self.highlightbackground=parsecolor(kwargs.get("highlightbg"))
  self.value=num0(kwargs.get("value"),50)
  self.minval=num0(kwargs.get("min"),0)
  self.maxval=self.value if kwargs.get("max",100)<self.value else kwargs.get("max")
  self.step=kwargs.get("step",1)
  self.orientation=kwargs.get("orientation") if kwargs.get("orientation") in ["vertical","horizontal"] else "horizontal"
  self.resolution=num0(kwargs.get("resolution"),1)
  self.digits=num0(kwargs.get("digits"))
  self.length=num0(kwargs.get("length"),200)
  super().__init__(master,takefocus=self.takefocus,highlightcolor=self.highlightcolor,highlightbackground=self.highlightbackground,highlightthickness=self.highlightthickness,activeforeground=self.activeforeground,activebackground=self.activebackground,relief=self.relief,cursor=self.cursor,fg=self.fg,bg=self.bg,font=self.font,from_=self.minval,to=self.maxval,orient=self.orientation,resolution=self.resolution,digits=self.digits,length=self.length)
  self._set(self.value)
 def _set(self,val):
  if nums(val):self.set(val)
 def _get(self):return self.get()
 def _delta(self):self.destroy()
class Menu(tk.Menu):
 def __init__(self,master,kwargs):
  self.back_bg=kwargs.get("back_bg")
  self.bg=parsecolor(kwargs.get("bg",self.back_bg or THEMES["bg1"]))
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.underline=False if kwargs.get("underline","normal")=="normal" else True
  self.weight=kwargs.get("weight") if kwargs.get("weight") in ["normal","bold"] else "normal"
  self.slant=kwargs.get("slant") if kwargs.get("slant") in ["roman","italic"] else "roman"
  self.overstrike=False if kwargs.get("overstrike","normal")=="normal" else True
  self.font_family=kwargs.get("font_family","Meiryo")
  self.font_size=num0(kwargs.get("font_size"),14)
  self.font=kwargs.get("font",fonts(master,self.font_family,self.font_size,self.weight,self.slant,self.overstrike,self.underline))
  self.cursor=kwargs.get("cursor")
  self.takefocus=bols(kwargs.get("takefocus"))
  self.borderwidth=num0(kwargs.get("bd"))
  self.relief=kwargs.get("relief") if kwargs.get("relief") in relief_list else "flat"
  self.activeforeground=parsecolor(kwargs.get("activefg"))
  self.activebackground=parsecolor(kwargs.get("activebg"))
  self.menu_lists=kwargs.get("list",[])
  self.tearoff=bols(kwargs.get("tearoff"),False)
  super().__init__(master,takefocus=self.takefocus,activeforeground=self.activeforeground,activebackground=self.activebackground,relief=self.relief,cursor=self.cursor,tearoff=self.tearoff,bg=self.bg,fg=self.fg,font=self.font)
  self._create_menu_lists()
 def _create_menu_lists(self):
  self.delete(0,"end")
  for menus in self.menu_lists:
   if not isinstance(menus,list):continue
   for i in range(0,len(menus),2):
    if len(menus)<=i+1:break
    submenu=tk.Menu(self,tearoff=self.tearoff,bg=self.bg,fg=self.fg,font=self.font)
    self._add_items_recursive(submenu,menus[i+1])
    self.add_cascade(label=menus[i],menu=submenu)
 def _add_items_recursive(self,menu,items):
  i=0
  while i<len(items):
   item=items[i]
   if item=="---":
    menu.add_separator()
    i+=1
    continue
   if isinstance(item,dict):
    menu.add_command(label=item.get("label",""),command=lambda f=item.get("function"):wi._exec_funcs(f))
    i+=1
    continue
   if isinstance(item,str):
    if i+1<len(items) and isinstance(items[i+1],list):
     new_sub=tk.Menu(menu,tearoff=self.tearoff,bg=self.bg,fg=self.fg,font=self.font)
     self._add_items_recursive(new_sub,items[i+1])
     menu.add_cascade(label=item,menu=new_sub)
     i+=2
     continue
    else:
     menu.add_command(label=item)
     i+=1
     continue
   if isinstance(item,list):
    new_sub=tk.Menu(menu,tearoff=self.tearoff,bg=self.bg,fg=self.fg,font=self.font)
    self._add_items_recursive(new_sub,item)
    menu.add_cascade(label="Submenu",menu=new_sub)
    i+=1
    continue
  i+=1
 def get_items(self):return self.menu_lists
 def clear(self):
  self.delete(0,"end")
  self.menu_lists=[]
 def add_menu(self,label,submenu_lists):
  self.menu_lists.append([label,submenu_lists])
  self._create_menu_lists()
class Menubutton(tk.Menubutton):
 def __init__(self,master,kwargs):
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.bg=parsecolor(kwargs.get("bg",THEMES["bg2"]))
  self.button_underline=False if kwargs.get("underline","normal")=="normal" else True
  self.button_weight=kwargs.get("weight") if kwargs.get("weight") in ["normal","bold"] else "normal"
  self.button_slant=kwargs.get("slant") if kwargs.get("slant") in ["roman","italic"] else "roman"
  self.button_overstrike=False if kwargs.get("overstrike","normal")=="normal" else True
  self.button_fontfamily=kwargs.get("font_family","Meiryo")
  self.button_fontsize=num0(kwargs.get("font_size"),10)
  self.font=kwargs.get("font",fonts(master,self.button_fontfamily,self.button_fontsize,self.button_weight,self.button_slant,self.button_overstrike,self.button_underline))
  self.justify=kwargs.get("justify") if kwargs.get("justify") in ["right","center","left"] else "left"
  self.wraplength=num0(kwargs.get("wraplength"))
  self.cursor=kwargs.get("cursor")
  self.takefocus=bols(kwargs.get("takefocus"))
  self.borderwidth=num0(kwargs.get("bd"))
  self.relief=kwargs.get("relief") if kwargs.get("relief") in relief_list else "flat"
  self.padx=num0(kwargs.get("padx"),1)
  self.pady=num0(kwargs.get("pady"),1)
  self.anchor=kwargs.get("anchor","w") if get_dict(anchor_dict,kwargs.get("anchor","right"))[1] in anchor_list else "w"
  self.activeforeground=parsecolor(kwargs.get("activefg"))
  self.activebackground=parsecolor(kwargs.get("activebg"))
  self.highlightthickness=num0(kwargs.get("highlightthickness"))
  self.highlightcolor=parsecolor(kwargs.get("highlightfg"))
  self.highlightbackground=parsecolor(kwargs.get("highlightbg"))
  self.text=kwargs.get("text","Button")
  self.menu_lists=kwargs.get("list",[])
  self.tearoff=bols(kwargs.get("tearoff"),False)
  super().__init__(master,takefocus=self.takefocus,highlightcolor=self.highlightcolor,highlightbackground=self.highlightbackground,highlightthickness=self.highlightthickness,activeforeground=self.activeforeground,activebackground=self.activebackground,anchor=self.anchor,pady=self.pady,padx=self.padx,relief=self.relief,wraplength=self.wraplength,cursor=self.cursor,text=self.text,bg=self.bg,fg=self.fg,font=self.font)
  self.menu=tk.Menu(self,tearoff=self.tearoff,bg=self.bg,fg=self.fg,font=self.font)
  self._create_menu_lists()
  self["menu"]=self.menu
 def _create_menu_lists(self):
  for menus in self.menu_lists:
   if not isinstance(menus,list):continue
   for i in range(0,len(menus),2):
    if len(menus)<=i+1:break
    submenu=tk.Menu(self.menu,tearoff=self.tearoff,bg=self.bg,fg=self.fg,font=self.font)
    for item in menus[i+1]:
     if isinstance(item,dict):submenu.add_command(label=item.get("label",""),command=lambda f=item.get("function",None):wi._exec_funcs(f))
     elif item=="---":submenu.add_separator()
     elif isinstance(item,str):submenu.add_command(label=item)
    self.menu.add_cascade(label=menus[i],menu=submenu)
 def get_items(self):return self.menu_lists
 def clear(self):
  self.menu.delete(0,"end")
  self.menu_lists=[]
 def add_menu(self,label,submenu_lists):
  self.menu_lists.append([label,submenu_lists])
  self._create_menu_lists(self.menu_lists)
 def _delta(self):self.destroy()
class Frames(tk.LabelFrame):
 def __init__(self,master,kwargs):
  self.back_bg=kwargs.get("back_bg")
  self.bg=parsecolor(kwargs.get("bg",self.back_bg or THEMES["bg1"]))
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.underline=False if kwargs.get("underline","normal")=="normal" else True
  self.weight=kwargs.get("weight") if kwargs.get("weight") in ["normal","bold"] else "normal"
  self.slant=kwargs.get("slant") if kwargs.get("slant") in ["roman","italic"] else "roman"
  self.overstrike=False if kwargs.get("overstrike","normal")=="normal" else True
  self.font_family=kwargs.get("font_family","Meiryo")
  self.font_size=num0(kwargs.get("font_size"),14)
  self.font=kwargs.get("font",fonts(master,self.font_family,self.font_size,self.weight,self.slant,self.overstrike,self.underline))
  self.cursor=kwargs.get("cursor")
  self.takefocus=bols(kwargs.get("takefocus"))
  self.borderwidth=num0(kwargs.get("bd"),1)
  self.relief=kwargs.get("relief") if kwargs.get("relief") in relief_list else "flat"
  self.padx=num0(kwargs.get("padx"))
  self.pady=num0(kwargs.get("pady"))
  self.highlightthickness=num0(kwargs.get("highlightthickness"))
  self.highlightcolor=parsecolor(kwargs.get("highlightfg"))
  self.highlightbackground=parsecolor(kwargs.get("highlightbg"))
  self.title=kwargs.get("title","frame")
  self.labelanchor=kwargs.get("labelanchor","nw")
  self.size=wi._size(kwargs)
  self.width=self.size[0]
  self.height=self.size[1]
  super().__init__(master,takefocus=self.takefocus,highlightcolor=self.highlightcolor,highlightbackground=self.highlightbackground,highlightthickness=self.highlightthickness,pady=self.pady,padx=self.padx,relief=self.relief,cursor=self.cursor,labelanchor=self.labelanchor,text=self.title,font=self.font,bg=self.bg,fg=self.fg)
 def _delta(self):self.destroy()
class Column(tk.Frame):
 def __init__(self,master,kwargs):
  self.back_bg=kwargs.get("back_bg")
  self.bg=parsecolor(kwargs.get("bg",self.back_bg or THEMES["bg1"]))
  self.cursor=kwargs.get("cursor")
  self.takefocus=bols(kwargs.get("takefocus"))
  self.borderwidth=num0(kwargs.get("bd"))
  self.relief=kwargs.get("relief") if kwargs.get("relief") in relief_list else "flat"
  self.padx=num0(kwargs.get("padx"))
  self.pady=num0(kwargs.get("pady"))
  self.highlightthickness=num0(kwargs.get("highlightthickness"))
  self.highlightcolor=parsecolor(kwargs.get("highlightfg"))
  self.highlightbackground=parsecolor(kwargs.get("highlightbg"))
  self.size=wi._size(kwargs)
  self.width=self.size[0]
  self.height=self.size[1]
  super().__init__(master,takefocus=self.takefocus,highlightcolor=self.highlightcolor,highlightbackground=self.highlightbackground,highlightthickness=self.highlightthickness,pady=self.pady,padx=self.padx,relief=self.relief,cursor=self.cursor,bg=self.bg)
 def _delta(self):self.destroy()
class Tab(tk.Frame):
 def __init__(self,master,kwargs):
  super().__init__(master)
  self.back_bg=kwargs.get("back_bg")
  self.bg=parsecolor(kwargs.get("bg",self.back_bg or THEMES["bg1"]))
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.underline=False if kwargs.get("underline","normal")=="normal" else True
  self.weight=kwargs.get("weight") if kwargs.get("weight") in ["normal","bold"] else "normal"
  self.slant=kwargs.get("slant") if kwargs.get("slant") in ["roman","italic"] else "roman"
  self.overstrike=False if kwargs.get("overstrike","normal")=="normal" else True
  self.font_family=kwargs.get("font_family","Meiryo")
  self.font_size=num0(kwargs.get("font_size"),14)
  self.font=kwargs.get("font",fonts(master,self.font_family,self.font_size,self.weight,self.slant,self.overstrike,self.underline))
  self.justify=kwargs.get("justify") if kwargs.get("justify") in ["right","center","left"] else "left"
  self.wraplength=num0(kwargs.get("wraplength"))
  self.cursor=kwargs.get("cursor")
  self.takefocus=bols(kwargs.get("takefocus"))
  self.borderwidth=num0(kwargs.get("bd"))
  self.relief=kwargs.get("relief") if kwargs.get("relief") in relief_list else "flat"
  self.padx=num0(kwargs.get("padx"))
  self.pady=num0(kwargs.get("pady"))
  self.anchor=kwargs.get("anchor","w") if get_dict(anchor_dict,kwargs.get("anchor","right"))[1] in anchor_list else "w"
  self.activeforeground=parsecolor(kwargs.get("activefg"))
  self.activebackground=parsecolor(kwargs.get("activebg"))
  self.highlightthickness=num0(kwargs.get("highlightthickness"))
  self.highlightcolor=parsecolor(kwargs.get("highlightfg"))
  self.highlightbackground=parsecolor(kwargs.get("highlightbg"))
  style=ttk.Style()
  self.stylename=f"Custom{kwargs.get("count")}.TNotebook"
  style.theme_use("default")
  style.configure(self.stylename,background=self.back_bg)
  style.configure(f"{self.stylename}.Tab",background=self.bg,foreground=self.fg,font=self.font)
  style.map(f"{self.stylename}.Tab",background=[("selected",("#cccccc"))])
  self.frames=[]
  self.nb=ttk.Notebook(self,takefocus=self.takefocus,style=self.stylename)
  self.nb.pack(fill="both",expand=True)
 def _delta(self):self.nb.destroy()
 def add_tab(self,title,frame):
  self.nb.add(frame,text=title)
  self.frames.append(frame)
 def select_tab(self,index):
  try:self.nb.select(index)
  except Exception as e:print("タブ選択エラー:",e)
 def get_current_tab(self):
  try:return self.nb.tab(self.nb.select(),"text")
  except:return None
class Calendars(tkc.Calendar):
 def __init__(self,master,kwargs):
  self.back_bg=kwargs.get("back_bg")
  self.bg=parsecolor(kwargs.get("bg",self.back_bg or THEMES["bg1"]))
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.underline=False if kwargs.get("underline","normal")=="normal" else True
  self.weight=kwargs.get("weight") if kwargs.get("weight") in ["normal","bold"] else "normal"
  self.slant=kwargs.get("slant") if kwargs.get("slant") in ["roman","italic"] else "roman"
  self.overstrike=False if kwargs.get("overstrike","normal")=="normal" else True
  self.font_family=kwargs.get("font_family","Meiryo")
  self.font_size=num0(kwargs.get("font_size"),10)
  self.font=kwargs.get("font",fonts(master,self.font_family,self.font_size,self.weight,self.slant,self.overstrike,self.underline))
  self.justify=kwargs.get("justify") if kwargs.get("justify") in ["right","center","left"] else "left"
  self.wraplength=num0(kwargs.get("wraplength"))
  self.cursor=kwargs.get("cursor")
  self.borderwidth=num0(kwargs.get("bd"))
  self.relief=kwargs.get("relief") if kwargs.get("relief") in relief_list else "flat"
  self.padx=num0(kwargs.get("padx"))
  self.pady=num0(kwargs.get("pady"))
  self.anchor=kwargs.get("anchor","w") if get_dict(anchor_dict,kwargs.get("anchor","right"))[1] in anchor_list else "w"
  self.activeforeground=parsecolor(kwargs.get("activefg"))
  self.activebackground=parsecolor(kwargs.get("activebg"))
  self.highlightthickness=num0(kwargs.get("highlightthickness"))
  self.highlightcolor=parsecolor(kwargs.get("highlightfg"))
  self.highlightbackground=parsecolor(kwargs.get("highlightbg"))
  self.dates=kwargs.get("date") if kwargs.get("date") and type(kwargs.get("date"))==datetime else date.today()
  self.year=self.dates.year
  self.month=self.dates.month
  self.day=self.dates.day
  self.showweek=bols(kwargs.get("showweek",False),False)
  self.selectmode=kwargs.get("selectmode") if kwargs.get("selectmode") in ["none","day"] else "day"
  self.format=kwargs.get("format") if formatfunc(kwargs.get("format",None)) else fotmat_list["format0"]
  self.headersbackground=parsecolor(kwargs.get("headersbg","gray70"))
  self.headersforeground=parsecolor(kwargs.get("headersfg","black"))
  self.othermonthbackground=parsecolor(kwargs.get("othermonthbg","gray93"))
  self.othermonthforeground=parsecolor(kwargs.get("othermonthfg","gray45"))
  self.weekendbackground=parsecolor(kwargs.get("weekendbg","gray80"))
  self.weekendforeground=parsecolor(kwargs.get("weekendfg","gray30"))
  self.locale=kwargs.get("locale","ja_JP")
  self.firstweekday=kwargs.get("firstweekday","sunday")
  super().__init__(master,firstweekday=self.firstweekday,locale=self.locale,weekendforeground=self.weekendforeground,weekendbackground=self.weekendbackground,othermonthforeground=self.othermonthforeground,othermonthbackground=self.othermonthbackground,headersbackground=self.headersbackground,headersforeground=self.headersforeground,selectmode=self.selectmode,year=self.year,month=self.month,day=self.day,font=self.font,showweeknumbers=self.showweek,date_pattern=self.format)
 def move_date(self,year=None,month=None,day=None):
  now=datetime.date(year,month,day)
  self.selection_set(now)
  self.configure(year=year,month=month)
 def move_today(self):
  now=datetime.today()
  self.move_date(year=now.year,month=now.month,day=now.day)
 def move_select(self):
  selects=self.get_select()
  self.selection_set(selects)
  self.configure(year=selects.year,month=selects.month)
 def get_select(self):return self.selection_get()
 def get_date(self):return self.get_date()
 def select_clear(self):return self.selection_clear()
 def nowdate_show(self):return self.get_displayed_month()
 def get_bg(self):return self.bg
 def set_bg(self,nbg):
  if nbg and isinstance(nbg,str):
   self.bg=nbg
   self.config(bg=nbg)
 def get_fg(self):return self.fg
 def set_fg(self,nfg):
  if nfg and isinstance(nfg,str):
   self.fg=nfg
   self.config(fg=nfg)
 def get_font(self):return self.font
 def set_font(self,nfont):
  if nfont and isinstance(nfont,tuple):
   self.font=nfont
   self.config(font=nfont)
class InputDate(tkc.DateEntry):
 def __init__(self,master,kwargs):
  self.showweek=bols(kwargs.get("showweek"),False)
  self.selectmode=kwargs.get("selectmode") if kwargs.get("selectmode") in ["none","day"] else "day"
  self.locale=kwargs.get("locale","ja_JP")
  self.states=kwargs.get("state") if kwargs.get("state") in ["normal","readonly","disabled"] else "normal"
  self.format=kwargs.get("format") if formatfunc(kwargs.get("format",None)) else fotmat_list["format0"]
  self.firstweekday=kwargs.get("firstweekday","sunday")
  self.dates=kwargs.get("date") if kwargs.get("date") and type(kwargs.get("date"))==datetime else date.today()
  self.year=self.dates.year
  self.month=self.dates.month
  self.day=self.dates.day
  self.back_bg=kwargs.get("back_bg")
  self.bg=parsecolor(kwargs.get("bg",self.back_bg or THEMES["bg1"]))
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.headersbackground=parsecolor(kwargs.get("headersbg","gray70"))
  self.headersforeground=parsecolor(kwargs.get("headersfg","black"))
  self.othermonthbackground=parsecolor(kwargs.get("othermonthbg","gray93"))
  self.othermonthforeground=parsecolor(kwargs.get("othermonthfg","gray45"))
  self.normalbg=parsecolor(kwargs.get("normalbg","gray93"))
  self.normalfg=parsecolor(kwargs.get("normalfg","gray45"))
  self.weekendbackground=parsecolor(kwargs.get("weekendbg","gray80"))
  self.weekendforeground=parsecolor(kwargs.get("weekendfg","gray30"))
  super().__init__(master,weekendbackground=self.weekendbackground,weekendforeground=self.weekendforeground,normalforeground=self.normalfg,normalbackground=self.normalbg,headersforeground=self.headersforeground,headersbackground=self.headersbackground,bg=self.bg,fg=self.fg,state=self.states,locale=self.locale,date_pattern=self.format,firstweekday=self.firstweekday,day=self.day,month=self.month,year=self.year,selectmode=self.selectmode,showweeknumbers=self.showweek)
class Progressbar(ttk.Progressbar):
 def __init__(self,master,kwargs):
  self.cursor=kwargs.get("cursor")
  self.takefocus=bols(kwargs.get("takefocus"))
  self.value=num0(kwargs.get("value"))
  self.maximum=num0(kwargs.get("max"),100)
  self.length=num0(kwargs.get("length"),200)
  self.mode=kwargs.get("mode") if kwargs.get("mode") in ["determinate","indeterminate"] else "determinate"
  self.orient=kwargs.get("orient") if kwargs.get("orient") in ["horizontal","vertical"] else "horizontal"
  self.fg=parsecolor(kwargs.get("fg",THEMES["fg1"]))
  self.back_bg=kwargs.get("back_bg")
  self.bg=parsecolor(kwargs.get("bg",self.back_bg or THEMES["bg1"]))
  self.funcs=kwargs.get("function")
  style=ttk.Style()
  self.style_name=f"Custom{kwargs.get("count")}.Horizontal.TProgressbar" if self.orient=="horizontal" else f"Custom{kwargs.get("count")}.Vertical.TProgressbar"
  style.theme_use("default")
  style.layout(self.style_name,style.layout("Horizontal.TProgressbar" if self.orient=="horizontal" else "Vertical.TProgressbar"))
  style.configure(self.style_name,background=self.fg,troughcolor=self.bg,thickness=20)
  super().__init__(master,takefocus=self.takefocus,cursor=self.cursor,orient=self.orient,length=self.length,mode=self.mode,style=self.style_name,maximum=self.maximum)
  self._set(self.value)
  if self.funcs:self.bind("<Button-1>",lambda e,f=self.funcs:wi._exec_funcs(f))
 def get_max(self):return self.maximum
 def _set(self,val):
  try:self["value"]=val
  except:self["value"]=0
 def _get(self):
  try:return self["value"]
  except:return
 def _start(self):
  try:self.start()
  except:pass
 def _stop(self):
  try:self.stop()
  except:pass
 def _delta(self):self.destroy()
# 自作　既存にはないウィジェット
class Link(tk.Label):
 def __init__(self,master,kwargs):
  self.fg=parsecolor(kwargs.get("fg",THEMES["link"]))
  self.back_bg=kwargs.get("back_bg")
  self.bg=parsecolor(kwargs.get("bg",self.back_bg or THEMES["bg1"]))
  self.underline=True if kwargs.get("underline","normal")=="normal" else False
  self.weight=kwargs.get("weight") if kwargs.get("weight") in ["normal","bold"] else "normal"
  self.slant=kwargs.get("slant") if kwargs.get("slant") in ["roman","italic"] else "roman"
  self.overstrike=False if kwargs.get("overstrike","normal")=="normal" else True
  self.font_family=kwargs.get("font_family","Meiryo")
  self.font_size=num0(kwargs.get("font_size"),14)
  self.font=kwargs.get("font",fonts(master,self.font_family,self.font_size,self.weight,self.slant,self.overstrike,self.underline))
  self.justify=kwargs.get("justify") if kwargs.get("justify") in ["right","center","left"] else "left"
  self.wraplength=num0(kwargs.get("wraplength"))
  self.cursor=kwargs.get("cursor")
  self.takefocus=bols(kwargs.get("takefocus"))
  self.borderwidth=num0(kwargs.get("bd"))
  self.relief=kwargs.get("relief") if kwargs.get("relief") in relief_list else "flat"
  self.padx=num0(kwargs.get("padx"))
  self.pady=num0(kwargs.get("pady"))
  self.anchor=kwargs.get("anchor","w") if get_dict(anchor_dict,kwargs.get("anchor","right"))[1] in anchor_list else "w"
  self.activeforeground=parsecolor(kwargs.get("activefg"))
  self.activebackground=parsecolor(kwargs.get("activebg"))
  self.highlightthickness=num0(kwargs.get("highlightthickness"))
  self.highlightcolor=parsecolor(kwargs.get("highlightfg"))
  self.highlightbackground=parsecolor(kwargs.get("highlightbg"))
  self.link_url=kwargs.get("link")
  self.linkchecks(self.link_url)
  txt=kwargs.get("text")
  if (self.link_url and self.link_url!="") and (txt and txt!=""):self.text=txt
  elif (self.link_url and self.link_url!="") and (not txt or txt==""):self.text=self.link_url
  else:self.text=""
  self.size=wi._size(kwargs)
  self.width=self.size[0]
  self.height=self.size[1]
  super().__init__(master,takefocus=self.takefocus,highlightcolor=self.highlightcolor,highlightbackground=self.highlightbackground,highlightthickness=self.highlightthickness,activeforeground=self.activeforeground,activebackground=self.activebackground,anchor=self.anchor,pady=self.pady,padx=self.padx,relief=self.relief,wraplength=self.wraplength,cursor=self.cursor,text=self.text,bg=self.bg,fg=self.fg,font=self.font,width=self.width,height=self.height,justify=self.justify)
  self.bind("<Button-1>",self._link)
 def _delta(self):self.destroy()
 def _link(self,event):
  if self.links==True and self.link_url and self.link_url!="":
   try:webbrowser.open(self.link_url)
   except Exception as e:print(f"error:{e}")
  elif self.links==False:print("error")
 def linkchecks(self,url):self.links=urlcheck(url)
 def get_link(self):return self.link_url
 def set_link(self,link):self.link_url=link
 def get_size(self):return (self.width,self.height)
 def get_text(self):return self.text
 def set_text(self,txt):
  if txt:
   self.text=txt
   self.config(text=txt)
 def get_bg(self):return self.bg
 def set_bg(self,nbg):
  if nbg and isinstance(nbg,str):
   self.bg=nbg
   self.config(bg=nbg)
 def get_fg(self):return self.fg
 def set_fg(self,nfg):
  if nfg and isinstance(nfg,str):
   self.fg=nfg
   self.config(fg=nfg)
 def get_font(self):return self.font
 def set_font(self,nfont):
  if nfont and isinstance(nfont,tuple):
   self.font=nfont
   self.config(font=nfont)
class Images(tk.Label):
 def __init__(self,master,kwargs):
  self.master=master
  self.path=Path(kwargs.get("path"))
  self.size=self._img_size(kwargs,self.path)
  self.takefocus=bols(kwargs.get("takefocus"))
  self.width=self.size[0]
  self.height=self.size[1]
  self.image_ref=None
  self.image=None
  self._image_set()
 def _img_size(self,kwargs,path):
  size=list(kwargs.get("size",(100,100)))
  if size and isinstance(size,tuple) and len(size)==2:
   width,height=nums(kwargs.get("width",None)),nums(kwargs.get("height",None))
   return (width if size[0]==None and width!=None else size[0],height if size[1]==None and height!=None else size[1])
  try:
   with Image.open(path) as img:return img.size
  except:return (100,100)
 def _image_set(self,path=None):
  try:
   if path==None:path=self.path
   img=Image.open(path)
   if self.size and isinstance(self.size,tuple):img=img.resize(self.size)
   self.image_ref=ImageTk.PhotoImage(img)
   super().__init__(self.master,takefocus=self.takefocus,image=self.image_ref,height=self.height,width=self.width)
   self.image=self.image_ref
   self.path=path
  except:
   e_txt=f"error:{self.path}"
   super().__init__(self.master,takefocus=self.takefocus,text=e_txt,height=1,width=len(e_txt))
 def _delta(self):self.destroy()
 def clear(self):
  self.image=None
  self.image_ref=None
  self.config(image="",text="")
 def get_path(self):return self.path
 def get_ex(self):return os.path.split(self.path)[1].split(".",1)[1]