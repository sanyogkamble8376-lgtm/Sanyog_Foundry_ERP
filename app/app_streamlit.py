import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Sanyog Foundry Operations Dashboard",
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
    </style>
""", unsafe_allow_html=True)

# Top Header Section
st.markdown("""
    <div class="main-header">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h2>🏭 SANYOG FOUNDRY OPERATIONS DASHBOARD</h2>
                <p style="color: #94a3b8; margin: 0;">Quality Castings | On-Time Delivery | Sustainable Growth</p>
            </div>
            <div style="display: flex; gap: 15px;">
                <div style="background: #334155; padding: 8px 15px; border-radius: 8px; font-size: 0.9rem;">
                    📅 <strong>Date:</strong> 08 Oct 2026
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
st.markdown("### 🔄 End-to-End Foundry Process Flow")
flow_cols = st.columns(9)
flows = ["Sales", "Development", "Purchase", "Store", "Production", "Core", "Fettling", "Dispatch", "Customer"]
for i, col in enumerate(flow_cols):
    with col:
        st.markdown(f'<div class="flow-bar">{flows[i]}</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Initialize Session State for Navigation if not present
if 'selected_dept' not in st.session_state:
    st.session_state.selected_dept = "Operations Master Dashboard"

# Sidebar Navigation Options
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
    "🤝 Sales Department"
]

# Ensure current state exists in options, default to 0 if not found
current_selection = st.session_state.selected_dept
if current_selection not in view_options:
    current_selection = "Operations Master Dashboard"
    
currentIndex = view_options.index(current_selection)

# Sidebar Navigation
st.sidebar.title("🎛️ Navigation")
selected_view = st.sidebar.radio("Select View", view_options, index=currentIndex)
st.session_state.selected_dept = selected_view

if st.session_state.selected_dept == "Operations Master Dashboard":
    
    departments = [
        {"name": "📦 Store Department", "work": "• RM, consumables, spares & FG receipt\n• Inventory control & stock records\n• Material issue & traceability", "kpi": "Inventory Accuracy: 98%\nStock Variance: < 2%"},
        {"name": "🔧 Maintenance Department", "work": "• Preventive & breakdown maintenance\n• Furnace, machines, compressors\n• Equipment reliability & downtime", "kpi": "Machine Availability: 95%\nMTTR: < 4 hrs"},
        {"name": "🚚 Dispatch Department", "work": "• Final quantity verification\n• Packing & identification\n• GRN, challan, invoice documentation", "kpi": "On-Time Delivery: 98%\nDispatch Accuracy: 99%"},
        {"name": "📊 Accounts Department", "work": "• Financial transactions & billing\n• Payroll, costing, taxation\n• Financial records & reporting", "kpi": "Cost Variance: < 3%\nFinancial Accuracy: 99%"},
        {"name": "🛒 Purchase Department", "work": "• Raw material & alloy sourcing\n• Supplier selection & negotiation\n• Quotation comparison & quality", "kpi": "Cost Saving: 5%\nSupplier OTD: 95%"},
        {"name": "🛡️ Core Department", "work": "• Core sand preparation & mixing\n• Core making, curing & baking\n• Dimensional inspection & storage", "kpi": "Core Rejection: < 3%\nCore Productivity: 10% ↑"},
        {"name": "⚙️ Fettling Department", "work": "• Sand removal & riser cutting\n• Shot blasting & grinding\n• Dressing & finishing operations", "kpi": "Finishing Rejection: < 2%\nProductivity: 10% ↑"},
        {"name": "🔬 Quality Department", "work": "• Material to final inspection\n• Process control & defect analysis\n• CAPA & customer quality control", "kpi": "PPM < 500: < 9%\nCustomer Complaints: < 1%"},
        {"name": "🏭 Production Department", "work": "• Production planning & scheduling\n• Manpower & machine utilization\n• Process control & safe production", "kpi": "Achievement: 95%\nOEE: 78.5%"},
        {"name": "💡 Development Department", "work": "• New casting/product development\n• Process & pattern development\n• Trial casting & customer support", "kpi": "Lead Time: -20%\nTrial Success: 90%"},
        {"name": "🧪 Laboratory Department", "work": "• Chemical analysis & spectrometer\n• Sand & hardness testing\n• Microstructure testing & reports", "kpi": "Testing Accuracy: 99%\nTurnaround Time: < 24 hrs"},
        {"name": "🤝 Sales Department", "work": "• Enquiry handling & quotation\n• Order follow-up & customer care\n• Sales planning & business growth", "kpi": "Order Growth: 10%\nEnquiry Conversion: 25%"}
    ]

    # Grid Display with Clickable Buttons
    for i in range(0, len(departments), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(departments):
                dept = departments[i + j]
                with cols[j]:
                    with st.container(border=True):
                        st.markdown(f"### {dept['name']}")
                        st.markdown(f"**Operations:**\n{dept['work']}")
                        st.info(f"**Key KPI:**\n{dept['kpi']}")
                        
                        if st.button(f"Manage {dept['name'].split(' ', 1)[1]}", key=f"btn_{i+j}"):
                            st.session_state.selected_dept = dept['name']
                            st.rerun()

    # Bottom Summary Bar
    st.markdown("---")
    b_cols = st.columns(4)
    with b_cols[0]:
        st.metric(label="Total Production (MT)", value="1,250 MT", delta="8% vs last month")
    with b_cols[1]:
        st.metric(label="Rejection Rate", value="2.1%", delta="-1.2% vs last month")
    with b_cols[2]:
        st.metric(label="On-Time Delivery", value="98%", delta="3% vs last month")
    with b_cols[3]:
        st.metric(label="Customer Satisfaction", value="96%", delta="2% vs last month")

else:
    # Specific Department Management View
    current_dept = st.session_state.selected_dept
    st.title(f"🛠️ {current_dept} Management Portal")
    st.write(f"Welcome to the dedicated management module for **{current_dept}**. Here you can handle transactions, records, and reports.")
    
    if st.button("⬅️ Back to Operations Master Dashboard"):
        st.session_state.selected_dept = "Operations Master Dashboard"
        st.rerun()
        
    # Department specific placeholder tabs/forms
    tab1, tab2, tab3 = st.tabs(["Active Records", "Add New Entry", "Reports"])
    with tab1:
        st.subheader("Recent Entries")
        st.dataframe(pd.DataFrame({
            "ID": [101, 102, 103],
            "Date": ["2026-10-06", "2026-10-07", "2026-10-08"],
            "Status": ["Completed", "In Progress", "Pending Approval"]
        }), use_container_width=True)
    with tab2:
        st.subheader("New Record Entry Form")
        with st.form(key=f"form_{current_dept}"):
            st.text_input("Record Name / Item")
            st.number_input("Quantity / Value", 0.0)
            st.text_area("Remarks / Notes")
            st.form_submit_button("Save Record")
    with tab3:
        st.subheader("Department Reports & Analytics")
        st.line_chart([10, 20, 15, 30, 45, 40]).