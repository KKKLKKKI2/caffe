def classification(net,model,label,image):
    import numpy as np
    import sys,os
    plat_path = "/usr/lib/python3.5/plat-x86_64-linux-gnu"
    if(not plat_path in sys.path):
        sys.path.append(plat_path)
    #设置当前目录
    caffe_root = 'C:/Users/D300_ADAS/Desktop/caffe-windows/'
    #caffe_root = ''
    sys.path.insert(0, caffe_root + 'python')
    import caffe
    os.chdir(caffe_root)
    #a = 'examples/test_photo/google_deploy.prototxt'
    #b = 'examples/test_photo/_iter_50000.caffemodel'
    #c = 'C:/Users\D300_ADAS\Desktop/test_photo/Erebidae_mean.binaryproto'
    #d = 'examples/test_photo/Moth_Habitat_Merge_Label_Family.txt'

    net_file=net
    caffe_model=model
    #mean_file=caffe_root + c

    net = caffe.Net(net_file,caffe_model,caffe.TEST)
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_transpose('data', (2,0,1))
    #transformer.set_mean('data', np.load(mean_file).mean(1).mean(1))
    transformer.set_raw_scale('data', 255)
    transformer.set_channel_swap('data', (2,1,0))

    im=caffe.io.load_image(image)
    net.blobs['data'].data[...] = transformer.preprocess('data',im)
    out = net.forward()


    imagenet_labels_filename = label
    labels = np.loadtxt(imagenet_labels_filename, str, delimiter='\t')

    top_k = net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]
    #prob = net.blobs['prob'].data[0].flatten()
    #prob.sort()
    #print (prob[-1])
    #for i in np.arange(1):
        #print(top_k[0], labels[top_k[0]])


    return labels[top_k[0]], labels[top_k[1]], labels[top_k[2]], labels[top_k[3]],labels[top_k[4]]

    #return  labels[top_k[0]],labels[top_k[0]],labels[top_k[0]],labels[top_k[0]],labels[top_k[0]]