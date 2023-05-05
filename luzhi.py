from os import mkdir
from os.path import isdir
import datetime
from threading import Thread
import cv2

def write():
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:     #写入视频文件
            aviFile.write(frame)
    aviFile.release()
    
cap = cv2.VideoCapture(0)
now = str(datetime.datetime.now())[:19].replace(':', '_')       # 当前日期时间，如2023-05-01 23:11:00
dir_name = now[:10]
file_path = 'record/'+dir_name+'/'+now+'.avi'
if not isdir('record'):
    mkdir('record')
if not isdir('record/'+dir_name):
    mkdir('record/'+dir_name)

# 保存视频文件
aviFile = cv2.VideoWriter(file_path,cv2.VideoWriter_fourcc('M','J','P','G'),25, (640,480))  # 帧,宽,高

t=Thread(target=write).start()
input('Enter any key to end the recording:')
cap.release()
