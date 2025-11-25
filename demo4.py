from mylibral import *
def files():sgg.Popup(message=win.get("file_load")._choose_pas())
def folders():sgg.Popup(message=win.get("folder_load")._choose_pas())
def colors():sgg.Popup(message=win.get("color_select")._choose_color())
layout=[
[sgg.Text(text="ファイルを選ぶ")],
[sgg.FileLoad(key="file_load")],
[sgg.Button(function=[files],text="選択したファイル")],
[sgg.Text(text="フォルダを選ぶ")],
[sgg.FolderLoad(key="folder_load")],
[sgg.Button(text="選択したフォルダ",function=[folders])],
[sgg.Text(text="色を選ぶ")],
[sgg.Colorbtn(key="color_select")],
[sgg.Button(text="選択した色",function=[colors])],
[sgg.Text(text="タブ")],
[sgg.Tab(tabs=[
["tab1",[[sgg.Text(text="tab1")]]],
["tab2",[[sgg.Text(text="tab2")]]]
],key="tabs1")]
]
win=sgg.window(title="mylibral ウィジェット デモ",layout=layout,scroll_x=True,scroll_y=True,maxmine=True)
win.run()