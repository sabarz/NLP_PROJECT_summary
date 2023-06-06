#!/bin/bash
cd ..
cd src
cd final\final\spiders
scrapy runspider books.py 
cd ..
cd ..
python cleaning.py
python sentenceBroken.py
python wordBroken.py
cd ..
cd ..
cd stats
python stats.py
cd ..
pdflatex -interaction=nonstopmode -output-directory=$(dirname "./Phase1-Report.pdf") "./stats/main.tex"
