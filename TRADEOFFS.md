# Tradeoffs and Limitations

## SQLite instead of PostgreSQL
SQLite was chosen for faster local setup and simplicity.
For production-scale applications PostgreSQL would be preferred.

## Simple Suspicious Detection
Implemented rule-based suspicious detection instead of machine learning to keep the solution simple and explainable.

## No Authentication
Authentication was skipped to focus on core ESG workflow functionality.

## Limited Validation
Basic validation is implemented, but advanced CSV schema validation can be improved.

## Local File Processing
CSV files are processed directly in memory. Large file optimization was not implemented.

## UI Design
Focused more on functionality and workflow completion rather than advanced UI/UX polish.