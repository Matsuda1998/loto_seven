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
    print(recent_result)#直近ｎ回の当選番号のリスト
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

def int_column(n,m):
    """第ｎ回の第ｍ数字の値とその第ｍ数字の列における出現間隔値を調べる
    先頭数字の評価に使う"""
    n_result=total_result[n][m]
    m_column=[]#第ｍ数字のリスト
    for i in range(1,n+1):
        m_column.append(total_result[i][m])
    m_column.reverse()#新しいほうからへ並び替え
    m_column[0]=None#インデックス０は第ｎ回そのものなのでＮＯＮＥで埋める
    if n_result in m_column:
        int_n=m_column.index(n_result)#数字がなかった時の処理考える
    else :
        int_n=0
    print(n_result)
    print(m_column)
    print(int_n)
int_column(7,2)

def int_all(n,m):
    """第ｎ回の第ｍ数字の値とすべての位置での出現間隔値を調べる"""
    n_result=total_result[n][m]
    sub_total_result=total_result[:n]
    sub_reverse_result=reversed(sub_total_result)#新しいほうからへ並び替え
    sub_reverse_result=list(sub_reverse_result)#イデレータをリスト化
    int_n=0
    for i in range(n-1):
        if n_result in sub_reverse_result[i]:
            int_n=i+1
            break
    print(total_result)
    print(n_result)
    print(sub_reverse_result)
    print(int_n)
int_all(9,1)

def next_number(n,m):
    """第ｎ回の当選番号の第ｍ数字から次回にその第ｍ数字の列に
    出た数字を調べる"""
    n_result=total_result[n][m]
    appear=[None,[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],
            [8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],
            [15,0],[16,0],[17,0],[18,0],[19,0],[20,0],[21,0],
            [22,0],[23,0],[24,0],[25,0],[26,0],[27,0],[28,0],
            [29,0],[30,0],[31,0],[32,0],[33,0],[34,0],[35,0],
            [36,0],[37,0]]#1~37に出現回数を割り当てるためのリスト
    for i in range(1,len(total_result)-1):#len()-1:最新の結果は除く(次回はないため)
        if n_result == total_result[i][m]:
            next=total_result[i+1][m]
            appear[next][1]+=1
    appear.pop(0)
    appear.sort(key=lambda x: x[1],reverse=True)
    print(appear)
next_number(10,2)

def present_one_digit(n):
    """直近ｎ回の下一桁数字（０～９）とその位置（第ｍ数字として）を
    調べる"""
    m=n*-1
    recent_result=total_result[m:]
    print(recent_result)#直近ｎ回の当選番号のリスト
    recent_one_digit=[None]
    for j,val in enumerate(recent_result):
        str_line=[]
        for i in range(1,8):
            str_rize=str(val[i])#文字化
            str_rize=str_rize[-1]#下一桁を取り出す(最後のインデックス)
            str_line.append(str_rize)
        recent_one_digit.append(str_line)
        recent_one_digit[j+1].insert(0,None)
    print(recent_one_digit)

    checker=["0","1","2","3","4","5","6","7","8","9"]
    one_digit_posi=[None]
    for j in range(1,n+1):
        sub_posi=[["0"],["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"]]
        for i,val in enumerate(recent_one_digit[j]):
            for check in checker:
                if check == val:
                    sub_posi[checker.index(check)].append(i)
        one_digit_posi.append(sub_posi)
    print(one_digit_posi)
    return one_digit_posi

present_one_digit(2)

def sort_pre_one_digit(s):
    """関数present_one_digitで得られたリスト(引数)をソート、カット
    リストのようなミュータブルオブジェクトの場合、b=a(参照渡し)とやると
    b或いはaの変更が、a或いはbにも反映されてしまう。
    (文字列、タプルのようなイミュータブルは気にしないでＯＫ）
    なので関数を分ける。参考：https://snowtree-injune.com/2018/07/17/post-565/"""
    s.pop(0)
    for i in range(len(s)):
        s[i].sort(key=lambda x: len(x),reverse=True)
    print(s)

sort_pre_one_digit(present_one_digit(2))