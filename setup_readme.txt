Docker command to start cassandra
----------------------------------

docker compose -f docker-compose.yml up -d

* Once cassandra container started, open the terminal of docker container
* type cqlsh on terminal
* cqlsh shell will be opened and now cassandra related commands can be executed

Cassandra table Creation
-------------------------------

CREATE KEYSPACE IF NOT EXISTS healthcare_store WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };

CREATE TABLE healthcare_store.healthcare_fact (
    patient_id TEXT,
    age INT,
    gender TEXT,
    diagnosis_code TEXT,
    diagnosis_description TEXT,
    diagnosis_date DATE,
    flag BOOLEAN,
    PRIMARY KEY (diagnosis_date, patient_id)
);


CREATE TABLE healthcare_store.disease_gender_distn(
    diagnosis_date DATE,
    diagnosis_description TEXT,
    diagnosis_code TEXT,
    percentage_male DOUBLE,
    percentage_female DOUBLE
    PRIMARY KEY (diagnosis_date, diagnosis_code)
);

CREATE TABLE healthcare_store.common_diseases(
    rank INT,
    diagnosis_date DATE,
    diagnosis_description TEXT,
    PRIMARY KEY (diagnosis_date, rank)
);

CREATE TABLE healthcare_store.age_group_distn(
    diagnosis_date DATE,
    diagnosis_description TEXT,
    diagnosis_code TEXT,
    cnt_30_40 INT,
    cnt_41_50 INT,
    cnt_51_60 INT,
    cnt_61_70 INT,
    cnt_more_than_70 INT
    PRIMARY KEY (diagnosis_date, diagnosis_code)
);

-----------------------------------------------------------------------------------------------------
Redshift table Creation

CREATE TABLE IF NOT EXISTS healthcare.healthcare_fact (
    patient_id VARCHAR(255), 
    age SMALLINT, 
    gender CHAR(20), 
    diagnosis_code VARCHAR(255), 
    diagnosis_description VARCHAR(255), 
    diagnosis_date DATE,
    flag BOOLEAN,
    PRIMARY KEY (diagnosis_date, patient_id)
)
DISTSTYLE KEY
DISTKEY (diagnosis_date)
SORTKEY (diagnosis_date, patient_id);
