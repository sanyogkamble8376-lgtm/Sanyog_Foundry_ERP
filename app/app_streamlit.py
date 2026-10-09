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
        {"name": "🔬 Quality Department", "color": "#8b5cf6", "work": "• Incoming to final casting quality planning, inspection & process control\n• Defect analysis, CAPA & customer complaint reduction", "kpi": "PPM < 500: < 9%\nCustomer Complaints: < 1%"},
        {"name": "🏭 Production Department", "color": "#3b82f6", "work": "• Production planning, manpower & machine utilization\n• Process control, productivity & safe efficient production", "kpi": "Achievement: 95%\nOEE: 78.5%"},
        {"name": "💡 Development Department", "color": "#06b6d4", "work": "• New casting/product, process & pattern/core development\n• Trial casting, process optimization & successful transfer to production", "kpi": "Lead Time: -20%\nTrial Success: 90%"},
        {"name": "🧪 Laboratory Department", "color": "#1e40af", "work": "• Chemical analysis, spectrometer, sand, hardness & microstructure tests\n• Maintaining test reports & material/process traceability", "kpi": "Testing Accuracy: 99%\nTurnaround Time: < 24 hrs"},
        {"name": "🤝 Sales Department", "color": "#be185d", "work": "• Customer requirements, enquiry handling, quotation & order follow-up\n• Customer communication, sales planning & business development", "kpi": "Order Growth: 10%\nEnquiry Conversion: 25%"},
        {"name": "👔 Plant Head Portal", "color": "#10b981", "work": "• Plant-level coordination & monitoring of Production, Quality, Maintenance & Safety\n• Improving productivity, quality, delivery & profitability", "kpi": "Plant OEE: 78.5%\nPlant Safety: 100%"},
        {"name": "👑 Company Head / Management", "color": "#f43f5e", "work": "• Business strategy, financial planning, investment & policy making\n• Leadership, overall performance & long-term growth & profitability", "kpi": "Revenue Growth: 12%\nProfitability: 8%"}
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
        st.metric(label="Rejection Rate", value="2.1%", delta="-1.2% vs last month")
    with b_cols[2]:
        st.metric(label="On-Time Delivery", value="98%", delta="3% vs last month")
    with b_cols[3]:
        st.metric(label="Customer Satisfaction", value="96%", delta="2% vs last month")

else:
    # Specific Department Management Portal
    current_dept = st.session_state.selected_dept
    st.title(f"🛠️ {current_dept} Management Portal")
    st.write(f"Complete operational workspace and specialized records for **{current_dept}**.")
    
    if st.button("⬅️ Back to Operations Master Dashboard"):
        st.session_state.selected_dept = "Operations Master Dashboard"
        st.rerun()
        
    tab1, tab2, tab3 = st.tabs(["Active Records & Tracking", "Add New Entry / Form", "Month-Wise Reports & Analytics"])
    
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
            st.subheader("Equipment Maintenance & Downtime Control")
            st.dataframe(pd.DataFrame({"Equipment": ["Induction Furnace", "Core Shooter", "Compressor"], "Type": ["Breakdown", "Preventive", "Routine"], "Downtime (Hrs)": [2.5, 1.0, 0.5], "Status": ["Resolved", "Completed", "Scheduled"]}), use_container_width=True)
        with tab2:
            st.subheader("Log Maintenance Activity")
            with st.form("maint_form"):
                st.selectbox("Equipment / Machine", ["Furnace", "Moulding Line", "Compressor", "Pump", "Electrical System"])
                st.text_input("Fault / Maintenance Description")
                st.number_input("Downtime Hours", 0.0)
                st.form_submit_button("Submit Maintenance Log")
        with tab3:
            st.subheader("🔧 Maintenance Department Month-Wise Report")
            selected_month = st.selectbox("Select Month for Maintenance Report", months_list, index=9)
            st.write(f"Equipment availability, MTTR, and breakdown hours for **{selected_month} 2026**.")
            st.dataframe(pd.DataFrame({
                "Equipment": ["Furnace 1", "Furnace 2", "Core Shooter", "Moulding Line"],
                "Total Breakdown Hours": [4.5, 2.0, 3.0, 5.5],
                "Availability %": ["95.2%", "97.8%", "96.5%", "94.0%"]
            }), use_container_width=True)
            st.line_chart(pd.DataFrame({"Availability %": [93, 94, 95, 95.5]}))

    # 3. DISPATCH DEPARTMENT
    elif "Dispatch" in current_dept:
        with tab1:
            st.subheader("Final Verification & Customer Dispatches")
            st.dataframe(pd.DataFrame({"Challan No": ["CH-089", "CH-090"], "Customer": ["Tata Motors", "Kirloskar"], "Weight (MT)": [12.5, 8.0], "OTD Status": ["On-Time", "On-Time"]}), use_container_width=True)
        with tab2:
            st.subheader("Create Dispatch Entry")
            with st.form("dispatch_form"):
                st.text_input("Customer Name")
                st.text_input("Challan / Invoice No")
                st.number_input("Dispatched Weight (MT)", 0.0)
                st.form_submit_button("Generate Dispatch")
        with tab3:
            st.subheader("🚚 Dispatch Department Month-Wise Report")
            selected_month = st.selectbox("Select Month for Dispatch Report", months_list, index=9)
            st.write(f"Dispatch tonnage and On-Time Delivery (OTD) summary for **{selected_month} 2026**.")
            st.bar_chart(pd.DataFrame({"Dispatched Tonnage (MT)": [310, 330, 345, 360]}))

    # 4. ACCOUNTS DEPARTMENT
    elif "Accounts" in current_dept:
        with tab1:
            st.subheader("Financial Transactions & Costing")
            st.dataframe(pd.DataFrame({"Voucher ID": ["V-101", "V-102"], "Particulars": ["Alloy Sourcing", "Payroll"], "Type": ["Debit", "Debit"], "Amount (₹)": [450000, 120000]}), use_container_width=True)
        with tab2:
            st.subheader("Add Financial Record")
            with st.form("acc_form"):
                st.text_input("Particulars / Description")
                st.selectbox("Transaction Type", ["Receipt", "Payment", "Billing", "Payroll"])
                st.number_input("Amount (₹)", 0.0)
                st.form_submit_button("Save Transaction")
        with tab3:
            st.subheader("📊 Accounts Department Month-Wise Report")
            selected_month = st.selectbox("Select Month for Accounts Report", months_list, index=9)
            st.write(f"Financial billing, collections, and cost variance report for **{selected_month} 2026**.")
            st.metric("Total Monthly Billing", "₹ 4.15 Crores", "5% vs last month")
            st.line_chart(pd.DataFrame({"Cost Variance %": [2.8, 2.5, 2.2, 2.0]}))

    # 5. PURCHASE DEPARTMENT
    elif "Purchase" in current_dept:
        with tab1:
            st.subheader("Sourcing, Quotations & Supplier OTD")
            st.dataframe(pd.DataFrame({"PO No": ["PO-501", "PO-502"], "Vendor": ["JSW Steel", "National Alloys"], "Material": ["Pig Iron", "Ferro Silicon"], "Status": ["Approved", "Dispatched"]}), use_container_width=True)
        with tab2:
            st.subheader("Create Purchase Order")
            with st.form("purchase_form"):
                st.text_input("Vendor Name")
                st.text_input("Material / Service Description")
                st.number_input("Estimated Cost (₹)", 0.0)
                st.form_submit_button("Issue PO")
        with tab3:
            st.subheader("🛒 Purchase Department Month-Wise Report")
            selected_month = st.selectbox("Select Month for Purchase Report", months_list, index=9)
            st.write(f"Supplier OTD and procurement cost savings for **{selected_month} 2026**.")
            st.line_chart(pd.DataFrame({"Supplier OTD %": [92, 93, 94, 95]}))

    # 6. CORE DEPARTMENT
    elif "Core" in current_dept:
        with tab1:
            st.subheader("Core Sand Preparation & Curing Logs")
            st.dataframe(pd.DataFrame({"Core Box ID": ["CB-12", "CB-14"], "Sand Mix": ["Furan", "CO2"], "Cores Produced": [450, 320], "Rejection %": [2.5, 1.8]}), use_container_width=True)
        with tab2:
            st.subheader("Log Core Production")
            with st.form("core_form"):
                st.text_input("Core Box ID")
                st.selectbox("Sand Type", ["Furan Sand", "CO2 Sand", "Shell Sand"])
                st.number_input("Production Count", 0)
                st.number_input("Rejection Count", 0)
                st.form_submit_button("Save Core Entry")
        with tab3:
            st.subheader("🛡️ Core Department Month-Wise Report")
            selected_month = st.selectbox("Select Month for Core Report", months_list, index=9)
            st.write(f"Core production count and rejection rate analysis for **{selected_month} 2026**.")
            st.line_chart(pd.DataFrame({"Rejection %": [3.5, 3.1, 2.8, 2.4]}))

    # 7. FETTLING DEPARTMENT
    elif "Fettling" in current_dept:
        with tab1:
            st.subheader("Finishing, Grinding & Blasting Status")
            st.dataframe(pd.DataFrame({"Casting Part": ["Housing", "Cover"], "Operation": ["Shot Blasting", "Grinding"], "OK Pcs": [120, 95], "Rejection Pcs": [2, 1]}), use_container_width=True)
        with tab2:
            st.subheader("Log Fettling Output")
            with st.form("fettling_form"):
                st.text_input("Casting Part Name")
                st.selectbox("Process", ["Riser Cutting", "Shot Blasting", "Grinding", "Dressing"])
                st.number_input("OK Pieces", 0)
                st.form_submit_button("Save Fettling Record")
        with tab3:
            st.subheader("⚙️ Fettling Department Month-Wise Report")
            selected_month = st.selectbox("Select Month for Fettling Report", months_list, index=9)
            st.write(f"Finishing productivity and dressing output for **{selected_month} 2026**.")
            st.line_chart(pd.DataFrame({"Output Pcs/Day": [210, 220, 235, 245]}))

    # 8. QUALITY DEPARTMENT
    elif "Quality" in current_dept:
        with tab1:
            st.subheader("Inspection, Defect Analysis & CAPA")
            st.dataframe(pd.DataFrame({"Heat No": ["H-891", "H-892"], "Defect": ["Blowhole", "Shrinkage"], "PPM": [420, 380], "Status": ["CAPA Applied", "Resolved"]}), use_container_width=True)
        with tab2:
            st.subheader("Log Inspection & Defects")
            with st.form("quality_form"):
                st.text_input("Heat / Casting ID")
                st.selectbox("Defect Type", ["Blowhole", "Shrinkage", "Sand Inclusion", "Crack", "None"])
                st.number_input("PPM Level", 0)
                st.text_input("Corrective Action (CAPA)")
                st.form_submit_button("Save Quality Record")
        with tab3:
            st.subheader("🔬 Quality Department Month-Wise Report")
            selected_month = st.selectbox("Select Month for Quality Report", months_list, index=9)
            st.write(f"PPM trend, defect analysis, and customer complaints summary for **{selected_month} 2026**.")
            st.line_chart(pd.DataFrame({"PPM Level": [550, 490, 440, 420]}))

    # 9. PRODUCTION DEPARTMENT
    elif "Production" in current_dept:
        with tab1:
            st.subheader("Production Planning & Machine Utilization")
            st.dataframe(pd.DataFrame({"Shift": ["Morning", "Evening"], "Grade": ["FG-260", "FG-300"], "Target (MT)": [25, 25], "Actual (MT)": [24.5, 26.0]}), use_container_width=True)
        with tab2:
            st.subheader("Log Shift Production")
            with st.form("prod_form"):
                st.selectbox("Shift", ["Morning Shift", "Evening Shift", "Night Shift"])
                st.text_input("Grade / Item Casted")
                st.number_input("Actual Tonnage (MT)", 0.0)
                st.slider("OEE %", 50, 100, 78)
                st.form_submit_button("Save Production Log")
        with tab3:
            st.subheader("🏭 Production Department Month-Wise Report")
            selected_month = st.selectbox("Select Month for Production Report", months_list, index=9)
            st.write(f"Production tonnage achievement and OEE efficiency for **{selected_month} 2026**.")
            st.line_chart(pd.DataFrame({"Monthly OEE %": [75, 76.5, 78, 78.5]}))

    # 10. DEVELOPMENT DEPARTMENT
    elif "Development" in current_dept:
        with tab1:
            st.subheader("New Product Trials & Pattern Development")
            st.dataframe(pd.DataFrame({"Pattern ID": ["PAT-301", "PAT-302"], "Component": ["Motor Body", "Impeller"], "Stage": ["Trial Casting", "Pattern Mod"], "Status": ["Approved", "In Progress"]}), use_container_width=True)
        with tab2:
            st.subheader("Log Trial Development")
            with st.form("dev_form"):
                st.text_input("Component Name")
                st.selectbox("Development Stage", ["Pattern Design", "Trial Casting", "Dimensional Audit", "Client Approval"])
                st.form_submit_button("Save Development Entry")
        with tab3:
            st.subheader("💡 Development Department Month-Wise Report")
            selected_month = st.selectbox("Select Month for Development Report", months_list, index=9)
            st.write(f"New casting trial success rate and lead time analysis for **{selected_month} 2026**.")
            st.line_chart(pd.DataFrame({"Trial Success %": [82, 85, 88, 90]}))

    # 11. LABORATORY DEPARTMENT
    elif "Laboratory" in current_dept:
        with tab1:
            st.subheader("Spectrometer, Sand & Hardness Test Reports")
            st.dataframe(pd.DataFrame({"Sample Code": ["SMP-01", "SMP-02"], "Carbon %": [3.25, 3.30], "Silicon %": [2.10, 2.05], "Hardness BHN": [210, 215]}), use_container_width=True)
        with tab2:
            st.subheader("Add Lab Test Result")
            with st.form("lab_form"):
                st.text_input("Sample Code")
                st.number_input("Carbon %", 0.0, format="%.2f")
                st.number_input("Silicon %", 0.0, format="%.2f")
                st.number_input("Hardness BHN", 0.0)
                st.form_submit_button("Save Lab Report")
        with tab3:
            st.subheader("🧪 Laboratory Department Month-Wise Report")
            selected_month = st.selectbox("Select Month for Lab Report", months_list, index=9)
            st.write(f"Testing accuracy and report turnaround time for **{selected_month} 2026**.")
            st.line_chart(pd.DataFrame({"Testing Accuracy %": [98.5, 99, 99.2, 99.5]}))

    # 12. SALES DEPARTMENT
    elif "Sales" in current_dept:
        with tab1:
            st.subheader("Customer Inquiries, Quotations & Orders")
            st.dataframe(pd.DataFrame({"Client": ["Bharat Forge", "Endurance"], "Item": ["Bracket", "Cylinder Block"], "Value (₹)": [1200000, 3500000], "Status": ["Quotation Sent", "Confirmed"]}), use_container_width=True)
        with tab2:
            st.subheader("New Sales Lead / Inquiry")
            with st.form("sales_form"):
                st.text_input("Client Name")
                st.text_input("Casting Requirement")
                st.number_input("Estimated Order Value (₹)", 0.0)
                st.form_submit_button("Save Lead")
        with tab3:
            st.subheader("🤝 Sales Department Month-Wise Report")
            selected_month = st.selectbox("Select Month for Sales Report", months_list, index=9)
            st.write(f"Order booking, enquiry conversion rate, and business growth for **{selected_month} 2026**.")
            st.bar_chart(pd.DataFrame({"Order Value (Lakhs ₹)": [42, 47, 51, 55]}))

    # 13. PLANT HEAD PORTAL
    elif "Plant Head" in current_dept:
        st.subheader("👔 Plant Head Month-Wise Executive Report")
        selected_month = st.selectbox("Select Month for Plant Report", months_list, index=9)
        st.write(f"Comprehensive plant-level coordination, efficiency, and safety review for **{selected_month} 2026**.")
        st.dataframe(pd.DataFrame({
            "Department": ["Production", "Quality", "Maintenance", "Store", "Dispatch"],
            "Monthly Efficiency %": [95, 98, 96, 94, 98],
            "Safety Incidents": [0, 0, 0, 0, 0]
        }), use_container_width=True)
        st.line_chart(pd.DataFrame({"Plant Efficiency %": [91, 93, 94, 95.5]}))

    # 14. COMPANY HEAD / MANAGEMENT
    elif "Company Head" in current_dept:
        st.subheader("👑 Management Month-Wise Financial & Growth Report")
        selected_month = st.selectbox("Select Month for Management Report", months_list, index=9)
        st.write(f"Executive business performance, profitability, and revenue summary for **{selected_month} 2026**.")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Monthly Revenue", "₹ 4.15 Crores", "12% YoY")
        with col2:
            st.metric("Net Profitability", "14.2%", "1.5% YoY")
        with col3:
            st.metric("Overall OEE", "78.5%", "2.1% ↑")
        st.bar_chart(pd.DataFrame({"Revenue (Crores ₹)": [3.5, 3.8, 4.0, 4.15]}))