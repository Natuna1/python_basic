"""
任意の行数および任意の列数での掛け算の結果が得られます
行数を入力してください: 4
列数を入力してください: 6
"""


X = int(input("行数を入力してください:"))
Y = int(input("列数を入力してください:"))

for attack in range(X):
    for jreceive in range(Y):
        print((attack + 1) * (jreceive + 1), end=" ")
    print()
