#!/bin/bash -ue
echo Nuubo_assessment.json
python /app/aggregation.py -b metrics_output -a Nuubo_assessment.json -o results_dir --offline 1
