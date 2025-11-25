from mylibral import *
tree_values=[
"あ行",["あ","い","う","え","お"],
"か行",["か","き","く","け","こ"],
"が行",["が","ぎ","ぐ","げ","ご"]
]
layout=[
[sgg.Text(text="表(縦見出しあり)")],
[sgg.Table(header=["列A","列B"],values=[["r1c1","r1c2"],["r2c1","r2c2"]],rowheader=["aa","bb"],key="table1")],
[sgg.Text(text="表(縦見出しなし)")],
[sgg.Table(header=["列A","列B"],values=[["r1c1","r1c2"],["r2c1","r2c2"]],key="table2")],
[sgg.Text(text="ツリー")],
[sgg.Tree(values=tree_values,header=["あ","い","う","え","お"],key="tree1")]
]
win=sgg.window(title="mylibral ウィジェット デモ",layout=layout,scroll_x=True,scroll_y=True,maxmine=True)
win.run()