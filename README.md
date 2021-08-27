## 学校训练营作业：使用yolov4-tf2对部分垃圾进行垃圾分类
---
注：作业中使用的yolov4-tf2链接：https://github.com/bubbliiiing/yolov4-tf2  

## 作业说明
3月本来打算利用这个yolov4-tf2做一个智能垃圾桶参加全国大学生工程训练综合能力竞赛，奈何团队对于机械结构的设计十分不精，其他方面能力也不太行，最后半途而废，这是一个半成品，但又刚好符合本次训练营的作业要求，于是作为作业上传（本来想再训练一下提高模型的精度，但是我的电脑实在是跑不动了）

## 作业内容
本次作业主要对如下垃圾进行了垃圾分类：（参考全国大学生工程训练综合能力竞赛）
有害垃圾（Harmful Waste）：电池（battery）
可回收垃圾（Recyclable Waste）：塑料瓶（plastic bottle） 易拉罐（can）
厨余垃圾（Kitchen Waste）：水果（fruit） 蔬菜（vegetable）
其他垃圾（Other Waste）：瓷片砖瓦（china） 烟头（cigarette）
```python
classes_path = 'model_data/trash_classes.txt' 
classes = ["battery", "plastic bottle", "can", "fruit", "vegetable", "china", "cigarette"]
```
训练所用图片存放在 VOCdevkit\VOC2007\JPEGImages 路径中 
图片对应的数据集存放在 VOCdevkit\VOC2007\Annotations 路径中 
训练权重使用的是yolo4_weight.h5
数据集下载：
链接：https://pan.baidu.com/s/11T7NXy1DllZKoYBz0GSs0g 
提取码：rqhm 

当时训练的时候batch_size我们用的是3，但总会出现显存不足的报错
下调batch_size又会使训练时长变长不少
由于我们太菜不知道怎么解决这个问题
试过几次之后实在没有办法就直接采用了训练到一半的模型进行预测
因此这个模型的正确率并不是很理想
我们训练得到的模型(存放在logs文件夹中）下载链接：
链接：https://pan.baidu.com/s/1kVdMDX18wDQ55Wx9CF_rxg 
提取码：79wl
训练权重文件见下方原作者作者内容

当时做这个项目的时候本打算先把垃圾识别出来再进行分类
然后为了省事就直接改了一下yolo.py文件里的detect_image()函数
在这个函数里进行垃圾分类的操作
因此这个项目要用于其他用途时还需要改一下这个函数

正如我前文所述 这个项目本打算来参加比赛
所以根目录里还有一些其他的文件:bin.py take_out.py take_photo.py
这些都是为做垃圾桶准备的在树莓派上跑的
由于能力有限 代码写得十分拙劣
大可忽略这些内容

## 团队成员及分工
廖乾超：项目寻找 数据集制作
汪田径：数据集制作 训练调整模型
宋继峰：数据集制作 代码改进 
王子诚：爬取训练图片

## 下面是原作者关于yolov4-tf2的说明


## YOLOV4：You Only Look Once目标检测模型在Tensorflow2当中的实现

**2021年2月7日更新：**   
**加入letterbox_image的选项，关闭letterbox_image后网络的map得到大幅度提升。**

## 目录
1. [性能情况 Performance](#性能情况)
2. [实现的内容 Achievement](#实现的内容)
3. [所需环境 Environment](#所需环境)
4. [注意事项 Attention](#注意事项)
5. [小技巧的设置 TricksSet](#小技巧的设置)
6. [文件下载 Download](#文件下载)
7. [预测步骤 How2predict](#预测步骤)
8. [训练步骤 How2train](#训练步骤)
9. [参考资料 Reference](#Reference)

## 性能情况
| 训练数据集 | 权值文件名称 | 测试数据集 | 输入图片大小 | mAP 0.5:0.95 | mAP 0.5 |
| :-----: | :-----: | :------: | :------: | :------: | :-----: |
| VOC07+12+COCO | [yolo4_voc_weights.h5](https://github.com/bubbliiiing/yolov4-tf2/releases/download/v1.0/yolo4_voc_weights.h5) | VOC-Test07 | 416x416 | - | 88.9
| COCO-Train2017 | [yolo4_weight.h5](https://github.com/bubbliiiing/yolov4-tf2/releases/download/v1.0/yolo4_weight.h5) | COCO-Val2017 | 416x416 | 46.4 | 70.5

## 实现的内容
- [x] 主干特征提取网络：DarkNet53 => CSPDarkNet53
- [x] 特征金字塔：SPP，PAN
- [x] 训练用到的小技巧：Mosaic数据增强、Label Smoothing平滑、CIOU、学习率余弦退火衰减
- [x] 激活函数：使用Mish激活函数
- [ ] ……balabla


## 所需环境
tensorflow-gpu==2.2.0  

## 注意事项
代码中的yolo4_weights.h5是基于608x608的图片训练的，但是由于显存原因。我将代码中的图片大小修改成了416x416。有需要的可以修改回来。 代码中的默认anchors是基于608x608的图片的。  

**这个库里面的h5和Keras的h5不同，不要混用。**   
**视频中说的速度慢问题已经解决了很多，现在train.py和train_eager.py速度差距不大，如果还有改进速度的地方可以私信告诉我!**  

**注意不要使用中文标签，文件夹中不要有空格！**   
**在训练前需要务必在model_data下新建一个txt文档，文档中输入需要分的类，在train.py中将classes_path指向该文件**。  

## 小技巧的设置
在train.py和train_eager.py文件下：   
1、mosaic参数可用于控制是否实现Mosaic数据增强。   
2、Cosine_scheduler可用于控制是否使用学习率余弦退火衰减。   
3、label_smoothing可用于控制是否Label Smoothing平滑。  

在train_eager.py文件下：   
1、regularization参数可用于控制是否实现正则化损失。  

## 文件下载
训练所需的yolo4_weights.h5可在百度网盘中下载。  
链接: https://pan.baidu.com/s/1jDOPTel7mTXxNDliuKbmvA 提取码: irgc   
yolo4_weights.h5是coco数据集的权重。  
yolo4_voc_weights.h5是voc数据集的权重。

## 预测步骤
### a、使用预训练权重
1. 下载完库后解压，在百度网盘下载yolo4_weights.h5或者yolo4_voc_weights.h5，放入model_data，运行predict.py，输入  
```python
img/street.jpg
```  
2. 利用video.py可进行摄像头检测。  
#### b、使用自己训练的权重
1. 按照训练步骤训练。  
2. 在yolo.py文件里面，在如下部分修改model_path和classes_path使其对应训练好的文件；**model_path对应logs文件夹下面的权值文件，classes_path是model_path对应分的类**。  
```python
_defaults = {
    "model_path": 'model_data/yolo4_weight.h5',
    "anchors_path": 'model_data/yolo_anchors.txt',
    "classes_path": 'model_data/coco_classes.txt',
    "score" : 0.5,
    "iou" : 0.3,
    # 显存比较小可以使用416x416
    # 显存比较大可以使用608x608
    "model_image_size" : (416, 416)
}
```
3. 运行predict.py，输入  
```python
img/street.jpg
```
4. 利用video.py可进行摄像头检测。   

## 训练步骤
1. 本文使用VOC格式进行训练。  
2. 训练前将标签文件放在VOCdevkit文件夹下的VOC2007文件夹下的Annotation中。  
3. 训练前将图片文件放在VOCdevkit文件夹下的VOC2007文件夹下的JPEGImages中。  
4. 在训练前利用voc2yolo4.py文件生成对应的txt。  
5. 再运行根目录下的voc_annotation.py，运行前需要将classes改成你自己的classes。**注意不要使用中文标签，文件夹中不要有空格！**   
```python
classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
```
6. 此时会生成对应的2007_train.txt，每一行对应其**图片位置**及其**真实框的位置**。  
7. **在训练前需要务必在model_data下新建一个txt文档，文档中输入需要分的类，在train.py中将classes_path指向该文件**，示例如下：   
```python
classes_path = 'model_data/new_classes.txt'    
```
model_data/new_classes.txt文件内容为：   
```python
cat
dog
...
```
8. 运行train.py即可开始训练。

## mAP目标检测精度计算更新
更新了get_gt_txt.py、get_dr_txt.py和get_map.py文件。  
get_map文件克隆自https://github.com/Cartucho/mAP  
具体mAP计算过程可参考：https://www.bilibili.com/video/BV1zE411u7Vw

## Reference
https://github.com/qqwweee/keras-yolo3/  
https://github.com/Cartucho/mAP  
https://github.com/Ma-Dan/keras-yolo4  

