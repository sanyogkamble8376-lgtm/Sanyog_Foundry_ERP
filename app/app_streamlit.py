import streamlit as st
import sqlite3
import pandas as pd
import io
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# --- Page Configuration ---
st.set_page_config(
    page_title="Sanyog Foundry ERP",
    page_icon="🏭",
    layout="wide"
)

DB_NAME = 'company_erp.db'

# --- Database Setup ---
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

init_db()

# --- Department & Submodule Mapping ---
fitling_sub_modules = [
    "Fitling Dashboard", "Fitling Job Entry", "Production Request", "Material Requirement",
    "Material Issue", "Fitling Process", "Employee Assignment", "Workstation", "Tools",
    "Quality Check", "Rework", "Rejection", "Time Tracking", "Daily Production", "Fitling Reports"
]

DEPARTMENT_SUBMODULES = {
    'Sales': ["Sales Dashboard", "Customer Management", "Product Management", "Lead Management", "Quotation", "Sales Order", "Invoice / Billing", "Delivery Tracking", "Payment Management", "Sales Reports"],
    'Development': ["Development Dashboard", "Project Management", "Module Management", "Task Management", "Requirement Management", "Bug Management", "Testing / QA", "Documentation", "Development Reports"],
    'Purchase': ["Purchase Dashboard", "Supplier Master", "Item Master", "Purchase Requisition", "RFQ", "Supplier Quotation", "Purchase Order", "GRN", "Purchase Return", "Purchase Reports"],
    'Store': ["Store Dashboard", "Item Master", "Category Management", "Godown Management", "Opening Stock", "Goods Receipt (GRN)", "Material Issue", "Material Return", "Stock Transfer", "Store Reports"],
    'Production': ["Production Dashboard", "Product Master", "Bill of Materials", "Production Planning", "Production Order", "Material Requirement", "Material Issue", "WIP Management", "Production Reports"],
    'Core': ["Core Dashboard", "Work Order", "Production Planning", "Job Card", "Process Management", "Raw Material Requirement", "Material Issue", "Core Reports"],
    'Fettling': fitling_sub_modules,
    'Quality': ["Quality Dashboard", "Incoming Quality Inspection", "In-Process Quality", "Final Quality Inspection", "Quality Standards", "NCR Management", "Quality Reports"],
    'Laboratory': ["Lab Dashboard", "Sample Registration", "Sample Receiving", "Test Request", "Test Execution", "Result Entry", "Certificate Generation", "Lab Reports"],
    'Dispatch': ["Dispatch Dashboard", "Dispatch Order", "Order Verification", "Picking", "Packing", "Dispatch Challan", "Shipment Tracking", "Dispatch Reports"],
    'Accounts': ["Accounts Dashboard", "Chart of Accounts", "Sales Invoicing", "Purchase Bills", "Receipts", "Payments", "Expenses", "Tax / GST Reports", "Accounts Reports"],
    'HR': ["HR Dashboard", "Employee Master", "Attendance Entry", "Leave Management", "Payroll & Salary", "HR Reports"],
    'Maintenance': ["Maintenance Dashboard", "Asset Management", "Maintenance Request", "Breakdown Management", "Preventive Maintenance", "Maintenance Reports"],
    'Plant Head': ["Plant Overview Dashboard", "Plant KPI", "Shift Approvals", "Resource Planning"],
    'Management': ["Executive Dashboard", "Financial Overview", "Strategic Reports", "ROI Tracking"]
}

# --- PDF Generation Function ---
def generate_pdf_report(records, title):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
    story = []

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'TitleStyle', parent=styles['Heading1'], fontSize=15, leading=18, textColor=colors.HexColor("#1e293b"), spaceAfter=15
    )
    story.append(Paragraph(f"<b>Report: {title}</b>", title_style))
    story.append(Spacer(1, 10))

    table_data = [["ID", "Record Name", "Ref / Spec", "Date", "Qty", "Rate", "Details"]]
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
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#f8fafc")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))

    story.append(pdf_table)
    doc.build(story)
    buffer.seek(0)
    return buffer

# --- Sidebar UI ---
st.sidebar.title("🏭 Sanyog Foundry ERP")
selected_dept = st.sidebar.selectbox("Select Department", list(DEPARTMENT_SUBMODULES.keys()))
submodules = DEPARTMENT_SUBMODULES[selected_dept]
selected_submodule = st.sidebar.radio("Select Sub-Module", submodules)

st.title(f"{selected_dept} Department")
st.caption(f"Sub-module: **{selected_submodule}**")

# --- Form Section ---
with st.expander("➕ Add New Record Entry", expanded=True):
    with st.form("entry_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            rec_name = st.text_input("Record Name *")
            ref_no = st.text_input("Reference No / Specification")
            date_val = st.date_input("Record Date")
        with col2:
            rate = st.number_input("Rate / Amount", min_value=0.0, step=0.01)
            quantity = st.text_input("Quantity / Days")
            details = st.text_area("Additional Details / Remarks")
        
        submit_btn = st.form_submit_button("Save Record")
        if submit_btn:
            if not rec_name:
                st.error("Please provide a Record Name!")
            else:
                conn = get_db_connection()
                conn.execute('''
                    INSERT INTO department_records (department, sub_module, record_name, reference_no, date_val, rate, quantity, details)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (selected_dept.lower(), selected_submodule, rec_name, ref_no, str(date_val), rate, quantity, details))
                conn.commit()
                conn.close()
                st.success(f"Record saved under {selected_submodule}!")

# --- Data Display & Filtering Section ---
st.divider()
st.subheader("📋 Saved Records")

conn = get_db_connection()
query = "SELECT * FROM department_records WHERE department = ? AND sub_module = ? ORDER BY id DESC"
records = conn.execute(query, (selected_dept.lower(), selected_submodule)).fetchall()
conn.close()

if records:
    df = pd.DataFrame([dict(r) for r in records])
    st.dataframe(df[['id', 'record_name', 'reference_no', 'date_val', 'rate', 'quantity', 'details', 'status']], use_container_width=True)

    # --- Export Section ---
    col1, col2 = st.columns(2)
    with col1:
        # Excel Export
        excel_buffer = io.BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='ERP_Report')
        excel_buffer.seek(0)
        st.download_button(
            label="📊 Download Excel Report",
            data=excel_buffer,
            file_name=f"{selected_dept}_{selected_submodule}_report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    
    with col2:
        # PDF Export
        pdf_data = generate_pdf_report(records, f"{selected_dept} - {selected_submodule}")
        st.download_button(
            label="📄 Download PDF Report",
            data=pdf_data,
            file_name=f"{selected_dept}_{selected_submodule}_report.pdf",
            mime="application/pdf"
        )
else:
    st.info("No records found for this sub-module yet.")