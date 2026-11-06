"""Train and compare CreditLens models. Uses the supplied processed dataset when available."""
from pathlib import Path
import pandas as pd, numpy as np, json, joblib
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
from sklearn.inspection import permutation_importance
ROOT=Path(__file__).resolve().parents[2]
df=pd.read_csv(ROOT/'data/processed/german_credit_clean.csv')
X=df.drop(columns=['class','applicant_id'],errors='ignore'); y=df['class'].map({'good':0,'bad':1})
cat=X.select_dtypes(include='object').columns.tolist(); num=[c for c in X.columns if c not in cat]
pre=ColumnTransformer([('num',Pipeline([('imputer',SimpleImputer(strategy='median')),('scale',StandardScaler())]),num),('cat',Pipeline([('imputer',SimpleImputer(strategy='most_frequent')),('onehot',OneHotEncoder(handle_unknown='ignore'))]),cat)])
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,stratify=y,random_state=42)
models={'Logistic Regression':LogisticRegression(max_iter=1500,class_weight='balanced',random_state=42),'Random Forest':RandomForestClassifier(n_estimators=250,max_depth=8,min_samples_leaf=3,class_weight='balanced',random_state=42),'Gradient Boosting':GradientBoostingClassifier(n_estimators=160,max_depth=3,learning_rate=.05,random_state=42)}
results={}; fitted={}
for name,m in models.items():
    pipe=Pipeline([('preprocessor',pre),('model',m)]); pipe.fit(Xtr,ytr); pred=pipe.predict(Xte); prob=pipe.predict_proba(Xte)[:,1]
    results[name]={'accuracy':accuracy_score(yte,pred),'precision':precision_score(yte,pred,zero_division=0),'recall':recall_score(yte,pred,zero_division=0),'f1':f1_score(yte,pred,zero_division=0),'roc_auc':roc_auc_score(yte,prob),'confusion_matrix':confusion_matrix(yte,pred).tolist()}; fitted[name]=pipe
best=max(results,key=lambda n:(results[n]['f1'],results[n]['roc_auc']))
joblib.dump(fitted[best],ROOT/'models/creditlens_model.joblib'); joblib.dump({'model_name':best,'feature_columns':list(X.columns)},ROOT/'models/model_metadata.joblib')
perm=permutation_importance(fitted[best],Xte,yte,n_repeats=8,random_state=42,scoring='roc_auc')
feature_importance=[{'feature':c,'importance':float(max(0,v))} for c,v in sorted(zip(X.columns,perm.importances_mean),key=lambda z:z[1],reverse=True)]
json.dump({'selected_model':best,'metrics':{k:{m:float(v) if not isinstance(v,list) else v for m,v in d.items()} for k,d in results.items()},'feature_importance':feature_importance},open(ROOT/'models/model_metrics.json','w'),indent=2)
print('Selected model:',best); print(json.dumps(results[best],indent=2))
