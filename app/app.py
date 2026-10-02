from flask import Flask, render_template, request, redirect, url_for, session, flash, Response, send_file
import sqlite3
import os
import csv
import io
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)
app.secret_key = 'company_erp_secret_key'

DB_NAME = 'company_erp.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    # Department records table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS department_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            department TEXT NOT NULL,
            sub_module TEXT NOT NULL,
            record_name TEXT NOT NULL,
            reference_no TEXT,
            date_val TEXT,
            rate REAL,
            quantity TEXT,
            details TEXT,
            status TEXT DEFAULT 'Active'
        )
    ''')
    
    # Users table for login authentication
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')
    
    # Insert default superadmin user (Username: superadmin, Password: admin123)
    conn.execute('''
        INSERT OR IGNORE INTO users (username, password, role)
        VALUES ('superadmin', 'admin123', 'Superadmin')
    ''')
    
    conn.commit()
    conn.close()

# Initialize database tables and default admin on startup
with app.app_context():
    init_db()

fitling_sub_modules = [
    "Fitling Dashboard",
    "Fitling Job Entry",
    "Production Request",
    "Material Requirement",
    "Material Issue",
    "Fitling Process",
    "Employee Assignment",
    "Workstation",
    "Tools",
    "Quality Check",
    "Rework",
    "Rejection",
    "Time Tracking",
    "Daily Production",
    "Fitling Reports"
]

DEPARTMENT_SUBMODULES = {
    'fitling': fitling_sub_modules,
    'fitting': fitling_sub_modules, 
    'production': [
        "Production Dashboard", "Product Master", "Bill of Materials", "Production Planning",
        "Production Order", "Material Requirement", "Material Issue", "Work Center",
        "Operation / Routing", "Machine Management", "Operator Management", "Production Entry",
        "WIP Management", "Quality Integration", "Rework / Scrap", "Downtime",
        "Shift Management", "Finished Goods", "Production Cost", "Production Reports"
    ],
    'quality': [
        "Quality Dashboard", "Incoming Quality Inspection", "In-Process Quality", "Final Quality Inspection",
        "Quality Standards", "Test Management", "Sampling Management", "Inspection Checklist",
        "NCR Management", "CAPA", "Rejection Management", "Rework Management", "Supplier Quality",
        "Customer Complaint", "Calibration", "Quality Documents", "Quality Reports"
    ],
    'maintenance': [
        "Maintenance Dashboard", "Asset Management", "Maintenance Request", "Breakdown Management",
        "Work Order", "Preventive Maintenance", "Corrective Maintenance", "Technician Management",
        "Spare Parts", "Vendor Management", "AMC Management", "Calibration", "Inspection",
        "Maintenance History", "Downtime Tracking", "Maintenance Cost", "Maintenance Reports"
    ],
    'dispatch': [
        "Dispatch Dashboard", "Dispatch Order", "Order Verification", "Picking", "Packing",
        "Dispatch Challan", "Vehicle Management", "Transport Management", "Shipment Tracking",
        "Delivery Management", "POD Management", "Partial Dispatch", "Dispatch Return",
        "Damage / Loss", "Dispatch Reports"
    ],
    'accounts': [
        "Accounts Dashboard", "Chart of Accounts", "Sales Invoicing", "Purchase Bills", "Receipts",
        "Payments", "Expenses", "Income", "Customer Ledger", "Vendor Ledger", "Cash Book",
        "Bank Book", "Bank Reconciliation", "Journal Entry", "Credit Note", "Debit Note",
        "Outstanding", "Tax / GST Reports", "Financial Reports", "Audit Trail"
    ],
    'development': [
        "Development Dashboard", "Project Management", "Module Management", "Task Management",
        "Developer Management", "Requirement Management", "Bug Management", "Testing / QA",
        "Code / Version Management", "Git / Repository", "Deployment Management",
        "Client / Project Communication", "Documentation", "Time Tracking", "Development Reports"
    ],
    'store': [
        "Store Dashboard", "Item Master", "Category Management", "Godown Management", "Opening Stock",
        "Goods Receipt (GRN)", "Material Issue", "Material Return", "Stock Transfer", "Stock Adjustment",
        "Stock Verification", "Minimum Stock Level", "Low Stock Alert", "Reorder Level", "Purchase Request",
        "PO Status", "Supplier / Vendor", "Batch Management", "Expiry Management", "Serial Number Tracking",
        "Damaged Stock", "Scrap Management", "Barcode / QR Code", "Material Search", "Stock Ledger", "Store Reports"
    ],
    'purchase': [
        "Purchase Dashboard", "Supplier Master", "Item Master", "Purchase Requisition", "RFQ",
        "Supplier Quotation", "Quotation Comparison", "Purchase Order", "PO Approval", "GRN",
        "Purchase Return", "Invoice Tracking", "Payment Tracking", "Purchase Reports"
    ],
    'sales': [
        "Sales Dashboard", "Customer Management", "Product Management", "Lead Management",
        "Quotation", "Sales Order", "Invoice / Billing", "Delivery Tracking", "Payment Management",
        "Return / Credit Note", "Discount Management", "Salesperson Management", "Follow-up",
        "Sales Reports", "Search & Filters"
    ],
    'lab': [
        "Lab Dashboard", "Sample Registration", "Sample Receiving", "Sample Tracking", "Test Request",
        "Test Master", "Test Assignment", "Test Scheduling", "Test Execution", "Result Entry",
        "Reference Range", "Pass / Fail Validation", "Retest Management", "Test Approval", "Test Report",
        "Certificate Generation", "Equipment Management", "Calibration Log", "Chemical / Reagent Stock",
        "Reagent Consumption", "Equipment Maintenance", "QC Management", "Audit Trail", "Lab Reports"
    ],
    'core': [
        "Core Dashboard", "Work Order", "Production Planning", "Job Card", "Process Management",
        "Machine Management", "Machine Allocation", "Production Entry", "Raw Material Requirement",
        "Material Issue", "Material Consumption", "WIP Tracking", "Quality Check", "Lab Request",
        "Rejection Management", "Rework Management", "Downtime", "Maintenance Request", "Manpower Allocation",
        "Shift Management", "Production Target", "Process Approval", "Core Reports"
    ],
    'admin': ["Users", "Roles & Permissions", "System Logs"]
}

@app.route('/')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()
        
        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid Credentials', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/global-po-tracker')
def global_po_tracker():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('global_po_tracker.html')

@app.route('/department/<dept_name>/<path:item>', methods=['GET', 'POST'])
def department_module(dept_name, item):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    dept_key = dept_name.lower().strip()
    dept_display = "Fitling" if dept_key in ["fitling", "fitting"] else dept_name.replace('-', ' ').title()
    formatted_name = dept_display + " Department"
    
    sub_modules = DEPARTMENT_SUBMODULES.get(dept_key, ["Main", "Reports", "Settings"])
    
    actual_item = item
    for sub in sub_modules:
        if sub.lower().replace('/', '-').replace(' ', '-') == item.lower().replace('/', '-').replace(' ', '-'):
            actual_item = sub
            break
    
    conn = get_db_connection()

    if request.method == 'POST':
        target_sub_module = request.form.get('sub_module_selected', actual_item)
        rec_name = request.form.get('record_name')
        ref_no = request.form.get('reference_no')
        date_val = request.form.get('date_val')
        rate = request.form.get('rate')
        quantity = request.form.get('quantity')
        details = request.form.get('details')
        
        if rec_name:
            conn.execute('''
                INSERT INTO department_records (department, sub_module, record_name, reference_no, date_val, rate, quantity, details)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (dept_key, target_sub_module, rec_name, ref_no, date_val, rate, quantity, details))
            conn.commit()
            flash('Record added successfully!', 'success')
        conn.close()
        
        safe_item = target_sub_module.replace('/', '-')
        return redirect(url_for('department_module', dept_name=dept_name, item=safe_item))

    start_date = request.args.get('start_date', '')
    end_date = request.args.get('end_date', '')
    export_format = request.args.get('export')

    # Date Filtering Query
    if start_date and end_date:
        query = 'SELECT * FROM department_records WHERE department = ? AND sub_module = ? AND date_val BETWEEN ? AND ?'
        db_entries = conn.execute(query, (dept_key, actual_item, start_date, end_date)).fetchall()
    elif start_date:
        query = 'SELECT * FROM department_records WHERE department = ? AND sub_module = ? AND date_val >= ?'
        db_entries = conn.execute(query, (dept_key, actual_item, start_date)).fetchall()
    else:
        db_entries = conn.execute('SELECT * FROM department_records WHERE department = ? AND sub_module = ?', (dept_key, actual_item)).fetchall()

    # Export Handlers (CSV, Excel, PDF)
    if export_format == 'csv':
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['ID', 'Department', 'Sub-Module', 'Record Name', 'Reference No', 'Date', 'Rate', 'Quantity', 'Details', 'Status'])
        for row in db_entries:
            writer.writerow([row['id'], row['department'], row['sub_module'], row['record_name'], row['reference_no'], row['date_val'], row['rate'], row['quantity'], row['details'], row['status']])
        conn.close()
        return Response(output.getvalue(), mimetype="text/csv", headers={"Content-Disposition": f"attachment;filename={dept_key}_{actual_item}_report.csv"})

    elif export_format == 'excel':
        df = pd.DataFrame([dict(row) for row in db_entries])
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Report')
        output.seek(0)
        conn.close()
        return send_file(output, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", as_attachment=True, download_name=f"{dept_key}_{actual_item}_report.xlsx")

    elif export_format == 'pdf':
        output = io.BytesIO()
        p = canvas.Canvas(output, pagesize=letter)
        p.drawString(50, 750, f"Report: {formatted_name} - {actual_item}")
        y = 720
        for row in db_entries:
            p.drawString(50, y, f"ID: {row['id']} | Name: {row['record_name']} | Date: {row['date_val']} | Qty: {row['quantity']}")
            y -= 20
            if y < 50:
                p.showPage()
                y = 750
        p.save()
        output.seek(0)
        conn.close()
        return send_file(output, mimetype="application/pdf", as_attachment=True, download_name=f"{dept_key}_{actual_item}_report.pdf")

    conn.close()

    return render_template('generic_module.html', 
                           module_name=formatted_name, 
                           dept_slug=dept_key, 
                           sub_modules=sub_modules, 
                           current_item=actual_item, 
                           entries=db_entries,
                           start_date=start_date,
                           end_date=end_date)

@app.route('/admin-module')
def admin_module():
    return redirect(url_for('department_module', dept_name='admin', item='Users'))

if __name__ == '__main__':
    app.run(debug=True)