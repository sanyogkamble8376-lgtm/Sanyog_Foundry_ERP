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
    .metric-container {
        background-color: #1e293b;
        border: 1px solid #334155;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        color: white;
    }
    .dept-card {
        background-color: #1e293b;
        border-radius: 10px;
        padding: 18px;
        border-top: 5px solid #3b82f6;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        margin-bottom: 20px;
        color: #f8fafc;
        min-height: 280px;
    }
    .card-title {
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 10px;
        color: #38bdf8;
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

# Sidebar Navigation for detailed modules
st.sidebar.title("🎛️ Navigation")
view_mode = st.sidebar.radio("Select View", ["Operations Master Dashboard", "Department Management", "Reports & Analytics"])

if view_mode == "Operations Master Dashboard":
    
    # Department Cards Grid (4 columns x 3 rows)
    departments = [
        {"name": "📦 Store Department", "color": "#f97316", "work": "• RM, consumables, spares & FG receipt\n• Inventory control & stock records\n• Material issue & traceability", "kpi": "Inventory Accuracy: 98%\nStock Variance: < 2%"},
        {"name": "🔧 Maintenance Department", "color": "#0ea5e9", "work": "• Preventive & breakdown maintenance\n• Furnace, machines, compressors\n• Equipment reliability & downtime", "kpi": "Machine Availability: 95%\nMTTR: < 4 hrs"},
        {"name": "🚚 Dispatch Department", "color": "#22c55e", "work": "• Final quantity verification\n• Packing & identification\n• GRN, challan, invoice documentation", "kpi": "On-Time Delivery: 98%\nDispatch Accuracy: 99%"},
        {"name": "📊 Accounts Department", "color": "#a855f7", "work": "• Financial transactions & billing\n• Payroll, costing, taxation\n• Financial records & reporting", "kpi": "Cost Variance: < 3%\nFinancial Accuracy: 99%"},
        {"name": "🛒 Purchase Department", "color": "#6366f1", "work": "• Raw material & alloy sourcing\n• Supplier selection & negotiation\n• Quotation comparison & quality", "kpi": "Cost Saving: 5%\nSupplier OTD: 95%"},
        {"name": "🛡️ Core Department", "color": "#14b8a6", "work": "• Core sand preparation & mixing\n• Core making, curing & baking\n• Dimensional inspection & storage", "kpi": "Core Rejection: < 3%\nCore Productivity: 10% ↑"},
        {"name": "⚙️ Fettling Department", "color": "#eab308", "work": "• Sand removal & riser cutting\n• Shot blasting & grinding\n• Dressing & finishing operations", "kpi": "Finishing Rejection: < 2%\nProductivity: 10% ↑"},
        {"name": "🔬 Quality Department", "color": "#8b5cf6", "work": "• Material to final inspection\n• Process control & defect analysis\n• CAPA & customer quality control", "kpi": "PPM < 500: < 9%\nCustomer Complaints: < 1%"},
        {"name": "🏭 Production Department", "color": "#3b82f6", "work": "• Production planning & scheduling\n• Manpower & machine utilization\n• Process control & safe production", "kpi": "Achievement: 95%\nOEE: 78.5%"},
        {"name": "💡 Development Department", "color": "#06b6d4", "work": "• New casting/product development\n• Process & pattern development\n• Trial casting & customer support", "kpi": "Lead Time: -20%\nTrial Success: 90%"},
        {"name": "🧪 Laboratory Department", "color": "#1e40af", "work": "• Chemical analysis & spectrometer\n• Sand & hardness testing\n• Microstructure testing & reports", "kpi": "Testing Accuracy: 99%\nTurnaround Time: < 24 hrs"},
        {"name": "🤝 Sales Department", "color": "#be185d", "work": "• Enquiry handling & quotation\n• Order follow-up & customer care\n• Sales planning & business growth", "kpi": "Order Growth: 10%\nEnquiry Conversion: 25%"}
    ]

    # Display in 3 columns grid
    for i in range(0, len(departments), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(departments):
                dept = departments[i + j]
                with cols[j]:
                    st.markdown(f"""
                        <div class="dept-card" style="border-top-color: {dept['color']};">
                            <div class="card-title">{dept['name']}</div>
                            <hr style="margin: 5px 0 10px 0; border-color: #334155;">
                            <p style="font-size: 0.85rem; color: #cbd5e1; margin-bottom: 8px;"><strong>Key Operations:</strong><br>{dept['work'].replace(chr(10), '<br>')}</p>
                            <div style="background: rgba(15, 23, 42, 0.6); padding: 8px; border-radius: 6px; font-size: 0.85rem; border-left: 3px solid {dept['color']};">
                                <strong>Key KPI:</strong><br>{dept['kpi'].replace(chr(10), '<br>')}
                            </div>
                        </div>
                    """, unsafe_allow_html=True)

    # Bottom Summary Bar
    st.markdown("---")
    b_cols = st.columns(4)
    with b_cols[0]:
        st.metric(label="Total Production (MT)", value="1,250 MT", delta="8% vs last month")
    with b_cols[1]:
        st.metric(label="Rejection Rate", value="2.1%", delta="-1.2% vs last month", delta_value="inverse")
    with b_cols[2]:
        st.metric(label="On-Time Delivery", value="98%", delta="3% vs last month")
    with b_cols[3]:
        st.metric(label="Customer Satisfaction", value="96%", delta="2% vs last month")

else:
    st.info("Switch to 'Operations Master Dashboard' from sidebar to view the comprehensive foundry enterprise view.")