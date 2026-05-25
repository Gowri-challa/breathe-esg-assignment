# Data Model Overview

This project is built using Django ORM models for storing ESG emission data.

## Main Models

### Company
Stores company information.

Fields:
- name

### DataSource
Stores uploaded source information.

Fields:
- company (ForeignKey)
- source_type
- uploaded_at

### EmissionRecord
Stores normalized ESG emission records.

Fields:
- source (ForeignKey)
- category
- activity_type
- original_value
- original_unit
- normalized_value
- normalized_unit
- co2e
- suspicious_flag
- status
- created_at

## Relationships

- One Company can have many DataSources
- One DataSource can have many EmissionRecords

## Workflow

CSV File → Upload API → Data Normalization → Suspicious Detection → Database Storage → Review UI