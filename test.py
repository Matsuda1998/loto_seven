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
        one_digit_posi.append(sub_posi)#インデックス０は下一桁数字の値、インデックス１以降は位置(第ｍ数字として)
    print(one_digit_posi)
    return one_digit_posi

present_one_digit(2)

def sort_pre_one_digit(s):
    """関数present_one_digitで得られたリスト(引数)をソート、カット
    リストのようなミュータブルオブジェクトの場合、b=a(参照渡し)とやると
    b或いはaの変更が、a或いはbにも反映されてしまう。
    (文字列、タプルのようなイミュータブルは気にしないでＯＫ）
    なので関数を分ける。関数を分けても関数の戻り値(リスト)を変数に代入(参照渡し)して
    使いまわしたらダメ、影響を受ける。影響を受けないためには一々メモリにロードし別オブジェクトにする
    まとめ
    変数に代入(参照渡し)：ミュータブルオブジェクト(要素がイミュータブルでも)は変更が元のオブジェクトに反映
    浅いコピー(スライスとかcopyメソッド)：要素がミュータブルなら(リストの要素がリストとか)は影響される
    深いコピー(deepcopyメソッド)：大丈夫！
    参考：https://snowtree-injune.com/2018/07/17/post-565/とか
    https://note.nkmk.me/python-copy-deepcopy/
    """
    #↑これ大事。total_resultを加工したリストの変数を作りそれを加工するとtotal_resultが変わってしまう！
    #今まで作った関数チェックの事 
    #total_resultは要素がタプルなのでスライスして作ったオブジェクトは大丈夫！
    #one_digit_posiは要素がリストなのでそこから作ったオブジェクトを加工すると
    #元のオブジェクトも影響を受ける。deepcopyか関数を分ける
    s.pop(0)
    for i in range(len(s)):
        s[i].sort(key=lambda x: len(x),reverse=True)
    for i,val in enumerate(s):
        for j,val2 in enumerate(val):
            if len(val2)==2:
                break
        s[i]=s[i][:j]
    print(s)

sort_pre_one_digit(present_one_digit(6))

def next_one_digit(n):
    """第ｎ回の当選番号の下一桁数字が次回にどの下一桁数字が出たかを
    調べる。"""
    n_result=total_result[n:n+2]
    n_result.insert(0,None)
    print(n_result)#第ｎ回の当選番号のリスト
    n_one_digit=[None]
    for j,val in enumerate(n_result):
        if val == None:
            continue
        str_line=[]
        for i in range(1,8):
            str_rize=str(val[i])#文字化
            str_rize=str_rize[-1]#下一桁を取り出す(最後のインデックス)
            str_line.append(str_rize)
        n_one_digit.append(str_line)
        n_one_digit[j].insert(0,None)
    print(n_one_digit)

    next_list=[]
    for j ,val1 in enumerate(n_one_digit[1]):
        if val1 == None:
            continue
        for i ,val2 in enumerate(n_one_digit[2]):
            if val2 == None:
                continue
            if val1 == val2 :
                t=(val1,n_result[1][j],j,n_result[2][i],i)
                #下一桁数字,ｎ回の数字，ｎ回の位置（第ｍ数字）,次回（ｎ＋１）の数字，次回（ｎ＋１）の位置（第ｍ数字）
                next_list.append(t)
    print(next_list)

next_one_digit(2)
#前回の当選番号の数字からよく出ている下一桁数字を調べる関数を作る
#next_one_digitを複数回繰り返し良く出ている数字を調べる⇒あとで買い目を
#だすアルゴリズムを考える時


#present_one_digit&sortもう少し簡単にならないかやってみる。
#できた！上のpresent_one_digitとsort_pre_one_digitをひとつにまとめた！
def present_one_digit2(n):
    """直近ｎ回の下一桁数字（０～９）とその位置（第ｍ数字として）を
    調べる"""
    m=n*-1
    recent_result=total_result[m:]
    recent_result.insert(0,None)
    print(recent_result)#直近ｎ回の当選番号のリスト
    recent_one_digit=[None]
    for j,val in enumerate(recent_result):
        if val == None:
            continue
        str_line=[]
        for i in range(1,8):
            str_rize=str(val[i])#文字化
            str_rize=str_rize[-1]#下一桁を取り出す(最後のインデックス)
            str_line.append(str_rize)
        recent_one_digit.append(str_line)
        recent_one_digit[j].insert(0,None)
    print(recent_one_digit)

    checker=["0","1","2","3","4","5","6","7","8","9"]
    one_digit_posi=[None]
    for j in range(1,n+1):
        sub_posi=[]
        sub_posi2=[]
        for i,val in enumerate(recent_one_digit[j]):
            if val == None:
                continue
            for h in checker:
                if h == val:
                    l=[h,recent_result[j][i],i]#下一桁数字，その数字，位置（第ｍ数字として）
                    sub_posi.append(l)
        print(sub_posi)
        #ここにsub_posiのインデックス０を評価して出現回数が２未満は消すコードを入れる
        l2=[x[0] for x in sub_posi]
        print(l2)
        l2=[val2 for val2 in l2 if l2.count(val2)>1]
        print(l2)
        l3=[]
        l2=[x for x in l2 if x not in l3 and not l3.append(x)]
        print(l2)
        for m in l2:
            for val3 in sub_posi:
                if val3[0] == m:
                    sub_posi2.append(val3)
        one_digit_posi.append(sub_posi2)
    return one_digit_posi

present_one_digit2(3)

def next_conti_number(n):
    """第ｎ回の当選番号の中から次回も継続して出た数字を調べる
    （引っ張り数字）"""
    n_result=total_result[n:n+2]
    n_result.insert(0,None)
    print(n_result)#第ｎ回の当選番号のリスト
    
    next_list=[]
    for j,val1 in enumerate(n_result[1]):
        if val1 == None:
            continue
        for i,val2 in enumerate(n_result[2]):
            if val2 == None:
                continue
            if val1 == val2 :
                t=(str(val1),n_result[1][j],j,n_result[2][i],i)
                #継続数字,ｎ回の数字，ｎ回の位置（第ｍ数字）,次回（ｎ＋１）の数字，次回（ｎ＋１）の位置（第ｍ数字）
                #上でインデックス１、３はいらないがとりあえずnext_one_digitの戻り値と形を合わせておく
                next_list.append(t)
    print(next_list)

next_conti_number(9)

def present_serial_number(n):
    """第ｎ回の連続数字（ｘ，ｘ２）とその位置（第ｍ，ｍ２数字として）を
    調べる"""
    n_result=total_result[n]
    print(n_result)#第ｎ回の当選番号のリスト
    serial_list=[]
    for i in range(1,7):
        if n_result[i] == n_result[i+1]-1:
            val=[n_result[i],n_result[i+1],i,i+1]#ｘ，ｘ２，ｍ，ｍ２
            serial_list.append(val)
    print(serial_list)

present_serial_number(1)
