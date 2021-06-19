# 起動
```
docker-compose build
docker-compose run darknet bash
```

# YOLOv3-tiny 学習
```
cd /darknet/ws
mkdir backup

/darknet/darknet detector train ./data/obj.data ./yolov3-tiny.cfg ./yolov3-tiny.conv.11
```


# [補足] yolov3.cfgの変更箇所
1クラスの場合の例

max_batchesは 'クラス数 ☓ 2000'<br>
stepsはmax_batchesの80%と90%の値

classesはクラス数に合わせる<br>
filtersは '(クラス数 + 5) ☓ マスク数'

tinyの場合はclassesの指定が2箇所になる

```diff
--- yolov3.cfg.org	2021-04-30 05:42:14.331812130 +0000
+++ yolov3.cfg	2021-04-30 05:52:38.123834977 +0000
@@ -17,9 +17,9 @@
 
 learning_rate=0.001
 burn_in=1000
-max_batches = 500200
+max_batches = 2000
 policy=steps
-steps=400000,450000
+steps=1600,1800
 scales=.1,.1
 
 [convolutional]
@@ -600,14 +600,14 @@
 size=1
 stride=1
 pad=1
-filters=255
+filters=18	# (classes + 5) * mask_num
 activation=linear
 
 
 [yolo]
 mask = 6,7,8
 anchors = 10,13,  16,30,  33,23,  30,61,  62,45,  59,119,  116,90,  156,198,  373,326
-classes=80
+classes=1
 num=9
 jitter=.3
 ignore_thresh = .7
@@ -686,14 +686,14 @@
 size=1
 stride=1
 pad=1
-filters=255
+filters=18
 activation=linear
 
 
 [yolo]
 mask = 3,4,5
 anchors = 10,13,  16,30,  33,23,  30,61,  62,45,  59,119,  116,90,  156,198,  373,326
-classes=80
+classes=1
 num=9
 jitter=.3
 ignore_thresh = .7
@@ -773,14 +773,14 @@
 size=1
 stride=1
 pad=1
-filters=255
+filters=18
 activation=linear
 
 
 [yolo]
 mask = 0,1,2
 anchors = 10,13,  16,30,  33,23,  30,61,  62,45,  59,119,  116,90,  156,198,  373,326
-classes=80
+classes=1
 num=9
 jitter=.3
 ignore_thresh = .7
```
