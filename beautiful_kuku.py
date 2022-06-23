"""
下記のような出力が得られる beautiful_kuku.py を実装してください
きれいに整っているので見やすくなっています
式が表示されている
結果の桁数が違う場合は適切な量の半角スペースを挿入しているので、みやすい
※結果が3桁の場合は崩れてもOKです

print(f"{i}x{j}={i*j:2}", end=" ")
"""

X = int(input("行数を入力してください:"))
Y = int(input("列数を入力してください:"))

for attack in range(1, X + 1):
    for jreceive in range(1, Y + 1):
        print(f"{attack} x {jreceive} = {attack * jreceive:2d} |", end=" ")
    print()
