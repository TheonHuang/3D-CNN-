import os, shutil


def wrong_filter(file_name):
    result = []
    # open a new train1.list to save the result
    with open(file_name) as train_list:
        # read each line
        for line in train_list.readlines():
            # print(line)
            try:
                # filter wrong line like
                # UFC101//walking/v_walk_dog_25_04 13
                # UFC101//walking/v_walk_dog_25 13  wrong
                last_second_element = line.split('/')[-1].split(' ')[-2].split('_')[-2]
                if not (last_second_element.isalpha()):
                    # print(line)
                    # make the
                    window_path = line.replace('//', '\\').replace('/', '\\')
                    print(window_path)
                    result.append(window_path)
            except:
                pass

    with open(file_name, 'w') as train_list:
        for i in result:
            train_list.write(i)

if __name__ == "__main__":
    train_file_name = 'train.list'
    test_file_name = 'test.list'

    wrong_filter(train_file_name)
