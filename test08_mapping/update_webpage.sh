#!/bin/sh

#environment

echo "Updating data..."

cd /home/jay/Opensource/COVID-19
git pull

echo "Setting conda environment..."
. "/home/jay/.bashrc_conda"

echo "Building data..."
cd /home/jay/Projects/MyCovid19/test08_mapping
./build_data.py

echo "Copying files..."
cp heatmap.html gendata.js /opt/jayflatland.com/covid/

echo "Done!"
