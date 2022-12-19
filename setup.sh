#! /bin/bash
pip3 install selenium
pip3 install webdriver-manager
docker-compose -f docker-compose.yaml up -d
# Prepare testdata
mkdir testdata
wget https://download.jetbrains.com/datagrip/datagrip-2022.3.1.tar.gz -O testdata/datagrip.tar.gz
echo "hello this normal file" > testdata/normal_file.txt