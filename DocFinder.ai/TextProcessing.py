# -*- coding: utf-8 -*-
"""TextProcessingDoc2csv.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DO68VzUvvocA3rlVVkOm_8JM7zgciO5a

##dataset preprocessing
"""

import os
import pandas as pd
import requests
import gzip
from io import BytesIO

# Set up URLs and paths
url_download = "https://www.boleary.com/blog/posts/202307-pmn/data/pmn_summary_text.csv.gz"
path_download = "data-raw"
filename_download = "pmn_summary_text.csv.gz"
filepath_download = os.path.join(path_download, filename_download)

# Create the data-raw directory if it doesn't exist
os.makedirs(path_download, exist_ok=True)

# Download the data
response = requests.get(url_download)
with open(filepath_download, "wb") as f:
    f.write(response.content)

with gzip.open(filepath_download, "rt") as f:
    pmn_summaries = pd.read_csv(f, sep=";", parse_dates=["date_obtained"], dtype={
        "submission_number": str,
        "page_number": int,
        "text_embedded": str,
        "text_ocr": str
    })

# Print the first few rows of the dataframe
print(pmn_summaries.head())

type(pmn_summaries)

df = pd.DataFrame(pmn_summaries)

df

# dfTest=df[:1000]

# dfTest.to_csv('pmn_summaries.csv')

# df.to_csv('pmn_summaries_Full.csv')

"""Changing the date format as per the table schema"""

import pandas as pd


# input_file=
def convert_date_format():
    # Read the CSV file into a pandas DataFrame
    # df = pd.read_csv(input_file)

    df['date_obtained'] = pd.to_datetime(df['date_obtained'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')

    # df.to_csv(output_file, index=False)

if __name__ == "__main__":
    convert_date_format()

df

df.to_csv('Gesund_Full.csv')
