import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Sanyog Foundry Operations Master Dashboard",
    page_icon="🏭",
    layout="wide"
)

# Custom CSS for Scroll-Free Clean Professional Layout
st.markdown("""
    <style>
    /* Global Background - Pure White */
    .stApp {
        background-color: #ffffff;
        color: #1e293b;
    }
    
    /* Top Enterprise Header - Dark Blue */
    .main-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%);
        padding: 16px 20px;
        border-radius: 10px;
        color: white;
        margin-bottom: 12px;
        box-shadow: 0 4px 8px rgba(30, 58, 138, 0.1);
    }
    
    /* Department Cards - Clean White with Dark Blue Accent Top */
    .dept-card {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 12px;
        border: 1px solid #e2e8f0;
        border-top: 4px solid #1e40af;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
        margin-bottom: 10px;
        color: #1e293b;
        min-height: 210px;
    }
    .card-title {
        font-size: 0.95rem;
        font-weight: 700;
        margin-bottom: 6px;
        color: #1e3a8a;
    }
    
    /* Dark Blue Action Buttons */
    .stButton>button {
        background-color: #1e40af !important;
        color: white !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
        border: none !important;
        padding: 6px 10px !important;
        width: 100% !important;
        font-size: 0.85rem !important;
    }
    .stButton>button:hover {
        background-color: #1e3a8a !important;
        color: white !important;
    }
    
    /* Sidebar Navigation Links Styling */
    section[data-testid="stSidebar"] {
        background-color: #f8fafc;
        border-right: 1px solid #e2e8f0;
        padding-top: 1rem;
    }
    
    /* Compact Layout Padding */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# Top Header Section
st.markdown("""
    <div class="main-header">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div style="display: flex; align-items: center; gap: 12px;">
                <div style="font-size: 1.8rem;">🏭</div>
                <div>
                    <h3 style="margin: 0; color: white; font-weight: 800;">SANYOG FOUNDRY</h3>
                    <p style="color: #bfdbfe; margin: 0; font-size: 0.8rem; font-weight: 500;">OPERATIONS MASTER DASHBOARD</p>
                </div>
            </div>
            <div style="display: flex; gap: 12px; align-items: center;">
                <div style="background: rgba(255,255,255,0.12); padding: 6px 10px; border-radius: 6px; font-size: 0.8rem;">
                    📅 <strong>09 Oct 2026</strong>
                </div>
                <div style="background: rgba(5, 150, 105, 0.25); padding: 6px 10px; border-radius: 6px; font-size: 0.8rem; color: #6ee7b7; border: 1px solid #059669;">
                    🟢 <strong>Running</strong>
                </div>
                <div style="background: rgba(255,255,255,0.12); padding: 6px 10px; border-radius: 6px; font-size: 0.8rem;">
                    🎯 <strong>OEE:</strong> 78.5%
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Initialize Session State for Navigation
if 'selected_dept' not in st.session_state:
    st.session_state.selected_dept = "Dashboard"

# Sidebar Quick Navigation Menu (Scroll-free clean buttons)
st.sidebar.markdown("### 🎛️ Quick Navigation")
if st.sidebar.button("🏠 Operations Dashboard", use_container_width=True):
    st.session_state.selected_dept = "Dashboard"
    st.rerun()

if st.sidebar.button("🔐 Access & Authority Matrix", use_container_width=True):
    st.session_state.selected_dept = "🔐 Access & Authority Matrix"
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown("**Departments Portal:**")

sidebar_depts = ["Store", "Maintenance", "Dispatch", "Accounts", "Purchase", "Core", "Fettling", "Quality", "Production", "Development", "Lab", "Sales", "Plant Head", "Company Head"]

for s_dept in sidebar_depts:
    if st.sidebar.button(f"👉 {s_dept}", key=f"side_{s_dept}", use_container_width=True):
        st.session_state.selected_dept = s_dept
        st.rerun()

# Main Body Logic
if st.session_state.selected_dept == "Dashboard":
    
    departments = [
        {"name": "📦 Store", "access": "Create/Edit Stock Entries, View PO & GRN", "auth": "Physical verification before receipt/issue", "kpi": "Inventory Accuracy 98%"},
        {"name": "🔧 Maintenance", "access": "Create/Edit PM & Breakdown Logs", "auth": "Authorized maintenance & safe restart confirmation", "kpi": "Machine Availability 95%"},
        {"name": "🚚 Dispatch", "access": "Create DC, Packing List, View Sales Order", "auth": "Dispatch after quality clearance & authorized documents", "kpi": "On-Time Delivery 98%"},
        {"name": "📊 Accounts", "access": "View PO, GRN, SO, Invoices, Ledgers", "auth": "Payment/billing approval workflow", "kpi": "Financial Accuracy 99%"},
        {"name": "🛒 Purchase", "access": "Create PR/PO, View Store Stock", "auth": "PO approval as per delegation", "kpi": "Supplier OTD 95%"},
        {"name": "🛡️ Core", "access": "Create Core Output, View Production Plan", "auth": "Approved recipe before core closure", "kpi": "Core Rejection < 3%"},
        {"name": "⚙️ Fettling", "access": "Create Output/Rework, View Job Card", "auth": "Operation completion & quality handover", "kpi": "Rework Rate < 4%"},
        {"name": "🔬 Quality", "access": "Create Inspection/NCR, Hold/Release", "auth": "Independent quality hold/release", "kpi": "First Pass Yield 97%"},
        {"name": "🏭 Production", "access": "Create Plan/Output, View Lab/Quality", "auth": "Production completion & quality handover", "kpi": "Plan Achievement 95%"},
        {"name": "💡 Development", "access": "Create Feasibility/Trials, View Reports", "auth": "Engineering change sathi designated approval.", "kpi": "First Trial Success: 88%"},
        {"name": "🧪 Lab", "access": "Create Test Results, View Heat/Specs", "auth": "Test report jari karne; commercial approval nahi.", "kpi": "Testing Accuracy: 99.5%"},
        {"name": "🤝 Sales", "access": "Create Quotations/SOs, View Dispatch/Accounts", "auth": "Delegated limit madhe quotation / order coordination.", "kpi": "Order Booking: ₹ 4.5 Cr"},
        {"name": "👔 Plant Head", "access": "View All Plant Reports & Department Records", "auth": "Delegated operational approvals & escalation.", "kpi": "Plant OEE: 78.5%"},
        {"name": "👑 Company Head", "access": "View All Consolidated Financials & KPIs", "auth": "Company policy, budget & major investments.", "kpi": "Monthly Revenue: ₹ 4.15 Cr"}
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
                            <hr style="margin: 2px 0 4px 0; border-color: #e2e8f0;">
                            <p style="font-size: 0.75rem; color: #475569; margin-bottom: 2px;"><strong>Access Rights:</strong><br>{dept['access']}</p>
                            <p style="font-size: 0.75rem; color: #475569; margin-bottom: 4px;"><strong>Authority:</strong><br>{dept['auth']}</p>
                            <div style="background: #f0f6ff; padding: 4px; border-radius: 4px; font-size: 0.75rem; border-left: 3px solid #1e40af; color: #1e40af;">
                                <strong>KPI:</strong> {dept['kpi']}
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    clean_name = dept['name'].split(' ', 1)[1].strip()
                    if st.button(f"Manage {clean_name}", key=f"btn_{i+j}", use_container_width=True):
                        st.session_state.selected_dept = clean_name
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
    
    if st.button("⬅️ Back to Dashboard"):
        st.session_state.selected_dept = "Dashboard"
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
    
    if st.button("⬅️ Back to Dashboard"):
        st.session_state.selected_dept = "Dashboard"
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