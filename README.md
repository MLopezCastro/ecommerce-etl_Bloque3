# 🧪 ETL Pipeline – Scalable Architecture with Python, Parquet & CLI

## 📍 Overview

This project represents the third stage of a progressive ETL pipeline development. After building a functional local script and transforming it into a modular and testable architecture, this phase focuses on **scalability, format optimization, and execution control**.

The pipeline ingests raw transactional `.csv` data from an ecommerce context, applies cleaning, enrichment, and business validations, and exports ready-to-analyze datasets in **CSV or Parquet** format, supporting **Snappy compression** for performance.

---

## 🌟 Technical Objectives

- Build a **scalable and modular** local ETL pipeline ready for integration with tools like **Airflow**, **AWS Lambda**, or **GitHub Actions**.
- Adopt **Parquet**, a columnar data format widely used in data lakes and analytics systems, with **Snappy** compression for efficiency.
- Implement a **Command Line Interface (CLI)** using `argparse` to make execution dynamic and reproducible.
- Apply **professional best practices**: modular code, reusable functions, logging, and clear logic separation.

---

## ✅ Key Features & Deliverables

- **Modular ETL pipeline**: Scripts divided into clear layers for transformation, validation, export, and execution.
- **Scalable output format**: Export to **CSV or Parquet** (with Snappy compression).
- **Business logic enforcement**: Validation rules ensure data quality (e.g. no nulls, valid emails, allowed statuses).
- **Logging**: Timestamped `.log` file captures process duration, errors, and row counts.
- **Command-line interface (CLI)**: Run pipeline with full control over input/output and format selection.
- **Professional folder structure**: Clean separation for raw data, output, logs, and code.

---

## 🧠 Why Parquet + Snappy?

> Parquet is a **columnar storage format** optimized for big data analytics:
- Reads only needed columns → faster queries.
- Supports advanced compression (Snappy, Gzip).
- Compatible with Athena, BigQuery, Spark, pandas.

> Snappy is a fast, lightweight compression format:
- Recommended for production environments.
- Used by Google, Facebook, and many open-source tools.
- Balances speed and compression size.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **pandas**
- **pyarrow** (Parquet support)
- **argparse** (CLI parser)
- **logging** (monitoring)

---

## 📁 Project Structure

```
ecommerce-etl-pipeline/
├── data/
│   ├── raw/
│   │   ├── orders.csv
│   │   └── customers.csv
│   └── output/
│       └── orders_enriched.snappy.parquet
├── logs/
│   └── etl.log
├── scripts/
│   ├── transform.py       # Data cleaning and enrichment
│   ├── validate.py        # Business rules
│   ├── export.py          # Output to CSV or Parquet
│   └── helpers.py         # (optional) utilities
├── main.py                # CLI orchestrator
├── requirements.txt       # Dependencies
└── README.md
```

---

## 🚀 How to Run the Pipeline

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run pipeline with CLI:

```bash
python main.py   --orders data/raw/orders.csv   --customers data/raw/customers.csv   --output data/output/orders_enriched.parquet   --format parquet
```

3. Output will be logged in `logs/etl.log`.

---

## 🧪 Example Validations

- `order_id` must be unique
- `quantity`, `unit_price` must be > 0
- `email` must be valid
- `status` must belong to accepted values
- `order_date` must not be in the future
- No nulls in critical fields (`country`, `email`)

---

## 📝 Learning Outcomes

- Learned the **difference between row-based (CSV) and column-based (Parquet)** formats and when to use them.
- Gained experience building **reusable ETL components** ready for orchestration.
- Created a **CLI interface** to run flexible data pipelines.
- Practiced **production-grade logging** and error tracking.
- Set the foundation for **future cloud automation** (Airflow, AWS).

---

## 🙌 Acknowledgment

Special thanks to **Data Engineer Ian Saura**, whose clear guidance helped me execute this project successfully and think like a real data engineer.