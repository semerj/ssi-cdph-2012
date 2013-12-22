#!/usr/bin/Python

from itertools import groupby
import pandas as pd
import re
import os
import glob

def main(doc):
    pages = []
    with open(doc, 'r') as inputfile:
	fx = lambda x:re.search(r'Page \d+ of \d+', x)
	for k, g in groupby(inputfile, key=fx):
	    if not k:
	        pages.append(list(g))

    # for all lines with 5 capitalized letters, return a list if srings are separated by 2 or more spaces
    data = pd.DataFrame()
    procs = []
    for p in pages:
        df = [re.split(r'\s{2,}', d.strip()) for d in p if re.findall(r'[A-Z]{5}', d)]
        df = pd.DataFrame(df)
        matched = re.findall(r'for (?!the )([^]]*) in', " ".join(p[0:2]).replace('\n', ''))
        if matched:
            procs.append(matched[0])
            df['procs'] = matched[0]
        data = data.append(df)

    data.columns = ['hosp', 'procCount', 'infCount', 'sir', 'ci', 'comp', 'procs']
    
    data['ci'] = data['ci'].str.replace('[(,)]', '')
    data['ci-low'] = data.ci.str.split().str[0]
    data['ci-high'] = data.ci.str.split().str[1]
    del data['ci']
    data = data[['hosp', 'procs', 'procCount', 'infCount', 'sir', 'ci-low', 'ci-high', 'comp']]
    
    data.to_csv(str(file.split('.')[0]) + '.csv', index=False)

if __name__ == "__main__":
    txt_files = glob.glob('*.txt')
    for txt in txt_files:
        main(txt)
