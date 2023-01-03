import sklearn.datasets

digits=sklearn.datasets.load_digits()

print('データの個数',len(digits.images))
print('画像のデータ',digits.images[0])#数字0の画像データ
print('何の数字か',digits.target[0])#0の教師データ
print(digits.data)

from matplotlib import pyplot as plt

for i in range(50):
    plt.subplot(5,10,i+1)#5ｘ10でグラフを複数描くうちのi+1番目を描く
    plt.axis('off')#軸線をなしにする
    plt.title(digits.target[i])
    im=plt.imshow(digits.images[i],cmap='Greys')
    #plt.colorbar(im)
plt.show()

