# ml
machine learning

# 创建实验环境

- docker pull tensorflow/tensorflow:latest
- docker run -it -d -p 6006:6006 -p 8888:8888 -v <host-path>:<container-path>  tensorflow/tensorflow bash
- docker exec -it <container_id> bash
