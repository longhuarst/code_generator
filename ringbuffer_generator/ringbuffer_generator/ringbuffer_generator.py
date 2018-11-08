import re #正则库


ringbuffer_h = '''

#ifndef __ringbuffer$(_type)_h
#define __ringbuffer$(_type)_h

#include <stdint.h>
#include <stdbool.h>


typedef struct{
    uint32_t w_idx;//写指针
    uint32_t r_idx;//读指针
    uint32_t size;//大小
    uint32_t length;//长度
}ringbuffer$(_type)_type;



void ringbuffer$(_type)_init()






#endif //____ringbuffer_$(type)_h
'''



ringbuffer_c = '''
#include "ringbuffer$(_type).h"





//初始化循环缓冲区
void ringbuffer$(_type)_init()
{
    
}








'''


def main():

    str = ringbuffer.replace("$(type)","")
    print(str)







if __name__ == '__main__': 

    main()





