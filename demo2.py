from mylibral import *
# 配列
list_val=["赤","青","黄"]
list_val2=["赤","青","黄","赤","青","黄","赤","青","黄","赤","青","黄"]
layout=[
[sgg.Text(text="入力欄->"),sgg.Input(text="入力欄")],
[sgg.Text(text="パスワード入力->"),sgg.Input(show="※")],
[sgg.Text(text="複数行表示できる入力欄")],
[sgg.Multiline(text="複数行表示可能の入力欄",key="multiline1"),sgg.Multiline(text=["配列でも","表示可能"],key="multiline2")],
[sgg.Text(text="赤に選択されたリストボックス")],
[sgg.Listbox(values=list_val,select=0)],
[sgg.Combobox(values=list_val,default="好きな色を選ぼう!")],
[sgg.Text(text="数値入力")],
[sgg.InputNumber(key="number")],
[sgg.Text(text="スクロールを追加する")],
[
sgg.Input(text="こんにちは。初めまして。",width=10,scroll_x=True),
sgg.Multiline(text=[1,2,3,4,5,6,7,8,9,10],size=(10,5),scroll_x=True,scroll_y=True,key="multiline1"),
sgg.Listbox(values=list_val2,select=0,scroll_y=True)
]
]
win=sgg.window(title="mylibral ウィジェット デモ",layout=layout,scroll_x=True,scroll_y=True,maxmine=True)
win.run()