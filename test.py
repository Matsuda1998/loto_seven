import re


total_result=[None,(None,7,10,12,17,23,28,34),(None,20,24,29,31,33,34,35),
            (None,2,7,8,11,14,23,31),(None,12,13,22,23,24,28,29),(None,1,3,4,5,16,21,28),
            (None,5,15,19,23,30,34,35),(None,1,3,5,7,27,29,33),(None,2,21,28,29,30,32,36),
            (None,3,4,15,23,27,30,36),(None,1,2,3,6,24,28,30)]

def up_result() :
    """変数total_result(今までの当選数字)を更新する。本数字のみ
    """
    n=len(total_result)
    print("第 {} 回の結果を入力します。中止は'q'".format(n),"\n")
    result=[None]
    for i in range(1,8):
        m=input("第 {} 数字を入力してください".format(i))
        if m == "q":
            break
        result.append(m)
    if len(result) == 8:
        result=tuple(result)
        total_result.append(result)


up_result()
#更新したtotal_resultをファイルに書き込まなきゃ。
#ifループの中で1~37以外を入力したときはエラーを出す(continue?)
#数字を昇順に並べ替える必要あり


class Anal_column:
    """直近ｎ回の第ｍ数字をいろいろ解析する
    """
    def __init__(self,n,m):
       self.n=n*-1
       self.m=m
    
    def appear_column(self):
        """出現頻度を調べる"""
        column=[]
        for i in range(self.n,0):
            column.append(total_result[i])

def appear_column(n,m):
    """直近ｎ回の第ｍ数字の出現頻度を調べる
    先頭数字の評価に使う"""
    n=n*(-1)
    column=[]#直近ｎ回の第ｍ数字のリスト
    for i in range(n,0):
        column.append(total_result[i][m])
    print(column)
    appear=[None,[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],
            [8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],
            [15,0],[16,0],[17,0],[18,0],[19,0],[20,0],[21,0],
            [22,0],[23,0],[24,0],[25,0],[26,0],[27,0],[28,0],
            [29,0],[30,0],[31,0],[32,0],[33,0],[34,0],[35,0],
            [36,0],[37,0]]#1~37に出現回数を割り当てるためのリスト
    for val in column:
        appear[val][1] += 1
    appear.pop(0)#Noneが混在してるとsortできない
    #無名関数lambdaの引数xはappearの各要素、戻り値:各要素のindex１でソートする
    appear.sort(key=lambda x: x[1],reverse=True)
    print(appear)

appear_column(10,1)

def appear_all(n):
    """直近ｎ回のすべての位置での出現頻度を調べる"""
    n=n*-1
    recent_result=total_result[n:]
    print(recent_result)
    appear=[None,[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],
            [8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],
            [15,0],[16,0],[17,0],[18,0],[19,0],[20,0],[21,0],
            [22,0],[23,0],[24,0],[25,0],[26,0],[27,0],[28,0],
            [29,0],[30,0],[31,0],[32,0],[33,0],[34,0],[35,0],
            [36,0],[37,0]]#1~37に出現回数を割り当てるためのリスト
    for val in recent_result:
        for i in range(1,8):
            appear[val[i]][1]+=1
    appear.pop(0)
    appear.sort(key=lambda x: x[1],reverse=True)
    print(appear)
appear_all(2)
   