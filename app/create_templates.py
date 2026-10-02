import os

# Create templates folder
os.makedirs("templates", exist_ok as True if False else "templates")

dashboard_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sanyog Foundry ERP - Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background: #f8f9fa; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        .sidebar { width: 280px; position: fixed; top: 0; bottom: 0; left: 0; background: #0f172a; color: #fff; overflow-y: auto; padding: 20px; }
        .sidebar a { color: #cbd5e1; text-decoration: none; display: block; padding: 8px 12px; border-radius: 4px; margin-bottom: 4px; font-size: 13px; }
        .sidebar a:hover, .sidebar a.active { background: #1e293b; color: #fff; }
        .sidebar h6 { color: #38bdf8; font-weight: bold; margin-top: 15px; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; }
        .main-content { margin-left: 280px; padding: 30px; }
    </style>
</head>
<body>
    <div class="sidebar">
        <h4 class="text-white mb-4">Sanyog Foundry ERP</h4>
        <a href="{{ url_for('dashboard') }}" class="active">Dashboard</a>
        <a href="{{ url_for('global_po_tracker') }}">Global PO Tracker</a>
        <hr class="border-secondary">
        {% for dept, items in departments.items() %}
            <h6>{{ dept }}</h6>
            {% for item in items %}
                <a href="{{ url_for('module', dept=dept, item=item|lower|replace(' ', '-')) }}">{{ item }}</a>
            {% endfor %}
        {% endfor %}
    </div>
    <div class="main-content">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h2>Welcome, {{ session.name }} ({{ session.role }})</h2>
            <a href="{{ url_for('logout') }}" class="btn btn-outline-danger btn-sm">Logout</a>
        </div>
        
        <div class="row mb-4">
            <div class="col-md-4">
                <div class="card shadow-sm p-3 border-primary">
                    <h5>Total Enterprise Records</h5>
                    <h3>{{ total_records }}</h3>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card shadow-sm p-3 border-success">
                    <h5>Global Master Tracking</h5>
                    <a href="{{ url_for('global_po_tracker') }}" class="btn btn-success btn-sm mt-2">Open Global Tracker &rarr;</a>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card shadow-sm p-3 border-warning">
                    <h5>System Status</h5>
                    <span class="badge bg-success mt-2 p-2">Secure & Active (2026)</span>
                </div>
            </div>
        </div>

        <div class="card shadow-sm p-4">
            <h4>Department Quick Navigation</h4>
            <p class="text-muted">Select any department or module from the left sidebar to manage entries, view reports, or export PDFs/Excel.</p>
        </div>
    </div>
</body>
</html>
"""

global_po_tracker_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Global PO Tracker - Sanyog Foundry ERP</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background: #f8f9fa; }
        .sidebar { width: 280px; position: fixed; top: 0; bottom: 0; left: 0; background: #0f172a; color: #fff; overflow-y: auto; padding: 20px; }
        .sidebar a { color: #cbd5e1; text-decoration: none; display: block; padding: 8px 12px; border-radius: 4px; margin-bottom: 4px; font-size: 13px; }
        .sidebar a:hover { background: #1e293b; color: #fff; }
        .sidebar h6 { color: #38bdf8; font-weight: bold; margin-top: 15px; font-size: 11px; text-transform: uppercase; }
        .main-content { margin-left: 280px; padding: 30px; }
    </style>
</head>
<body>
    <div class="sidebar">
        <h4 class="text-white mb-4">Sanyog Foundry ERP</h4>
        <a href="{{ url_for('dashboard') }}">Dashboard</a>
        <a href="{{ url_for('global_po_tracker') }}" class="active">Global PO Tracker</a>
        <hr class="border-secondary">
        {% for dept, items in departments.items() %}
            <h6>{{ dept }}</h6>
            {% for item in items %}
                <a href="{{ url_for('module', dept=dept, item=item|lower|replace(' ', '-')) }}">{{ item }}</a>
            {% endfor %}
        {% endfor %}
    </div>
    <div class="main-content">
        <h2>Global PO & Transaction Tracker</h2>
        <form method="GET" class="row g-3 my-3">
            <div class="col-md-4">
                <input type="text" name="po_search" class="form-control" placeholder="Search PO Number..." value="{{ po_query }}">
            </div>
            <div class="col-md-2">
                <button type="submit" class="btn btn-primary w-100">Search</button>
            </div>
        </form>
        <div class="card shadow-sm p-3">
            <table class="table table-striped table-hover">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Department</th>
                        <th>Module</th>
                        <th>PO Number</th>
                        <th>Entity Name</th>
                        <th>Quantity</th>
                        <th>Weight</th>
                        <th>Amount</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {% for row in tracker_entries %}
                    <tr>
                        <td>{{ row.id }}</td>
                        <td>{{ row.department }}</td>
                        <td>{{ row.module_name }}</td>
                        <td>{{ row.po_number }}</td>
                        <td>{{ row.entity_name }}</td>
                        <td>{{ row.quantity }}</td>
                        <td>{{ row.weight }}</td>
                        <td>Rs. {{ row.amount }}</td>
                        <td><span class="badge bg-info">{{ row.status }}</span></td>
                    </tr>
                    {% else %}
                    <tr><td colspan="9" class="text-center text-muted">No records found.</td></tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>
"""

generic_module_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ module_name }} - Sanyog Foundry ERP</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background: #f8f9fa; }
        .sidebar { width: 280px; position: fixed; top: 0; bottom: 0; left: 0; background: #0f172a; color: #fff; overflow-y: auto; padding: 20px; }
        .sidebar a { color: #cbd5e1; text-decoration: none; display: block; padding: 8px 12px; border-radius: 4px; margin-bottom: 4px; font-size: 13px; }
        .sidebar a:hover { background: #1e293b; color: #fff; }
        .sidebar h6 { color: #38bdf8; font-weight: bold; margin-top: 15px; font-size: 11px; text-transform: uppercase; }
        .main-content { margin-left: 280px; padding: 30px; }
    </style>
</head>
<body>
    <div class="sidebar">
        <h4 class="text-white mb-4">Sanyog Foundry ERP</h4>
        <a href="{{ url_for('dashboard') }}">Dashboard</a>
        <a href="{{ url_for('global_po_tracker') }}">Global PO Tracker</a>
        <hr class="border-secondary">
        {% for dept, items in departments.items() %}
            <h6>{{ dept }}</h6>
            {% for item in items %}
                <a href="{{ url_for('module', dept=dept, item=item|lower|replace(' ', '-')) }}">{{ item }}</a>
            {% endfor %}
        {% endfor %}
    </div>
    <div class="main-content">
        <div class="d-flex justify-content-between align-items-center mb-3">
            <div>
                <span class="text-muted">{{ department }}</span>
                <h2>{{ module_name }}</h2>
            </div>
            <div>
                <a href="{{ url_for('download_pdf', dept=department, item=module_name|lower|replace(' ', '-')) }}" class="btn btn-danger btn-sm">Download PDF</a>
                <a href="{{ url_for('download_excel', dept=department, item=module_name|lower|replace(' ', '-')) }}" class="btn btn-success btn-sm">Download Excel</a>
            </div>
        </div>

        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        <div class="card shadow-sm p-4 mb-4">
            <h5>Add New Entry / Transaction</h5>
            <form action="{{ url_for('save_transaction') }}" method="POST" class="row g-3 mt-1">
                <input type="hidden" name="department" value="{{ department }}">
                <input type="hidden" name="module_name" value="{{ module_name }}">
                <div class="col-md-3">
                    <label class="form-label">PO Number</label>
                    <input type="text" name="po_number" class="form-control" value="PO-2026-001" required>
                </div>
                <div class="col-md-3">
                    <label class="form-label">Entity / Customer / Supplier Name</label>
                    <input type="text" name="entity_name" class="form-control" placeholder="Enter name" required>
                </div>
                <div class="col-md-3">
                    <label class="form-label">Material / Item Type</label>
                    <input type="text" name="material_type" class="form-control" placeholder="e.g. SG Iron / Pig Iron">
                </div>
                <div class="col-md-3">
                    <label class="form-label">Quantity</label>
                    <input type="number" step="0.01" name="quantity" class="form-control" value="1">
                </div>
                <div class="col-md-3">
                    <label class="form-label">Weight (kg)</label>
                    <input type="number" step="0.01" name="weight" class="form-control" value="0">
                </div>
                <div class="col-md-3">
                    <label class="form-label">Amount (Rs.)</label>
                    <input type="number" step="0.01" name="amount" class="form-control" value="0">
                </div>
                <div class="col-md-6">
                    <label class="form-label">Remarks / Notes</label>
                    <input type="text" name="remarks" class="form-control" placeholder="Optional notes">
                </div>
                <div class="col-12">
                    <button type="submit" class="btn btn-primary">Save Entry</button>
                </div>
            </form>
        </div>

        <div class="card shadow-sm p-3">
            <h5>Existing Records</h5>
            <table class="table table-striped table-hover mt-2">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>PO Number</th>
                        <th>Entity Name</th>
                        <th>Material</th>
                        <th>Qty</th>
                        <th>Weight</th>
                        <th>Amount</th>
                        <th>Status</th>
                        <th>Created By</th>
                    </tr>
                </thead>
                <tbody>
                    {% for row in entries %}
                    <tr>
                        <td>{{ row.id }}</td>
                        <td>{{ row.po_number }}</td>
                        <td>{{ row.entity_name }}</td>
                        <td>{{ row.material_type }}</td>
                        <td>{{ row.quantity }}</td>
                        <td>{{ row.weight }} kg</td>
                        <td>Rs. {{ row.amount }}</td>
                        <td><span class="badge bg-warning text-dark">{{ row.status }}</span></td>
                        <td>{{ row.created_by }}</td>
                    </tr>
                    {% else %}
                    <tr><td colspan="9" class="text-center text-muted">No records found for this module. Add a new entry above.</td></tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>
"""

with open("templates/dashboard.html", "w", encoding="utf-8") as f:
    f.write(dashboard_html)

with open("templates/global_po_tracker.html", "w", encoding="utf-8") as f:
    f.write(global_po_tracker_html)

with open("templates/generic_module.html", "w", encoding="utf-8") as f:
    f.write(generic_module_html)

print("Templates created successfully!")