from mylibral import *
# 実行する関数
def txtchange():
 win.get("txt1").set_text("!!!変わった!!!")
layout=[
[sgg.Text(text="Textウィジェット")],
[sgg.Text(text="keyがtxt1のTextウィジェット",key="txt1"),
sgg.Text(key="txt2",text="文字色が水色,背景色が赤色,\nサイズが30文字の幅で高さが3文字分の\nTextウィジェット",
bg="red",fg="aqua",size=(30,3))
],
[sgg.Button(text="ボタンウィジェット",key="btn1")],
[sgg.Text(text="keyがtxt1のTextのテキストを変えるボタン->"),
sgg.Button(text="!!変える!!",function=[txtchange],key="btn2")],
[sgg.Link(link="https://www.google.com/",text="googleのサイトを開く")],
[sgg.Images(path="img.png")],
[sgg.Text(text="↑画像表示(PGM,PPM,GIF,PNG,XBMでしか表示されない)")],
[sgg.Images(path="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg48GxlSXF_4b4XZmtOALPhe3mD5iREyN-Ks6Q2hdviWeDHOcG_AUOS3nn2i-E9g5jD1_7-2o9PZF5MUQEanceM7b07viAr9M6h4C7jDqGhKdF0LzHzn2IBS_A2Fvpv605wIRf9ohIPiv-HStNDjk8JdN2hU-0GTI-OsjRraMo1HnGkTALf6v7qBbHufj04/s400/pose_galpeace_schoolgirl.png")],
[sgg.Text(text="↑URLで指定された画像ファイルは読み取れない")]
]
win=sgg.window(
title="mylibral ウィジェット デモ",# ウィンドウのタイトルを決める
layout=layout,# ウィンドウにウィジェットを設置する
scroll_x=True,# x軸方向にスクロール設置 Falseが初期値でTrueでスクロール
scroll_y=True,# y軸方向にスクロール設置 Falseが初期値でTrueでスクロール
maxmine=True# ウィンドウ最大表示
)
win.run()