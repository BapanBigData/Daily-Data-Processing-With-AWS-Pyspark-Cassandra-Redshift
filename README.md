# Daily-Data-Processing-With-AWS-Pyspark-Cassandra-Redshift
Overview

This project aims to automate the processing of daily CSV files retrieved from an AWS S3 bucket using a Spark application. The processed data is transformed and stored in a Cassandra table for further analysis. Additionally, the Spark application incrementally loads modified data into AWS Redshift for enhanced analytics and visualization. Upon completion of data processing, the daily CSV file is archived in the S3 bucket's archive folder.

Features

Automated Data Processing:

* Utilizes a Spark application to process daily CSV files (file_yyyy_mm_dd.csv) from an AWS S3 bucket.
Implements specific transformations tailored for subsequent analysis and visualization.

Data Storage and Retrieval:

* Stores the transformed data in a Cassandra table, enabling efficient data retrieval and management.
Utilizes Cassandra's distributed architecture for scalability and fault tolerance.

Integration with AWS Redshift:

* Incrementally loads modified data into AWS Redshift for further analysis and visualization.
* Facilitates seamless integration with Redshift's analytical capabilities for comprehensive data insights.

Usage

Setup AWS Credentials:

* Ensure AWS credentials are properly configured to access the S3 bucket, Cassandra, and Redshift.

Running the Spark Application:

* Execute the Spark application to process daily CSV files and perform transformations.
* Monitor the progress and ensure successful completion of data processing tasks.

Data Analysis with Cassandra and Redshift:

* Analyze the processed data stored in Cassandra tables for insights and trends.
* Leverage AWS Redshift for advanced analytics and visualizations using the incrementally loaded data.

Archiving Daily CSV Files:

* Verify that the processed daily CSV files are moved to the archive folder in the S3 bucket.
* Maintain a structured and organized data storage system for historical data access and compliance.

Note:

To get the transformation code please follow `staging_healthcare_data_analysis.ipynb`.