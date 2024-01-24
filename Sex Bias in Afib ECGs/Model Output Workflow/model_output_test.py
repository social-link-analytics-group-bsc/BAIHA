# METRICS:
# TP - True positives, model predicted positive and true value is positive (count)
# TN - True negatives, model predicted negative and true value is negative (count)
# FP - False positives, model predicted positive but true value is negative (count)
# FN - False negatives, model predicted negative but true value is positive (count)
# Overall accuracy - Equal accuracy (correct predictions) for each subgroup (TP + TN) / (total count)
# Statistical Parity - Fractions of assigned positive labels are the same in subgroups, 
#   or align with known percentage distributions (TP + FP) / (total count)
# Equal Opportunity - True positive rates are equal for subgroups TP / (TP + FN)
# Predictive Equality -  False positive rates are equal for subgroups FP / (FP + TN)
# False Negative Rate - False negative rates are equal for subgroups FN / (FN + TP)

# DATA FORMAT:
# - column labeled 'id' that is the unique identifier number of patient?
# From participant...
# - column labeled 'sex' that has sex of patient
# - column labeled 'model_output' that has 'Yes' for atrial fibrillation detected and 'No' for atrial fibrillation not detected BY MODEL
# From golden dataset...
# - column labeled 'true_value' that has '1' for atrial fibrillation and '0' for no atrial fibrillation

import numpy as np
import os
import pandas as pd
import math
import json
import io
from argparse import ArgumentParser
from JSON_templates import JSON_templates


def main(args):

    # input parameters
    input_model_output = args.input
    community = args.community_name
    challenges = args.challenges
    participant_name = args.participant_name
    gold_standards_dir = args.metrics_ref
    out_path = args.output

    # Assuring the output path does exist
    if not os.path.exists(os.path.dirname(out_path)):
        try:
            os.makedirs(os.path.dirname(out_path))
            with open(out_path, mode="a"):
                pass
        except OSError as exc:
            print("OS error: {0}".format(exc) + "\nCould not create output path: " + out_path)

    compute_metrics(input_model_output,  gold_standards_dir, challenges, participant_name, community, out_path)


def compute_metrics(input_model_output,  gold_standards_dir, challenges, participant_name, community, out_path):

    # Load model output
    df = pd.read_csv(input_model_output, sep='\t', comment="#", header=0)

    # Load true values 
    df_golden = pd.read_csv(gold_standards_dir, sep='\t', comment="#", header=0)
    df_golden = df_golden[['patient_id', 'true_value']]

    # Join model output and true values 
    # The resulting df will contain only the common key values between the two datasets, will drop ids that are in one but not the other
    df = df.join(df_golden, on='patient_id', how='inner')

    # Calculate simple metric values (TP, TN, FP, FN)
    TP = df[df['diagnosis'] == 'Yes' and df['true_value'] == 1]
    TN = df[df['diagnosis'] == 'No' and df['true_value'] == 0]
    FP = df[df['diagnosis'] == 'Yes' and df['true_value'] == 0]
    FN = df[df['diagnosis'] == 'No' and df['true_value'] == 1]
    total_count = len(df)

    # Calculate complex metrics 
    overall_accuracy = (TP + TN) / (total_count)
    statistical_parity = (TP + FP) / (total_count)
    equal_opportunity = TP / (TP + FN)
    predictive_equality = FP / (FP + TN)
    false_negative_rate = FN / (FN + TP)

    # Export metrics in correct format
    ALL_ASSESSMENTS = []
    assessment_data = {'toolname': participant_name, 'OA': overall_accuracy, 'SP': statistical_parity, 
                       'EO': equal_opportunity, 'PE': predictive_equality, 'FNR': false_negative_rate}
    
    for key, value in assessment_data.items():
        if key != 'toolname':
            data_id = community + ":" + "_" + key + "_" + participant_name + "_A"
            assessment = JSON_templates.write_assessment_dataset(data_id, community, participant_name, key, value)
            # push the assessment datasets for each metric to the main dataset array
            ALL_ASSESSMENTS.extend(assessment)

    # once all assessments have been added, print to json file
    with io.open(out_path,
                 mode='w', encoding="utf-8") as f:
        jdata = json.dumps(ALL_ASSESSMENTS, sort_keys=True, indent=4, separators=(',', ': '))
        f.write(jdata)


if __name__ == '__main__':
    
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", help="path to input dataset to be validated", required=True)
    parser.add_argument("-com", "--community_name", help="name of benchmarking community", required=True)
    parser.add_argument("-c", "--challenges", nargs='+', help="list the challenges that this input data is for", required=True)
    parser.add_argument("-p", "--participant_name", help="name of the tool used for prediction", required=True)
    parser.add_argument("-o", "--output", help="output path where participant JSON file will be written", required=True)
    parser.add_argument("-m", "--metrics_ref", help="directory that contains the golden dataset", required=True)
    
    args = parser.parse_args()

    main(args)