"""
3都府県のいくつかの駅名とある日の最高気温のデータを辞書として持っています
このデータを使って3つの問を満たす実装をしてください
"""


def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
        {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
        {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},
        {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
        {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
        {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},
        {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
        {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)
    X = 0
    total = len(weather_information)

    for r in range(0, total):
        temp = weather_information[r]["temperature"]
        X = X + temp

    average = X / total
    print(average)

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    for r in range(len(weather_information)):
        if weather_information[r]["prefecture"] == "大阪府":
            print(weather_information[r]["station"], end=",")

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    # if weather_information == "福岡県"
    # for r in range(7, 8)

    X = 0
    total = 0
    for r in range(0, 8):
        if weather_information[r]["prefecture"] == "福岡県":
            temp_fukuoka = weather_information[r]["temperature"]
            total += temp_fukuoka
            X = X + 1

    avetage = total / X
    print(avetage)


if __name__ == "__main__":
    main()
