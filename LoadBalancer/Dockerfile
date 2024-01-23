FROM  python:3.10-slim 

COPY . /LoadBalancer

WORKDIR /LoadBalancer
EXPOSE 5000     
# COPY requirements.txt .

# RUN --mount=type=cache,target=/root/.cache/pip \
#     pip3 install -r requirements.txt

# RUN --mount=type=cache,target=/root/.cache/pip \
#     pip3 install -r requirements.txt

ENV server_id = 1
RUN pip install --trusted-host pypi.python.org flask


# run pip install flask
CMD ["python","App.py"]