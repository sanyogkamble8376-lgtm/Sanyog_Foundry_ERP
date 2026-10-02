# Foundry ERP V3

Flask + SQLite Foundry ERP foundation with working Production Plan and Job Cards.

## Run on Windows PowerShell
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

Demo login: admin / admin123

### Working Production Flow
Production Plan -> Approval -> Job Card -> Submit -> Approve -> Release -> Complete

Job Cards can be created from Approved Production Plans; plan details auto-fill into the Job Card form.
