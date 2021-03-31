import copy
import random

data = {}
point = 0
def add(ja,en):
    data[ja] = en

add("うつくしい","beautiful")
add("ハンバーガー","hamburger")
add("アメリカ","America")
add("オーストラリア","Australia")
add("私も","also")

fast_data_len = int(len(list(data.keys())))

while fast_data_len != point:
    data_len = int(len(list(data.keys())))
    nm = random.randint(0,data_len-1)
    ja = list(data.keys())[nm]

    en = data[ja]
    
    print("{0}を英語にして" .format(ja))

    user = input().rstrip()

    if en == user:
        point += 1
        print("正解")
        del data[ja]

    else:
        print("こたえは{0}".format(en))

print("終了")