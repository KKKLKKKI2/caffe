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

net_file=caffe_root + 'examples/moth/caffe_deploy.prototxt'
caffe_model=caffe_root + 'examples/moth/caffe_iter_20000.caffemodel'
mean_file=caffe_root + 'examples/moth/moth_mean.binaryproto'

net = caffe.Net(net_file,caffe_model,caffe.TEST)
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))
#transformer.set_mean('data', np.load(mean_file).mean(1).mean(1))
transformer.set_raw_scale('data', 255)
transformer.set_channel_swap('data', (2,1,0))

im=caffe.io.load_image(caffe_root+'examples/moth/SingleTest_ID/V22-20150110-019.jpg')
net.blobs['data'].data[...] = transformer.preprocess('data',im)
out = net.forward()


imagenet_labels_filename = caffe_root + 'examples/moth/Family_Lable_Converttable.txt'
labels = np.loadtxt(imagenet_labels_filename, str, delimiter='\t')

top_k = net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]
for i in np.arange(1):
    print(top_k[i], labels[top_k[i]])