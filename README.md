# Hello World

Hello world Docker image for testing :).

This is referenced in <https://blog.openshift.com/telepresence-local-development/> and at various places in [the Telepresence documentation](https://www.telepresence.io/discussion/overview).

## Usage

### Clone this repository

Open up your terminal, and then run something similar to the below commands.
```shell
cd ~
mkdir code
cd code
git clone git@github.com:rewardops/k8s-workshop.git
```
If you want to put the repo somewhere other than in `~/code`, feel free.

### Run it locally

```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -qr requirements.txt

$ python3 server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 196-776-054
127.0.0.1 - - [03/Apr/2019 13:07:30] "GET / HTTP/1.1" 200 -
[...]
```

Does your terminal output look similar to the above? Yes? Great! You just started up a sample Flask server. You can close the Flask server with control+c now and move onto the next step.

### Build a Docker image

```shell
$ docker build -t rewardops/k8s-workshop .
Sending build context to Docker daemon  20.99kB
Step 1/7 : FROM python:3-alpine
 ---> a93594ce93e7
Step 2/7 : WORKDIR /usr/src/app
 ---> Running in 99c72d9f80c6
Removing intermediate container 99c72d9f80c6
 ---> ae6cf20413de
Step 3/7 : EXPOSE 8000
 ---> Running in 5feb111b3909
Removing intermediate container 5feb111b3909
 ---> b02c0d3d44cb
Step 4/7 : COPY requirements.txt .
 ---> f78be477ef4c
Step 5/7 : RUN pip install -qr requirements.txt
 ---> Running in 81044c1a701a
Removing intermediate container 81044c1a701a
 ---> f34572dbcf4a
Step 6/7 : COPY server.py .
 ---> 49185ab473c5
Step 7/7 : CMD ["python3", "./server.py"]
 ---> Running in 2446171f3946
Removing intermediate container 2446171f3946
 ---> 7d692d619894
Successfully built 7d692d619894
Successfully tagged rewardops/k8s-workshop:latest
```

### Run it in Docker

Build the image first, then launch it using `docker run`.

```shell
$ docker run --rm -it -p 8000:8000 rewardops/k8s-workshop
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 121-217-524
172.17.0.1 - - [03/Apr/2019 17:04:59] "GET / HTTP/1.1" 200 -
```

Now open up your web browser and navigate to http://0.0.0.0:8000 . If your browser says "Hello, world!" and if you see output similar to the above in your terminal, then congrats, you just ran the Flask server in a Docker coontainer.

### Run it in minikube
```shell
minikube start
eval $(minikube -p minikube docker-env)
docker build -t rewardops/k8s-workshop .
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/secrets.yaml
kubectl apply -f k8s/service.yaml
minikube service hello-world
```

### Clean up

Delete minikube
```shell
minikube delete
```

If you are running it from your laptop and would like to clean all images you can run:
```shell
docker system prune -a
```
## License

Licensed under Apache 2.0. Please see [License](LICENSE) for details.
