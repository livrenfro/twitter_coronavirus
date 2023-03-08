#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt 
from matplotlib.font_manager import FontProperties
import numpy as np
import pandas as pd

#font stuff
properties = []
properties.append(FontProperties(fname='/home/Olivia.Renfro.23/twitter_coronavirus/NotoSerifKR-Light.otf'))
print(properties)
#font_dir = ['/home/Olivia.Renfro.23/twitter_coronavirus/NotoSerifKR-Light.otf']
#font_manager.fontManager.addfont('/home/Olivia.Renfro.23/twitter_coronavirus/NotoSerifKR-Light.otf')


# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)[:10]
print(items)
print(type(items))
print(type(items[1]))

for k,v in items:
    print(k,':',v)

#if os.environ.get('DISPLAY','') == '':
 #   print('no display found. Using non-interactive Agg backend')
  #  mpl.use('Agg')

# sorting, taking top ten, storing in variables
#items = sorted(sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)[:10], key=lambda x: x[1])

topten = sorted(sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)[:10], key=lambda x: x[1])
print("Top 10=", topten)

x = []
y = []
for k, v in topten:
    x.append(k)
    y.append(v)
print(x)
print(y)
x = pd.Categorical(x, categories = x , ordered = True)
#xs, ys = zip(*sorted(zip(x, y)))

#df = pd.DataFrame(items, columns=['x', 'y'])
#df = df.sort_values("y")
#k = list(zip(*items))[0]
#v = list(zip(*items))[1]

plt.bar(x,y, color='olive')
plt.ylabel('Number of Tweets')
argument = args.key[1:]
key = args.input_path
plt.xlabel(("{}".format(args.input_path)).replace("reduced.", " ").title())

if "코로나바이러스" in args.key: 
    language = "Korean"
else:
    language = "English"

if language == "Korean":
    plt.title("Hashtag Usage: " + args.key, fontproperties=properties[0])
else:
    plt.title("Hashtag Usage: " + args.key)

name = "{}_{}_foo".format(key, argument)
plt.savefig("plots/" + name + ".png")
