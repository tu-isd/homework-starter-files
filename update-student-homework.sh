#!/usr/bin/env bash

if [ $# -ne 1 ]; then
	echo "usage: $0 <students-file>"
	exit 1
fi
students_file=$1

set -x

for student in $(cat $students_file)
do
	sysvbanner $student
	git checkout -b working-branch $student/master
	git merge master -m'Merge updated homework'
	git push $student HEAD:master
	git checkout master
	git branch -d working-branch
done
