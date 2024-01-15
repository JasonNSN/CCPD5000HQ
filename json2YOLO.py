import os
import json

"""将json格式标注文件转为YOLO格式"""

filedir = './labelme2yolo'
files = os.listdir(filedir)
for file in files:
    if os.path.splitext(file)[1] != '.json':
        continue
    filename = os.path.splitext(file)[0]  # 文件名
    i = int(filename.split('CCPD')[1])
    f = open(filedir + './' + file, 'r')
    content = f.read()
    a = json.loads(content)  # json文件
    f.close()

    [point_lt, point_rb] = a['shapes'][0]['points']
    plate_number = a['shapes'][0]['description']
    [point1] = a['shapes'][1]['points']  # 左上角
    [point2] = a['shapes'][2]['points']  # 右上角
    [point4] = a['shapes'][3]['points']  # 左下角
    [point3] = a['shapes'][4]['points']  # 右下角
    height = a['imageHeight']
    width = a['imageWidth']

    content = []  # 要写入label的数组
    if i <= 2499:
        content.append(0)
    else:
        content.append(1)
    cx = ((point_lt[0] + point_rb[0]) / 2) / width  # 归一化Bounding Box中心点x
    cy = ((point_lt[1] + point_rb[1]) / 2) / height  # 归一化Bounding Box中心点y
    content.append(round(cx, 5))
    content.append(round(cy, 5))

    bb_width = (point_rb[0] - point_lt[0]) / width  # 归一化Bounding Box宽度
    bb_height = (point_rb[1] - point_lt[1]) / height  # 归一化Bounding Box宽度
    content.append(round(bb_width, 5))
    content.append(round(bb_height, 5))

    content.append(round(point1[0] / width, 5))
    content.append(round(point1[1] / height, 5))
    content.append(2)
    content.append(round(point2[0] / width, 5))
    content.append(round(point2[1] / height, 5))
    content.append(2)
    content.append(round(point3[0] / width, 5))
    content.append(round(point3[1] / height, 5))
    content.append(2)
    content.append(round(point4[0] / width, 5))
    content.append(round(point4[1] / height, 5))
    content.append(2)

    with open('{}/{}.txt'.format(filedir, filename), 'w') as f2:
        f2.write(' '.join(str(item) for item in content))

    print(i)
