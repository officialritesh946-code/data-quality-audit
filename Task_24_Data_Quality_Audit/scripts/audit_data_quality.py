"""Task 24 - reusable data-quality audit using Pandas."""
import sys
from pathlib import Path
import pandas as pd

def audit(path):
    df = pd.read_csv(path)
    rows = []
    def add(rule_id, category, field, rule, failed):
        rows.append({"Rule ID":rule_id,"Category":category,"Field":field,
                     "Validation Rule":rule,"Failed Records":int(failed),
                     "Status":"PASS" if failed == 0 else "FAIL"})
    add("DQ-01","Completeness","All columns","No missing/null values",df.isna().sum().sum())
    add("DQ-02","Uniqueness","All columns","No fully duplicated rows",df.duplicated().sum())
    add("DQ-03","Range","Sales","Sales must be >= 0",(df["Sales"]<0).sum())
    add("DQ-04","Range","Quantity","Quantity must be a positive integer",
        ((df["Quantity"]<=0)|(df["Quantity"]%1!=0)).sum())
    add("DQ-05","Range","Discount","Discount must be between 0 and 1",
        ((df["Discount"]<0)|(df["Discount"]>1)).sum())
    add("DQ-06","Format","Postal Code","ZIP should be a 5-character text value",
        df["Postal Code"].astype(str).str.len().eq(4).sum())
    return df, pd.DataFrame(rows)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python audit_data_quality.py input.csv output_folder")
    out = Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
    df, results = audit(sys.argv[1])
    results.to_csv(out/"validation_results.csv",index=False)
    df["Postal Code"] = df["Postal Code"].astype("Int64").astype(str).str.zfill(5)
    df.to_csv(out/"cleaned_sample.csv",index=False)
    print(results.to_string(index=False))
