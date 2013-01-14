'''Usage: barchart_top_issues.py <rating.csv file> <topn>

By Saravana <tutysara@gmail.com>'''

import csv
import sys
from pylab import *

fileName = sys.argv[1]
topn = int(sys.argv[2])

def getRatings(fileName, topn):
    issues = []
    ratings = []
    f = open(fileName)
    reader = csv.reader(f)
    reader.next() # neglect headers
    for issue, rating in reader:
        issues.append(issue)
        ratings.append(float(rating))
    labels = issues[0:topn] # take top n values
    data =   ratings[0:topn]
    x = arange(1, len(data)+1)
    y = data
    width = 1 # adjust for bar thickness
    fig = plt.figure()
    fig.subplots_adjust(bottom=0.6) # reduce this percentage to reduce sapce at the bottom of graph         
    ax = fig.add_subplot(111)
    ax.bar(x,y)
    ax.ticklabel_format(style='plain')       
    ax.set_yticks(arange(1,11))
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45)
    ax.set_xlabel("Performace Area")
    ax.set_ylabel("Score (out of 10)")
    plt.savefig(fileName+".png")
