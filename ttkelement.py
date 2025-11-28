import tkinter as tk,webbrowser
from manyfunction import *
from tkinter import ttk
from widgets import __Widget__,fonts
class TButton(ttk.Button):
 def __init__(self,master,kwargs):
  self.funcs=kwargs.get("function")
  self.text=kwargs.get("text","")
  self.size=__Widget__._size(kwargs)
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
  super().__init__(master,takefocus=self.takefocus,highlightcolor=self.highlightcolor,highlightbackground=self.highlightbackground,highlightthickness=self.highlightthickness,activeforeground=self.activeforeground,activebackground=self.activebackground,anchor=self.anchor,pady=self.pady,padx=self.padx,relief=self.relief,wraplength=self.wraplength,cursor=self.cursor,text=self.text,bg=self.bg,fg=self.fg,font=self.font,command=lambda f=self.funcs:__Widget__._exec_funcs(f),width=self.width,height=self.height)
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
