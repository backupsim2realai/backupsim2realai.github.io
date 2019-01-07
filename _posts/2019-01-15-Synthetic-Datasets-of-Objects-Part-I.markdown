---
layout: post
title: "Cataloguing Datasets of 3D Objects: Part I"
date: 2019-01-15 13:32:20 +0100
description: Cataloguing datasets of object models # Add post description (optional)
img:  # Add image post (optional)
---

Desirable properties for any object dataset

-  Large size
-  Variation 
-  Diversity 
-  Parametric representation 
-  High Entropy (balance in the classes) 

### Historic Perspective 


<!--[![](/assets/img/2019-01-15/The-history-of-CAD_CADENAS_R3.jpg)](/assets/img/2019-01-15/The-history-of-CAD_CADENAS_R3.jpg)
-->

Sizing image
![](/assets/img/2019-01-15/The-history-of-CAD_CADENAS_R3.jpg){:height="50%" width="50%"}

<!--<center><img src="/assets/img/2019-01-15/The-history-of-CAD_CADENAS_R3.jpg" width="1024"></center>
-->

Credits: https://partsolutions.com/wp-content/uploads/2017/09/The-history-of-CAD_CADENAS_R3.png

STL format explanation https://all3dp.com/what-is-stl-file-format-extension-3d-printing/

### Synthetic Datasets

|           Dataset          | Year |    Articulations   |                                Source Link                               |
|:--------------------------:|:----:|:------------------:|:------------------------------------------------------------------------:|
|   NTU 3D Model  Benchmark  | 2003 |         :x:        |                        http://3d.csie.ntu.edu.tw/                        |
|  Mesh Deformation Dataset  | 2004 |         :x:        |     http://people.csail.mit.edu/sumner/research/deftransfer/data.html    |
|         PrincetonSB        | 2004 |         :x:        |                 http://shape.cs.princeton.edu/benchmark/                 |
| AIM@SHAPE shape Repository | 2006 |         :x:        |      http://visionair.ge.imati.cnr.it/ontologies/shapes/releases.jsp     |
|  McGill 3D Shape Benchmark | 2008 |         :x:        |                http://www.cim.mcgill.ca/~shape/benchMark/                |
|          SHREC' 08         | 2008 |         :x:        |              https://engineering.purdue.edu/PRECISE/shrec08              |
|   Columbia Grasp Database  | 2009 |         :x:        |                     http://grasping.cs.columbia.edu/                     |
|          SHREC' 10         | 2010 |         :x:        |       http://tosca.cs.technion.ac.il/book/shrec_robustness2010.html      |
|  Toyohashi Shape Benchmark | 2012 |         :x:        |                http://www.kde.cs.tut.ac.jp/benchmark/tsb/                |
|            IKEA            | 2013 |         :x:        |                        http://ikea.csail.mit.edu/                        |
|          PASCAL3D+         | 2014 |         :x:        |              http://cvgl.stanford.edu/projects/pascal3d.html             |
|            CAPOD           | 2014 |         :x:        |           https://sites.google.com/site/pgpapadakis/home/CAPOD           |
|          ModelNet          | 2015 |         :x:        |                     http://modelnet.cs.princeton.edu/                    |
|            NIST            | 2016 | :heavy_check_mark: | https://catalog.data.gov/dataset/nist-cad-models-and-step-files-with-pmi |
|          Thingi10K         | 2016 |         :x:        |                 https://ten-thousand-models.appspot.com/                 |
|         ObjectNet3D        | 2016 |         :x:        |              http://cvgl.stanford.edu/projects/objectnet3d/              |
|          ShapeNet          | 2016 |         :x:        |                         https://www.shapenet.org/                        |
|           PartNet          | 2018 | :heavy_check_mark: |                 https://cs.stanford.edu/~kaichun/partnet/                |
|             ABC            | 2018 | :heavy_check_mark: |                   https://arxiv.org/pdf/1812.06216.pdf                   |

Talk about DexNet: https://berkeleyautomation.github.io/dex-net/

CAPOD dataset: https://sites.google.com/site/pgpapadakis/home/CAPOD

<center><img src="/assets/img/2019-01-15/object_datasets.jpg" width="640"></center>

### Real World Datasets

|        Dataset       | Year |    Articulations   |                          Source Link                          |
|:--------------------:|:----:|:------------------:|:-------------------------------------------------------------:|
|         B3DO         | 2011 |         :x:        |                     http://kinectdata.com/                    |
| RGB-D Object Dataset | 2011 |         :x:        |        http://rgbd-dataset.cs.washington.edu/index.html       |
|          KIT         | 2012 |         :x:        | https://journals.sagepub.com/doi/abs/10.1177/0278364912445831 |
|        BigBird       | 2014 |         :x:        |                http://rll.berkeley.edu/bigbird/               |
|          YCB         | 2015 |         :x:        |                 http://www.ycbbenchmarks.com/                 |
|        3DScan        | 2016 |         :x:        |                http://redwood-data.org/3dscan/                |
|        T-LESS        | 2017 |         :x:        |                http://cmp.felk.cvut.cz/t-less/                |
|          RBO         | 2018 | :heavy_check_mark: |         https://tu-rbo.github.io/articulated-objects/         |


<center><img src="/assets/img/2019-01-15/book_cabinet_rubiks.gif" height="200"></center>

More datasets in the table here https://arxiv.org/pdf/1502.03143.pdf


> For physics simulation, articulations in the form of hinges and joints as well as collisions shapes of objects in the form of bounding volumes etc. are important.

Collision Shapes: https://www.toptal.com/game/video-game-physics-part-ii-collision-detection-for-solid-objects



#### Authors 
Ankur Handa and Miles Brundage
