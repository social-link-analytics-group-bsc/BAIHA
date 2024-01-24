#!/bin/bash -ue
echo challenge_id
python /app/training_dataset_test.py -i /home/cfurtick/Desktop/Projects/Severo Ochoa/Sex Bias in Afib ECGs/input_data/Nuubo_dataset.csv -p Nuubo -com BAIHA -c training_dataset -o Nuubo_assessment.json
