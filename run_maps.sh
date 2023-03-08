#!/bin/bash

#for i in /data/'Twitter dataset'/geoTwitter20*.zip;
#do nohup ./src/map.py --input_path="$i" > output_map/$(basename "$tweet"|cut -f 1 -d '.') & 
#done


for file in /data/Twitter\ dataset/*20-*
do nohup ./src/map.py --input_path="$file" > output_map/$(basename "$file"|cut -f 1 -d '.') & done
