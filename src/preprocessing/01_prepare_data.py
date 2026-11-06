from pathlib import Path
import pandas as pd, json
ROOT=Path(__file__).resolve().parents[2]
src=ROOT/'data/demo/german_credit_synthetic.csv'; out=ROOT/'data/processed/german_credit_clean.csv'
df=pd.read_csv(src).drop_duplicates()
df.drop(columns=['applicant_id']).to_csv(out,index=False)
audit={'rows':len(df),'columns':len(df.columns)-1,'duplicates':int(df.duplicated().sum()),'missing_cells':int(df.isna().sum().sum()),'default_risk_class_rate':float((df['class']=='bad').mean()),'dataset_status':'synthetic_demo_data'}
(ROOT/'data/processed/data_audit.json').write_text(json.dumps(audit,indent=2))
print(f'Phase 1 completed successfully. Rows: {len(df)}. Columns: {len(df.columns)}. Duplicates: {df.duplicated().sum()}. Missing cells: {df.isna().sum().sum()}.')
