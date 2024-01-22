
FROM  python:3.10-slim 
COPY . /LoadBalancer

WORKDIR /LoadBalancer

# COPY requirements.txt .

# RUN --mount=type=cache,target=/root/.cache/pip \
#     pip3 install -r requirements.txt

# RUN pip3 install -r requirements.txt
# RUN --mount=type=cache,target=/root/.cache/pip \
#     pip3 install -r requirements.txt

ENV server_id = 1
RUN apt-get update
RUN apt-get -y install sudo

# RUN apt-get update && \
#     apt-get -y install apt-transport-https ca-certificates curl gnupg software-properties-common

# # RUN apt-get -y install apt-transport-https ca-certificates curl gnupg2 software-properties-common
# RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
# RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
# RUN apt-get update
# RUN apt-get -y install docker-ce-cli

# Install dependencies

# Install Docker
# RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
# RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
# RUN apt-get update && \
#     apt-get -y install docker-ce-cli
RUN apt-get update
RUN sudo apt-get install -y gnupg
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/docker-archive-keyring.gpg
RUN sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
RUN sudo apt install update

RUN sudo apt install docker-ce docker-ce-cli containerd.io
EXPOSE 5000
# run pip install flask
CMD ["python","App.py"]