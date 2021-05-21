import requests,bs4
from bs4 import BeautifulSoup

while True:
        word=input("調べたい単語を入力して下さい。qで終了。:")
        if word=="q":
            print("Thank you!")
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
        
