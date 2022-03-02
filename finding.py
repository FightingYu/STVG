import os
path_total= "E:\\Downloaad\\Vidor\\video"
file_total=os.listdir(path_total)#读取video下面的文件夹

miss_id = '3043431641'


for total_ in file_total:
    id_file = os.listdir(path_total+ total_ + os.sep)
    if miss_id in idfile_nums:
        print(idfile_nums)



'''
for val_test in file_list:#遍历roe_video里的文件
    val_test_path = path + os.sep + val_test
    dir_list = os.listdir(val_test_path)#读取test/val下的编号文件夹
    for dir in dir_list:#遍历每一个编号文件
        in_path = val_test_path + os.sep + dir
        video_list = os.listdir(in_path)
        for video in video_list:
            oldname=in_path+ os.sep+video   # os.sep添加系统分隔符
        #设置新文件名
            newname=oldname+'.mp4'
    
            os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
            print(oldname,'======>',newname)
            '''