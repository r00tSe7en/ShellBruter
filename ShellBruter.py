#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:Se7en
#读取文件
def ReadPass(pass_file,result_file):
    # 定义分割大小
    segmentation = 1000
    # 定义存放总列表
    pass_list = []
    with open(pass_file, "r", encoding='utf-8') as pass_file:
        lines = pass_file.readlines()
    pass_file.close()
    # 生成可用参数格式并存入列表pass_list
    for line in lines:
        pass_list.append('&'+line.strip()+'=echo "'+line.strip()+'";')
    list_length = len(pass_list) # 列表元素个数
    '''
    print("列表元素个数:"+str(list_length))
    '''
    times = int(list_length/segmentation) # 分割总次数
    time = 1 # 第几次分割
    temp = 0 # 递增临时变量
    with open(result_file, "w", encoding='utf-8') as result_file: # 写入结果文件
        #此处存放满足1000个元素并写入
        while(time<=times):
            temp2 = 0  # 递增临时变量
            '''
            print("第"+ str(time) +"次分割：")
            print(str(temp+1)+" -> "+str(temp+1000)) # 当前分段
            '''
            for line in pass_list[temp:temp+segmentation]: # 循环写入当前分段
                result_file.write(pass_list[temp+temp2])
                temp2=temp2+1
            result_file.write("\n")
            '''
            print(pass_list[temp:temp+1000])
            '''
            time = time+1
            temp = temp+segmentation
        #此处存放剩余不足1000个元素并写入
        '''
        print("剩余不足1000个元素：")
        print(str(times*1000+1)+" -> "+str(list_length))
        print(pass_list[times*1000:list_length])
        '''
        temp3 = 0  # 递增临时变量
        for line in pass_list[times*segmentation:list_length]:
            result_file.write(pass_list[times*segmentation+temp3])
            temp3 = temp3 + 1
        result_file.write("\n")
    result_file.close()

if __name__ == '__main__':
    # 只需提供password.txt即可，文本内容尽量提前去重
    banner = """

      _________.__           .__  .__ __________                __                
     /   _____/|  |__   ____ |  | |  |\______   \_______ __ ___/  |_  ___________ 
     \_____  \ |  |  \_/ __ \|  | |  | |    |  _/\_  __ \  |  \   __\/ __ \_  __ \\
     /        \|   Y  \  ___/|  |_|  |_|    |   \ |  | \/  |  /|  | \  ___/|  | \/
    /_______  /|___|  /\___  >____/____/______  / |__|  |____/ |__|  \___  >__|   
            \/      \/     \/                 \/                         \/ 
                                                                         _by Se7en 

    """
    print(banner)
    try:
        ReadPass('password.txt', 'result_file.txt')
        print("Enjoy your result_file.txt!")
    except:
        print("You need to provide the password dictionary first!")
