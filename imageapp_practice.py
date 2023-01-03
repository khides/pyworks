import tkinter as tk#ウィンドウを表示するモジュール
from tkinter import filedialog as fd#ファイルダイアログを使うモジュール
import PIL.Image#画像を扱うモジュール
import PIL.ImageTk##tkinterで作った画面上に画像を表示させるモジュール

root=tk.Tk()
root.geometry('400x350')
imageLabel=tk.Label()


###ボタンを押したときの命令を作る###############################

def dispPhoto(path):
    image=PIL.Image.open(path).convert('L').resize((32,32)).resize((300,300)) 
    #画像ファイルを縮尺変更して読み込む
    imageData=PIL.ImageTk.PhotoImage(image)
    #読み込んだ画像をtkで対応できる型にする
    imageLabel.configure(image=imageData) #tk画面のラベルを修正する
    imageLabel.image=imageData #tk画面のラベルに画像を表示する

def openFile():
    fpath=fd.askopenfilename()#ファイルダイアログを開いてファイルを選択する
    if fpath:
        dispPhoto(fpath)

###############################################################



button=tk.Button(text='ファイルを開く',command=openFile)
button.pack()
imageLabel.pack()
tk.mainloop()
