import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Sanyog Foundry Operations Master Dashboard",
    page_icon="🏭",
    layout="wide"
)

# Custom CSS for Professional White & Faint Blue Enterprise Dashboard Styling
st.markdown("""
    <style>
    /* Global App Background & Font */
    .stApp {
        background-color: #f8fafc;
        color: #1e293b;
    }
    
    /* Top Enterprise Header */
    .main-header {
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
        padding: 22px;
        border-radius: 12px;
        color: white;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    /* End-to-End Process Flow Bar */
    .flow-bar {
        background-color: #e0f2fe;
        border: 1px solid #bae6fd;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        font-weight: 600;
        color: #0369a1;
        font-size: 0.85rem;
    }
    
    /* Professional Department Cards (White & Faint Blue Theme) */
    .dept-card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 18px;
        border: 1px solid #e2e8f0;
        border-top: 5px solid #0284c7;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
        margin-bottom: 20px;
        color: #1e293b;
        min-height: 290px;
    }
    .card-title {
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 8px;
        color: #0369a1;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #f1f5f9;
        border-right: 1px solid #e2e8f0;
    }
    </style>
""", unsafe_allow_html=True)

# Top Header Section
st.markdown("""
    <div class="main-header">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h2>🏭 SANYOG FOUNDRY OPERATIONS MASTER DASHBOARD</h2>
                <p style="color: #e0f2fe; margin: 0;">Quality Castings | On-Time Delivery | Professional Enterprise ERP</p>
            </div>
            <div style="display: flex; gap: 15px;">
                <div style="background: rgba(255,255,255,0.15); padding: 8px 15px; border-radius: 8px; font-size: 0.9rem;">
                    📅 <strong>Date:</strong> 09 Oct 2026
                </div>
                <div style="background: #059669; padding: 8px 15px; border-radius: 8px; font-size: 0.9rem; color: white;">
                    🟢 <strong>Plant Status:</strong> Running
                </div>
                <div style="background: rgba(255,255,255,0.15); padding: 8px 15px; border-radius: 8px; font-size: 0.9rem;">
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

# Sidebar Navigation Options (All 14 Modules + Access Matrix)
view_options = [
    "Operations Master Dashboard", 
    "🔐 Access & Authority Matrix",
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

# Sidebar Navigation (Instant Response Selectbox)
st.sidebar.title("🎛️ Navigation & Control")
selected_view = st.sidebar.selectbox("Select View / Department", view_options, index=currentIndex)

if selected_view != st.session_state.selected_dept:
    st.session_state.selected_dept = selected_view
    st.rerun()

if st.session_state.selected_dept == "Operations Master Dashboard":
    
    departments = [
        {"name": "📦 Store Department", "color": "#0284c7", "access": "Create/Edit Stock Entries, View PO & GRN", "auth": "Physical verification nantar receipt/issue नोंद करणे.", "kpi": "Inventory Accuracy: 98%"},
        {"name": "🔧 Maintenance Department", "color": "#0284c7", "access": "Create/Edit PM & Breakdown Logs", "auth": "Authorized maintenance & safe restart confirmation.", "kpi": "Machine Availability: 95%"},
        {"name": "🚚 Dispatch Department", "color": "#0284c7", "access": "Create DC, Packing list, View Sales Order", "auth": "Quality clearance & authorized documents nantar dispatch.", "kpi": "On-Time Delivery: 98%"},
        {"name": "📊 Accounts Department", "color": "#0284c7", "access": "View PO, GRN, SO, Invoices, Ledgers", "auth": "Payment/billing approval workflow nustar entries.", "kpi": "Financial Accuracy: 99%"},
        {"name": "🛒 Purchase Department", "color": "#0284c7", "access": "Create PR/PO, View Store Stock", "auth": "PO approval delegation nustar issue karne.", "kpi": "Supplier OTD: 95%"},
        {"name": "🛡️ Core Department", "color": "#0284c7", "access": "Create Core Output, View Production Plan", "auth": "Approved recipe nusar core closure.", "kpi": "Core Rejection: < 3%"},
        {"name": "⚙️ Fettling Department", "color": "#0284c7", "access": "Create Output/Rework, View Job Card", "auth": "Operation completion; final quality release nahi.", "kpi": "Finishing Rejection: < 2%"},
        {"name": "🔬 Quality Department", "color": "#0284c7", "access": "Create Inspection/NCR, Hold/Release", "auth": "Quality hold/release niyamanusar final clearance.", "kpi": "First Pass Yield: 96.5%"},
        {"name": "🏭 Production Department", "color": "#0284c7", "access": "Create Plan/Output, View Lab/Quality", "auth": "Production completion; quality release nahi.", "kpi": "Target Achievement: 96%"},
        {"name": "💡 Development Department", "color": "#0284c7", "access": "Create Feasibility/Trials, View Reports", "auth": "Engineering change sathi designated approval.", "kpi": "First Trial Success: 88%"},
        {"name": "🧪 Laboratory Department", "color": "#0284c7", "access": "Create Test Results, View Heat/Specs", "auth": "Test report jari karne; commercial approval nahi.", "kpi": "Testing Accuracy: 99.5%"},
        {"name": "🤝 Sales Department", "color": "#0284c7", "access": "Create Quotations/SOs, View Dispatch/Accounts", "auth": "Delegated limit madhe quotation / order coordination.", "kpi": "Order Booking: ₹ 4.5 Cr"},
        {"name": "👔 Plant Head Portal", "color": "#059669", "access": "View All Plant Reports & Department Records", "auth": "Delegated operational approvals & escalation.", "kpi": "Plant OEE: 78.5%"},
        {"name": "👑 Company Head / Management", "color": "#0369a1", "access": "View All Consolidated Financials & KPIs", "auth": "Company policy, budget & major investments.", "kpi": "Monthly Revenue: ₹ 4.15 Cr"}
    ]

    # Grid Display (3 columns per row)
    for i in range(0, len(departments), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(departments):
                dept = departments[i + j]
                with cols[j]:
                    st.markdown(f"""
                        <div class="dept-card">
                            <div class="card-title">{dept['name']}</div>
                            <hr style="margin: 4px 0 8px 0; border-color: #e2e8f0;">
                            <p style="font-size: 0.82rem; color: #475569; margin-bottom: 6px;"><strong>Access Rights:</strong><br>{dept['access']}</p>
                            <p style="font-size: 0.82rem; color: #475569; margin-bottom: 8px;"><strong>Authority:</strong><br>{dept['auth']}</p>
                            <div style="background: #f0f9ff; padding: 8px; border-radius: 6px; font-size: 0.82rem; border-left: 3px solid #0284c7; color: #0369a1;">
                                <strong>Key KPI:</strong> {dept['kpi']}
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

elif st.session_state.selected_dept == "🔐 Access & Authority Matrix":
    st.title("🔐 Department-wise Access Rights & Approval Authority Matrix")
    st.write("Complete system permissions, access levels (View, Create, Edit, Approve, Release), and financial/operational authority limits across all 14 departments.")
    
    if st.button("⬅️ Back to Operations Master Dashboard"):
        st.session_state.selected_dept = "Operations Master Dashboard"
        st.rerun()
        
    st.subheader("📋 Master Access & Authority Table")
    matrix_df = pd.DataFrame({
        "Department": ["Sales", "Development", "Purchase", "Store", "Production", "Core", "Fettling", "Quality", "Lab", "Maintenance", "Dispatch", "Accounts", "Plant Head", "Company Head"],
        "Access Level": ["Create/Edit SO & Quotes", "Create Feasibility & Trials", "Create PR/PO", "Create GRN/Issue", "Create Plan & Output", "Create Core Output", "Create Fettling/Rework", "Create Inspection/NCR", "Create Test Reports", "Create PM/Breakdown", "Create DC & Packing", "Create/Edit Vouchers", "View All Plant Reports", "View Consolidated Data"],
        "Other Dept Access": ["View Production, Dispatch, Accounts", "View Quality, Lab, Production", "View Store Stock, GRN, Accounts", "View PO & Approved Requests", "View Store, Lab, Quality", "View Production Plan & Recipes", "View Job Card & Quality Instructions", "View Production, Lab, Dispatch", "View Heat, Batch, Specs", "View Machine Schedule, Spare Stock", "View Sales Order, Released Stock", "View Approved PO, GRN, SO, DC", "View All Operational Records", "View All Financial & Op Data"],
        "Approval Authority / Limit": ["Delegated Limit Quotation", "Designated Engineering Change", "PO Approval Delegation", "Physical Verification Receipt", "Production Completion", "Core Job Closure", "Operation Completion", "Quality Hold / Release", "Test Report Release", "Work Order Closure", "Dispatch Document Release", "Payment/Billing Workflow", "Operational Escalations & Actions", "Budget, Capex & Major Contracts"]
    })
    st.dataframe(matrix_df, use_container_width=True)

else:
    current_dept = st.session_state.selected_dept
    st.title(f"🛠️ {current_dept} Management Portal")
    st.write(f"Complete operational workspace, access controls, and specialized records for **{current_dept}**.")
    
    if st.button("⬅️ Back to Operations Master Dashboard"):
        st.session_state.selected_dept = "Operations Master Dashboard"
        st.rerun()
        
    tab1, tab2, tab3 = st.tabs(["Active Records & Tracking", "Add New Entry / Form", "Month-Wise Reports & KPIs"])
    
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
            st.info("💡 **Access & Authority:** Store has **Create/Edit** access for inward/GRN and issue entries after physical verification.")
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
            st.dataframe(pd.DataFrame({
                "Metric": ["Total Inward Transactions", "Total Material Issues", "Stock Reconciliation Accuracy", "Stock Variances Noted"],
                f"{selected_month} Value": ["145 Entries", "110 Slips", "98.5%", "1.5%"]
            }), use_container_width=True)

    # 2. MAINTENANCE DEPARTMENT
    elif "Maintenance" in current_dept:
        with tab1:
            st.subheader("🔧 Machine Asset Register & Breakdown History")
            st.dataframe(pd.DataFrame({
                "Asset ID": ["AST-F01", "AST-CS02", "AST-SB03", "AST-CMP04"],
                "Machine Name": ["Induction Furnace 1", "Core Shooter", "Shot Blasting Machine", "Air Compressor"],
                "Department": ["Furnace Dept", "Core Shop", "Fettling", "Utilities"],
                "Status": ["Running", "Under Maintenance", "Running", "Running"]
            }), use_container_width=True)
            st.info("💡 **Access & Authority:** Maintenance has **Create/Edit** access for PM schedules and breakdown work orders with safe restart verification.")
        with tab2:
            st.subheader("Maintenance Work Order & Breakdown Entry Form")
            with st.form("maint_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input("Asset ID / Machine ID")
                    st.text_input("Breakdown No. / Complaint No.")
                    st.text_input("WO No. - Work Order No.")
                    st.selectbox("Maintenance Type", ["Preventive Maintenance", "Breakdown Maintenance", "Condition Monitoring"])
                with col2:
                    st.text_input("Assigned Technician Name")
                    st.number_input("Downtime Hours", 0.0)
                    st.text_input("Root Cause (RCA)")
                    st.text_input("Action Taken & Restart Time")
                st.text_area("Fault Description & Remarks")
                st.form_submit_button("Save Maintenance & WO Record")
        with tab3:
            st.subheader("🔧 Maintenance Department Month-Wise Report & KPIs")
            selected_month = st.selectbox("Select Month for Maintenance Report", months_list, index=9)
            col_m1, col_m2, col_m3, col_m4 = st.columns(4)
            with col_m1: st.metric("Machine Availability", "95.5%")
            with col_m2: st.metric("PM Compliance", "98.0%")
            with col_m3: st.metric("MTTR", "3.2 Hrs")
            with col_m4: st.metric("MTBF", "164 Hrs")

    # 3. DISPATCH DEPARTMENT
    elif "Dispatch" in current_dept:
        with tab1:
            st.subheader("📦 Dispatch Register & Order Tracking")
            st.dataframe(pd.DataFrame({
                "Dispatch Date": ["08-Oct-2026", "08-Oct-2026"],
                "Customer Name": ["Tata Motors", "Kirloskar Brothers"],
                "Part No.": ["TM-HSG-01", "KB-IMP-04"],
                "Dispatch Qty (MT)": [12.5, 8.0],
                "DC No.": ["DC-2026-101", "DC-2026-102"],
                "POD Status": ["Received", "Pending"]
            }), use_container_width=True)
            st.info("💡 **Access & Authority:** Dispatch can create DCs and packing lists only after Quality clearance and authorized Sales Order verification.")
        with tab2:
            st.subheader("Create New Dispatch Entry & Document Generation")
            with st.form("dispatch_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input("Customer Name & PO No.")
                    st.text_input("Sales Order No. & Dispatch Plan No.")
                    st.text_input("Part No. & Grade / Batch No.")
                    st.number_input("Dispatch Qty (MT)", 0.0)
                with col2:
                    st.text_input("Inspection Report No. (Quality Clearance)")
                    st.text_input("DC No. - Delivery Challan")
                    st.text_input("Vehicle No. & Driver Name")
                    st.text_input("E-way Bill No.")
                st.text_area("Delivery Instructions & Remarks")
                st.form_submit_button("Generate Dispatch & Save Record")
        with tab3:
            st.subheader("🚚 Dispatch Department Month-Wise Report & KPIs")
            selected_month = st.selectbox("Select Month for Dispatch Report", months_list, index=9)
            col_d1, col_d2 = st.columns(2)
            with col_d1: st.metric("Total Dispatch Tonnage", "1,250 MT")
            with col_d2: st.metric("On-Time Delivery (OTD)", "98.2%")

    # 4. ACCOUNTS DEPARTMENT
    elif "Accounts" in current_dept:
        with tab1:
            st.subheader("📊 Ledger & Voucher Register (Purchase, Sales & Receipts)")
            st.dataframe(pd.DataFrame({
                "Voucher No.": ["PV-2026-101", "RV-2026-102"],
                "Voucher Type": ["Payment", "Receipt"],
                "Party Name": ["JSW Steel (Supplier)", "Tata Motors (Customer)"],
                "Amount (₹)": [450000, 1250000],
                "Status": ["Paid (UTR-9981)", "Received"]
            }), use_container_width=True)
            st.info("💡 **Access & Authority:** Accounts has **Approve/Release** authority for payments and billing based on 3-way matching (PO + GRN + Invoice).")
        with tab2:
            st.subheader("Bill Booking, Payment & Receipt Voucher Entry Form")
            with st.form("accounts_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.selectbox("Voucher Type", ["Purchase Bill Booking", "Sales Invoice", "Payment Voucher", "Receipt Voucher"])
                    st.text_input("Voucher No. & Party Name")
                    st.text_input("PO No. / GRN No. / Invoice No.")
                    st.number_input("Taxable Amount (₹)", 0.0)
                with col2:
                    st.number_input("GST / TDS Amount (₹)", 0.0)
                    st.number_input("Total Amount (₹)", 0.0)
                    st.selectbox("Payment Mode", ["NEFT / RTGS", "Cheque", "UPI"])
                    st.text_input("Bank UTR No.")
                st.text_area("Narration & Reconciliation Status")
                st.form_submit_button("Save Accounts Voucher & Post Entry")
        with tab3:
            st.subheader("📊 Accounts Department Month-Wise Report & Financial KPIs")
            selected_month = st.selectbox("Select Month for Accounts Report", months_list, index=9)
            col_a1, col_a2 = st.columns(2)
            with col_a1: st.metric("Customer Receivables", "₹ 2.45 Cr")
            with col_a2: st.metric("Supplier Payables", "₹ 1.85 Cr")

    # 5. PURCHASE DEPARTMENT
    elif "Purchase" in current_dept:
        with tab1:
            st.subheader("🛒 Purchase Requisitions, Comparative Statements & PO Register")
            st.dataframe(pd.DataFrame({
                "PR No.": ["PR-2026-011", "PR-2026-012"],
                "Item Description": ["Pig Iron (Grade-1)", "Resin Binder"],
                "PO No.": ["PO-501", "PO-502"],
                "Supplier Name": ["JSW Steel", "National Chem"],
                "Status": ["PO Issued", "Approved"]
            }), use_container_width=True)
            st.info("💡 **Access & Authority:** Purchase issues POs within approved budget and delegation limits. PR creator and PO approver must be separate.")
        with tab2:
            st.subheader("Create Purchase Requisition, RFQ & Purchase Order (PO)")
            with st.form("purchase_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input("PR No. & Department")
                    st.text_input("RFQ No. & Supplier Name")
                    st.text_input("PO No. - Purchase Order No.")
                with col2:
                    st.text_input("Item Code & Description")
                    st.number_input("Order Quantity", 0.0)
                    st.number_input("Negotiated Rate (₹)", 0.0)
                st.text_area("Terms, Conditions & Remarks")
                st.form_submit_button("Save Purchase Record & Release PO")
        with tab3:
            st.subheader("🛒 Purchase Department Month-Wise Report & KPIs")
            selected_month = st.selectbox("Select Month for Purchase Report", months_list, index=9)
            col_p1, col_p2 = st.columns(2)
            with col_p1: st.metric("Total Purchase Value", "₹ 2.10 Cr")
            with col_p2: st.metric("Supplier OTD %", "95.2%")

    # 6. CORE DEPARTMENT
    elif "Core" in current_dept:
        with tab1:
            st.subheader("🛡️ Core Production Register & Batch Tracking")
            st.dataframe(pd.DataFrame({
                "Prod Plan No.": ["PLN-2026-081", "PLN-2026-082"],
                "Part Name": ["Housing Cover", "Hydraulic Body"],
                "Core Box ID": ["CB-101", "CB-104"],
                "Actual Qty": [485, 350],
                "Status": ["Completed", "Issued to Moulding"]
            }), use_container_width=True)
            st.info("💡 **Access & Authority:** Core department produces cores according to approved recipes and core box IDs.")
        with tab2:
            st.subheader("Core Production & Inspection Entry Form")
            with st.form("core_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input("Production Plan No. & Part No.")
                    st.text_input("Core Box ID & Machine ID")
                    st.number_input("Resin % & Hardener %", 0.0, format="%.2f")
                with col2:
                    st.number_input("Target Qty vs Actual Produced Qty", 0)
                    st.number_input("Rejected Qty", 0)
                    st.selectbox("Core Status", ["Ready in Stock", "Issued to Moulding", "Rework Required"])
                st.text_area("Curing Parameters & Remarks")
                st.form_submit_button("Save Core Production Record")
        with tab3:
            st.subheader("🛡️ Core Department Month-Wise Report & KPIs")
            selected_month = st.selectbox("Select Month for Core Report", months_list, index=9)
            col_c1, col_c2 = st.columns(2)
            with col_c1: st.metric("Core Productivity", "125 Pcs/Hr")
            with col_c2: st.metric("Core Rejection Rate", "2.1%")

    # 7. FETTLING DEPARTMENT
    elif "Fettling" in current_dept:
        with tab1:
            st.subheader("⚙️ Fettling & Casting Finishing Register")
            st.dataframe(pd.DataFrame({
                "Receipt No.": ["RPT-2026-301", "RPT-2026-302"],
                "Part Name": ["Housing Cover", "Hydraulic Body"],
                "Received Qty": [450, 320],
                "Grinding Status": ["Completed", "In Progress"],
                "Status": ["Handed over to FG", "Processing"]
            }), use_container_width=True)
            st.info("💡 **Access & Authority:** Fettling completes finishing operations but does not have final quality release authority.")
        with tab2:
            st.subheader("Casting Finishing, Grinding & Shot Blasting Entry Form")
            with st.form("fettling_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input("Casting Receipt No. & Batch No.")
                    st.text_input("Part Name & Grade")
                    st.number_input("Received Qty", 0)
                with col2:
                    st.selectbox("Gate/Riser Removal Status", ["Completed Clean", "Rework Required"])
                    st.number_input("Accepted Finished Qty vs Rejected Qty", 0)
                    st.text_input("Handover Slip No. (To FG Store)")
                st.text_area("Surface Defects & Remarks")
                st.form_submit_button("Save Fettling Record")
        with tab3:
            st.subheader("⚙️ Fettling Department Month-Wise Report & KPIs")
            selected_month = st.selectbox("Select Month for Fettling Report", months_list, index=9)
            col_f1, col_f2 = st.columns(2)
            with col_f1: st.metric("Finishing Productivity", "94.5%")
            with col_f2: st.metric("Fettling Rejection %", "1.5%")

    # 8. QUALITY DEPARTMENT
    elif "Quality" in current_dept:
        with tab1:
            st.subheader("🔬 Quality Assurance, Inspection & Defect Register")
            st.dataframe(pd.DataFrame({
                "Inspection ID": ["INS-2026-901", "INS-2026-902"],
                "Heat No.": ["H-2026-410", "H-2026-411"],
                "Part Name": ["Housing Cover", "Hydraulic Body"],
                "Stage": ["Final Casting", "Incoming Material"],
                "Defect Noted": ["Blowhole", "None (OK)"],
                "Status": ["Released / Approved", "Passed"]
            }), use_container_width=True)
            st.info("💡 **Access & Authority:** Quality has sole authority for final casting release, NCR generation, and hold/rejection disposition.")
        with tab2:
            st.subheader("Quality Inspection, Testing & NCR Entry Form")
            with st.form("quality_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input("Inspection Report No. & Heat No.")
                    st.text_input("Part Name & Grade")
                    st.selectbox("Inspection Stage", ["Incoming", "In-Process", "Final Inspection"])
                with col2:
                    st.selectbox("Defect Category", ["Blowhole", "Shrinkage", "Sand Inclusion", "None (OK)"])
                    st.selectbox("Quality Clearance Status", ["Released / Approved", "Rework Given", "Rejected / Scrap"])
                    st.text_input("NCR No. & CAPA Reference")
                st.text_area("Quality Inspector Remarks & Sign-off")
                st.form_submit_button("Save Quality Inspection Record")
        with tab3:
            st.subheader("🔬 Quality Department Month-Wise Report & KPIs")
            selected_month = st.selectbox("Select Month for Quality Report", months_list, index=9)
            col_q1, col_q2 = st.columns(2)
            with col_q1: st.metric("First Pass Yield", "96.5%")
            with col_q2: st.metric("Customer PPM", "380 PPM")

    # 9. PRODUCTION DEPARTMENT
    elif "Production" in current_dept:
        tab_p1, tab_p2, tab_p3 = st.tabs(["Active Records & Tracking", "Add New Entry / Form", "Month-Wise Reports & Daily Report"])
        with tab_p1:
            st.subheader("🏭 Production Planning, Shift Register & Melting Logs")
            st.dataframe(pd.DataFrame({
                "Prod Plan No.": ["PLN-2026-501", "PLN-2026-502"],
                "Shift": ["Morning Shift", "Evening Shift"],
                "Casting Grade": ["FG-260", "FG-300"],
                "Target (MT)": ["30 MT", "25 MT"],
                "Actual Produced": ["29.2 MT", "25.5 MT"],
                "Status": ["Achieved", "Achieved"]
            }), use_container_width=True)
            st.info("💡 **Access & Authority:** Production executes the approved plan and logs outputs; final quality release is strictly reserved for Quality.")
        with tab2:
            st.subheader("Shift Production Planning & Melting Entry Form")
            with st.form("production_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input("Production Plan No. & Job Card No.")
                    st.selectbox("Shift", ["Morning Shift", "Evening Shift", "Night Shift"])
                    st.text_input("Heat Number / Batch Record No.")
                with col2:
                    st.number_input("Target Qty vs Actual Produced Qty", 0)
                    st.slider("Material Yield %", 0.0, 100.0, 72.0)
                    st.slider("OEE %", 0.0, 100.0, 78.5)
                st.text_area("Shift Notes & Furnace Parameters")
                st.form_submit_button("Save Production & Heat Log Record")
        with tab3:
            st.subheader("📊 Production Month-Wise Report & Daily Report")
            selected_month = st.selectbox("Select Month for Production Report", months_list, index=9)
            col_pr1, col_pr2 = st.columns(2)
            with col_pr1: st.metric("Monthly Production", "1,250 MT")
            with col_pr2: st.metric("Plant OEE", "78.5%")

    # 10. DEVELOPMENT DEPARTMENT
    elif "Development" in current_dept:
        with tab1:
            st.subheader("💡 New Product Development & Trial Casting Register")
            st.dataframe(pd.DataFrame({
                "Dev ID": ["DEV-2026-01", "DEV-2026-02"],
                "Customer": ["Tata Motors", "Kirloskar"],
                "Part Name": ["Housing Cover", "Impeller"],
                "Stage": ["Trial Casting", "Sample Approval"],
                "Status": ["In Progress", "Submitted"]
            }), use_container_width=True)
            st.info("💡 **Access & Authority:** Development handles feasibility, tooling, and trial casting with designated engineering change approvals.")
        with tab2:
            st.subheader("New Product Development & Trial Entry Form")
            with st.form("development_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input("Development ID & Customer Name")
                    st.text_input("Part Name & Grade")
                    st.text_input("Pattern / Tooling ID")
                with col2:
                    st.selectbox("Development Stage", ["Feasibility", "Tooling", "Trial Casting", "Sample Approval", "Handover"])
                    st.selectbox("Trial Status", ["Success", "Defect - RCA Required", "Customer Approved"])
                    st.number_input("Development Lead Time (Days)", 0)
                st.text_area("Technical Feasibility Notes")
                st.form_submit_button("Save Development Record")
        with tab3:
            st.subheader("💡 Development Department Month-Wise Report & KPIs")
            selected_month = st.selectbox("Select Month for Development Report", months_list, index=9)
            col_dev1, col_dev2 = st.columns(2)
            with col_dev1: st.metric("First Trial Success %", "88.0%")
            with col_dev2: st.metric("On-Time Development %", "95.0%")

    # 11. LABORATORY DEPARTMENT
    elif "Laboratory" in current_dept:
        with tab1:
            st.subheader("🧪 Laboratory Test Register & Spectrometer Log")
            st.dataframe(pd.DataFrame({
                "Sample ID": ["SMP-2026-801", "SMP-2026-802"],
                "Heat No.": ["H-2026-410", "H-2026-411"],
                "Test Type": ["Chemical Analysis (Spectrometer)", "Hardness Test (BHN)"],
                "Key Result": ["C: 3.25% | Si: 2.10%", "BHN: 215"],
                "Status": ["Approved", "Approved"]
            }), use_container_width=True)
            st.info("💡 **Access & Authority:** Lab records test results and issues reports; it does not grant commercial or casting acceptance approval.")
        with tab2:
            st.subheader("Lab Test Request & Spectrometer Entry Form")
            with st.form("lab_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input("Sample ID & Heat Number")
                    st.selectbox("Test Category", ["Chemical Analysis", "Sand Testing", "Hardness Test (BHN)"])
                    st.number_input("Carbon % vs Silicon %", 0.0, format="%.2f")
                with col2:
                    st.number_input("Hardness BHN or Sand Moisture %", 0.0)
                    st.selectbox("Result Status", ["Within Specification", "Out-of-Specification", "Retest Required"])
                    st.text_input("Technician Name")
                st.text_area("Lab Test Remarks & Observations")
                st.form_submit_button("Save Lab Test Report")
        with tab3:
            st.subheader("🧪 Laboratory Department Month-Wise Report & KPIs")
            selected_month = st.selectbox("Select Month for Lab Report", months_list, index=9)
            col_l1, col_l2 = st.columns(2)
            with col_l1: st.metric("Testing Accuracy", "99.5%")
            with col_l2: st.metric("Avg Turnaround Time", "1.8 Hrs")

    # 12. SALES DEPARTMENT
    elif "Sales" in current_dept:
        with tab1:
            st.subheader("🤝 Sales Pipeline, Customer Orders & Enquiry Register")
            st.dataframe(pd.DataFrame({
                "SO ID": ["SO-2026-301", "SO-2026-302"],
                "Customer Name": ["Tata Motors", "Kirloskar Brothers"],
                "Part Name": ["Housing Cover", "Impeller"],
                "Order Value (₹)": ["₹ 35,00,000", "₹ 18,50,000"],
                "Status": ["Confirmed / In Production", "Confirmed / Dispatch Planned"]
            }), use_container_width=True)
            st.info("💡 **Access & Authority:** Sales manages enquiries, quotations within delegated limits, and order coordination.")
        with tab2:
            st.subheader("Customer Enquiry, Quotation & Sales Order Entry Form")
            with st.form("sales_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input("Customer Name & Enquiry No.")
                    st.text_input("Part Name & Grade")
                    st.number_input("Requirement Quantity", 0)
                with col2:
                    st.number_input("Approved Selling Rate / Total Value (₹)", 0.0)
                    st.date_input("Committed Delivery Date")
                    st.selectbox("Sales Status", ["Enquiry Received", "Quotation Sent", "PO Confirmed & SO Issued"])
                st.text_area("Customer Special Instructions & Terms")
                st.form_submit_button("Save Sales Order & Pipeline")
        with tab3:
            st.subheader("🤝 Sales Department Month-Wise Report & KPIs")
            selected_month = st.selectbox("Select Month for Sales Report", months_list, index=9)
            col_s1, col_s2 = st.columns(2)
            with col_s1: st.metric("Monthly Sales Value", "₹ 4.15 Cr")
            with col_s2: st.metric("New Order Booking", "₹ 4.50 Cr")

    # 13. PLANT HEAD PORTAL
    elif "Plant Head" in current_dept:
        with tab1:
            st.subheader("👔 Plant Head Operational Control & Daily Review Register")
            st.dataframe(pd.DataFrame({
                "Metric Category": ["Production & Output", "Quality & Rejection", "Machine Availability", "Safety & Compliance"],
                "Daily Target": ["40 MT / Day", "Rejection < 2%", "Availability > 95%", "100% Safe Shift"],
                "Today's Actual": ["39.5 MT", "1.8%", "95.5%", "Zero Incidents"],
                "Status": ["On Track", "Controlled", "Optimal", "Compliant"]
            }), use_container_width=True)
            st.info("💡 **Access & Authority:** Plant Head has full view of all operational departments and holds delegated operational approval and escalation authority.")
        with tab2:
            st.subheader("Plant Head Operational Review & Escalation Entry Form")
            with st.form("plant_head_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.date_input("Plant Review Date")
                    st.number_input("Total Actual Production (MT)", 0.0)
                    st.number_input("Plant OEE (%)", 0.0, 100.0, 78.5)
                with col2:
                    st.number_input("Internal Rejection Rate (%)", 0.0, 100.0, 1.8)
                    st.selectbox("Plant Operational Status", ["Normal Operations", "Minor Bottleneck Resolved", "Critical Escalation"])
                    st.text_input("Plant Head Sign-off")
                st.text_area("Plant Head Daily Observations & Corrective Actions")
                st.form_submit_button("Save Plant Head Review & Log")
        with tab3:
            st.subheader("👔 Plant Head Month-Wise Executive Report & KPIs")
            selected_month = st.selectbox("Select Month for Plant Report", months_list, index=9)
            col_ph1, col_ph2 = st.columns(2)
            with col_ph1: st.metric("Plant OEE", "78.5%")
            with col_ph2: st.metric("Safety Compliance", "100%")

    # 14. COMPANY HEAD / MANAGEMENT
    elif "Company Head" in current_dept:
        with tab1:
            st.subheader("👑 Management Executive Dashboard & Business Performance Register")
            st.dataframe(pd.DataFrame({
                "Business Parameter": ["Monthly Revenue", "Operating Profit Margin", "Order Book Value", "Customer Receivables"],
                "Current Value": ["₹ 4.15 Crores", "14.2%", "₹ 14.50 Crores", "₹ 2.45 Crores"],
                "Target / Budget": ["₹ 4.00 Crores", "14.0%", "₹ 12.00 Crores", "< ₹ 2.50 Crores"],
                "Status": ["Exceeded", "Achieved", "Strong", "Controlled"]
            }), use_container_width=True)
            st.info("💡 **Access & Authority:** Company Head / Managing Director has complete oversight of financials, strategic decisions, budgeting, and major capital investments.")
        with tab2:
            st.subheader("Management Review, Strategic Decision & CapEx Entry Form")
            with st.form("company_head_doc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    st.date_input("Management Review Date")
                    st.number_input("Monthly Revenue (Crores ₹)", 0.0, format="%.2f")
                    st.number_input("Operating Profit Margin (%)", 0.0, 100.0, 14.2)
                with col2:
                    st.number_input("Order Book Value (Crores ₹)", 0.0, format="%.2f")
                    st.selectbox("Business Health", ["High Growth & Profitable", "Stable & On Budget", "Expansion Phase"])
                    st.text_input("Managing Director Sign-off")
                st.text_area("Management Strategic Decisions & Board Directives")
                st.form_submit_button("Save Management Review Record")
        with tab3:
            st.subheader("👑 Management Month-Wise Financial & Growth Report")
            selected_month = st.selectbox("Select Month for Management Report", months_list, index=9)
            col_ch1, col_ch2 = st.columns(2)
            with col_ch1: st.metric("Monthly Revenue", "₹ 4.15 Cr")
            with col_ch2: st.metric("Operating Profit", "14.2%")