def startprediction(net_file,caffe_model,label,image):
    import numpy as np

    import sys,os
    plat_path = "/usr/lib/python3.5/plat-x86_64-linux-gnu"
    if(not plat_path in sys.path):
        sys.path.append(plat_path)
    #设置当前目录
    caffe_root = 'C:/Users/D300_ADAS/Desktop/caffe-windows/'
    sys.path.insert(0, caffe_root + 'python')
    import caffe
    os.chdir(caffe_root)

    #net_file=caffe_root + 'examples/moth/google_deploy.prototxt'
    #caffe_model=caffe_root + 'examples/moth/google_iter_20000.caffemodel'
    #mean_file=caffe_root + 'examples/moth/moth_mean.binaryproto'

    net = caffe.Net(net_file,caffe_model,caffe.TEST)
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_transpose('data', (2,0,1))
    #transformer.set_mean('data', np.load(mean_file).mean(1).mean(1))
    transformer.set_raw_scale('data', 255)
    transformer.set_channel_swap('data', (2,1,0))

    im=caffe.io.load_image(image)
    net.blobs['data'].data[...] = transformer.preprocess('data', im)
    out = net.forward()


    imagenet_labels_filename = label
    labels = np.loadtxt(imagenet_labels_filename, str, delimiter='\t')
    prob = []
    top_k = net.blobs['prob'].data[0].flatten().argsort()[-1:-7:-1]
    prob = net.blobs['prob'].data[0].flatten()
    prob.sort()
    #for i in np.arange(1):
    #    print(top_k[i], labels[top_k[i]])
    return prob,top_k,labels