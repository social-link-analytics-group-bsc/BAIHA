#!/bin/bash -ue
python /app/aggregation.py -b metrics_output -a Nuubo_assessment.json -o results_dir --offline 1
python /app/merge_data_model_files.py -v Nuubo_validation.json -m metrics_output -c training_dataset -a results_dir -o consolidated_result.json
