#!/bin/bash
# Test All the testcase
time python ../source/main.py '../data/zhwiki-latest-pages-articles.xml.bz2' '../model/words.vec'
for test in $(ls  | grep '.py'); 
do
	time python $test
done;