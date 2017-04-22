#!/bin/bash
if [ -f "$1.html" ]
then
    echo "The file $1.html already exist, Master"
else
    touch $1.html
    echo "The file $1.html has been created on $PWD, Master"
    echo "<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    
</body>
</html>" > $1.html
fi