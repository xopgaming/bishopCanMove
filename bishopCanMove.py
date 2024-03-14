#　インプット形式はスタート位置のｘ軸、ｙ軸、目標点のｘ軸、ｙ軸、の順番で半角英数字を半角スペースで区切った４つの数字
#　例：1 8 2 5

pos = list(map(int, input("４つの半角英数字を半角スペースで区切って入力してください: ").split(" ")))

dx = abs(pos[0]-pos[2])
dy = abs(pos[1]-pos[3])
if dx == dy:
    print("YES")
else:
    print("NO")