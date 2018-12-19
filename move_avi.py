import os, shutil


# move avi file to super folder before execute ./convert_video_to_image
def mv():
    dst_dir_list = []
    cwd = os.getcwd()
    for dir in os.listdir(cwd+'/UFC101'):
        if os.path.isdir(dir):
            dst_dir_list.append(cwd+'/UFC101/'+dir)
            # print (cwd+'/'+dir)
    print(dst_dir_list)

    src_dir_list = []
    for dir1 in dst_dir_list:
        for dir2 in os.listdir(dir1):
            if os.path.isdir(dir1+'/'+dir2):
                print(dir1+'/'+dir2)
                # os.remove(dir1+'/'+dir2)
                for avi_file in os.listdir(dir1+'/'+dir2):
                    if 'avi' in avi_file:
                        # print(avi_file)
                        avi_file_path = dir1+'/'+dir2 + '/' + avi_file
                        destination = dir1+'/'+avi_file
                        shutil.move(avi_file_path, destination)

if __name__ == "__main__":
    mv()
