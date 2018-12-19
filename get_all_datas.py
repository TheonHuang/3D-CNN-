import os
import numpy as np
import cv2

# clips = []
#
# labels = []
# clip_length = 10
def shuffled_data_label(clips,labels):
    permutation = np.random.permutation(labels.shape[0])
    shuffled_dataset = clips[permutation, :, :,:]
    shuffled_labels = labels[permutation,:]
    return shuffled_dataset,shuffled_labels
def get_datas(filenames):
    clips = []
    clip_length = 10
    labels = []
    #subfile represent the name of class
    i = 0
    for subfile in os.listdir(filenames):
        # travel the imagefile in subfiles
        for image_file in os.listdir(os.path.join(filenames,subfile)):
            clip = []
            labels
            #get images from image files and resize the image
            for image in os.listdir(os.path.join(filenames,subfile,image_file)):
                res = cv2.imread(os.path.join(filenames, subfile, image_file,image))
                res = cv2.resize(res, (56, 56), interpolation=cv2.INTER_CUBIC)
                clip.append(res)
            clip = np.array(clip)
            clip.reshape([clip_length, 56, 56, 3])
            clips.append(clip)
            oh_labels = np.zeros([1, 11]).astype(np.int64)
            oh_labels[0, i] = 1
            print(oh_labels)
            labels.append(oh_labels)
        i = i+1
    clips = np.array(clips)
    clips = clips.reshape([156,10,10,56,56,3])
    #print(clips.shape)
    labels = np.array(labels)
    labels = labels.reshape([156,10,11])
    out_clips,out_labels=shuffled_data_label(clips,labels)
    # print(clips.shape)
    # print(clips[0].shape)
    # print(labels.shape)
    # print(labels[0].shape)
    return out_clips,out_labels
images,labels=get_datas("action10")
# print("images_shape",images.shape)
# print("labels_shape",labels.shape)