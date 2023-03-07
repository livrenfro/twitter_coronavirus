# Project Details

The purpose of this project is to scan all geotagged tweets sent in 2020 to monitor for the spread of the coronavirus on social media.
This project was divided into three main components: 
1. Mapping
2. Reduing
3. Visualizing

 The `map.py` file processes the zip file for an individual day. The shell script `run\_maps.sh` takes advantage of the glob operator and a simple for loop, paired with a `no hup` command to process all tweets from 2020 in parallel. After being mapped, the files were reduced into a file for language data and a file for country data, under `reduced.lang` and `reduced.country`. The last step was visualizing the top ten countries and languages per input hashtag, the results graphs tested on `#coronavirus` and `#코로나바이러스`. The Korean hashtag was accommodated in the figures through custom font loading. 

The outputs from the MapReduce exercise are as follows:

<img src=plots/reduced.country_coronavirus_final.png width=100% />

<img src=plots/reduced.lang_coronavirus_final.png width=100% />

<img src=plots/reduced.country_코로나바이러스_final.png width=100% />

<img src=plots/reduced.lang_코로나바이러스_final.png width=100% />
