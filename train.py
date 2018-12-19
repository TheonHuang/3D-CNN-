import tensorflow as tf
import numpy as np
import get_all_datas

TF_CPP_MIN_LOG_LEVEL=2
batch_size = 10
clip_length = 10
image_height = 56
image_weight = 56
chanel = 3
num_class = 11
batch_clips = tf.placeholder(tf.float32, [batch_size, clip_length, image_height, image_weight,chanel] )
batch_labels = tf.placeholder(tf.int32, [batch_size, num_class] )
keep_prob = tf.placeholder(tf.float32)
#3d convolution network
kernel1 = tf.Variable(tf.random_normal([3,3,3,3,4]))
kernel2 = tf.Variable(tf.random_normal([3,3,3,4,8]))
#full_connect1 = tf.Variable(tf.random_normal([10,5*28*28*128]))
#change full1 from 28 to 56
full_connect1 = tf.Variable([tf.random_normal([5*28*28*8,4096])])
full_connect1 = tf.reshape(full_connect1,[5*28*28*8,4096])
full_connect2 = tf.Variable([tf.random_normal([4096,num_class])])
full_conncet3 = tf.reshape(full_connect2,[4096,11])
out1 = tf.nn.conv3d(batch_clips,kernel1,strides=[1,1,1,1,1],padding="SAME")
#try to change the last p of ksize
out1_p = tf.nn.max_pool3d(out1,ksize=[1,2,2,2,1],strides = [1,2,2,2,1],padding="SAME")
#shape of conv3d layer becomes [10,5,64,64,64]
out2 = tf.nn.conv3d(out1,kernel2,strides=[1,1,1,1,1],padding = "SAME")
out2_p = tf.nn.max_pool3d(out2,ksize=[1,1,2,2,1],strides=[1,2,2,2,1],padding="SAME")
#shape of con3d layer becomes [10,5,28,28,128]
out2_p = tf.reshape(out2_p,[batch_size,5*28*28*8])
full_out1 = tf.matmul(out2_p,full_connect1)
logitis = tf.matmul(full_out1,full_conncet3)
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logitis, labels=batch_labels))
    tf.summary.scalar('loss', loss)
accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(logitis, 1), tf.argmax(batch_labels, 1)), np.float64))
optimizer = tf.train.AdamOptimizer(0.001).minimize(loss)

#reshape as fully_connect layer

#send data to nectwork
images,label=get_all_datas.get_datas("action10")

with tf.Session() as sess:
    merged = tf.summary.merge_all()
    writer = tf.summary.FileWriter("G:/finalpj/testtboard2", sess.graph)
    sess.run(tf.global_variables_initializer())
    sess.run(tf.local_variables_initializer())

    #coord = tf.train.Coordinator()
    #tread = tf.train.start_queue_runners(sess, coord)
    print("p4")
    for epoch in range(10):
        batch_accuracy = []
        #total batch_size is 156
        for i in range(156):

           # ib ,lb= sess.run([image_batch,label_batch])
           #  ib=np.array(ib)
           #  ib1 = ib.reshape([1,10,56,56,3])
           #  lb=np.array(lb)
           #  lb1 = lb.reshape([1,11])

            loss_out, accuracy_out,_ = sess.run([loss, accuracy,optimizer],
                                              feed_dict={batch_clips: images[i],
                                                         batch_labels: label[i],
                                                         })
            batch_accuracy.append(accuracy_out)
            if i%10 == 0:
                print(i,"batch_accuracy :",accuracy_out)
                result = sess.run(merged, feed_dict={batch_clips: images[i],
                                                         batch_labels: label[i],})
                writer.add_summary(result, i)

        new_batch_accuracy = np.array(batch_accuracy)
        new_batch_accuracy = np.mean(new_batch_accuracy)
        print("new_batch_accruracy is ",new_batch_accuracy)
        if epoch%2 == 0:
            print("epoch_time",epoch)