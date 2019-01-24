# ml
machine learning

## experimental environment

#### CPU

- docker pull tensorflow/tensorflow:latest
- docker run -it -d -p 6006:6006 -p 8888:8888 -v <host-path>:<container-path>  tensorflow/tensorflow bash
- docker exec -it <container_id> bash
  
### GPU
`note: If it is a GPU machine, you need to install GPU driver.`

- docker pull tensorflow/tensorflow:latest-gpu 
- docker run -it -d -p 6006:6006 -p 8888:8888 -v <host-path>:<container-path>  tensorflow/tensorflow:latest-gpu  bash
- docker exec -it <container_id> bash
