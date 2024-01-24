#!/bin/bash -ue
echo Nuubo_assessment.json
python /app/aggregation.py -b metrics_output -a Nuubo_assessment.json -o results_dir --offline 1
python /app/merge_data_model_files.py -v Nuubo_validation.json -m Nuubo_assessment.json -c training_dataset -a results_dir -o consolidated_result.json
