# Student Performance Data Pipeline

A complete data engineering project that involves generating raw dirty data, cleaning it using Pandas, and loading it into a MySQL database.

## Project Structure

```
student-performance-data-pipeline/
│
├── CSV/
│   ├── students_performance.csv        # Raw dirty data (100,000 rows)
│   └── clean_csv/
│       └── students_performance_clean.csv   # Cleaned data (90,240 rows)
│
├── scripts/
│   ├── students_clean.ipynb            # Data cleaning notebook (Google Colab)
│   └── load_to_mysql.py               # MySQL loading script
│
├── .gitignore
└── README.md
```

## Project Overview

This project simulates a real-world data engineering pipeline:

- Generated 100,000 rows of student performance data with intentional dirty data
- Cleaned and validated the data using Pandas
- Loaded the cleaned data into a MySQL database
- Queried the database using SQL

## Dataset

The raw dataset contained the following issues that were handled during cleaning:

- 5,000 duplicate rows
- Nulls across multiple columns (scores, email, phone, city, gender, attendance)
- Negative score values (data entry errors)
- Score values above 100 (impossible values)
- Inconsistent gender values (M, F, male, FEMALE, unknown)
- Leading and trailing whitespace in name columns

## Tech Stack

- **Python** — core language
- **Pandas** — data cleaning and manipulation
- **NumPy** — numerical operations and null handling
- **SQLAlchemy** — database connection
- **PyMySQL** — MySQL driver
- **MySQL** — database
- **Google Colab** — cleaning notebook environment
- **VS Code** — local development

## Cleaning Steps

1. Inspected shape, dtypes, null counts and duplicates
2. Removed 5,000 duplicate rows
3. Fixed impossible score values (converted to NaN)
4. Standardized gender categories
5. Stripped whitespace from string columns
6. Dropped rows with null emails
7. Imputed nulls — scores with median, age with mode, categories with Unknown
8. Recomputed total score, average score and grade from scratch
9. Validated all columns with assertions

## Results

| Metric | Value |
|--------|-------|
| Raw rows | 100,000 |
| Cleaned rows | 90,240 |
| Duplicates removed | 5,000 |
| Rows dropped (null email) | 4,760 |
| Columns | 20 |
| Database | MySQL (students_db) |
| Table | student_performance |

## SQL Queries

After loading, the following queries were run to validate and analyze the data:

```sql
-- Students per department
SELECT COUNT(student_id), department 
FROM student_performance 
GROUP BY department;

-- Average score per grade
SELECT grade, AVG(average_score) as avg_score 
FROM student_performance 
GROUP BY grade 
ORDER BY grade;

-- City with highest average attendance
SELECT city, AVG(attendance_pct) as avg_attendance 
FROM student_performance 
GROUP BY city 
ORDER BY avg_attendance DESC 
LIMIT 1;
```

## Author

**Abubakkar Ghaswala**
GitHub: [@Abubakkar Ghaswala](https://github.com/AbubakkarGhaswala)
