# Task 24 — Data Quality Audit

## Objective
Audit a Superstore dataset for missing, duplicate, range, format, and consistency issues and create a repeatable quality checklist.

## Audit snapshot
- **Rows:** 9,977
- **Columns:** 13
- **Missing cells:** 0
- **Duplicate rows:** 0
- **Validation rules:** 13
- **Rules passed:** 12
- **Actionable issues:** 1

## Main finding
**Postal Code formatting:** 449 records were stored as four-digit integer values because leading zeros were not preserved.

**Resolution:** Postal Code is standardized as a five-character text value using zero-padding.

Negative Profit is intentionally retained because a negative profit is a valid business result.

## Repository structure
```text
Task_24_Data_Quality_Audit/
├── Task_24_Data_Quality_Audit.xlsx
├── Data_Quality_Audit_Report.pdf
├── README.md
├── requirements.txt
├── data/
│   ├── validation_checklist.csv
│   ├── issue_log.csv
│   ├── cleaned_sample.csv
│   └── data_profile.csv
├── documentation/
│   └── data_quality_audit_notes.md
└── scripts/
    └── audit_data_quality.py
```

## Reproduce the audit
```bash
pip install -r requirements.txt
python scripts/audit_data_quality.py input.csv output_folder
```

## Tools
Python • Pandas • OpenPyXL • ReportLab
