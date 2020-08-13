## External Data Ingestion
- Domestic Flight Data from 2016-2018
- Sources:
  - S3
  - PostGres SQL
  - External HDFS Cluster

### -----------------------------Project Components-----------------------------


#### -------Accessing External Data
[Accessing_Flight_Data.ipynb](view/Accessing_Flight_Data.ipynb) 

#### -------Merging External Data into a Domino Dataset
[dataset-creator.sh](view/data_ingestion.py) 
- Python script based on Jupyter notebook
- ingests data and saves it to Domino Dataset

#### ------Quick Exploratory Analysis of airline dataset using open source Pandas Profiling utility
[produce_profile.py](view/produce_profile.py) Shell script that creates pandas profile of ingested data
![Pandas](raw/latest/results/Profile_report.png?inline=true)

