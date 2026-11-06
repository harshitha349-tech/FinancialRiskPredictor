from pathlib import Path
import sqlite3, json
ROOT=Path(__file__).resolve().parents[1]
DB=ROOT/'data/creditlens.db'

def conn():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c

def init_db():
    c=conn()
    c.executescript('''
    CREATE TABLE IF NOT EXISTS applicants(id TEXT PRIMARY KEY, profile_json TEXT NOT NULL, created_at TEXT DEFAULT CURRENT_TIMESTAMP, updated_at TEXT DEFAULT CURRENT_TIMESTAMP);
    CREATE TABLE IF NOT EXISTS assessments(id INTEGER PRIMARY KEY AUTOINCREMENT, applicant_id TEXT, risk_score INTEGER, category TEXT, default_probability REAL, recommendation TEXT, dimensions_json TEXT, explanation_json TEXT, created_at TEXT DEFAULT CURRENT_TIMESTAMP);
    CREATE TABLE IF NOT EXISTS risk_history(id INTEGER PRIMARY KEY AUTOINCREMENT, applicant_id TEXT, risk_score INTEGER, category TEXT, default_probability REAL, note TEXT, created_at TEXT DEFAULT CURRENT_TIMESTAMP);
    CREATE INDEX IF NOT EXISTS idx_assess_applicant ON assessments(applicant_id);
    CREATE INDEX IF NOT EXISTS idx_history_applicant ON risk_history(applicant_id);
    '''); c.commit(); c.close()

def upsert_applicant(applicant_id, profile):
    c=conn(); c.execute('INSERT INTO applicants(id,profile_json) VALUES(?,?) ON CONFLICT(id) DO UPDATE SET profile_json=excluded.profile_json,updated_at=CURRENT_TIMESTAMP',(applicant_id,json.dumps(profile))); c.commit(); c.close()

def save_assessment(applicant_id,result):
    c=conn(); c.execute('INSERT INTO assessments(applicant_id,risk_score,category,default_probability,recommendation,dimensions_json,explanation_json) VALUES(?,?,?,?,?,?,?)',(applicant_id,result['risk_score'],result['category'],result['default_probability'],result['recommendation']['recommendation'],json.dumps(result['dimensions']),json.dumps(result['explanation']))); c.execute('INSERT INTO risk_history(applicant_id,risk_score,category,default_probability,note) VALUES(?,?,?,?,?)',(applicant_id,result['risk_score'],result['category'],result['default_probability'],result['recommendation']['recommendation'])); c.commit(); c.close()

def get_applicant(applicant_id):
    c=conn(); r=c.execute('SELECT * FROM applicants WHERE id=?',(applicant_id,)).fetchone(); c.close(); return dict(r) if r else None

def list_applicants():
    c=conn(); rows=c.execute('''SELECT a.id,a.profile_json, h.risk_score,h.category,h.default_probability,h.created_at FROM applicants a LEFT JOIN risk_history h ON h.id=(SELECT id FROM risk_history h2 WHERE h2.applicant_id=a.id ORDER BY id DESC LIMIT 1) ORDER BY a.updated_at DESC''').fetchall(); c.close(); return [dict(r) for r in rows]

def history(applicant_id):
    c=conn(); rows=c.execute('SELECT risk_score,category,default_probability,note,created_at FROM risk_history WHERE applicant_id=? ORDER BY id',(applicant_id,)).fetchall(); c.close(); return [dict(r) for r in rows]

def assessments(limit=8):
    c=conn(); rows=c.execute('SELECT * FROM assessments ORDER BY id DESC LIMIT ?',(limit,)).fetchall(); c.close(); return [dict(r) for r in rows]
