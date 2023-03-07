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

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=False)
print(items)
print(type(items))
print(type(items[1]))

for k,v in items:
    print(k,':',v)

#if os.environ.get('DISPLAY','') == '':
 #   print('no display found. Using non-interactive Agg backend')
  #  mpl.use('Agg')

# sorting, taking top ten, storing in variables
items = items[:10]
k = list(zip(*items))[0]
v = list(zip(*items))[1]

plt.bar(k,v, color='olive')
plt.ylabel('Number of Tweets')
argument = args.key[1:]
plt.xlabel("Hashtag: " + ("{}".format(argument)).replace("_", " ").title())

key = args.input_path
name = "{}.{}_graph".format(key, argument)
plt.savefig("plots/" + name + ".png")
