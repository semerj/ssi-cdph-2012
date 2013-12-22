#!/bin/bash

wget http://www.cdph.ca.gov/programs/hai/Documents/2012-SSI-T1-T12.pdf
wget http://www.cdph.ca.gov/programs/hai/Documents/2012-SSI-T13-T24.pdf

for f in *.pdf
do
  qpdf --password= --decrypt $f out-$f
  pdftotext -layout out-$f
done

python ssi2012.py

rm -r *.pdf *.txt
