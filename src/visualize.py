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

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
print(items)
print(type(items))
print(type(items[1]))

for k,v in items:
    print(k,':',v)

import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

items.sort(key=lambda x: x[1], reverse=True) 
k = list(zip(*items))[0]
v = list(zip(*items))[1]
x_pos = np.arange(len(k)) 

plt.bar(x_pos[0:10],v[0:10], data=items)
plt.ylabel('Number of Tweets')
argument = args.input_path
plt.xlabel("{}".format(argument))
key = args.key[1:]
name = "{}.{}_graph.png".format(argument,key)
plt.savefig(name)
