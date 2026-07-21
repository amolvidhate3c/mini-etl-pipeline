# Mini ETL Pipeline (Python)

A lightweight, automated Python-based **ETL (Extract, Transform, Load)** pipeline designed to process raw datasets, clean anomalies, and generate operational summary metrics in real-time.

## Pipeline Architecture
1. **Extract:** Reads raw transactional/employee data from a CSV source (`data.csv`).
2. **Transform:** Cleans the data by filtering out records with missing critical values, handling type conversions, and removing exact duplicates.
3. **Load:** Exports the sanitized data into a structured output file (`processed_summary.csv`) and computes aggregate insights.

## Features
* **Automated Data Hygiene:** Handles missing data points and row-level duplicates programmatically.
* **Real-Time Event Trigger (`watcher.py`):** Background file watcher that automatically triggers the ETL pipeline the moment the source data (`data.csv`) is modified.
* **Error Handling:** Robust exception handling for file validation and data type parsing.
* **Metrics Generation:** Calculates key performance/operational metrics (e.g., total valid record count, average salary breakdown).

## Tech Stack
* **Language:** Python 3
* **Libraries:** Built-in Python modules (`csv`, `os`, `subprocess`, `time`) ensuring lightweight execution.

## How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/amolvidhate3c/mini-etl-pipeline.git](https://github.com/amolvidhate3c/mini-etl-pipeline.git)
   cd mini-etl-pipeline

Run manually:

Bash
python3 etl.py
Run with Real-Time Automation Trigger:

Bash
python3 watcher.py
