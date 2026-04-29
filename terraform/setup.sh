#!/bin/bash
sudo apt-get update
sudo apt-get install -y docker.io docker-compose
git clone https://github.com/your-repo/microservices.git
cd microservices
sudo docker-compose up -d
