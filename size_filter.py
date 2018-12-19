# coding:utf-8
import os, shutil

def size_filter(num):
    # get all class folders path
    class_path_list = os.listdir(os.getcwd() + '/UFC101')
    for class_path in class_path_list:

        # 打开类文件夹 UFC101/volleyball_spiking
        if os.path.isdir(os.getcwd()+'/UFC101/'+class_path):
            for folder in os.listdir(os.getcwd()+'/UFC101/'+class_path):

                # UFC101/volleyball_spiking/v_spiking_07_01
                if os.path.isdir(os.getcwd() + '/UFC101/'+class_path+'/'+folder):
                    sub_folders = os.listdir(os.getcwd() + '/UFC101/'+class_path+'/'+folder)

                    # get permission to delete
                    os.chmod(os.getcwd() + '/UFC101/' + class_path + '/' + folder, 0o777)

                    # remove folder that contains less than 10 pictures
                    if len(sub_folders)<num:
                        print(os.getcwd() + '/UFC101/' + class_path + '/' + folder)
                        shutil.rmtree(os.getcwd() + '/UFC101/' + class_path + '/' + folder)

                    # remove files until remaining 10 pictures.
                    elif len(sub_folders)>num:
                        while len(os.listdir(os.getcwd() + '/UFC101/'+class_path+'/'+folder))>10:
                            os.remove(os.getcwd() + '/UFC101/' + class_path + '/' + folder+ '/'+os.listdir(os.getcwd() + '/UFC101/'+class_path+'/'+folder)[-1])



if __name__ == "__main__":
    size_filter(10)
