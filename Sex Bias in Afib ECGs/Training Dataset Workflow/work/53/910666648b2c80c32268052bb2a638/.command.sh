#!/bin/bash -ue
echo challenge_id
python /app/training_dataset_test.py -i Nuubo_dataset.csv -p Nuubo -com BAIHA -c training_dataset -o Nuubo_assessment.json
