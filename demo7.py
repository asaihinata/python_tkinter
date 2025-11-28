from manyfunction import *
clear()
from mylibral import *
menus=[
["ファイル",
["開く",
[["SubmenuのMenu"],"メニュー2",["メニュー2のMenu"],"メニュー3","メニュー4"],
"---",
{"label":"閉じる","function":lambda:win.root.quit()}
]
],
["ヘルプ",
[
{"label":"バージョン"}
]
]
]
layout=[
[sgg.Menu(list=menus,key="menus")],
[sgg.Text(text="メニューボタン")],
[sgg.Menubutton(list=menus)]
]
win=sgg.window(title="mylibral ウィジェット デモ",layout=layout,scroll_x=True,scroll_y=True,maxmine=True)
win.run()