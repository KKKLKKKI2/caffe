import prediction
import timeit
import read_txt

caffe_root = 'C:/Users/D300_ADAS/Desktop/caffe-windows/'
net_file = caffe_root + 'examples/moth/google_deploy.prototxt'
caffe_model = caffe_root + 'examples/moth/google_iter_20000.caffemodel'
mean_file = caffe_root + 'examples/moth/moth_mean.binaryproto'
label = caffe_root + 'examples/moth/Family_Lable_Converttable.txt'
path = caffe_root+'examples\moth\SingleTest_ID/'
image = path+'V15-20141121-020'+'.jpg'

start = timeit.default_timer()
#txt_data=read_txt.dirs_readtxt()
prob, top_k, labels = prediction.startprediction(net_file, caffe_model, label,image)

for i in range(1, 6):
    print(labels[top_k[i]], prob[-i])
stop = timeit.default_timer()
print("end", stop-start)
