#!/bin/bash
app="kommcenta/news-service:v1.0.0"
docker build -t ${app} .
docker run -d -p 8090:5000 \
  --name=kc-news-service \
  -v $PWD:/app ${app}
