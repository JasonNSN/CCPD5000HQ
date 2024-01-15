# CCPD5000HQ数据集

包含了图片以及对应的.json标注文件，可以直接用labelme打开

前2500张图片为绿牌（来自CCPD2020），后2500张图片为蓝牌（来自CCPD2019）

链接：

- [百度网盘](https://pan.baidu.com/s/1cfOVSorQ738E6Prs8cNnbA?pwd=rk1u)
- [Google Drive](https://drive.google.com/file/d/15TdoN9y7nnhFMNpfLE28v3doQ7Hqpc0T/view?usp=drive_link)

# CCPD5000HQ_YOLO数据集

包含了图片以及对应的YOLO格式的.txt标注文件，并且划分了训练集、验证集、测试集，可以直接拿来训练YOLOv8模型

前2500张图片为绿牌（来自CCPD2020，类别为0），后2500张图片为蓝牌（来自CCPD2019，类别为1）

链接：

- [百度网盘](https://pan.baidu.com/s/1We3Fcd9Z4Al4HSoPyUXQvQ?pwd=q2h8)
- [Google Drive](https://drive.google.com/file/d/1NZ4yYoSFmftT-xSLCmuM7dBkPgKlM4sd/view?usp=drive_link)

**并且提供了相应的Python代码（json2YOLO.py），可以直接将.json文件转为YOLO格式的.txt文件**

# 参考链接

CCPD数据集：https://github.com/detectRecog/CCPD

Labelme：https://github.com/labelmeai/labelme
