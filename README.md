#  Installing Qiskit in your M1 machine

## Contents
-[Requirements](#Requirements)

-[Installation](#Installation)


# Requirements 

-[Download docker:](https://docs.docker.com/desktop/mac/apple-silicon/) docker desktop for Apple siclicon machines
<p  align="center">
<img width 600 src = "https://raw.githubusercontent.com/jpbayonap/qiskit-docker/master/DockerM1.png" >
</p>


- `Install rosseta:` install Rosetta 2 manually from the command line
```shell
softwareupdate --install-rosetta  
```

# Installation

- Clone the following Github repository
```shell
git clone https://github.com/jpbayonap/qiskit-docker
cd qiskit-docker
```
- In order to use Docker, the Docker desktop application must be running 
<p  align="center">
<img width 600 src = "https://raw.githubusercontent.com/jpbayonap/qiskit-docker/master/DockerApp.png">
</p>


- Build an image for your docker container
 ```shell
  docker-compose build 
 ```
 - Build and run the container 
```shell
docker-compose up
```


# Open Jupyter Notebook


Open the following link in your browser 

[Launch jupyter notebook](http://localhost:8888/?token=abcd):  http://localhost:8888/?token=abcd


`In order to use jupyter notebook, your Docker container must be running in the Docker desktop. `






# Adding python libraries

- In order to add python libraries to your container, you shoul modify the [Dockerfile](./Dockerfile) in the current folder `(qiskit-docker/)`
 ```docker
 ## Add Python libraries for your projects/新しいらいバリをインストールする
#example/例  RUN python -m pip install ライバリ名

RUN python -m pip install pandas
 ```

 - Update the  docker image

 ```shell
 docker-compose build
  ```

# Stop running container
After finishing running your scripts you may stop your running container by typing the following 
- usage

```shell
docker stop python-qiskit
```

# Start container

To start your container type the following command 


- usage

```shell
docker start python-qiskit
```
