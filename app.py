from flask import Flask, render_template
import pandas as pd
import os
# import cv2

app = Flask(__name__)
path = "static/images"
images = os.listdir(path)

labels = ['가진기 소음','센터콘솔 암레스트 래틀1', '센터콘솔 암레스트 래틀2','센터콘솔 암레스트 래틀3', '시트레일 래틀1','시트레일 래틀2','시트 백보드 래틀','썬바이저 래틀','CPAD 래틀','2열시트 암레스트 래틀']
bsr_idx = 1
# path = "static/data/sample{}.csv".format(bsr_idx)
path = "static/data/Y_hat_test.csv"
df = pd.read_csv(path, header=None)
df.columns = labels


#get images from video
# vidcap = cv2.VideoCapture('sample.mp4')
#
# def getFrame(sec, count):
#     vidcap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
#     hasFrames, image = vidcap.read()
#     if hasFrames:
#         resize_img = cv2.resize(image, (0, 0), fx=1 / 3, fy=1 / 3)
#         crop_img = resize_img[0:100, 220:370]
#         cv2.imwrite(path+'/image' + str(count).zfill(3) + ".jpg", crop_img)  # save frame as JPG file
#
#     return hasFrames
#
#
# count = 0
# sec = 0
# frameRate = 1
# success = getFrame(sec, count)
# while success:
#     sec = sec + frameRate
#     sec = round(sec, 2)
#     success = getFrame(sec, count)
#     count += 1




@app.route("/")
def chart():
    colors = ['#75a3d4', '#F28E2B', '#E15759', '#76B7B2', '#59A14F', '#EDC948', '#B07AA1', '#FF9DA7', '#af9181', '#BAB0AC']

    legends = [df.columns[i] for i in range(10)]
    value_list = [list(df[legend].values) for legend in legends]
    duration = [[0,0,0,0,0,0,0,0,0,0]]
    for i in range(len(df)):
        temp = [x for x in duration[i]]
        for j in range(10):
            if df.loc[i][j] > 0.9:
                temp[j] = round(temp[j]+0.02, 2)
        duration.append(temp)



    return render_template('main.html', value_list=value_list, legends=legends, colors=colors, images=images, row_valuelist = duration)




if __name__ == '__main__':
    app.run(host='0.0.0.0')
