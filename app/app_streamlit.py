import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Sanyog Foundry Operations Master Dashboard",
    page_icon="🏭",
    layout="wide"
)

# Custom CSS for Clean Professional White, Faint Blue & Dark Blue Theme (Fixed Input & Table Visibility)
st.markdown("""
    <style>
    /* Global Background - Pure White */
    .stApp {
        background-color: #ffffff;
        color: #1e293b;
    }
    
    /* Top Enterprise Header - Dark Blue */
    .main-header {
        background: linear-gradient(135deg, #1e40af 0%, #1e3a8a 100%);
        padding: 16px 20px;
        border-radius: 10px;
        color: white;
        margin-bottom: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    /* Process Flow Bar - Faint Blue */
    .flow-bar {
        background-color: #eff6ff;
        border: 1px solid #bfdbfe;
        padding: 6px;
        border-radius: 6px;
        text-align: center;
        font-weight: 600;
        color: #1e40af;
        font-size: 0.8rem;
    }
    
    /* Department Cards - White with Dark Blue Top Border */
    .dept-card {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 14px;
        border: 1px solid #e2e8f0;
        border-top: 4px solid #1e40af;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
        margin-bottom: 12px;
        color: #1e293b;
        min-height: 250px;
    }
    .card-title {
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 6px;
        color: #1e40af;
    }
    
    /* Dark Blue Action Buttons */
    .stButton>button {
        background-color: #1e40af !important;
        color: white !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
        border: none !important;
        padding: 6px 12px !important;
    }
    .stButton>button:hover {
        background-color: #1e3a8a !important;
        color: white !important;
    }
    
    /* Red Accent Alert Styling */
    .alert-box {
        background-color: #fef2f2;
        border: 1px solid #fecaca;
        color: #dc2626;
        padding: 10px;
        border-radius: 6px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 10px;
    }
    
    /* Input Fields, Selectboxes, and Forms Background Fix (Clean Light Look) */
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #f8fafc !important;
        color: #1e293b !important;
        border: 1px solid #cbd5e1 !important;
    }
    
    /* Tabs Clear Visibility */
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 1rem !important;
        font-weight: 700 !important;
        color: #1e40af !important;
    }
    
    /* Sidebar Styling - Faint Blue Tint */
    section[data-testid="stSidebar"] {
        background-color: #f8fafc;
        border-right: 1px solid #e2e8f0;
    }
    
    /* Compact Spacing */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 1rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# Top Header Section
st.markdown("""
    <div class="main-header">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h3 style="margin: 0; color: white;">🏭 SANYOG FOUNDRY OPERATIONS MASTER DASHBOARD</h3>
                <p style="color: #bfdbfe; margin: 0; font-size: 0.85rem;">Quality Castings | On-Time Delivery | Professional Enterprise ERP</p>
            </div>
            <div style="display: flex; gap: 10px;">
                <div style="background: rgba(255,255,255,0.15); padding: 6px 12px; border-radius: 6px; font-size: 0.8rem;">
                    📅 <strong>Date:</strong> 09 Oct 2026
                </div>
                <div style="background: #1e40af; padding: 6px 12px; border-radius: 6px; font-size: 0.8rem; color: white; border: 1px solid #bfdbfe;">
                    🟢 <strong>Plant Status:</strong> Running
                </div>
                <div style="background: rgba(255,255,255,0.15); padding: 6px 12px; border-radius: 6px; font-size: 0.8rem;">
                    🎯 <strong>OEE:</strong> 78.5%
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# End-to-End Process Flow Bar
st.markdown("##### 🔄 Foundry End-to-End Process Flow")
flow_cols = st.columns(9)
flows = ["Sales", "Development", "Purchase", "Store", "Production", "Core", "Fettling", "Quality/Lab", "Dispatch"]
for i, col in enumerate(flow_cols):
    with col:
        st.markdown(f'<div class="flow-bar">{flows[i]}</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Initialize Session State for Navigation
if 'selected_dept' not in st.session_state:
    st.session_state.selected_dept = "Operations Master Dashboard"

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

# Sidebar Navigation
st.sidebar.markdown("### 🎛️ Navigation & Control")
selected_view = st.sidebar.selectbox("Select View / Department", view_options, index=currentIndex)

if selected_view != st.session_state.selected_dept:
    st.session_state.selected_dept = selected_view
    st.rerun()

if st.session_state.selected_dept == "Operations Master Dashboard":
    
    departments = [
        {"name": "📦 Store Department", "access": "Create/Edit Stock Entries, View PO & GRN", "auth": "Physical verification nantar receipt/issue नोंद करणे.", "kpi": "Inventory Accuracy: 98%"},
        {"name": "🔧 Maintenance Department", "access": "Create/Edit PM & Breakdown Logs", "auth": "Authorized maintenance & safe restart confirmation.", "kpi": "Machine Availability: 95%"},
        {"name": "🚚 Dispatch Department", "access": "Create DC, Packing list, View Sales Order", "auth": "Quality clearance & authorized documents nantar dispatch.", "kpi": "On-Time Delivery: 98%"},
        {"name": "📊 Accounts Department", "access": "View PO, GRN, SO, Invoices, Ledgers", "auth": "Payment/billing approval workflow nustar entries.", "kpi": "Financial Accuracy: 99%"},
        {"name": "🛒 Purchase Department", "access": "Create PR/PO, View Store Stock", "auth": "PO approval delegation nustar issue karne.", "kpi": "Supplier OTD: 95%"},
        {"name": "🛡️ Core Department", "access": "Create Core Output, View Production Plan", "auth": "Approved recipe nusar core closure.", "kpi": "Core Rejection: < 3%"},
        {"name": "⚙️ Fettling Department", "access": "Create Output/Rework, View Job Card", "auth": "Operation completion; final quality release nahi.", "kpi": "Finishing Rejection: < 2%"},
        {"name": "🔬 Quality Department", "access": "Create Inspection/NCR, Hold/Release", "auth": "Quality hold/release niyamanusar final clearance.", "kpi": "First Pass Yield: 96.5%"},
        {"name": "🏭 Production Department", "access": "Create Plan/Output, View Lab/Quality", "auth": "Production completion; quality release nahi.", "kpi": "Target Achievement: 96%"},
        {"name": "💡 Development Department", "access": "Create Feasibility/Trials, View Reports", "auth": "Engineering change sathi designated approval.", "kpi": "First Trial Success: 88%"},
        {"name": "🧪 Laboratory Department", "access": "Create Test Results, View Heat/Specs", "auth": "Test report jari karne; commercial approval nahi.", "kpi": "Testing Accuracy: 99.5%"},
        {"name": "🤝 Sales Department", "access": "Create Quotations/SOs, View Dispatch/Accounts", "auth": "Delegated limit madhe quotation / order coordination.", "kpi": "Order Booking: ₹ 4.5 Cr"},
        {"name": "👔 Plant Head Portal", "access": "View All Plant Reports & Department Records", "auth": "Delegated operational approvals & escalation.", "kpi": "Plant OEE: 78.5%"},
        {"name": "👑 Company Head / Management", "access": "View All Consolidated Financials & KPIs", "auth": "Company policy, budget & major investments.", "kpi": "Monthly Revenue: ₹ 4.15 Cr"}
    ]

    for i in range(0, len(departments), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(departments):
                dept = departments[i + j]
                with cols[j]:
                    st.markdown(f"""
                        <div class="dept-card">
                            <div class="card-title">{dept['name']}</div>
                            <hr style="margin: 4px 0 6px 0; border-color: #e2e8f0;">
                            <p style="font-size: 0.78rem; color: #475569; margin-bottom: 4px;"><strong>Access Rights:</strong><br>{dept['access']}</p>
                            <p style="font-size: 0.78rem; color: #475569; margin-bottom: 6px;"><strong>Authority:</strong><br>{dept['auth']}</p>
                            <div style="background: #eff6ff; padding: 6px; border-radius: 6px; font-size: 0.78rem; border-left: 3px solid #1e40af; color: #1e40af;">
                                <strong>Key KPI:</strong> {dept['kpi']}
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    clean_name = dept['name']
                    if st.button(f"Manage {clean_name.split(' ', 1)[1]}", key=f"btn_{i+j}", use_container_width=True):
                        st.session_state.selected_dept = dept['name']
                        st.rerun()

    st.markdown("---")
    b_cols = st.columns(4)
    with b_cols[0]: st.metric(label="Total Production (MT)", value="1,250 MT", delta="8% vs last month")
    with b_cols[1]: st.metric(label="Rejection Rate", value="1.8%", delta="-0.5% vs last month")
    with b_cols[2]: st.metric(label="On-Time Delivery", value="98%", delta="3% vs last month")
    with b_cols[3]: st.metric(label="Monthly Revenue", value="₹ 4.15 Cr", delta="12% YoY")

elif st.session_state.selected_dept == "🔐 Access & Authority Matrix":
    st.title("🔐 Department-wise Access Rights & Approval Authority Matrix")
    st.write("Complete system permissions, access levels, and financial/operational authority limits.")
    
    if st.button("⬅️ Back to Operations Master Dashboard"):
        st.session_state.selected_dept = "Operations Master Dashboard"
        st.rerun()
        
    matrix_df = pd.DataFrame({
        "Department": ["Sales", "Development", "Purchase", "Store", "Production", "Core", "Fettling", "Quality", "Lab", "Maintenance", "Dispatch", "Accounts", "Plant Head", "Company Head"],
        "Access Level": ["Create/Edit SO & Quotes", "Create Feasibility & Trials", "Create PR/PO", "Create GRN/Issue", "Create Plan & Output", "Create Core Output", "Create Fettling/Rework", "Create Inspection/NCR", "Create Test Reports", "Create PM/Breakdown", "Create DC & Packing", "Create/Edit Vouchers", "View All Plant Reports", "View Consolidated Data"],
        "Approval Authority / Limit": ["Delegated Limit Quotation", "Designated Engineering Change", "PO Approval Delegation", "Physical Verification Receipt", "Production Completion", "Core Job Closure", "Operation Completion", "Quality Hold / Release", "Test Report Release", "Work Order Closure", "Dispatch Document Release", "Payment/Billing Workflow", "Operational Escalations", "Budget, Capex & Major Contracts"]
    })
    st.dataframe(matrix_df, use_container_width=True)

else:
    current_dept = st.session_state.selected_dept
    st.title(f"🛠️ {current_dept} Management Portal")
    st.markdown(f'<div class="alert-box">⚠️ Active Module: {current_dept} | Strict Compliance & Quality Control Mode Active.</div>', unsafe_allow_html=True)
    
    if st.button("⬅️ Back to Operations Master Dashboard"):
        st.session_state.selected_dept = "Operations Master Dashboard"
        st.rerun()
        
    tab1, tab2, tab3 = st.tabs(["Active Records & Tracking", "Add New Entry / Form", "Month-Wise Reports & KPIs"])
    months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    with tab1:
        st.subheader(f"📋 {current_dept} - Active Records & Register")
        st.dataframe(pd.DataFrame({
            "Transaction ID": ["TXN-2026-101", "TXN-2026-102", "TXN-2026-103"],
            "Description": [f"Standard Operation Log for {current_dept}", "Material & Process Verification", "Quality / Dispatch Clearance"],
            "Status": ["Active / Running", "Completed", "Verified"]
        }), use_container_width=True)

    with tab2:
        st.subheader(f"✍️ {current_dept} - New Entry & Transaction Form")
        with st.form(f"{current_dept}_form"):
            col1, col2 = st.columns(2)
            with col1:
                st.text_input("Reference No. / Batch No.")
                st.text_input("Item / Component Name")
            with col2:
                st.number_input("Quantity / Value", 0.0)
                st.selectbox("Status", ["Draft", "Pending Approval", "Approved & Completed"])
            st.text_area("Remarks & Operational Notes")
            st.form_submit_button(f"Save {current_dept} Record")

    with tab3:
        st.subheader(f"📊 {current_dept} - Month-Wise Report & KPIs")
        sel_m = st.selectbox("Select Month for Report", months_list, index=9)
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.metric("Efficiency / Accuracy", "98.5%", "1.2% ↑")
        with col_m2:
            st.metric("Status Summary", "Optimal", "On Track")
        st.dataframe(pd.DataFrame({
            "Metric Name": ["Total Transactions", "Approved Records", "Pending Actions", "Audit Status"],
            f"{sel_m} 2026 Data": ["120 Entries", "115 Completed", "5 In Progress", "Verified"]
        }), use_container_width=True)