#!/bin/bash
# Test All the testcase
for test in $(ls  | grep '.py'); 
do
	python $test
done;