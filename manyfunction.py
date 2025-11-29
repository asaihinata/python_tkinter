import re,os,platform,requests,matplotlib.colors as mcolors
from typing import Optional
def clear():os.system("cls" if platform.system()=="Windows" else "clear")
# 文字列(str)
def strs(txt,other=""):return txt if isinstance(txt,str) else other
# 数値(int,float)
def nums(val,other=None):return val if isinstance(val,(int,float)) else other
def num1(val=0,mins=1):return val if isinstance(val,(int,float)) and 1<val else mins# 1以下ならminsを返す
def num1s(val=0,mins=1):return val if isinstance(val,(int,float)) and 1<=val else mins# 1以下ならminsを返す
def num0(val=0,mins=0):return val if isinstance(val,(int,float)) and 0<val else mins# 0以下ならminsを返す
def num0s(val=0,mins=0):return val if isinstance(val,(int,float)) and 0<=val else mins# 0以下ならminsを返す
def range_num(val,mins=None,maxs=None,others=None):# 範囲化を調べる
 if(mins is not None and val<mins):return others
 if(maxs is not None and val>maxs):return others
 return val
# 真偽(bool)
def bols(j,o=True):return j if isinstance(j,bool) else o
# 配列
def litus(lists,other=[]):return lists if isinstance(lists,(list,tuple)) else other
def lis(lists,other=[]):return lists if isinstance(lists,list) else other
def tus(lists,other=()):return lists if isinstance(lists,tuple) else other
# 条件分岐
def ifs(val=None,tr=True,fal=False):return tr if val else fal
# その他
# 色
def parsecolor(value):# 色変換
 if value==None:return None
 value=value.lower()
 if isinstance(value,str):
  v=value.strip()
  if v.startswith("rgb"):
   nums=re.findall(r"\d+",v)
   if len(nums)==3:
    r,g,b=[int(x)for x in nums]
    return f"#{r:02x}{g:02x}{b:02x}"
  if re.match(r"^#[0-9a-fA-F]{6}$",v):return v
 return value
def validate_color(s=None):
 if s==None and not isinstance(s,str):return None
 t=s.strip()
 try:
  mcolors.to_rgba(t)
  return t
 except:pass
 m=re.fullmatch(r'rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)',t,flags=re.IGNORECASE)
 if m:
  r,g,b=map(int,m.groups())
  if 0<=r<=255 and 0<=g<=255 and 0<=b<=255:return t
 m=re.fullmatch(r'rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*([0-9]*\.?[0-9]+)\s*\)',t,flags=re.IGNORECASE)
 if m:
  r,g,b=map(int,m.groups()[:3])
  if 0<=r<=255 and 0<=g<=255 and 0<=b<=255 and 0<=float(m.group(4))<=1:return t
 return None
def markers(m):return m if m in marker_list else "o"
def lines(m):return m if m in linestyle_list else "-"
def formatfunc(val=None):
 if val==None:return None
 for i in fotmat_list:
  if val in [i,fotmat_list[i]]:return i
def get_dict(dicts,val,ret=None):
 if not (type(dicts)!=dict or not isinstance(val,(int,float,str))):
  for key,item in dicts.items():
   if val in [key,item]:return(key,item)
 return ret
def urlcheck(link):
 try:return True if requests.get(link).status_code==200 else False
 except:return False
# マーカー・アイコン
# ポップアップ用
icon_list=["error","info","question","warning"]
# 日付日時のフォーマット
fotmat_list={"format0":"yyyy/mm/dd","format1":"yyyy-mm-dd","format2":"dd/mm/yyyy","format3":"dd-mm-yyyy"}
# テーマカラーの設定
THEMES={
"scroll_bg":"#a6b2be",
"link":"#0000ee",
"link_visited":"#551a8b",
"fg1":"#000000",
"bg1":"#64778d",# 既存背景
"bg2":"#e0e0e0",# ボタン背景
"bg3":"#f9f9f9",# Inputウィジェットなどの記入背景
"bg4":"#cccccc",# ヘッダー背景
"bg5":"#1967d2",# Listboxで要素が選択中でかつ選択中の要素の上にマウスがある
"bg6":"#ffffff",# グラフの背景
"font_family":"Meiryo",
"font_size":14,
"font":("Meiryo",14),
"button_font":("Meiryo",10),
"entry_font":("Meiryo",10),
"calendar_font":("Meiryo",10),
"size0":(20,1),
"size0":(20,5)
}
graph_color=["#4477AA","#EE7733","#228833","#AA66CC","#77AADD","#FFA94D","#55AA55","#CC3311","#CC99FF","#FF8888","#444444","#888888","#332288","#88ccee","#44aa99","#117733","#999933","#ddcc77","#cc6677","#882255","#aa4499","#dddddd"]
linestyle_list=["-","solid","--","dashed","-.","dashdot",":","dotted","none","None",""," "]
marker_list=[".",",","o","v","^","<",">","1","2","3","4","8","s","p","P","*","h","H","+","x","X","D","d","|","_",]
# ボーダー枠
relief_list=["raised","sunken","flat","ridge","solid","groove"]
# anchor
anchor_list=["center","n","s","ne","e","se","nw","w","sw"]
anchor_dict={"center":"center","top":"n","bottom":"s","lefttop":"ne","left":"e","leftbottom":"se","righttop":"nw","right":"w","rightbottom":"sw"}