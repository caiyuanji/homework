#!/bin/bash

if [ -z $1 ] ; then
	echo "Syntax error，Usage: sh $0 ImageName:Tag"
else
	docker build -t $1 ./
	docker push $1
fi
