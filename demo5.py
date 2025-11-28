from mylibral import *
def progress_start():win.get("prigress")._start()
layout=[
[sgg.Text(text="カレンダー")],
[sgg.Calendars(key="cal")],
[sgg.Text(text="日付を選択する")],
[sgg.InputDate(key="inputcal")],
[sgg.Text(text="スライダー")],
[sgg.Slidebar(value=20)],
[sgg.Text(text="プログレスバー")],
[sgg.Progressbar(key="prigress")]
]
win=sgg.window(title="mylibral ウィジェット デモ",layout=layout,scroll_x=True,scroll_y=True,maxmine=True,
load=[progress_start]# ウィンドウ読み込み時実行
)
win.run()