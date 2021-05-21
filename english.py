

#正式なプログラム。単語をデータベースに登録する機能、１で登録した単語一覧を表示する機能（１の中に搭載してもよい）、

#ランダムな登録した英単語を出力しテストする機能（和英、英和両方）、英単語辞書機能を搭載。）

#１、ユーザーが入力した単語、意味をデータベースに登録する機能。
import sqlite3
import os
import random
import requests,bs4
from bs4 import BeautifulSoup

#注意：正式に起動しない場合bs4、request,sqlite3などがインストール出来ていない可能性がある。
#      そういう時はコマンドプロンプト内でpip install <インストールしたいモジュール>と書く 例: pip install bs4

##############################超重要！！！########################################
"""
英単語を保存したいフォルダへのパスを下のpathに代入すること。
パスは適当なフォルダを右クリックして、プロパティ→場所に書いてあるパスをコピーする。
そのままpathに代入した後、\の部分を\\と２つに置き換えて完了！！
path=ex:C:\\Users\\ユーザー名
"""
#########################ここに入れる#############################################

path=""

#########################ここに入れる#############################################







def english_db():
    #1,dbファイルがない場合、dbファイルを作成
    d_path=path
    d_path2="English_words_data"
    os.chdir(d_path)
    
    #dbfileがあるかcheck, isolation_level=None=自動コミットモード＝c.commitがいらない。
    c = sqlite3.connect(d_path2, isolation_level=None)
    #カーソル作成
    cur = c.cursor()
    
    # データテーブルを作成する(存在する場合エラーを吐く。...対処としてIF NOT EXISTSを注入するとエラーを吐かなくなる。)
    #executeはsqliteに命令するときに使う。(id INTEGER PRIMARY KEY AUTOINCREMENT)...自動でidを追加。
    sql = "create table IF NOT EXISTS english_word_db(id INTEGER PRIMARY KEY AUTOINCREMENT,english_word text , japanese_word text)"
    cur.execute(sql)
    
       #それぞれ必要な関数を作成する。
    while True:
        #userに英単語を登録、もしくは削除、一覧を表示　かを選ばせる。
        print("\n＜＜＜１　英単語　登録　削除　一覧標示　＞＞＞\n")
        print("使いたい機能を選択してください。\n\n1. 英単語、和訳を登録　\n2. 英単語を削除　\n3. 登録した英単語一覧を表示")
    

        a=input("使いたい機能を選択してください。qで終了:")
        if a=="q":
            print("１の機能を終了します。")
            cur.close()
            break
        elif a=="1":
            register_english(cur)
           
            #英単語を登録する関数を置く。
            
        elif a=="2":
            delite_english(cur)
            

        elif a=="3":
            print("＜＜＜登録した単語一覧＞＞＞\n\n")
            en_list(cur)
            

        else:
            print("有効な値を入力してください。")

#英単語を登録する関数
#必要な変数がenglish_dbのローカルにある。
#例：）cur.execute('INSERT INTO sample_table3(english_word,japanese_word) values("car","車")')

#とりあえずc,curだけ変数に持って動くか確かめてみる。テストしたところ、異常は見られなかった。引数がcurだけでもしっかり機能。
def register_english(cur):
    #本番：cur.executeの中にユーザーがinputしたものを代入し（和訳、単語）、printで登録したものを表示する。
    while True:
        en_word=input("登録したい英単語を入力してください。(qで終了):")
        if en_word=="q":
            print("終了します。")
            break
        jp_word=input("登録したい日本語を入力してください。(qで終了):")
        if jp_word=="q":
            print("終了します。")
            break
        
        cur.execute('INSERT INTO english_word_db(english_word,japanese_word) values("{}","{}")'.format(en_word,jp_word))
        print("登録しました。")
        #下の2文はテスト用
        cur.execute('SELECT * FROM english_word_db')
        
    
def delite_english(cur):
    #まず登録した英単語の一覧を表示。(削除するたびに表示したほうがいいかも。)
    en_list(cur)
    #削除する英単語を選択
    while True:
        delite=input("削除する英単語を選んでください。（番号で指定。qで終了。）:")
        if delite=="q":
            print("終了します。")
            break
        
        #tryでuserが間違った入力をした場合、continueで回す。
        #(存在しない値(数値)を入力してもエラーを吐かない。)、つまり値が存在するか確かめるコードが必要。...余裕があったらの課題。
        try:
            cur.execute("delete from english_word_db where id = {}".format(delite))
            print("削除しました。\n")
        except Exception:
            print("有効な値を入力してください。")
        
        en_list(cur)


        
        
def en_list(cur):
    #登録されている単語一覧を表示する関数。
    try:
        cur.execute('SELECT * FROM english_word_db')#呼び出す度に初期化する。これを外で
    except Exception:
        print("エラーが発生しました。")
        

    #定義すると呼び出す度に初期化されず、空のリストになってしまう。
    while True:
        result = cur.fetchone()
        if result is None :
            break
        print(result)
        
        
        
#--------------------------------------------ここまでが１の機能で使った関数。-----------------------------------------------------------

#ここからが２の機能。

#最初は１のenglish_db関数とあまり変わらない。
#１．英単語データベースを呼び出す。２．fetch_oneでランダムな場所の和訳を出す。３．ユーザーに入力を求め正誤判定をする。４．正解数をカウントし、中身がなくなったら結果を発表する。

def english_db2():
    
    #1,dbファイルがない場合、dbファイルを作成
    d_path=path
    d_path2="English_words_data"
    os.chdir(d_path)
    
    #dbfileがあるかcheck, isolation_level=None=自動コミットモード＝c.commitがいらない。
    c = sqlite3.connect(d_path2, isolation_level=None)
    #カーソル作成
    cur = c.cursor()

#2.fetch_oneでランダムな場所の和訳を出す。
    #まず何問出題するかユーザーに聞く。
    cur.execute("select * FROM english_word_db")
    
    #後でfetchmany()にq1を代入する。
    while True:
        q1=input("何問解く？（番号で指定）　\n\n1. 50問\n2. 100問\n3. 全部\n :")
        print(q1)
        if q1=="1" or q1=="2" or q1=="3":
            break
        else:
            print("\n無効な値です。再度入力してください。\n")
    #ユーザーが入力した値によって問題数を変える。
            
    question=0#問題数
    
    if q1=="1":
        question=50
    elif q1=="2":
        question=100
    elif q1=="3":
        question=65535
        
        
    #テストを作成
    result=cur.fetchall()
    result_list=[]
    for c in result:
        c_list=list(c)#list化させる。今後のキーとなる変数。
        result_list.append(c_list)
    random.shuffle(result_list)
    #問題数を調整
    result_list=result_list[:question]
   
    
    #正解カウント
    count=0

    #userに問題を出す。
    print("\n問題を開始します。\n")
    for i in result_list:
        #問題を出題
        print("{} の英訳は？".format(i[2]))
        answer=input("答え :")
        #正解の場合
        if answer==i[1]:
            print("正解！\n")
            count=count+1
        else:
            print("残念！正解は {}\n".format(i[1]))

    #結果発表
    print("\n\n正解数は{}。\n\n".format(count))

    cur.close()
        

#--------------------------ここまでが２の機能----------------------------------

#最後に3の機能。調べた単語をデータベースに格納できるようにする。
#前作ったスクレイピング機能を使用する。


def interpriter():
    d_path=path
    d_path2="English_words_data"
    os.chdir(d_path)
    
    #dbfileがあるかcheck, isolation_level=None=自動コミットモード＝c.commitがいらない。
    c = sqlite3.connect(d_path2, isolation_level=None)
    #カーソル作成
    cur = c.cursor()

    #スクレイピングする。
    while True:
        word=input("調べたい単語を入力して下さい。qで終了。:")
        if word=="q":
            print("Thank you!")
            cur.close()
            break
        res=requests.get("https://ejje.weblio.jp/content/"+str(word))
        contents=res.content
        no_starch_soup=BeautifulSoup(contents,"html.parser")
        title=no_starch_soup.find_all("td",{"class":"content-explanation ej"})

        #titleが空の場合そのまま次のループに入る。
        if title==[]:
            print("単語が見つかりませんでした。\n")
            continue
        
        for t in title:
            print(t.text)
        
        #ここから追加した機能。（スクレイピングした単語を格納するかどうか）
       
        q3=input("スクレイピングした単語を保存しますか？y/n")
        if q3=="y":
            cur.execute('INSERT INTO english_word_db(english_word,japanese_word) values("{}","{}")'.format(word,t.text))
            print("登録しました。\n")

            
        if q3=="n":
            continue


#--------------------------------------------------完成-----------------------------------------------------------

    
    

#まず、ユーザーにどの機能を使用するか選択させる。
while True:
    print("\n    ＜＜＜英語学習システム＞＞＞\n\n1. 英単語、和訳を登録、削除。登録した単語一覧を表示。 \n2. １で登録した単語をテスト。\n3. ネット辞書で単語の意味を調べる。（調べた単語を登録）\n")
    
    choice=input("\n使いたい機能を数字で示して下さい。qで終了。:")
    if choice =="q":
        print("終了します。")
        break
    #それぞれの機能へ飛ぶように設定する。
    elif choice=="1":
        english_db()
    elif choice=="2":
        english_db2()
    elif choice=="3":
        interpriter()
    else:
        print("\n有効な値を入力してください。\n")
        



    
