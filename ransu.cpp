//���������@ �iwindows�œ���m�F�B�j

#include <stdio.h>
#include <conio.h>
#include <windows.h>

unsigned int first_num = 39; //�����̒l�͂Ȃ�ł������B�i������4,294,967,295�ȓ��ŁB�j

unsigned int ransu(void);

void main(void)
{
    printf("3�b��ɏ������J�n���܂��B��~�F�C�ӂ̃L�[����́B\n");
    Sleep(3 * 1000);   //3�b�Ԓ�~
    
    do {
        printf("%10d", ransu());
        if (_kbhit())  //�C�ӂ̃L�[�{�[�h���͂������true�ƂȂ�
            break;  //������ł��؂�
        Sleep(100); //0.1�b��~
    } while (1);

}
unsigned int ransu(void)        //�^�������𐶐�����֐��B
{
    first_num = (first_num * 13 + 1919) % 65536;
    
    /*13�̕�����8�Ŋ�����5�]��l�Ȃ牽�ł������B
    1919�̕����͊�ł���΁A65536�̕����͂Q�̗ݏ�Ȃ�Ȃ�ł�����
    (65536�����̐��l���^�������Ƃ��Đ��������B�Ⴆ��,65536�̕�����2�ɒu���������Ȃ琶������闐����1��0�̂݁B)*/


    return first_num;   //main�֐���first_num�̒l��Ԃ��B
}
