//乱数生成機 （windowsで動作確認。）

#include <stdio.h>
#include <conio.h>
#include <windows.h>

unsigned int first_num = 39; //ここの値はなんでもいい。（ただし4,294,967,295以内で。）

unsigned int ransu(void);

void main(void)
{
    printf("3秒後に処理を開始します。停止：任意のキーを入力。\n");
    Sleep(3 * 1000);   //3秒間停止
    
    do {
        printf("%10d", ransu());
        if (_kbhit())  //任意のキーボード入力があればtrueとなる
            break;  //処理を打ち切る
        Sleep(100); //0.1秒停止
    } while (1);

}
unsigned int ransu(void)        //疑似乱数を生成する関数。
{
    first_num = (first_num * 13 + 1919) % 65536;
    
    /*13の部分は8で割って5余る値なら何でもいい。
    1919の部分は奇数であれば、65536の部分は２の累乗ならなんでもいい
    (65536未満の数値が疑似乱数として生成される。例えば,65536の部分を2に置き換えたなら生成される乱数は1か0のみ。)*/


    return first_num;   //main関数にfirst_numの値を返す。
}
