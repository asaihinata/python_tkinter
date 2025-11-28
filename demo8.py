from manyfunction import *
clear()
from mylibral import *
layout=[
[sgg.Button(text="Popup(情報)",function=lambda:print(sgg.Popup(message="メッセージ")))],
[sgg.Button(text="Popupwarning(注意)",function=lambda:print(sgg.Popupwarning(message="メッセージ")))],
[sgg.Button(text="Popupwarningyesno(注意)",function=lambda:print(sgg.Popupwarningyesno(message="メッセージ")))],
[sgg.Button(text="Popuperror(エラー)",function=lambda:print(sgg.Popuperror(message="メッセージ")))],
[sgg.Button(text="Popupyesno(bool型を返す)",function=lambda:print(sgg.Popupyesno(message="メッセージ")))],
[sgg.Button(text="Popupokcancel(bool型を返す)",function=lambda:print(sgg.Popupokcancel(message="メッセージ")))],
[sgg.Button(text="Popupquestion(YesかNoを返す)",function=lambda:print(sgg.Popupquestion(message="メッセージ")))],
[sgg.Button(text="Popupyesnocancel(bool型とNoneを返す)",function=lambda:print(sgg.Popupyesnocancel(message="メッセージ")))],
[sgg.Button(text="Popuptrycancel(bool型を返す)",function=lambda:print(sgg.Popuptrycancel(message="メッセージ")))]
]
win=sgg.window(title="mylibral ウィジェット デモ",layout=layout,scroll_x=True,scroll_y=True,maxmine=True)
win.run()