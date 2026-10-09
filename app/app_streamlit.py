import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Sanyog Foundry Operations Master Dashboard",
    page_icon="🏭",
    layout="wide"
)

# Custom CSS for Professional Enterprise Dashboard Styling
st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        padding: 20px;
        border-radius: 12px;
        color: white;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .flow-bar {
        background-color: #334155;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        font-weight: 600;
        color: #f1f5f9;
        font-size: 0.85rem;
    }
    .dept-card {
        background-color: #1e293b;
        border-radius: 10px;
        padding: 18px;
        border-top: 5px solid #3b82f6;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        margin-bottom: 20px;
        color: #f8fafc;
        min-height: 290px;
    }
    .card-title {
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 8px;
        color: #38bdf8;
    }
    </style>
""", unsafe_allow_html=True)

# Top Header Section
st.markdown("""
    <div class="main-header">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h2>🏭 SANYOG FOUNDRY OPERATIONS MASTER DASHBOARD</h2>
                <p style="color: #94a3b8; margin: 0;">Quality Castings | On-Time Delivery | Sustainable Growth & Enterprise ERP</p>
            </div>
            <div style="display: flex; gap: 15px;">
                <div style="background: #334155; padding: 8px 15px; border-radius: 8px; font-size: 0.9rem;">
                    📅 <strong>Date:</strong> 09 Oct 2026
                </div>
                <div style="background: #065f46; padding: 8px 15px; border-radius: 8px; font-size: 0.9rem;">
                    🟢 <strong>Plant Status:</strong> Running
                </div>
                <div style="background: #1e3a8a; padding: 8px 15px; border-radius: 8px; font-size: 0.9rem;">
                    🎯 <strong>Overall OEE:</strong> 78.5%
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# End-to-End Process Flow Bar
st.markdown("### 🔄 Foundry End-to-End Process Flow")
flow_cols = st.columns(9)
flows = ["Sales", "Development", "Purchase", "Store", "Production", "Core", "Fettling", "Quality/Lab", "Dispatch"]
for i, col in enumerate(flow_cols):
    with col:
        st.markdown(f'<div class="flow-bar">{flows[i]}</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Initialize Session State for Navigation
if 'selected_dept' not in st.session_state:
    st.session_state.selected_dept = "Operations Master Dashboard"

# Sidebar Navigation Options (All 14 Modules)
view_options = [
    "Operations Master Dashboard", 
    "📦 Store Department", 
    "🔧 Maintenance Department", 
    "🚚 Dispatch Department", 
    "📊 Accounts Department", 
    "🛒 Purchase Department", 
    "🛡️ Core Department", 
    "⚙️ Fettling Department", 
    "🔬 Quality Department", 
    "🏭 Production Department", 
    "💡 Development Department", 
    "🧪 Laboratory Department", 
    "🤝 Sales Department",
    "👔 Plant Head Portal",
    "👑 Company Head / Management"
]

current_selection = st.session_state.selected_dept
if current_selection not in view_options:
    current_selection = "Operations Master Dashboard"
    
currentIndex = view_options.index(current_selection)

# Sidebar Navigation
st.sidebar.title("🎛️ Navigation & Control")
selected_view = st.sidebar.radio("Select View / Department", view_options, index=currentIndex)
st.session_state.selected_dept = selected_view

if st.session_state.selected_dept == "Operations Master Dashboard":
    
    departments = [
        {"name": "📦 Store Department", "color": "#f97316", "work": "• RM, consumables, tools, spares & FG receipt, storage & issue\n• Inventory control & FIFO/traceability maintenance", "kpi": "Inventory Accuracy: 98%\nStock Variance: < 2%"},
        {"name": "🔧 Maintenance Department", "color": "#0ea5e9", "work": "• Furnace, moulding equipment, compressors, pumps & electricals\n• Preventive & breakdown maintenance, downtime control", "kpi": "Machine Availability: 95%\nMTTR: < 4 hrs"},
        {"name": "🚚 Dispatch Department", "color": "#22c55e", "work": "• Final quantity verification, packing, identification & documentation\n• Customer dispatch & on-time delivery (OTD)", "kpi": "On-Time Delivery: 98%\nDispatch Accuracy: 99%"},
        {"name": "📊 Accounts Department", "color": "#a855f7", "work": "• Financial transactions, billing, payments, receipts & payroll\n• Costing, taxation, financial records & management reporting", "kpi": "Cost Variance: < 3%\nFinancial Accuracy: 99%"},
        {"name": "🛒 Purchase Department", "color": "#6366f1", "work": "• Raw material, alloys, sand & spare parts sourcing\n• Supplier selection, quotation comparison, negotiation & OTD", "kpi": "Purchase Cost Saving: 5%\nSupplier OTD: 95%"},
        {"name": "🛡️ Core Department", "color": "#14b8a6", "work": "• Sand preparation, core making, curing/baking & core box control\n• Dimensional inspection & core identification", "kpi": "Core Rejection: < 3%\nCore Productivity: 10% ↑"},
        {"name": "⚙️ Fettling Department", "color": "#eab308", "work": "• Sand removal, runner/riser removal, shot blasting & grinding\n• Dressing and finishing castings for inspection/dispatch", "kpi": "Finishing Rejection: < 2%\nProductivity: 10% ↑"},
        {"name": "🔬 Quality Department", "color": "#8b5cf6", "work": "• Incoming to final casting quality planning, inspection & process control\n• Defect analysis, CAPA & customer complaint reduction", "kpi": "First Pass Yield: 96.5%\nCustomer PPM: < 380"},
        {"name": "🏭 Production Department", "color": "#3b82f6", "work": "• Production planning, manpower & machine utilization\n• Process control, productivity & safe efficient production", "kpi": "Target Achievement: 96%\nOEE: 78.5%"},
        {"name": "💡 Development Department", "color": "#06b6d4", "work": "• New casting/product, process & pattern/core development\n• Trial casting, process optimization & successful transfer to production", "kpi": "First Trial Success: 88%\nOn-Time Dev: 95%"},
        {"name": "🧪 Laboratory Department", "color": "#1e40af", "work": "• Chemical analysis, spectrometer, sand, hardness & microstructure tests\n• Maintaining test reports & material/process traceability", "kpi": "Testing Accuracy: 99.5%\nAvg TAT: < 2 Hrs"},
        {"name": "🤝 Sales Department", "color": "#be185d", "work": "• Customer requirements, enquiry handling, quotation & order follow-up\n• Customer communication, sales planning & business development", "kpi": "Order Booking: ₹ 4.5 Cr\nEnquiry Conversion: 28%"},
        {"name": "👔 Plant Head Portal", "color": "#10b981", "work": "• Plant-level coordination & monitoring of Production, Quality, Maintenance & Safety\n• Improving productivity, quality, delivery & profitability", "kpi": "Plant OEE: 78.5%\nPlant Safety: 100%"},
        {"name": "👑 Company Head / Management", "color": "#f43f5e", "work": "• Business strategy, financial planning, investment & policy making\n• Leadership, overall performance & long-term growth & profitability", "kpi": "Monthly Revenue: ₹ 4.15 Cr\nNet Profit: 14.2%"}
    ]

    # Grid Display (3 columns per row)
    for i in range(0, len(departments), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(departments):
                dept = departments[i + j]
                with cols[j]:
                    st.markdown(f"""
                        <div class="dept-card" style="border-top-color: {dept['color']};">
                            <div class="card-title">{dept['name']}</div>
                            <hr style="margin: 4px 0 8px 0; border-color: #334155;">
                            <p style="font-size: 0.82rem; color: #cbd5e1; margin-bottom: 8px;"><strong>Core Functions:</strong><br>{dept['work'].replace(chr(10), '<br>')}</p>
                            <div style="background: rgba(15, 23, 42, 0.6); padding: 8px; border-radius: 6px; font-size: 0.82rem; border-left: 3px solid {dept['color']};">
                                <strong>Key KPIs:</strong><br>{dept['kpi'].replace(chr(10), '<br>')}
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    clean_name = dept['name']
                    if st.button(f"Manage {clean_name.split(' ', 1)[1]}", key=f"btn_{i+j}", use_container_width=True):
                        st.session_state.selected_dept = dept['name']
                        st.rerun()

    # Bottom Summary Bar
    st.markdown("---")
    b_cols = st.columns(4)
    with b_cols[0]:
        st.metric(label="Total Production (MT)", value="1,250 MT", delta="8% vs last month")
    with b_cols[1]:
        st.metric(label="Rejection Rate", value="1.8%", delta="-0.5% vs last month")
    with b_cols[2]:
        st.metric(label="On-Time Delivery", value="98%", delta="3% vs last month")
    with b_cols[3]:
        st.metric(label="Monthly Revenue", value="₹ 4.15 Cr", delta="12% YoY")

else:
    # Specific Department Management Portal
    current_dept = st.session_state.selected_dept
    st.title(f"🛠️ {current_dept} Management Portal")
    st.write(f"Complete operational workspace and specialized records for **{current_dept}**.")
    
    if st.button("⬅️ Back to Operations Master Dashboard"):
        st.session_state.selected_dept = "Operations Master Dashboard"
        st.rerun()
        
    tab1, tab2, tab3 = st.tabs(["Active Records & Tracking", "Add New Entry / Form", "Month-Wise Reports & KPIs"])
    
    # Common Month Selector for Reports Tab
    months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    # 1. STORE DEPARTMENT
    if "Store" in current_dept:
        with tab1:
            st.subheader("📦 Stock Ledger / Bin Card (Current Inventory & Movement)")
            st.dataframe(pd.DataFrame({
                "Item Name": ["Pig Iron", "Scrap Grade A", "Resin Binder", "Core Sand"],
                "Category": ["Raw Material", "Raw Material", "Consumables", "Raw Material"],
                "Stock Qty (Kg)": [15000, 8500, 420, 12000],
                "Min Stock Level": [5000, 3000, 200, 4000],
                "Status": ["Optimal", "Low - Reorder", "Optimal", "Optimal"]
            }), use_container_width=True)
            st.info("💡 **FIFO & Traceability:** Raw materials and finished castings are maintained strictly on FIFO basis.")
        with tab2:
            st.subheader("Store Document Tracking & Inward Entry Form")
            with st.form("store_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input("Gate Inward No.")
                    st.text_input("DC No. (Delivery Challan)")
                    st.text_input("PO No. (Purchase Order)")
                    st.text_input("PR No. (Purchase Requisition)")
                    st.text_input("MRN / Requisition No.")
                with col2:
                    st.text_input("GRN No. (Goods Receipt Note)")
                    st.text_input("Inspection Report No.")
                    st.text_input("Material Issue Slip No.")
                    st.text_input("Return Note No.")
                    st.text_input("NCR No. / Rejection Note")
                st.text_area("Material Details, Supplier Name & Remarks")
                st.form_submit_button("Save Store Document Record")
        with tab3:
            st.subheader("📦 Store Department Month-Wise Report")
            selected_month = st.selectbox("Select Month for Store Report", months_list, index=9)
            st.write(f"Showing inventory accuracy and stock variance summary for **{selected_month} 2026**.")
            st.dataframe(pd.DataFrame({
                "Metric": ["Total Inward Transactions", "Total Material Issues", "Stock Reconciliation Accuracy", "Stock Variances Noted"],
                f"{selected_month} Value": ["145 Entries", "110 Slips", "98.5%", "1.5%"]
            }), use_container_width=True)
            st.line_chart(pd.DataFrame({"Inventory Accuracy %": [97, 97.5, 98, 98.5, 99]}))

    # 2. MAINTENANCE DEPARTMENT
    elif "Maintenance" in current_dept:
        with tab1:
            st.subheader("🔧 Machine Asset Register & Breakdown History")
            st.dataframe(pd.DataFrame({
                "Asset ID": ["AST-F01", "AST-CS02", "AST-SB03", "AST-CMP04"],
                "Machine Name": ["Induction Furnace 1", "Core Shooter", "Shot Blasting Machine", "Air Compressor"],
                "Department": ["Furnace Dept", "Core Shop", "Fettling", "Utilities"],
                "Criticality": ["High", "Medium", "High", "Critical"],
                "Status": ["Running", "Under Maintenance", "Running", "Running"]
            }), use_container_width=True)
            st.info("💡 **Best Practice:** Each breakdown is linked with Machine ID + Breakdown No. + WO No. + Root Cause + Downtime + Action Taken for effective analysis.")
        with tab2:
            st.subheader("Maintenance Work Order & Breakdown Entry Form")
            with st.form("maint_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input("Asset ID / Machine ID")
                    st.text_input("Breakdown No. / Complaint No.")
                    st.text_input("WO No. - Work Order No.")
                    st.text_input("PM Schedule No. / PM Checklist No.")
                    st.selectbox("Maintenance Type", ["Preventive Maintenance", "Breakdown Maintenance", "Condition Monitoring", "Utility Service"])
                with col2:
                    st.text_input("Spare Requisition No. / Item Code")
                    st.text_input("Assigned Technician Name")
                    st.number_input("Downtime Hours", 0.0)
                    st.text_input("Root Cause (RCA)")
                    st.text_input("Action Taken & Restart Time")
                st.text_area("Fault Description & Work Description Remarks")
                st.form_submit_button("Save Maintenance & WO Record")
        with tab3:
            st.subheader("🔧 Maintenance Department Month-Wise Report & KPIs")
            selected_month = st.selectbox("Select Month for Maintenance Report", months_list, index=9)
            
            col_m1, col_m2, col_m3, col_m4 = st.columns(4)
            with col_m1:
                st.metric("Machine Availability", "95.5%", "1.2% vs last month")
            with col_m2:
                st.metric("PM Compliance", "98.0%", "2.5% ↑")
            with col_m3:
                st.metric("MTTR (Mean Time to Repair)", "3.2 Hrs", "-0.5 hrs")
            with col_m4:
                st.metric("MTBF (Mean Time Between Failures)", "164 Hrs", "12 hrs ↑")

            st.write(f"Detailed maintenance performance summary for **{selected_month} 2026**.")
            st.dataframe(pd.DataFrame({
                "Report Type": ["Daily Breakdown Report", "PM Due / Completed Report", "Machine Downtime Report", "Pending Work Orders", "Spare Parts Consumption", "Critical Spare Stock Report", "Monthly Maintenance Cost"],
                f"{selected_month} Status": ["Verified", "100% Completed", "Total 18.5 Hrs", "2 Open WOs", "₹ 2.4 Lakhs", "Optimal", "₹ 4.8 Lakhs"]
            }), use_container_width=True)
            st.line_chart(pd.DataFrame({"Machine Availability %": [93, 94, 95, 95.5]}))

    # 3. DISPATCH DEPARTMENT
    elif "Dispatch" in current_dept:
        with tab1:
            st.subheader("📦 Dispatch Register & Order Tracking")
            st.dataframe(pd.DataFrame({
                "Dispatch Date": ["08-Oct-2026", "08-Oct-2026", "07-Oct-2026"],
                "Customer Name": ["Tata Motors", "Kirloskar Brothers", "Bharat Forge"],
                "Customer PO No.": ["PO-8921", "PO-4412", "PO-9012"],
                "Part No. / Grade": ["TM-HSG-01 / FG-260", "KB-IMP-04 / FG-300", "BF-BRK-09 / SG-400"],
                "Dispatch Qty (MT)": [12.5, 8.0, 15.2],
                "DC No.": ["DC-2026-101", "DC-2026-102", "DC-2026-103"],
                "Vehicle No.": ["MH-11-Q-4521", "MH-14-BW-9921", "MH-09-AA-1234"],
                "POD Status": ["Received", "Pending", "Received"]
            }), use_container_width=True)
            st.info("💡 **Traceability Rule:** Complete traceability is maintained from Customer PO No. → Sales Order → Dispatch Plan → Quality Clearance → DC & Invoice → Gate Outward → POD Delivery.")
        with tab2:
            st.subheader("Create New Dispatch Entry & Document Generation")
            with st.form("dispatch_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input("Customer Name")
                    st.text_input("Customer PO No.")
                    st.text_input("Sales Order No.")
                    st.text_input("Dispatch Plan No.")
                    st.text_input("Part No. & Grade / Batch No.")
                    st.number_input("Planned Qty vs Dispatch Qty (MT)", 0.0)
                    st.text_input("Packing List No. & Box/Pallet Count")
                with col2:
                    st.text_input("Inspection Report No. (Quality Clearance)")
                    st.text_input("DC No. - Delivery Challan")
                    st.text_input("Invoice No. & Date")
                    st.text_input("Vehicle No. & Driver Name")
                    st.text_input("Transporter Name & LR/GR No.")
                    st.text_input("E-way Bill No.")
                    st.text_input("Gate Outward No. & Dispatch Time")
                st.text_area("Delivery Instructions, Remarks & Shortage/Damage Notes")
                st.form_submit_button("Generate Dispatch & Save Record")
        with tab3:
            st.subheader("🚚 Dispatch Department Month-Wise Report & KPIs")
            selected_month = st.selectbox("Select Month for Dispatch Report", months_list, index=9)
            col_d1, col_d2, col_d3, col_d4 = st.columns(4)
            with col_d1:
                st.metric("Total Dispatch Tonnage", "1,250 MT", "8% vs last month")
            with col_d2:
                st.metric("On-Time Delivery (OTD)", "98.2%", "1.5% ↑")
            with col_d3:
                st.metric("Pending Orders Qty", "45 MT", "-12 MT")
            with col_d4:
                st.metric("Document Errors", "0 Count", "Zero defect")
            st.write(f"Detailed dispatch and logistics performance summary for **{selected_month} 2026**.")
            st.dataframe(pd.DataFrame({
                "Parameter / Report Type": ["Daily Dispatch Schedule Tracking", "Finished Goods Stock Verification", "Quality Clearance Audit", "Transport & Vehicle Availability", "DC & Tax Invoice Reconciliation", "POD Collection Status", "Damage / Shortage Cases"],
                f"{selected_month} Status": ["100% On Schedule", "Available", "Approved", "Coordinated", "Reconciled", "96% Received", "0 Cases"]
            }), use_container_width=True)
            st.bar_chart(pd.DataFrame({"Dispatched Tonnage (MT)": [310, 330, 345, 360]}))

    # 4. ACCOUNTS DEPARTMENT
    elif "Accounts" in current_dept:
        with tab1:
            st.subheader("📊 Ledger & Voucher Register (Purchase, Sales & Receipts)")
            st.dataframe(pd.DataFrame({
                "Voucher No.": ["PV-2026-101", "RV-2026-102", "JV-2026-103", "PV-2026-104"],
                "Date": ["08-Oct-2026", "08-Oct-2026", "07-Oct-2026", "06-Oct-2026"],
                "Voucher Type": ["Payment", "Receipt", "Journal", "Payment"],
                "Party Name": ["JSW Steel (Supplier)", "Tata Motors (Customer)", "Depreciation Adjustment", "National Alloys"],
                "PO / Invoice No.": ["PO-501 / INV-881", "INV-2026-302", "JV-DEP-01", "PO-502 / INV-412"],
                "Amount (₹)": [450000, 1250000, 85000, 210000],
                "Status": ["Paid (UTR-9981)", "Received", "Adjusted", "Paid (UTR-7742)"]
            }), use_container_width=True)
            st.info("💡 **Traceability Rule:** Complete linkage is maintained: PO No. → GRN No. → Supplier Invoice → Payment Voucher, and Customer PO → Sales Invoice → DC → Receipt Voucher.")
        with tab2:
            st.subheader("Bill Booking, Payment & Receipt Voucher Entry Form")
            with st.form("accounts_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.selectbox("Voucher Type", ["Purchase Bill Booking (Payment)", "Sales Invoice (Receipt)", "Payment Voucher", "Receipt Voucher", "Journal Voucher (JV)"])
                    st.text_input("Voucher No. / Reference No.")
                    st.text_input("Party Name & Code")
                    st.text_input("PO No. / GRN No. / DC No.")
                    st.text_input("Supplier Invoice No. / Sales Invoice No.")
                    st.number_input("Taxable Amount (₹)", 0.0)
                with col2:
                    st.number_input("CGST / SGST / IGST Amount (₹)", 0.0)
                    st.number_input("TDS Amount Deducted (₹)", 0.0)
                    st.number_input("Total Amount (₹)", 0.0)
                    st.date_input("Due Date")
                    st.selectbox("Payment Mode", ["NEFT / RTGS", "Cheque", "UPI / NetBanking", "Cash"])
                    st.text_input("Bank UTR No. / Cheque No.")
                st.text_area("Narration, Remarks & Reconciliation Status")
                st.form_submit_button("Save Accounts Voucher & Post Entry")
        with tab3:
            st.subheader("📊 Accounts Department Month-Wise Report & Financial KPIs")
            selected_month = st.selectbox("Select Month for Accounts Report", months_list, index=9)
            
            col_a1, col_a2, col_a3, col_a4 = st.columns(4)
            with col_a1:
                st.metric("Customer Receivables", "₹ 2.45 Cr", "-5% vs last month")
            with col_a2:
                st.metric("Overdue Amount", "₹ 35.2 Lakhs", "Controlled")
            with col_a3:
                st.metric("Supplier Payables", "₹ 1.85 Cr", "On Schedule")
            with col_a4:
                st.metric("BRS Reconciliation", "100%", "Matched")

            st.write(f"Comprehensive financial summary, tax compliance, and billing report for **{selected_month} 2026**.")
            st.dataframe(pd.DataFrame({
                "Financial Activity / Report Type": ["Purchase Bill Booking & Verification", "Supplier Payment & UTR Reconciliation", "Customer Sales Billing & Invoicing", "Customer Receipt & Outstanding Tracking", "Bank Reconciliation Statement (BRS)", "GST Return & TDS Compliance Filing", "Monthly P&L & Costing Reconciliation"],
                f"{selected_month} Status": ["Verified", "Processed", "₹ 4.15 Cr Billed", "Reconciled", "Completed", "Filed on Portal", "Updated"]
            }), use_container_width=True)
            st.line_chart(pd.DataFrame({"Cost Variance %": [2.8, 2.5, 2.2, 2.0]}))

    # 5. PURCHASE DEPARTMENT
    elif "Purchase" in current_dept:
        with tab1:
            st.subheader("🛒 Purchase Requisitions, Comparative Statements & PO Register")
            st.dataframe(pd.DataFrame({
                "PR No.": ["PR-2026-011", "PR-2026-012", "PR-2026-013"],
                "Department": ["Furnace Dept", "Core Shop", "Maintenance"],
                "Item Description": ["Pig Iron (Grade-1)", "Resin Binder", "Hydraulic Pump Parts"],
                "Order Qty": ["15 MT", "2000 Kg", "1 Set"],
                "PO No.": ["PO-501", "PO-502", "PO-503"],
                "Supplier Name": ["JSW Steel", "National Chem", "Industrial Spares"],
                "Expected Delivery": ["12-Oct-2026", "15-Oct-2026", "20-Oct-2026"],
                "Status": ["PO Issued", "Approved", "In Transit"]
            }), use_container_width=True)
            st.info("💡 **Procurement Chain:** PR No. → RFQ → Comparative Statement (CS) → PO No. → Gate Inward → GRN No. → Supplier Invoice Matching.")
        with tab2:
            st.subheader("Create Purchase Requisition, RFQ & Purchase Order (PO)")
            with st.form("purchase_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input("PR No. & Requesting Department")
                    st.text_input("RFQ No. & Supplier Name")
                    st.text_input("Comparative Statement (CS) No.")
                    st.text_input("PO No. - Purchase Order No.")
                    st.text_input("Item Code & Material Description")
                    st.number_input("Order Quantity", 0.0)
                with col2:
                    st.number_input("Negotiated Rate (₹)", 0.0)
                    st.number_input("GST / Freight Charges (%)", 0.0)
                    st.date_input("Expected Delivery Date")
                    st.text_input("Gate Inward No. & GRN No. (Linking)")
                    st.text_input("Supplier Invoice No.")
                    st.selectbox("Supplier OTD & Quality Status", ["On-Time & Accepted", "Delayed Supply", "Quality Rejected / NCR", "Pending"])
                st.text_area("Terms & Conditions, Payment Terms & Remarks")
                st.form_submit_button("Save Purchase Record & Release PO")
        with tab3:
            st.subheader("🛒 Purchase Department Month-Wise Report & KPIs")
            selected_month = st.selectbox("Select Month for Purchase Report", months_list, index=9)
            
            col_p1, col_p2, col_p3, col_p4 = st.columns(4)
            with col_p1:
                st.metric("Total Purchase Value", "₹ 2.10 Cr", "4% vs last month")
            with col_p2:
                st.metric("Supplier OTD %", "95.2%", "2.1% ↑")
            with col_p3:
                st.metric("Cost Savings", "₹ 8.5 Lakhs", "Target Achieved")
            with col_p4:
                st.metric("PR-to-PO Lead Time", "1.5 Days", "Fast")

            st.write(f"Comprehensive procurement performance and supplier evaluation summary for **{selected_month} 2026**.")
            st.dataframe(pd.DataFrame({
                "Procurement Activity / Report": ["PR Verification & Prioritization", "RFQ & Comparative Statement Evaluation", "PO Generation & Supplier Follow-up", "Gate Inward & GRN Coordination", "Supplier Rejection & Replacement Tracking", "PO-GRN-Invoice Matching & Accounts Handover", "Monthly Supplier Rating & Cost Analysis"],
                f"{selected_month} Status": ["Completed", "Evaluated", "Issued", "Coordinated", "Resolved", "Matched", "Published"]
            }), use_container_width=True)
            st.line_chart(pd.DataFrame({"Supplier OTD %": [92, 93, 94, 95.2]}))

    # 6. CORE DEPARTMENT
    elif "Core" in current_dept:
        with tab1:
            st.subheader("🛡️ Core Production Register & Batch Tracking")
            st.dataframe(pd.DataFrame({
                "Prod Plan No.": ["PLN-2026-081", "PLN-2026-082", "PLN-2026-083"],
                "Part Name / No.": ["Housing Cover (TM-01)", "Hydraulic Body (KB-04)", "Bracket (BF-09)"],
                "Core Box ID": ["CB-101", "CB-104", "CB-112"],
                "Sand Batch No.": ["SB-2026-551", "SB-2026-552", "SB-2026-553"],
                "Target Qty": [500, 350, 400],
                "Actual Qty": [485, 350, 390],
                "Rejection %": ["3.0%", "0.0%", "2.5%"],
                "Status": ["Completed", "Completed", "Issued to Moulding"]
            }), use_container_width=True)
            st.info("💡 **Traceability Rule:** Core Batch No. is linked with Casting Batch No. to trace internal casting defects directly to the core department, sand mix, or machine setup.")
        with tab2:
            st.subheader("Core Production, Sand Mix & Inspection Entry Form")
            with st.form("core_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input("Production Plan No. & Part No.")
                    st.text_input("Core Box ID & Machine ID")
                    st.text_input("Sand Batch No. & Material Issue Slip No.")
                    st.number_input("Resin % & Hardener %", 0.0, format="%.2f")
                    st.text_input("Core Production Batch No.")
                    st.number_input("Target Qty vs Actual Produced Qty", 0)
                with col2:
                    st.number_input("Accepted Qty & Rejected Qty", 0)
                    st.text_input("Defect Code / Rejection Reason")
                    st.text_input("Inspection Report No. (Dimensional & Hardness)")
                    st.text_input("Core Issue Slip No. (To Moulding)")
                    st.text_input("Operator Name & Shift")
                    st.selectbox("Core Availability & Supply Status", ["Ready in Stock", "Issued to Moulding", "Under Inspection", "Rework Required"])
                st.text_area("Curing Parameters, Mixing Time & Remarks")
                st.form_submit_button("Save Core Production Record")
        with tab3:
            st.subheader("🛡️ Core Department Month-Wise Report & KPIs")
            selected_month = st.selectbox("Select Month for Core Report", months_list, index=9)
            
            col_c1, col_c2, col_c3, col_c4 = st.columns(4)
            with col_c1:
                st.metric("Core Productivity", "125 Pcs/Hr", "5% ↑")
            with col_c2:
                st.metric("Core Rejection Rate", "2.1%", "-0.8% vs last month")
            with col_c3:
                st.metric("Material Consumption", "Optimized", "Within limits")
            with col_c4:
                st.metric("On-Time Core Supply", "99.1%", "Excellent")

            st.write(f"Comprehensive core room performance, sand mix recipe compliance, and rejection analysis for **{selected_month} 2026**.")
            st.dataframe(pd.DataFrame({
                "Core Activity / Report": ["Production Plan & Target Verification", "Sand Mix Recipe & Resin % Audit", "Core Box & Machine Setup Inspection", "Core Making & Curing Process Control", "Dimensional & Hardness Quality Inspection", "Core Storage & Issue to Moulding Dept", "Rejection & Defect Reason Analysis"],
                f"{selected_month} Status": ["Achieved", "Compliant", "Verified", "Monitored", "Inspected", "Issued", "Analyzed"]
            }), use_container_width=True)
            st.line_chart(pd.DataFrame({"Core Rejection %": [3.5, 2.9, 2.4, 2.1]}))

    # 7. FETTLING DEPARTMENT
    elif "Fettling" in current_dept:
        with tab1:
            st.subheader("⚙️ Fettling & Casting Finishing Register")
            st.dataframe(pd.DataFrame({
                "Casting Receipt No.": ["RPT-2026-301", "RPT-2026-302", "RPT-2026-303"],
                "Part Name / No.": ["Housing Cover (TM-01)", "Hydraulic Body (KB-04)", "Bracket (BF-09)"],
                "Production Batch": ["BATCH-881", "BATCH-882", "BATCH-883"],
                "Received Qty": [450, 320, 380],
                "Gate/Riser Removal": ["Completed", "Completed", "In Progress"],
                "Shot Blasting Status": ["Done", "Done", "Pending"],
                "Accepted Qty": [435, 312, 360],
                "Status": ["Handed over to FG", "Handed over to FG", "Processing"]
            }), use_container_width=True)
            st.info("💡 **Traceability Rule:** Complete linkage from Casting Receipt Batch → Operation Card → Grinding/Shot Blasting → Final Inspection → Rework Tag / NCR → Handover Slip to FG Store.")
        with tab2:
            st.subheader("Casting Finishing, Grinding, Shot Blasting & Rework Entry Form")
            with st.form("fettling_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input("Casting Receipt No. & Production Batch No.")
                    st.text_input("Part Name, No. & Grade")
                    st.number_input("Received Quantity from Shakeout", 0)
                    st.text_input("Operation Card No. & Process Route")
                    st.selectbox("Gate, Runner & Riser Removal Status", ["Completed Clean", "Rework Required", "Pending"])
                    st.text_input("Grinding Machine ID & Operator Name")
                with col2:
                    st.number_input("Grinding Wheel Consumption (Pcs/Hrs)", 0.0)
                    st.text_input("Shot Blasting Machine ID & Cycle Time")
                    st.number_input("Accepted Finished Qty vs Rejected Qty", 0)
                    st.text_input("Rework Tag No. / NCR No. (if defect found)")
                    st.text_input("Inspection Report No. (Visual & Dimensional)")
                    st.text_input("Handover Slip No. (To Machining / FG Store)")
                st.text_area("Surface Defects, Excess Metal Notes & Remarks")
                st.form_submit_button("Save Fettling & Finishing Record")
        with tab3:
            st.subheader("⚙️ Fettling Department Month-Wise Report & KPIs")
            selected_month = st.selectbox("Select Month for Fettling Report", months_list, index=9)
            
            col_f1, col_f2, col_f3, col_f4 = st.columns(4)
            with col_f1:
                st.metric("Finishing Productivity", "94.5%", "3% ↑")
            with col_f2:
                st.metric("Fettling Rejection %", "1.5%", "Low")
            with col_f3:
                st.metric("Rework Rate", "3.2%", "Controlled")
            with col_f4:
                st.metric("Grinding Wheel Life", "Optimal", "Cost Efficient")

            st.write(f"Comprehensive casting finishing, grinding, shot blasting, and scrap reduction summary for **{selected_month} 2026**.")
            st.dataframe(pd.DataFrame({
                "Fettling Activity / Report": ["Casting Receipt & Batch Verification", "Gate, Runner & Riser Removal Operation", "Grinding & Surface Dressing Quality", "Shot Blasting & Media Cleanliness Audit", "Visual & Dimensional Surface Inspection", "Rework Tag & NCR Defect Control", "Handover Slip & Transfer to FG Store"],
                f"{selected_month} Status": ["Verified", "Completed", "Inspected", "Audited", "Approved", "Tracked", "Transferred"]
            }), use_container_width=True)
            st.line_chart(pd.DataFrame({"Fettling Output (MT/Day)": [22, 24, 25, 26.5]}))

    # 8. QUALITY DEPARTMENT
    elif "Quality" in current_dept:
        with tab1:
            st.subheader("🔬 Quality Assurance, Inspection & Defect Register")
            st.dataframe(pd.DataFrame({
                "Inspection ID": ["INS-2026-901", "INS-2026-902", "INS-2026-903"],
                "Heat / Batch No.": ["H-2026-410", "H-2026-411", "H-2026-412"],
                "Part Name & Grade": ["Housing Cover (FG-260)", "Hydraulic Body (FG-300)", "Bracket (SG-400)"],
                "Stage": ["Final Casting Inspection", "Incoming Material", "In-Process Pouring"],
                "Defect Noted": ["Blowhole", "None (OK)", "Shrinkage"],
                "PPM Level": [380, 0, 420],
                "CAPA Status": ["Applied & Resolved", "Passed", "Under Investigation"]
            }), use_container_width=True)
            st.info("💡 **Traceability Rule:** Complete traceability from Incoming Raw Material → Process Inspection → Lab/Metallurgical Testing → Dimensional & Visual Check → NCR / CAPA → Final Quality Clearance.")
        with tab2:
            st.subheader("Quality Inspection, Testing & NCR Entry Form")
            with st.form("quality_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input("Inspection Report No. & Heat No.")
                    st.text_input("Part Name, No. & Material Grade")
                    st.selectbox("Inspection Stage", ["Incoming Material Inspection", "Process Inspection (Moulding/Core)", "Lab / Metallurgical Testing", "Dimensional & Visual Inspection", "Fettling & Final Inspection"])
                    st.text_input("Chemical Analysis & Hardness Report Ref")
                    st.text_input("Dimensional Check Result (Vernier/Gauge)")
                    st.selectbox("Defect Category", ["Blowhole", "Shrinkage", "Sand Inclusion", "Mismatch", "Crack / Cold Shut", "None (OK)"])
                with col2:
                    st.number_input("Inspected Qty vs First-Time OK Qty", 0)
                    st.number_input("Rework Qty vs Rejection Qty", 0)
                    st.number_input("Calculated Customer PPM", 0)
                    st.text_input("NCR No. - Non-Conformance Report Ref")
                    st.text_input("CAPA / Root Cause Analysis (RCA) Ref")
                    st.selectbox("Quality Clearance Status", ["Released / Approved", "Rework Given", "Rejected / Scrap", "Customer Waiver Pending"])
                st.text_area("Quality Inspector Remarks, Calibration Ref & Sign-off")
                st.form_submit_button("Save Quality Inspection Record")
        with tab3:
            st.subheader("🔬 Quality Department Month-Wise Report & KPIs")
            selected_month = st.selectbox("Select Month for Quality Report", months_list, index=9)
            
            col_q1, col_q2, col_q3, col_q4 = st.columns(4)
            with col_q1:
                st.metric("First Pass Yield", "96.5%", "1.2% ↑")
            with col_q2:
                st.metric("Customer PPM", "380 PPM", "Target < 500")
            with col_q3:
                st.metric("NCR Closure Rate", "98.0%", "Fast Action")
            with col_q4:
                st.metric("Internal Rejection %", "1.8%", "-0.5%")

            st.write(f"Comprehensive quality performance, first pass yield, and defect analysis summary for **{selected_month} 2026**.")
            st.dataframe(pd.DataFrame({
                "Quality Activity / Report": ["Customer Drawing & Specification Review", "Incoming Raw Material Inspection", "Process & Lab / Metallurgical Testing", "Dimensional & Final Casting Inspection", "NCR Generation & Defect Disposition", "RCA & CAPA Corrective Action Tracking", "Final Quality Clearance & Release"],
                f"{selected_month} Status": ["Reviewed", "Verified", "Tested", "Inspected", "Tracked", "Closed", "Cleared"]
            }), use_container_width=True)
            st.line_chart(pd.DataFrame({"First Pass Yield %": [94.0, 95.2, 96.0, 96.5]}))

    # 9. PRODUCTION DEPARTMENT
    elif "Production" in current_dept:
        tab_p1, tab_p2, tab_p3 = st.tabs(["Active Records & Tracking", "Add New Entry / Form", "Month-Wise Reports & Daily Department Report"])
        
        with tab_p1:
            st.subheader("🏭 Production Planning, Shift Register & Melting/Pouring Logs")
            st.dataframe(pd.DataFrame({
                "Prod Plan No.": ["PLN-2026-501", "PLN-2026-502", "PLN-2026-503"],
                "Shift": ["Morning Shift", "Evening Shift", "Night Shift"],
                "Casting Grade / Part": ["FG-260 / Housing", "FG-300 / Body", "SG-400 / Bracket"],
                "Target (Qty/MT)": ["30 MT", "25 MT", "28 MT"],
                "Actual Produced": ["29.2 MT", "25.5 MT", "27.8 MT"],
                "OEE %": ["79.2%", "78.0%", "80.5%"],
                "Status": ["Achieved", "Achieved", "Achieved"]
            }), use_container_width=True)
            st.info("💡 **Traceability Rule:** Complete linkage from Production Plan → Job/Route Card → Material Issue Slip → Charge Calculation → Heat Number / Melting Log → Pouring → Shakeout → Fettling Handover.")
        
        with tab_p2:
            st.subheader("Shift Production Planning, Melting & Pouring Entry Form")
            with st.form("production_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input("Production Plan No. & Job Card / Route Card No.")
                    st.selectbox("Shift", ["Morning Shift", "Evening Shift", "Night Shift"])
                    st.text_input("Material Issue Slip No. & Charge Calculation Ref")
                    st.text_input("Heat Number / Batch Record No.")
                    st.text_input("Casting Grade & Part Name / No.")
                    st.number_input("Target Production Qty vs Actual Produced Qty", 0)
                with col2:
                    st.number_input("Total Metal Input Weight (Kg) vs Good Casting Weight (Kg)", 0.0)
                    st.slider("Material Yield %", 0.0, 100.0, 72.0)
                    st.slider("OEE % (Overall Equipment Effectiveness)", 0.0, 100.0, 78.5)
                    st.text_input("Furnace Temperature (°C) & Pouring Timing")
                    st.text_input("Machine Downtime Hours & Reason")
                    st.selectbox("Production Handover Status", ["Completed & Handed Over to Quality", "WIP in Process", "Pending Due to Breakdown"])
                st.text_area("Shift Notes, Lab Chemistry Correction & Remarks")
                st.form_submit_button("Save Production & Heat Log Record")
                
        with tab_p3:
            st.subheader("📊 Production Month-Wise Report & Daily Department Report")
            selected_month = st.selectbox("Select Month for Production Report", months_list, index=9)
            
            col_pr1, col_pr2, col_pr3, col_pr4 = st.columns(4)
            with col_pr1:
                st.metric("Monthly Production", "1,250 MT", "8% ↑")
            with col_pr2:
                st.metric("Target Achievement", "96.4%", "On Track")
            with col_pr3:
                st.metric("Material Yield %", "72.5%", "Optimal")
            with col_pr4:
                st.metric("Plant OEE", "78.5%", "Good")

            st.markdown("---")
            st.subheader("📋 Foundry Daily Department Report (Production vs Quality)")
            st.write(f"Daily operational summary for **{selected_month} 2026** across shifts.")
            
            daily_report_df = pd.DataFrame({
                "Department": ["Production Department", "Quality Department"],
                "A Shift": ["Target: 35 MT | Actual: 34 MT | OK: 33 MT | Rej: 1 MT", "Inspected: 34 MT | Yield: 97% | FPY: 96.5%"],
                "B Shift": ["Target: 35 MT | Actual: 35.5 MT | OK: 35 MT | Rej: 0.5 MT", "Inspected: 35.5 MT | Yield: 98% | FPY: 97.0%"],
                "C Shift": ["Target: 30 MT | Actual: 29.5 MT | OK: 28.8 MT | Rej: 0.7 MT", "Inspected: 29.5 MT | Yield: 97.5% | FPY: 96.8%"],
                "Daily Remarks": ["Minor furnace delay in A shift resolved", "All heats verified via spectrometer & lab test"]
            })
            st.dataframe(daily_report_df, use_container_width=True)
            st.bar_chart(pd.DataFrame({"Daily Production Tonnage": [34, 35.5, 29.5]}))

    # 10. DEVELOPMENT DEPARTMENT
    elif "Development" in current_dept:
        with tab1:
            st.subheader("💡 New Product Development & Trial Casting Register")
            st.dataframe(pd.DataFrame({
                "Dev ID": ["DEV-2026-01", "DEV-2026-02", "DEV-2026-03"],
                "Customer / Part Name": ["Tata Motors / Housing Cover", "Kirloskar / Impeller", "Bharat Forge / Bracket"],
                "Material Grade": ["FG-260", "FG-300", "SG-400"],
                "Pattern / Tooling ID": ["PAT-101", "PAT-102", "PAT-103"],
                "Development Stage": ["Trial Casting", "Customer Sample Approval", "Production Handover"],
                "Trial Success": ["Success", "Pending Approval", "Completed"],
                "Status": ["In Progress", "Submitted", "Handed Over"]
            }), use_container_width=True)
            st.info("💡 **Traceability Rule:** Customer Drawing / 3D Model → Feasibility Report → Tooling/Pattern ID → Trial Casting → Lab/Quality Testing → RCA & Defect Correction → Customer Sample Approval → Production Handover.")
        with tab2:
            st.subheader("New Product Development, Trial & Handover Entry Form")
            with st.form("development_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input("Development Project ID & Customer Name")
                    st.text_input("Component Part Name, No. & Material Grade")
                    st.text_input("Customer Drawing No. & Revision / ECN Ref")
                    st.text_input("Pattern / Core Box ID & Tooling Reference")
                    st.selectbox("Development Stage", ["Technical Feasibility & Cost Estimation", "Pattern & Tooling Development", "Trial Casting & Pouring", "Lab & Quality Testing", "Customer Sample Approval", "Production Handover"])
                    st.number_input("Trial Planned Qty vs Actual Trial Produced Qty", 0)
                with col2:
                    st.selectbox("Trial Result Status", ["First Trial Success (OK)", "Trial Defect - RCA Required", "Sample Submitted to Customer", "Customer Approved", "Production Handover Done"])
                    st.text_input("Dimensional & Metallurgical Report Ref")
                    st.text_input("Defect Analysis / RCA Ref (if trial failed)")
                    st.text_input("Sample Approval Report Ref")
                    st.text_input("Production Handover Checklist Ref")
                    st.number_input("Development Lead Time (Days)", 0)
                st.text_area("Technical Feasibility Notes, Process Parameters & Remarks")
                st.form_submit_button("Save Development & Trial Record")
        with tab3:
            st.subheader("💡 Development Department Month-Wise Report & KPIs")
            selected_month = st.selectbox("Select Month for Development Report", months_list, index=9)
            
            col_dev1, col_dev2, col_dev3, col_dev4 = st.columns(4)
            with col_dev1:
                st.metric("First Trial Success %", "88.0%", "5% ↑")
            with col_dev2:
                st.metric("On-Time Development %", "95.0%", "Optimal")
            with col_dev3:
                st.metric("Sample Approval Rate", "92.0%", "Fast")
            with col_dev4:
                st.metric("Handover Completion", "100%", "Completed")

            st.write(f"Comprehensive new product development performance, trial success rate, and lead time tracking for **{selected_month} 2026**.")
            st.dataframe(pd.DataFrame({
                "Development Activity / Report": ["Customer Drawing & Feasibility Review", "Tooling & Pattern Development Verification", "Trial Casting, Melting & Pouring Execution", "Lab Chemical & Dimensional Testing Review", "Defect Analysis & RCA Correction", "Customer Sample Submission & Approval", "Production & Quality Handover Completion"],
                f"{selected_month} Status": ["Reviewed", "Verified", "Executed", "Reviewed", "Resolved", "Approved", "Completed"]
            }), use_container_width=True)
            st.line_chart(pd.DataFrame({"First Trial Success %": [80, 83, 85, 88]}))

    # 11. LABORATORY DEPARTMENT
    elif "Laboratory" in current_dept:
        with tab1:
            st.subheader("🧪 Laboratory Test Register, Spectrometer & Sand Testing Log")
            st.dataframe(pd.DataFrame({
                "Sample ID": ["SMP-2026-801", "SMP-2026-802", "SMP-2026-803"],
                "Heat / Batch No.": ["H-2026-410", "H-2026-411", "SAND-BATCH-52"],
                "Test Type": ["Chemical Analysis (Spectrometer)", "Hardness Test (BHN)", "Sand Testing (Moisture & Strength)"],
                "Material Grade": ["FG-260", "SG-400", "Green Sand Mix"],
                "Key Result": ["C: 3.25% | Si: 2.10% | Mn: 0.75%", "BHN: 215 (Range: 200-230)", "Moisture: 3.8% | Strength: 145 kPa"],
                "Status": ["Approved", "Approved", "Approved"]
            }), use_container_width=True)
            st.info("💡 **Traceability Rule:** Test Request → Sample Collection & Preparation → Spectrometer Chemical Analysis / Sand Testing / Hardness Test → Result Verification → Out-of-Specification Alert / Retest → Lab Test Report linked with Heat Number.")
        with tab2:
            st.subheader("Lab Test Request, Spectrometer & Sand Testing Entry Form")
            with st.form("lab_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input("Sample ID & Heat Number / Batch Record No.")
                    st.selectbox("Testing Department Source", ["Production Furnace Melting", "Core / Moulding Sand Shop", "Quality Incoming Material", "Development Trial Casting"])
                    st.selectbox("Test Category", ["Chemical Composition (Spectrometer)", "Carbon / Carbon Equivalent Test", "Sand Testing (Moisture, AFS, Permeability, Strength)", "Hardness Test (BHN / Rockwell)", "Tensile / Mechanical Test", "Microstructure Test"])
                    st.text_input("Material Grade & Instrument Used")
                    st.number_input("Carbon % vs Silicon % (if applicable)", 0.0, format="%.2f")
                    st.number_input("Manganese % vs Sulphur/Phosphorus %", 0.0, format="%.3f")
                with col2:
                    st.number_input("Hardness BHN or Green Compression Strength (kPa)", 0.0)
                    st.number_input("Sand Moisture % or Permeability No.", 0.0)
                    st.selectbox("Result Status", ["Within Specification (Approved)", "Out-of-Specification (Alerted)", "Retest Required", "Correction Applied"])
                    st.text_input("Test Turnaround Time (TAT in Minutes)")
                    st.text_input("Calibration / Reference Standard Ref")
                    st.text_input("Lab Technician Name & Sign-off")
                st.text_area("Lab Test Remarks, Retest Reason & Technical Observations")
                st.form_submit_button("Save Lab Test Report & Link Heat No.")
        with tab3:
            st.subheader("🧪 Laboratory Department Month-Wise Report & KPIs")
            selected_month = st.selectbox("Select Month for Lab Report", months_list, index=9)
            
            col_l1, col_l2, col_l3, col_l4 = st.columns(4)
            with col_l1:
                st.metric("Testing Accuracy", "99.5%", "0.3% ↑")
            with col_l2:
                st.metric("Avg Turnaround Time", "1.8 Hrs", "Fast")
            with col_l3:
                st.metric("Calibration Compliance", "100%", "Up to Date")
            with col_l4:
                st.metric("Retest Rate", "1.2%", "Very Low")

            st.write(f"Comprehensive laboratory testing performance, spectrometer accuracy, sand test metrics, and calibration summary for **{selected_month} 2026**.")
            st.dataframe(pd.DataFrame({
                "Lab Activity / Report": ["Test Request Receipt & Sample Collection", "Spectrometer Chemical Composition Analysis", "Moulding & Core Sand Property Testing", "Hardness & Mechanical Property Testing", "Result Verification & Spec Comparison", "Out-of-Specification Alert & Retest Log", "Instrument Calibration & Maintenance Audit"],
                f"{selected_month} Status": ["Completed", "Verified", "Tested", "Tested", "Verified", "Tracked", "Audited"]
            }), use_container_width=True)
            st.line_chart(pd.DataFrame({"Lab Testing Accuracy %": [98.5, 99.0, 99.2, 99.5]}))

    # 12. SALES DEPARTMENT (Updated with professional foundry working, customer enquiry, PO, quotation, sales order & tracking)
    elif "Sales" in current_dept:
        with tab1:
            st.subheader("🤝 Sales Pipeline, Customer Orders & Enquiry Register")
            st.dataframe(pd.DataFrame({
                "Enquiry / SO ID": ["SO-2026-301", "SO-2026-302", "ENQ-2026-103"],
                "Customer Name": ["Tata Motors", "Kirloskar Brothers", "Bharat Forge"],
                "Part Name / Grade": ["Housing Cover (FG-260)", "Impeller (FG-300)", "Bracket (SG-400)"],
                "Order Qty": ["2,500 Pcs", "1,200 Pcs", "800 Pcs"],
                "Order Value (₹)": ["₹ 35,00,000", "₹ 18,50,000", "₹ 12,00,000"],
                "Delivery Schedule": ["15-Oct-2026", "22-Oct-2026", "30-Oct-2026"],
                "Status": ["Confirmed / In Production", "Confirmed / Dispatch Planned", "Quotation Sent"]
            }), use_container_width=True)
            st.info("💡 **Traceability Rule:** Customer Enquiry → Technical Feasibility (Dev/Prod) → Costing & Quotation → Quotation Approval → Customer PO & Sales Order → Order Planning → Dispatch Coordination → Invoice & Payment Follow-up.")
        with tab2:
            st.subheader("Customer Enquiry, Quotation & Sales Order Entry Form")
            with st.form("sales_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input("Customer Enquiry No. & Customer Name")
                    st.text_input("Part Name, Number & Material Grade")
                    st.number_input("Requirement Quantity vs Target Price (₹)", 0.0)
                    st.text_input("Feasibility & Costing Sheet Reference")
                    st.text_input("Quotation No. & Approved Selling Rate (₹)")
                    st.text_input("Customer Purchase Order (PO) No. & Date")
                with col2:
                    st.text_input("Sales Order (SO) Reference No.")
                    st.date_input("Committed Delivery Schedule Date")
                    st.number_input("Total Order Value (₹)", 0.0)
                    st.selectbox("Payment Terms & Credit Period", ["30 Days Credit", "45 Days Credit", "Advance / LC", "Against Delivery (COD)"])
                    st.text_input("Dispatch Plan & Accounts Billing Ref")
                    st.selectbox("Sales & Order Status", ["Enquiry Received", "Quotation Sent", "PO Confirmed & SO Issued", "In Production / Dispatch", "Completed & Invoiced"])
                st.text_area("Customer Special Instructions, Delivery Terms & Remarks")
                st.form_submit_button("Save Sales Order & Update Pipeline")
        with tab3:
            st.subheader("🤝 Sales Department Month-Wise Report & KPIs")
            selected_month = st.selectbox("Select Month for Sales Report", months_list, index=9)
            
            col_s1, col_s2, col_s3, col_s4 = st.columns(4)
            with col_s1:
                st.metric("Monthly Sales Value", "₹ 4.15 Cr", "12% vs last month")
            with col_s2:
                st.metric("New Order Booking", "₹ 4.50 Cr", "Target Met")
            with col_s3:
                st.metric("Enquiry Conversion %", "28.5%", "High")
            with col_s4:
                st.metric("On-Time Delivery %", "98.2%", "Excellent")

            st.write(f"Comprehensive sales performance, order booking value, customer conversion, and accounts receivable summary for **{selected_month} 2026**.")
            st.dataframe(pd.DataFrame({
                "Sales Activity / Report": ["Customer Enquiry & Drawing Review", "Technical Feasibility & Costing Evaluation", "Quotation Approval & Release", "Customer PO & Sales Order Verification", "Order Planning & Production Coordination", "Dispatch & Tax Invoice Coordination", "Customer Payment Follow-up & Outstanding Tracking"],
                f"{selected_month} Status": ["Reviewed", "Evaluated", "Approved", "Verified", "Coordinated", "Invoiced", "Tracked"]
            }), use_container_width=True)
            st.bar_chart(pd.DataFrame({"Monthly Sales Value (Crores ₹)": [3.6, 3.8, 4.0, 4.15]}))

    # 13. PLANT HEAD PORTAL (Updated with professional foundry working, daily review, OEE, yields, safety & departmental KPIs)
    elif "Plant Head" in current_dept:
        with tab1:
            st.subheader("👔 Plant Head Operational Control & Daily Review Register")
            st.dataframe(pd.DataFrame({
                "Metric Category": ["Production & Output", "Quality & Rejection", "Machine Availability", "Safety & Compliance", "Dispatch Commitment"],
                "Daily Target": ["40 MT / Day", "Rejection < 2%", "Availability > 95%", "100% Safe Shift", "35 MT / Day"],
                "Today's Actual": ["39.5 MT", "1.8%", "95.5%", "Zero Incidents", "36.0 MT"],
                "Status": ["On Track", "Controlled", "Optimal", "Compliant", "Achieved"]
            }), use_container_width=True)
            st.info("💡 **Plant Governance:** Daily Review Meeting → Production Planning Review → Quality & Rejection Analysis → Maintenance & Safety Audit → Material Shortage Escalation → Departmental Bottleneck Resolution → Shift Monitoring.")
        with tab2:
            st.subheader("Plant Head Operational Review & Escalation Entry Form")
            with st.form("plant_head_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.date_input("Plant Review Date")
                    st.number_input("Total Actual Production (MT) vs Target (MT)", 0.0)
                    st.number_input("Overall Plant OEE (%)", 0.0, 100.0, 78.5)
                    st.number_input("Internal Rejection Rate (%)", 0.0, 100.0, 1.8)
                    st.number_input("Metal Yield %", 0.0, 100.0, 72.5)
                    st.text_input("Total Machine Breakdown Hours & Root Cause")
                with col2:
                    st.number_input("Preventive Maintenance Compliance (%)", 0.0, 100.0, 98.0)
                    st.text_input("Material Shortage / Purchase Escalations")
                    st.text_input("Safety Incidents / Near Miss Count (Target: Zero)")
                    st.number_input("Total Dispatched Tonnage (MT)", 0.0)
                    st.selectbox("Plant Operational Status", ["Normal & Smooth Operations", "Minor Bottleneck Resolved", "Critical Escalation to Management", "Shift Handover Completed"])
                    st.text_input("Plant Head Sign-off & Reviewer Name")
                st.text_area("Plant Head Daily Observations, Corrective Actions & Strategic Instructions")
                st.form_submit_button("Save Plant Head Review & Operational Log")
        with tab3:
            st.subheader("👔 Plant Head Month-Wise Executive Report & Plant KPIs")
            selected_month = st.selectbox("Select Month for Plant Report", months_list, index=9)
            
            col_ph1, col_ph2, col_ph3, col_ph4 = st.columns(4)
            with col_ph1:
                st.metric("Plant OEE", "78.5%", "1.8% ↑")
            with col_ph2:
                st.metric("Rejection Rate", "1.8%", "-0.5% improvement")
            with col_ph3:
                st.metric("Machine Availability", "95.5%", "Optimal")
            with col_ph4:
                st.metric("Safety Compliance", "100%", "Zero Incident")

            st.write(f"Comprehensive plant-level performance review, departmental coordination summary, and operational efficiency for **{selected_month} 2026**.")
            st.dataframe(pd.DataFrame({
                "Plant Department / Report": ["Production Department Output & Yield", "Quality Department Rejection & FPY", "Maintenance Department Availability & PM", "Store & Purchase Material Availability", "Dispatch Department OTD & Tonnage", "Safety, Environment & Statutory Compliance", "Plant Head Daily Review & Action Tracking"],
                f"{selected_month} Status": ["Achieved", "Controlled", "Compliant", "Available", "Dispatched", "100% Safe", "Tracked"]
            }), use_container_width=True)
            st.line_chart(pd.DataFrame({"Plant OEE %": [75.0, 76.5, 77.8, 78.5]}))

    # 14. COMPANY HEAD / MANAGEMENT (Updated with professional foundry working, P&L, cash flow, order book, COPQ & management review)
    elif "Company Head" in current_dept:
        with tab1:
            st.subheader("👑 Management Executive Dashboard & Business Performance Register")
            st.dataframe(pd.DataFrame({
                "Business Parameter": ["Monthly Revenue", "Operating Profit Margin", "Order Book Value", "Customer Receivables", "Plant OEE & Yield", "Safety & Compliance"],
                "Current Month Value": ["₹ 4.15 Crores", "14.2%", "₹ 14.50 Crores", "₹ 2.45 Crores", "78.5% OEE | 72.5% Yield", "100% Compliant"],
                "Target / Budget": ["₹ 4.00 Crores", "14.0%", "₹ 12.00 Crores", "< ₹ 2.50 Crores", "> 78% OEE | > 72% Yield", "Zero Incident"],
                "Performance Status": ["Exceeded", "Achieved", "Strong", "Controlled", "Optimal", "Compliant"]
            }), use_container_width=True)
            st.info("💡 **Strategic Governance:** Business Planning → Financial Performance Review (P&L & Cash Flow) → Customer & Market Development → Plant Performance Review → Investment & CapEx Decisions → Risk & Compliance → Monthly Management Review (MMR).")
        with tab2:
            st.subheader("Management Review, Strategic Decision & CapEx Entry Form")
            with st.form("company_head_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.date_input("Management Review Date")
                    st.number_input("Monthly Revenue (Crores ₹) vs Budget (₹)", 0.0, format="%.2f")
                    st.number_input("Operating Profit / Margin (%)", 0.0, 100.0, 14.2)
                    st.number_input("Confirmed Order Book Value (Crores ₹)", 0.0, format="%.2f")
                    st.number_input("Customer Outstanding / Receivables (Crores ₹)", 0.0, format="%.2f")
                    st.text_input("Cash Flow & Working Capital Status Ref")
                with col2:
                    st.number_input("COPQ (Cost of Poor Quality) & Rejection Impact (₹)", 0.0)
                    st.text_input("Capital Expenditure (CapEx) / Machinery Investment Ref")
                    st.text_input("New Customer / Market Development Status")
                    st.selectbox("Strategic Business Health Status", ["High Growth & Profitable", "Stable & On Budget", "Requires Cost Optimization", "Expansion Phase Active"])
                    st.text_input("Managing Director / Company Head Sign-off")
                st.text_area("Management Strategic Decisions, Board Directives & Action Owners")
                st.form_submit_button("Save Management Review & Strategic Record")
        with tab3:
            st.subheader("👑 Management Month-Wise Financial & Growth Report")
            selected_month = st.selectbox("Select Month for Management Report", months_list, index=9)
            
            col_ch1, col_ch2, col_ch3, col_ch4 = st.columns(4)
            with col_ch1:
                st.metric("Monthly Revenue", "₹ 4.15 Cr", "12% YoY")
            with col_ch2:
                st.metric("Operating Profit", "14.2%", "0.8% ↑")
            with col_ch3:
                st.metric("Order Book", "₹ 14.5 Cr", "Robust")
            with col_ch4:
                st.metric("Overall OEE", "78.5%", "2.1% ↑")

            st.write(f"Executive business performance, financial profitability, order book strength, and long-term growth summary for **{selected_month} 2026**.")
            st.dataframe(pd.DataFrame({
                "Strategic Domain / Report": ["Annual Sales & Revenue Growth Review", "Profit & Loss (P&L) & Operating Margin", "Cash Flow & Working Capital Management", "Customer Outstanding & Receivable Risk", "Plant Performance & OEE Review", "Quality, COPQ & Rejection Cost Analysis", "Capital Expenditure & Strategic Investments"],
                f"{selected_month} Status": ["Achieved", "Profitable", "Healthy", "Controlled", "Optimized", "Minimized", "Approved"]
            }), use_container_width=True)
            st.bar_chart(pd.DataFrame({"Monthly Revenue (Crores ₹)": [3.6, 3.8, 4.0, 4.15]}))