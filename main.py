import tt
import read_txt
import timeit
import tkinter as tk
from tkinter import filedialog as fi
global root
root = "C:/Users\D300_ADAS\Desktop\caffe-windows\examples/family"
def click1():
    #global count
    #count += 1
    #label.configure(text="click"+str(count)+'times')
    name1=OpenFile()
    nn=name1.split('/')
    label2.configure(text=str(nn[-1]))
    global net_file
    net_file=name1
def click2():
    name2=OpenFile()
    nn=name2.split('/')
    label4.configure(text=str(nn[-1]))
    global caffemodel_file
    caffemodel_file=name2
def click3():
    name1=OpenFile()
    nn=name1.split('/')
    label6.configure(text=str(nn[-1]))
    global label_file
    label_file = name1
def click4():
    dir=openfiledir()
    label8.configure(text=str(dir))
    global image_path
    image_path = dir + '/'
def click5():
    #txt_dir = openfiledir()
    txt_file = OpenFile()
    nn = txt_file.split('/')
    label10.configure(text=str(nn[-1]))
    global test_txt
    #global test_path
    #test_path = txt_dir
    test_txt = txt_file
    t = test_txt.replace('.txt', '')
    tt = t.split('/')
    ttt = t.replace(tt[-1], '')
    global txt_data
    txt_data = read_txt.dirs_readtxt(ttt, tt[-1])
def click6():
        count = 0
        print("start classify")
        accuracy_top1 = 0
        accuracy_top2 = 0
        accuracy_top3 = 0
        accuracy_top4 = 0
        accuracy_top5 = 0
        # print(len(txt_data))
        #for i in range(10):
        for i in range(len(txt_data)):

            text = txt_data[i].split(' ')
            label = text[1].replace('\n', '')
            # print(text[0])
            #print(label)
            filename = text[0]
            image = image_path + filename + '.jpg'
            if (filename == ' '):
                break
            result_1, result_2, result_3, result_4, result_5 = tt.classification(net_file, caffemodel_file, label_file,
                                                               image)
            #print(result_1,result_2,result_3,result_4,result_5)
            if ((result_1) == (label)):
                # print(True)
                # print("data = %s, training result= %s" % (label, result))
                accuracy_top1 += 1
            elif (result_2 == label):
                accuracy_top2 += 1
            elif (result_3 == label):
                accuracy_top3 += 1
            elif (result_4 == label):
                accuracy_top4 += 1
            elif (result_5 == label):
                accuracy_top5 += 1
        print("TOP1: ", accuracy_top1)
        print("TOP2: ", accuracy_top2)
        print("TOP3: ", accuracy_top3)
        print("TOP4: ", accuracy_top4)
        print("TOP5: ", accuracy_top5)
        print("TOP1 accuracy: ",  accuracy_top1/len(txt_data))
        print("TOP2 accuracy: ", (accuracy_top1+accuracy_top2) / len(txt_data))
        print("TOP3 accuracy: ", (accuracy_top1+accuracy_top2+accuracy_top3) / len(txt_data))
        print("TOP4 accuracy: ", (accuracy_top1+accuracy_top2+accuracy_top3+accuracy_top4) / len(txt_data))
        print("TOP5 accuracy: ", (accuracy_top1+accuracy_top2+accuracy_top3+accuracy_top4+accuracy_top5)/len(txt_data))
        # print("data = %s, training result= %s"%(label,result))
        # print(False)
def openfiledir():
    dir = fi.askdirectory(initialdir=root,
                          title = 'choose a file')
    return dir
def OpenFile():
    name = fi.askopenfilename(initialdir=root,
                           filetypes =(("All Files","*.*"),("All Files","*.*")),
                           title = "Choose a file."
                           )

    #Using try in case user types in unknown file or closes without choosing a file.
    return name
    try:
        with open(name,'r') as UseFile:
            print(UseFile.read())
    except:
        print("No file exists")

print("begin")


global label_file
timer_start=timeit.default_timer()
win=tk.Tk()
win.title('FCC')
label1=tk.Label(win,text='net file :')
label1.grid(column=0,row=15)
label2=tk.Label(win,text='')
label2.grid(column=2,row=15)
button=tk.Button(win,text='ok',command=click1)
button.grid(column=0,row=18)
label3=tk.Label(win,text='caffe model :')
label3.grid(column=0,row=30)
label4=tk.Label(win,text='')
label4.grid(column=2,row=30)
button2=tk.Button(win,text='ok',command=click2)
button2.grid(column=0,row=50)
label5=tk.Label(win,text='label file :')
label5.grid(column=0,row=60)
label6=tk.Label(win,text='')
label6.grid(column=2,row=60)
button3=tk.Button(win,text='ok',command=click3)
button3.grid(column=0,row=70)
label7=tk.Label(win,text='image directory :')
label7.grid(column=0,row=80)
label8=tk.Label(win,text='')
label8.grid(column=2,row=80)
button4=tk.Button(win,text='ok',command=click4)
button4.grid(column=0,row=90)
label9=tk.Label(win,text='Test.txt :')
label9.grid(column=0,row=100)
label10=tk.Label(win,text='')
label10.grid(column=2,row=100)
button5=tk.Button(win,text='ok',command=click5)
button5.grid(column=0,row=110)
button5=tk.Button(win,height=10,width=10,text='RUN',command=click6)
button5.grid(column=500,row=300)
win.geometry("900x600+300+300")
win.mainloop()


#path='C:/Users\D300_ADAS\Desktop\caffe-windows\examples/test_pkoto_stop/'
#txt_data = read_txt.readtxt("SingleTest_ID")
#txt_data = read_txt.dirs_readtxt(path,'Moth_Family_Habitat_SingleTest_ID')

#net = path + 'google_deploy.prototxt'
#model = path + '_iter_20000.caffemodel'
#label_path = path + 'Moth_Habitat_Merge_Label_Family.txt'
#image_path = path + 'Moth_Family_Habitat_SingleTest_ID/'







#print("TOP1 accuracy: " , accuracy_top1/len(txt_data))
#print("TOP5 accuracy: " , (accuracy_top1+accuracy_top5)/len(txt_data))
timer_stop=timeit.default_timer()
print(timer_stop-timer_start)
print("Finish")