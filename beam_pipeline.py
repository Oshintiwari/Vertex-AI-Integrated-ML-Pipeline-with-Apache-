import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import json

# Load BigQuery configuration
with open('config/bigquery_config.json', 'r') as config_file:
    bigquery_config = json.load(config_file)

def run_beam_pipeline():
    pipeline_options = PipelineOptions()
    
    with beam.Pipeline(options=pipeline_options) as p:
        (
            p
            | "Read from BigQuery" >> beam.io.ReadFromBigQuery(
                query=bigquery_config["query"],
                use_standard_sql=True
            )
            | "Transform Data" >> beam.Map(lambda row: transform_data(row))
            | "Write to BigQuery" >> beam.io.WriteToBigQuery(
                table=bigquery_config["output_table"],
                write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE
            )
        )

def transform_data(row):
    # Example transformation logic
    row['processed_feature'] = row['feature'] * 2
    return row
