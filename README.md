# ml
machine learning

## experimental environment

#### CPU

- docker pull tensorflow/tensorflow:latest
- docker run -it -d -p 6006:6006 -p 8888:8888 -v <host-path>:<container-path>  tensorflow/tensorflow bash
- docker exec -it <container_id> bash
  
### GPU
###### Note: If it is a GPU machine, you need to install [GPU driver](https://www.nvidia.com/Download/index.aspx?lang=en-us) and [nvidia-docker](https://github.com/NVIDIA/nvidia-docker).

- docker pull tensorflow/tensorflow:latest-gpu 
- nvidia-docker run -it -d -p 6006:6006 -p 8888:8888 -v <host-path>:<container-path>  tensorflow/tensorflow:latest-gpu  bash
- docker exec -it <container_id> bash
  
### Verify installation

```
# python
Python 2.7.12 (default, Dec  4 2017, 14:50:18)
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
>>> hello = tf.constant("Hello TensorFlow!")
>>> sess = tf.Session()
2019-01-25 07:32:53.678952: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
>>> print(sess.run(hello))
Hello TensorFlow!
>>>
```
