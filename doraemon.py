#--------------必要なモジュールをimport。-----------------

import sys
import tkinter
#---------------------------------------------------------


#----------------基礎設定---------------------------------
board = tkinter.Tk()
board.title(u"ドラえもんお絵描き")
board.geometry("800x600")
canvas = tkinter.Canvas(board, width = 800, height = 600)
canvas.place(x=0, y=0)

#---------------------------------------------------------

#---------------必要な関数--------------------------------

def Doraemon(event):
    canvas.delete("all")
    canvas.create_oval(150, 150, 450, 450, tag="oval",fill='blue', width=5)#大外の丸
    canvas.create_oval(170, 210, 430, 450, tag="oval",fill='white', width=5) #内側の丸
    canvas.create_oval(235, 155, 300, 250, tag="oval",fill='white', width=5)#白目
    canvas.create_oval(300, 155, 365, 250, tag="oval",fill='white', width=5)#白目２
    canvas.create_oval(270, 200, 290, 225, fill='black')#黒目
    canvas.create_oval(310, 200, 330, 225, fill='black')#黒目
    canvas.create_oval(278, 210, 283, 215, tag="oval",fill='white',width=0)#目の光沢
    canvas.create_oval(318, 210, 323, 215, tag="oval",fill='white',width=0)#目の光沢
    canvas.create_oval(280, 230, 320, 270, tag="oval",fill='red', width=5)#鼻
    canvas.create_oval(290, 240, 300, 250, tag="oval",fill='white',width=0)#光沢
    canvas.create_line(300, 270, 300, 330, fill='black',width=5)#顔の線
    canvas.create_line(170, 235, 260, 265, fill='black',width=5)
    canvas.create_line(160, 280, 260, 280, fill='black',width=5)
    canvas.create_line(160, 315, 260, 295, fill='black',width=5)
    canvas.create_line(430, 235, 340, 265, fill='black',width=5)
    canvas.create_line(440, 280, 340, 280, fill='black',width=5)
    canvas.create_line(440, 315, 340, 295, fill='black',width=5)
    canvas.create_arc(400, 440,200, 240,extent=180,start=180,width=5,fill='red')#口
    canvas.create_oval(250, 438, 350, 400, tag="oval",fill='orange', width=0)
    draw1 = tkinter.Button(board, text=u'絵描き歌',width=15)
    draw1.bind("<Button-1>",D1)
    draw1.place(x=400,y=50)


    

def erase(event):
    canvas.delete("all")
    draw1 = tkinter.Button(board, text=u'絵描き歌',width=15)
    draw1.bind("<Button-1>",D1)
    draw1.place(x=400,y=50)


#↓絵描き歌関数    
def D1(event):
    canvas.delete("all")
    canvas.create_text(520, 300, text="ドラえもん絵描き歌始まるよ！", anchor="se", font=("HG丸ｺﾞｼｯｸM-PRO",24))
    draw1 = tkinter.Button(board, text=u'丸描いてチョン×２',width=15)
    draw1.bind("<Button-1>",D2)
    draw1.place(x=400,y=50)

def D2(event):
    canvas.delete("all")
    canvas.create_oval(235, 155, 300, 250, tag="oval",fill='white', width=5)#白目
    canvas.create_oval(300, 155, 365, 250, tag="oval",fill='white', width=5)#白目２
    canvas.create_oval(270, 200, 290, 225, fill='black')#黒目
    canvas.create_oval(310, 200, 330, 225, fill='black')#黒目
    canvas.create_oval(278, 210, 283, 215, tag="oval",fill='white',width=0)#目の光沢
    canvas.create_oval(318, 210, 323, 215, tag="oval",fill='white',width=0)#目の光沢
    draw1 = tkinter.Button(board, text=u'お豆に芽が出て',width=15)
    draw1.bind("<Button-1>",D3)
    draw1.place(x=400,y=50)

def D3(event):
    canvas.create_oval(280, 230, 320, 270, tag="oval",fill='red', width=5)#鼻
    canvas.create_oval(290, 240, 300, 250, tag="oval",fill='white',width=0)#光沢
    canvas.create_line(300, 270, 300, 330, fill='black',width=5)#顔の線
    draw1 = tkinter.Button(board, text=u'植木鉢～植木鉢',width=15)
    draw1.bind("<Button-1>",D4)
    draw1.place(x=400,y=50)

def D4(event):
    canvas.create_oval(150, 150, 450, 450, tag="oval",fill='blue', width=5)#大外の丸
    canvas.create_oval(170, 210, 430, 450, tag="oval",fill='white', width=5)#内側の丸

    #↓改良の余地あり。
    canvas.create_oval(235, 155, 300, 250, tag="oval",fill='white', width=5)#白目
    canvas.create_oval(300, 155, 365, 250, tag="oval",fill='white', width=5)#白目２
    canvas.create_oval(270, 200, 290, 225, fill='black')#黒目
    canvas.create_oval(310, 200, 330, 225, fill='black')#黒目
    canvas.create_oval(278, 210, 283, 215, tag="oval",fill='white',width=0)#目の光沢
    canvas.create_oval(318, 210, 323, 215, tag="oval",fill='white',width=0)#目の光沢
    canvas.create_oval(280, 230, 320, 270, tag="oval",fill='red', width=5)#鼻
    canvas.create_oval(290, 240, 300, 250, tag="oval",fill='white',width=0)#光沢
    canvas.create_line(300, 270, 300, 330, fill='black',width=5)#顔の線

    draw1 = tkinter.Button(board, text=u'～胴体は省略～',width=15)
    draw1.bind("<Button-1>",D5)
    draw1.place(x=400,y=50)

def D5(event):
    canvas.create_text(620, 300, text="胴体は割愛　～ごめんなさい～", anchor="se", font=("HG丸ｺﾞｼｯｸM-PRO",30),tag="text1")#削除できるようにtagを設定
    draw1 = tkinter.Button(board, text=u'お空に三日月のぼってた',width=15)
    draw1.bind("<Button-1>",D6)
    draw1.place(x=400,y=50)

def D6(event):
    canvas.delete("text1")
    canvas.create_arc(400, 440,200, 240,extent=180,start=180,width=5,fill='red')#口
    canvas.create_oval(250, 438, 350, 400, tag="oval",fill='orange', width=0)
    draw1 = tkinter.Button(board, text=u'髭をつけたら',width=15)
    draw1.bind("<Button-1>",D7)
    draw1.place(x=400,y=50)

def D7(event):
    canvas.create_line(170, 235, 260, 265, fill='black',width=5)
    canvas.create_line(160, 280, 260, 280, fill='black',width=5)
    canvas.create_line(160, 315, 260, 295, fill='black',width=5)
    canvas.create_line(430, 235, 340, 265, fill='black',width=5)
    canvas.create_line(440, 280, 340, 280, fill='black',width=5)
    canvas.create_line(440, 315, 340, 295, fill='black',width=5)
    draw1 = tkinter.Button(board, text=u'どらえもん～',width=15)
    draw1.bind("<Button-1>",D8)
    draw1.place(x=400,y=50)

def D8(event):
    canvas.create_text(390, 140, text="完成！！", anchor="se", font=("HG丸ｺﾞｼｯｸM-PRO",30))
    draw1 = tkinter.Button(board, text=u'絵描き歌',width=15)
    draw1.bind("<Button-1>",D1)
    draw1.place(x=400,y=50)

    
#描画ボタン
draw = tkinter.Button(board, text=u'ドラえもんを描く',width=15)
draw.bind("<Button-1>",Doraemon)
draw.place(x=100,y=50)


#消去ボタン
delete = tkinter.Button(board, text=u'全部消す',width=15)
delete.bind("<Button-1>",erase)
delete.place(x=250,y=50)

#1つずつ描画ボタン
draw1 = tkinter.Button(board, text=u'絵描き歌',width=15)
draw1.bind("<Button-1>",D1)
draw1.place(x=400,y=50)

#------------------------------------------------------------------
