import sklearn.datasets
import sklearn.svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import PIL.Image
import numpy
from tkinter import filedialog as fd
import tkinter as tk
import PIL.ImageTk

root=tk.Tk()
root.geometry('400x350')
imageLabel=tk.Label()
txtLabel=tk.Label()

def image2data(filename):
    image=PIL.Image.open(filename).convert('L').resize((8,8),PIL.Image.ANTIALIAS)
    #画像を開いて、グレースケール8x8に変換、
    #中間色を段階的に配置してぼかすことで自然な画像になるようにしている(アンチエイリアス)
    numlist=numpy.asarray(image,dtype=float)#画像を8ｘ8のリストに変換する
    numlist=numpy.floor(16-16*(numlist/256))#普通の画像は濃⇒薄(255-0)なので、
    #濃⇒薄(0-16)になるように変換する
    numlist=numlist.flatten()
    return numlist

def predict(data):
    digits=sklearn.datasets.load_digits()#教師データは8ｘ8のリスト
    X,y=digits.data,digits.target
    Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,random_state=0)
    model=sklearn.svm.SVC(kernel='rbf',gamma=0.001)#学習結果を受ける箱
    model.fit(Xtrain,ytrain)#データとターゲットを紐づけして学習する
    pred=model.predict(Xtest)
    score=accuracy_score(ytest,pred)
    print('正解率＝{}%'.format(score*100))
    n=model.predict([data])#学習結果を用いてdataを判別する
    print('予測＝',n)
    return n

def dispPhoto(path):#画像をラベルに表示する関数
    image=PIL.Image.open(path).convert('L').resize((32,32)).resize((300,300))
     #画像ファイルを縮尺変更して読み込む
    imageData=PIL.ImageTk.PhotoImage(image) #読み込んだ画像をtkで対応できる型にする
    imageLabel.configure(image=imageData) #tk画面のラベルを修正する
    imageLabel.image=imageData #tk画面のラベルに画像を表示する

def displabel(n):#テキストをラベルに表示する関数
    txtLabel.configure(text=('読み込んだ画像は{}です'.format(str(n))))

def openFile():#ボタンが押された後に実行される関数
    fpath=fd.askopenfilename() #ファイルダイアログを開いてファイルを選択する
    if fpath:
        data=image2data(fpath)#選択されたファイルの画像を数値リストに変換する
        n=predict(data)#数値リストから数字を予測する
        dispPhoto(fpath)#読み込んだ画像をラベルに表示する
        displabel(n)#予想された数字をラベルに表示する





button=tk.Button(text='ファイルを開く',command=openFile)
button.pack()
imageLabel.pack()
txtLabel.pack()
tk.mainloop()