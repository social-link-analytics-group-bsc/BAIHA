from __future__ import division, print_function
import pandas as pd
import numpy as np
import os, json
import sys
import re
from argparse import ArgumentParser
from JSON_templates import JSON_templates

parser = ArgumentParser()
parser.add_argument("-i", "--input", help="path to input dataset to be validated", required=True)
parser.add_argument("-com", "--community_name", help="name of benchmarking community", required=True)
parser.add_argument("-c", "--challenges", nargs='+', help="list the challenges that this input data is for", required=True)
parser.add_argument("-p", "--participant_name", help="name of the tool used for prediction", required=True)
parser.add_argument("-o", "--output", help="output path where participant JSON file will be written", required=True)


args = parser.parse_args()

def main(args):

    # input parameters
    input_dataset = args.input
    community = args.community_name
    challenges = args.challenges
    participant_name = args.participant_name
    out_path = args.output

    # Assuring the output path does exist
    if not os.path.exists(os.path.dirname(out_path)):
        try:
            os.makedirs(os.path.dirname(out_path))
            with open(out_path, mode="a") : pass
        except OSError as exc:
            print("OS error: {0}".format(exc) + "\nCould not create output path: " + out_path)

    validate_input_data(input_dataset, community, challenges, participant_name, out_path)


def validate_input_data(input_dataset, community, challenges, participant_name, out_path):
    # Load the dataset
    try:
        # sep specifies the delimiter, comment specifies that anything after a # should be regarded as a comment, header indicates that this index in the csv should be regarded as a header row and used for columnn names
        participant_data = pd.read_csv(input_dataset, sep='\t', comment="#", header=0) 
    except:
        sys.exit("ERROR: Submitted data file {} is not in a valid format!".format(input_dataset))

    submitted_fields = list(participant_data.columns.values)

    # Check that there is a column called 'patient_id'
    if 'patient_id' not in submitted_fields:
        raise ValueError(f"The data does not contain an patient_id field")

    # Check that 'id' column is of type 'string'
    if not all(participant_data['patient_id'].apply(lambda x: isinstance(x, str))):
        raise ValueError(f"The patient_id column contains non-string values.")

    # Check that there is a column called 'model_output'
    if 'diagnosis' not in submitted_fields:
        raise ValueError(f"The data does not contain an field called 'diagnosis")

    # Check that the 'model_output' column is of type 'boolean' (or 'integer'?)
    if not all(participant_data['diagnosis'].apply(lambda x: isinstance(x, int))):
        raise ValueError(f"The diagnosis column contains non-int values.")

    # Check that the 'model_output' column has values 0 or 1
    output_entries = participant_data['diagnosis'].dropna().isin([0, 1])
    if not output_entries.all():
        raise ValueError(f"The diagnosis column contains entries that are invalid.")
    
    # If the data passes the tests, convert to json format necessary for metrics assessment 
    data_id = community + ":" + participant_name + "_P"
    output_json = JSON_templates.write_participant_dataset(data_id, community, challenges, participant_name, True)

    with open(out_path , 'w') as f:
        json.dump(output_json, f, sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == '__main__':

    main(args)