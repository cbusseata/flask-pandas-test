import os
from pathlib import Path
from flask import Flask, jsonify, request
import jsonschema
import requestschema
import math
import numpy

import pandas as pd

app = Flask(__name__)

# @TODO: remove if moving past testing phase
@app.route('/test', methods=['GET'])
def test():
    return 'Up!'

@app.route('/organization/<int:organization_id>', methods=['GET'])
def get_organization(organization_id):
    organizationsDf = get_organizations_dataframe()
    organizationDf = organizationsDf.loc[organizationsDf['id'] == organization_id]

    if organizationDf.shape[0] <= 0:
        return jsonify({'error': 'No result'}), 404

    return jsonify(fix_up_response_dict_list(organizationDf.to_dict(orient = 'records'))[0]), 200

@app.route('/organizations', methods=['GET'])
def get_organizations():
    try:
        jsonschema.validate(request.args.to_dict(), requestschema.organizations)
    except jsonschema.exceptions.ValidationError as ve:
        # @TODO: figure out how to jsonify all errors
        return jsonify({
            'error': ve.message
        }), 400

    organizationsDf = get_organizations_dataframe()

    # Filter
    for field in ['id', 'name', 'city', 'state', 'postal']:
        if request.args.get(field):
            organizationsDf = organizationsDf.loc[organizationsDf[field] == request.args.get(field)]

    order_by = request.args.get('orderby')
    ascending = False if request.args.get('direction') and request.args.get('direction') == 'DSC' else True
    if order_by:
        organizationsDf = organizationsDf.sort_values(by=[order_by], ascending=ascending)

    if organizationsDf.shape[0] <= 0:
        return jsonify({'error': 'No results'}), 404

    return jsonify(fix_up_response_dict_list(organizationsDf.to_dict(orient = 'records'))), 200

def get_organizations_dataframe():
    """Gets a pandas DataFrame object to work with from the CSV.

    Returns:
        (DataFrame)
    """
    dir = str(Path(os.path.dirname(os.path.realpath(__file__))))
    
    data_frame = pd.read_csv(dir+"/organization_sample_data.csv") 

    # Trim whitespace from the fields
    return data_frame.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

def fix_up_response_dict_list(dict_list: list):
    """Fix up data from pandas - we don't want to convert postal to float, and we would prefer NULL over NaN in response.
    """
    ret = []
    for df_dict in dict_list:
        for key in df_dict:
            if df_dict[key] is numpy.nan or df_dict[key] != df_dict[key]:
                df_dict[key] = None
        ret.append(df_dict)

    return ret
