def main():
    import prediction
    import sys
    import os
    import skimage

    print(sys.argv[1])
    image_file = sys.argv[1]
    path = os.getcwd()
    print(path)
    net_file = path+'\deploy.prototxt'
    caffe_model = path + '\_iter_60000.caffemodel'
    label_file = path + '\Moth_Family_Sample_Label_Limit.txt'
    #image_file = 'C:/Users\D300_ADAS\Desktop\caffe-windows\python/V01-20141121-001.jpg'

    prob,top_k,labels=prediction.startprediction(net_file,caffe_model,label_file,image_file)

    for i in range(1, 6):
        print(labels[top_k[i]], prob[-i])


if __name__ =="__main__":
    main()


