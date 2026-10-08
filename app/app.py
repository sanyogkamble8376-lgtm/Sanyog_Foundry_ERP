from flask import Flask, render_template, request, redirect, url_for, session, flash, Response, send_file
import sqlite3
import os
import csv
import io
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

app = Flask(__name__)
app.secret_key = 'company_erp_secret_key'

DB_NAME = 'company_erp.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
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
    
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')
    
    conn.execute('''
        INSERT OR IGNORE INTO users (username, password, role)
        VALUES ('superadmin', 'admin123', 'Superadmin')
    ''')
    
    conn.commit()
    conn.close()

with app.app_context():
    init_db()

fitling_sub_modules = [
    "Fitling Dashboard", "Fitling Job Entry", "Production Request", "Material Requirement",
    "Material Issue", "Fitling Process", "Employee Assignment", "Workstation", "Tools",
    "Quality Check", "Rework", "Rejection", "Time Tracking", "Daily Production", "Fitling Reports"
]

DEPARTMENT_SUBMODULES = {
    'sales': ["Sales Dashboard", "Customer Management", "Product Management", "Lead Management", "Quotation", "Sales Order", "Invoice / Billing", "Delivery Tracking", "Payment Management", "Return / Credit Note", "Discount Management", "Salesperson Management", "Follow-up", "Sales Reports", "Search & Filters"],
    'development': ["Development Dashboard", "Project Management", "Module Management", "Task Management", "Developer Management", "Requirement Management", "Bug Management", "Testing / QA", "Code / Version Management", "Git / Repository", "Deployment Management", "Client / Project Communication", "Documentation", "Time Tracking", "Development Reports"],
    'purchase': ["Purchase Dashboard", "Supplier Master", "Item Master", "Purchase Requisition", "RFQ", "Supplier Quotation", "Quotation Comparison", "Purchase Order", "PO Approval", "GRN", "Purchase Return", "Invoice Tracking", "Payment Tracking", "Purchase Reports"],
    'store': ["Store Dashboard", "Item Master", "Category Management", "Godown Management", "Opening Stock", "Goods Receipt (GRN)", "Material Issue", "Material Return", "Stock Transfer", "Stock Adjustment", "Stock Verification", "Minimum Stock Level", "Low Stock Alert", "Reorder Level", "Purchase Request", "PO Status", "Supplier / Vendor", "Batch Management", "Expiry Management", "Serial Number Tracking", "Damaged Stock", "Scrap Management", "Barcode / QR Code", "Material Search", "Stock Ledger", "Store Reports"],
    'production': ["Production Dashboard", "Product Master", "Bill of Materials", "Production Planning", "Production Order", "Material Requirement", "Material Issue", "Work Center", "Operation / Routing", "Machine Management", "Operator Management", "Production Entry", "WIP Management", "Quality Integration", "Rework / Scrap", "Downtime", "Shift Management", "Finished Goods", "Production Cost", "Production Reports"],
    'core': ["Core Dashboard", "Work Order", "Production Planning", "Job Card", "Process Management", "Machine Management", "Machine Allocation", "Production Entry", "Raw Material Requirement", "Material Issue", "Material Consumption", "WIP Tracking", "Quality Check", "Lab Request", "Rejection Management", "Rework Management", "Downtime", "Maintenance Request", "Manpower Allocation", "Shift Management", "Production Target", "Process Approval", "Core Reports"],
    'fettling': fitling_sub_modules,
    'fitling': fitling_sub_modules,
    'fitting': fitling_sub_modules, 
    'quality': ["Quality Dashboard", "Incoming Quality Inspection", "In-Process Quality", "Final Quality Inspection", "Quality Standards", "Test Management", "Sampling Management", "Inspection Checklist", "NCR Management", "CAPA", "Rejection Management", "Rework Management", "Supplier Quality", "Customer Complaint", "Calibration", "Quality Documents", "Quality Reports"],
    'lab': ["Lab Dashboard", "Sample Registration", "Sample Receiving", "Sample Tracking", "Test Request", "Test Master", "Test Assignment", "Test Scheduling", "Test Execution", "Result Entry", "Reference Range", "Pass / Fail Validation", "Retest Management", "Test Approval", "Test Report", "Certificate Generation", "Equipment Management", "Calibration Log", "Chemical / Reagent Stock", "Reagent Consumption", "Equipment Maintenance", "QC Management", "Audit Trail", "Lab Reports"],
    'dispatch': ["Dispatch Dashboard", "Dispatch Order", "Order Verification", "Picking", "Packing", "Dispatch Challan", "Vehicle Management", "Transport Management", "Shipment Tracking", "Delivery Management", "POD Management", "Partial Dispatch", "Dispatch Return", "Damage / Loss", "Dispatch Reports"],
    'accounts': ["Accounts Dashboard", "Chart of Accounts", "Sales Invoicing", "Purchase Bills", "Receipts", "Payments", "Expenses", "Income", "Customer Ledger", "Vendor Ledger", "Cash Book", "Bank Book", "Bank Reconciliation", "Journal Entry", "Credit Note", "Debit Note", "Outstanding", "Tax / GST Reports", "Financial Reports", "Audit Trail"],
    'hr': ["HR Dashboard", "Employee Master", "Attendance Entry", "Leave Management", "Payroll & Salary", "Recruitment", "Performance / KPI", "Training & Skill", "HR Reports"],
    'maintenance': ["Maintenance Dashboard", "Asset Management", "Maintenance Request", "Breakdown Management", "Work Order", "Preventive Maintenance", "Corrective Maintenance", "Technician Management", "Spare Parts", "Vendor Management", "AMC Management", "Calibration", "Inspection", "Maintenance History", "Downtime Tracking", "Maintenance Cost", "Maintenance Reports"],
    'plant_head': ["Plant Overview Dashboard", "Plant KPI", "Shift Approvals", "Resource Planning"],
    'management': ["Executive Dashboard", "Financial Overview", "Strategic Reports", "ROI Tracking"],
    'admin': ["Users", "Roles & Permissions", "System Logs"]
}

DEPARTMENTS = {
    'sales': {'name': 'Sales', 'working': 'Lead tracking, customer orders, quotations, and sales analytics.', 'submodules': DEPARTMENT_SUBMODULES['sales']},
    'development': {'name': 'Development', 'working': 'Pattern making, methoding, sample development & trial approvals.', 'submodules': DEPARTMENT_SUBMODULES['development']},
    'purchase': {'name': 'Purchase', 'working': 'Vendor management, purchase requisitions, PO creation & tracking.', 'submodules': DEPARTMENT_SUBMODULES['purchase']},
    'store': {'name': 'Store', 'working': 'Raw material stock, GRN entry, material issuing & inventory control.', 'submodules': DEPARTMENT_SUBMODULES['store']},
    'production': {'name': 'Production', 'working': 'Melting, molding line operations, daily heat numbers & castings.', 'submodules': DEPARTMENT_SUBMODULES['production']},
    'core': {'name': 'Core', 'working': 'Core shop management, sand mix control, core making & baking.', 'submodules': DEPARTMENT_SUBMODULES['core']},
    'fettling': {'name': 'Fettling', 'working': 'Shot blasting, grinding, riser cutting & finishing activities.', 'submodules': DEPARTMENT_SUBMODULES['fettling']},
    'quality': {'name': 'Quality', 'working': 'Dimensional inspection, NDT, physical inspection & rejection analysis.', 'submodules': DEPARTMENT_SUBMODULES['quality']},
    'lab': {'name': 'Laboratory', 'working': 'Chemical analysis, spectro test, tensile test & microstructure.', 'submodules': DEPARTMENT_SUBMODULES['lab']},
    'dispatch': {'name': 'Dispatch', 'working': 'Invoicing, packing list, delivery challans & transport booking.', 'submodules': DEPARTMENT_SUBMODULES['dispatch']},
    'accounts': {'name': 'Accounts', 'working': 'Billing reconciliation, ledger, payment entry & GST filings.', 'submodules': DEPARTMENT_SUBMODULES['accounts']},
    'hr': {'name': 'Human Resources', 'working': 'Employee onboarding, attendance, leave tracking, payroll and HR reports.', 'submodules': DEPARTMENT_SUBMODULES['hr']},
    'maintenance': {'name': 'Maintenance', 'working': 'Preventive maintenance, breakdown logs & equipment spare parts.', 'submodules': DEPARTMENT_SUBMODULES['maintenance']},
    'plant_head': {'name': 'Plant Head', 'working': 'Overall plant performance, yield metrics & departmental approvals.', 'submodules': DEPARTMENT_SUBMODULES['plant_head']},
    'management': {'name': 'Management', 'working': 'High-level business reports, executive summary & profit margins.', 'submodules': DEPARTMENT_SUBMODULES['management']}
}

def generate_pdf_report(records, title):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
    story = []

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontSize=15,
        leading=18,
        textColor=colors.HexColor("#1e293b"),
        spaceAfter=15
    )
    
    story.append(Paragraph(f"<b>Report: {title}</b>", title_style))
    story.append(Spacer(1, 10))

    table_data = [
        ["ID", "Record Name", "Ref / Spec", "Date", "Qty / Days", "Rate / Salary", "Details / Remarks"]
    ]

    for row in records:
        table_data.append([
            str(row['id']),
            str(row['record_name']),
            str(row['reference_no'] if row['reference_no'] else '-'),
            str(row['date_val'] if row['date_val'] else '-'),
            str(row['quantity'] if row['quantity'] else '-'),
            str(row['rate'] if row['rate'] else '-'),
            str(row['details'] if row['details'] else '-')
        ])

    pdf_table = Table(table_data, colWidths=[30, 110, 80, 70, 75, 75, 110])
    pdf_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#0284c7")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('TOPPADDING', (0, 0), (-1, 0), 6),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#f8fafc")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))

    story.append(pdf_table)
    doc.build(story)
    
    buffer.seek(0)
    return buffer

@app.route('/')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', departments=DEPARTMENTS)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if (username in ['superadmin', 'store_sup', 'lab_tech', 'hr_mgr'] and password == 'admin123') or (username == 'admin' and password == 'admin'):
            session['user_id'] = 1
            session['username'] = username
            return redirect(url_for('dashboard'))
            
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
        
        safe_item = target_sub_module.replace('/', '-').replace(' ', '-')
        return redirect(url_for('department_module', dept_name=dept_name, item=safe_item))

    start_date = request.args.get('start_date', '')
    end_date = request.args.get('end_date', '')
    export_format = request.args.get('export')

    if start_date and end_date:
        query = 'SELECT * FROM department_records WHERE department = ? AND sub_module = ? AND date_val BETWEEN ? AND ?'
        db_entries = conn.execute(query, (dept_key, actual_item, start_date, end_date)).fetchall()
    elif start_date:
        query = 'SELECT * FROM department_records WHERE department = ? AND sub_module = ? AND date_val >= ?'
        db_entries = conn.execute(query, (dept_key, actual_item, start_date)).fetchall()
    else:
        db_entries = conn.execute('SELECT * FROM department_records WHERE department = ? AND sub_module = ?', (dept_key, actual_item)).fetchall()

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
        pdf_buffer = generate_pdf_report(db_entries, f"{formatted_name} - {actual_item}")
        conn.close()
        return send_file(pdf_buffer, mimetype="application/pdf", as_attachment=True, download_name=f"{dept_key}_{actual_item}_report.pdf")

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

