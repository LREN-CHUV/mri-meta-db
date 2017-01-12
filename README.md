[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9adcf4cbd730472386d0e71ab27b9b6b)](https://www.codacy.com/app/mirco-nasuti/mri-meta-db?utm_source=github.com&utm_medium=referral&utm_content=LREN-CHUV/mri-meta-db&utm_campaign=badger)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](https://github.com/LREN-CHUV/mri-meta-db/blob/master/LICENSE)

# MRI Meta DB

This project contains the model and migration scripts needed to deploy the mri-meta-db. This database is used to store metadata extracted mainly from DICOM files in the Data Factory.

## Prerequisites

* Alembic

## Usage

Write a configuration file called `alembic.ini` based on `alembic.ini.sample`, `cd` db_migrations folder and run `alembic upgrade head`. 
