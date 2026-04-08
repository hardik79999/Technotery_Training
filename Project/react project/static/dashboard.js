let taskChartInstance = null; // Global Chart Variable

document.addEventListener("DOMContentLoaded", function() {
    const token = localStorage.getItem('token');
    const role = localStorage.getItem('role');
    const username = localStorage.getItem('username') || "User"; 

    if (!token) { window.location.href = '/login'; return; }

    document.getElementById('userBadge').innerText = `👤 ${username} (${role.toUpperCase()})`;
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;

    const adminView = document.getElementById('admin-view');
    const managerView = document.getElementById('manager-view');
    const employeeView = document.getElementById('employee-view');
    const managerOption = document.getElementById('managerOption');

    if (role === 'admin' && adminView) adminView.style.display = 'block';
    if (role === 'manager' && managerView) {
        managerView.style.display = 'block';
        if (managerOption) managerOption.style.display = 'none';
    }
    if (role === 'employee' && employeeView) employeeView.style.display = 'block';
    
    fetchDashboardData();
});

window.fetchDashboardData = function() {
    axios.get('/dashboard-data').then(response => {
        const data = response.data;
        const role = localStorage.getItem('role');
        
        // 🚀 LIVE CHART UPDATE LOGIC
        if(data.chart_data) {
            updateChart(data.chart_data.pending, data.chart_data['in progress'], data.chart_data.completed);
        }

        // Admin/Manager Stats
        if((role === 'admin' || role === 'manager') && data.admin_stats) {
            let containerId = role === 'admin' ? 'admin-view' : 'manager-view';
            let statsContainer = document.getElementById(role + '-stats-container');
            if(!statsContainer) {
                statsContainer = document.createElement('div');
                statsContainer.id = role + '-stats-container';
                document.getElementById(containerId).appendChild(statsContainer);
            }
            let statsHTML = `<div class="p-3 mt-3 rounded" style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);">
                <h6 class="text-info mb-0">Total Team Size: ${data.admin_stats.total_employees}</h6>
            </div>`;
            statsContainer.innerHTML = statsHTML;
        }

        // Dropdown Update
        const assignDropdown = document.getElementById('assignToUser');
        if (assignDropdown && data.users) {
            const currentSelected = assignDropdown.value; 
            assignDropdown.innerHTML = '<option value="">Select Assignee...</option>';
            data.users.forEach(u => {
                assignDropdown.innerHTML += `<option value="${u.uuid}">${u.username} (${u.role})</option>`;
            });
            if (currentSelected) assignDropdown.value = currentSelected; 
        }

        // Task Render
        const container = document.getElementById('task-list-container');
        if (container) {
            if (!data.tasks || data.tasks.length === 0) {
                container.innerHTML = "<p class='text-muted mt-3'>No tasks found.</p>";
            } else {
                container.innerHTML = data.tasks.map(t => {
                    let badgeColor = t.status === 'completed' ? 'bg-success' : (t.status === 'in progress' ? 'bg-warning text-dark' : 'bg-danger');
                    return `
                    <div class="p-3 mb-3 rounded shadow-sm" style="background: rgba(0,0,0,0.3); border-left: 4px solid ${t.status==='completed'?'#38ef7d':'#00c6ff'};">
                        <div class="d-flex justify-content-between align-items-start">
                            <div>
                                <h5 class="text-white mb-1">${t.title}</h5>
                                <p class="text-light small mb-2">${t.description}</p>
                                <span class="badge ${badgeColor}">${t.status.toUpperCase()}</span>
                                <small class="text-secondary ms-2">User: ${t.assigned_to || t.assigned_by}</small>
                            </div>
                        </div>
                        ${t.is_my_task ? `
                            <div class="mt-3 d-flex gap-2">
                                <select id="status-${t.uuid}" class="form-select form-select-sm w-auto">
                                    <option value="pending" ${t.status==='pending'?'selected':''}>Pending</option>
                                    <option value="in progress" ${t.status==='in progress'?'selected':''}>In Progress</option>
                                    <option value="completed" ${t.status==='completed'?'selected':''}>Completed</option>
                                </select>
                                <button class="btn btn-sm btn-info fw-bold text-dark" onclick="updateTaskStatus('${t.uuid}')">Save</button>
                            </div>
                        ` : `<div class="mt-3"><button class="btn btn-sm btn-outline-danger" onclick="deleteTask('${t.uuid}')">Delete</button></div>`}
                    </div>
                `}).join('');
            }
        }
    }).catch(err => {
        if(err.response && err.response.status === 401) { logout(); }
    });
}

// 📈 CHART FUNCTION
function updateChart(pending, inProgress, completed) {
    const ctx = document.getElementById('taskChart').getContext('2d');
    
    if (taskChartInstance) {
        taskChartInstance.data.datasets[0].data = [pending, inProgress, completed];
        taskChartInstance.update();
    } else {
        taskChartInstance = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Pending', 'In Progress', 'Completed'],
                datasets: [{
                    data: [pending, inProgress, completed],
                    backgroundColor: ['#ff4b2b', '#f6d365', '#38ef7d'],
                    borderWidth: 0,
                    hoverOffset: 4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { position: 'right', labels: { color: '#ffffff' } }
                }
            }
        });
    }
}

// Actions (same as before)
window.updateTaskStatus = (uuid) => {
    axios.put(`/update/${uuid}`, { status: document.getElementById(`status-${uuid}`).value }).then(() => fetchDashboardData());
};
window.deleteTask = (uuid) => {
    if(confirm("Delete task?")) axios.delete(`/delete/${uuid}`).then(() => fetchDashboardData());
};

document.getElementById('createUserForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    const role = localStorage.getItem('role');
    const path = role === 'admin' ? '/admin/create-users' : '/manager/create-emp';
    const newRole = role === 'admin' ? document.getElementById('newRole').value : 'employee';
    document.getElementById('loadingOverlay').style.display = 'flex';

    axios.post(path, {
        username: document.getElementById('newUsername').value,
        email: document.getElementById('newEmail').value,
        password: document.getElementById('newPassword').value,
        role: newRole
    }).then(res => {
        document.getElementById('loadingOverlay').style.display = 'none';
        alert("🎉 " + res.data.message);
        bootstrap.Modal.getInstance(document.getElementById('createUserModal')).hide();
        document.getElementById('createUserForm').reset();
        fetchDashboardData();
    }).catch(err => {
        document.getElementById('loadingOverlay').style.display = 'none';
        alert("❌ " + (err.response?.data?.message || "Error"));
    });
});

document.getElementById('createTaskForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    const role = localStorage.getItem('role');
    const path = role === 'admin' ? '/admin/create-tasks' : '/manager/create-tasks';
    axios.post(path, {
        title: document.getElementById('taskTitle').value,
        description: document.getElementById('taskDesc').value,
        assigned_to: document.getElementById('assignToUser').value
    }).then(res => {
        alert("✅ " + res.data.message);
        bootstrap.Modal.getInstance(document.getElementById('createTaskModal')).hide();
        document.getElementById('createTaskForm').reset();
        fetchDashboardData();
    });
});

window.logout = () => { localStorage.clear(); window.location.href = '/login'; };