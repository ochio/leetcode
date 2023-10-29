#!/bin/bash

question_title=$(echo $1 | cut -d'/' -f1)

git pull
git add $question_title
git commit -m "$question_title"
