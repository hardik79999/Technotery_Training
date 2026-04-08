document.addEventListener("DOMContentLoaded", function() {
    const token = localStorage.getItem('token');
    const role = localStorage.getItem('role');
    const username = localStorage.getItem('username') || "User"; 

    if (!token) { 
        window.location.href = '/login'; 
        return; 
    }

    document.getElementById('userBadge').innerText = `Role: ${role.toUpperCase()} | User: ${username}`;
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
    
    if (role === 'employee' && employeeView) {
        employeeView.style.display = 'block';
    }
    
    fetchDashboardData();

    
});

window.fetchDashboardData = function() {
    axios.get('/dashboard-data').then(response => {
        const data = response.data;
        const role = localStorage.getItem('role');
        
        // Admin Stats Dashboard
        if((role === 'admin' || role === 'manager') && data.admin_stats) {
            let containerId = role === 'admin' ? 'admin-view' : 'manager-view';
            let statsContainer = document.getElementById(role + '-stats-container');
            if(!statsContainer) {
                statsContainer = document.createElement('div');
                statsContainer.id = role + '-stats-container';
                const parentDiv = document.getElementById(containerId);
                if (parentDiv) parentDiv.appendChild(statsContainer);
            }

            if (statsContainer) {
                let statsTitle = role === 'admin' ? '🏢 Total Employees' : '👥 Employees Created By You';
                let listTitle = role === 'admin' ? 'User Directory' : 'Your Team';
                
                let statsHTML = `
                <div class="p-3 bg-dark rounded border border-info mt-3">
                    <h5 class="text-info">${statsTitle}: ${data.admin_stats.total_employees}</h5>
                    <hr class="border-secondary">
                    <h6 class="text-warning">${listTitle}:</h6>
                    <ul class="list-group list-group-flush bg-transparent">`;
                
                let usersList = role === 'admin' ? data.users : (data.admin_stats.my_created_users || []);
                if (usersList.length === 0) {
                    statsHTML += `<li class="list-group-item bg-transparent text-muted px-0">No users found.</li>`;
                } else {
                    usersList.forEach(u => {
                        statsHTML += `<li class="list-group-item bg-transparent text-light border-secondary px-0">
                            👤 <b>${u.username}</b> (${u.role}) <span class="text-secondary small float-end">Created by: ${u.creator || 'System'}</span>
                        </li>`;
                    });
                }
                statsHTML += `</ul></div>`;
                statsContainer.innerHTML = statsHTML;
            }
        }

        // Dropdown Update
        const assignDropdown = document.getElementById('assignToUser');
        if (assignDropdown && data.users) {
            const currentSelected = assignDropdown.value; 
            assignDropdown.innerHTML = '<option value="">Select Assignee...</option>';
            data.users.forEach(u => {
                assignDropdown.innerHTML += `<option value="${u.uuid}">${u.username} (${u.role})</option>`;
            });
            if (currentSelected) {
                assignDropdown.value = currentSelected; 
            }
        }

        // Task Render
        const container = document.getElementById('task-list-container');
        if (container) {
            if (!data.tasks || data.tasks.length === 0) {
                container.innerHTML = "<p class='text-muted'>No tasks found.</p>";
            } else {
                container.innerHTML = data.tasks.map(t => `
                    <div class="border border-secondary p-3 mb-3 rounded bg-dark shadow-sm">
                        <div class="d-flex justify-content-between align-items-start">
                            <div>
                                <h5 class="text-info mb-1">${t.title}</h5>
                                <p class="text-light small mb-2">${t.description}</p>
                                <span class="badge bg-warning text-dark">${t.status}</span>
                                <small class="text-secondary ms-2">Related User: ${t.assigned_to || t.assigned_by}</small>
                                <br>
                                <small class="text-muted" style="font-size: 0.75rem;">Created: ${t.created_at || 'N/A'} | Updated: ${t.updated_at || 'Never'}</small>
                            </div>
                        </div>
                        ${t.is_my_task ? `
                            <div class="mt-3 d-flex gap-2">
                                <select id="status-${t.uuid}" class="form-select form-select-sm w-auto bg-dark text-white border-info">
                                    <option value="pending" ${t.status==='pending'?'selected':''}>Pending</option>
                                    <option value="in progress" ${t.status==='in progress'?'selected':''}>In Progress</option>
                                    <option value="completed" ${t.status==='completed'?'selected':''}>Completed</option>
                                </select>
                                <button class="btn btn-sm btn-info fw-bold text-dark" onclick="updateTaskStatus('${t.uuid}')">Update</button>
                            </div>
                        ` : `<div class="mt-3"><button class="btn btn-sm btn-outline-danger" onclick="deleteTask('${t.uuid}')">Delete</button></div>`}
                    </div>
                `).join('');
            }
        }
    }).catch(err => {
        if(err.response && err.response.status === 401) { logout(); }
    });
}

window.updateTaskStatus = (uuid) => {
    const status = document.getElementById(`status-${uuid}`).value;
    axios.put(`/update/${uuid}`, { status }).then(() => fetchDashboardData());
};

window.deleteTask = (uuid) => {
    if(confirm("Are you sure you want to delete this task?")) {
        axios.delete(`/delete/${uuid}`).then(() => fetchDashboardData());
    }
};

document.getElementById('createUserForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    const role = localStorage.getItem('role');
    const path = role === 'admin' ? '/admin/create-users' : '/manager/create-emp';
    const newRoleToCreate = role === 'admin' ? document.getElementById('newRole').value : 'employee';

    const loadingOverlay = document.getElementById('loadingOverlay');
    const loadingText = document.getElementById('loadingText');
    if (loadingOverlay) {
        loadingText.innerText = `Creating ${newRoleToCreate.toUpperCase()} and sending email... Please wait.`;
        loadingOverlay.style.display = 'flex';
    }

    axios.post(path, {
        username: document.getElementById('newUsername').value,
        email: document.getElementById('newEmail').value,
        password: document.getElementById('newPassword').value,
        role: newRoleToCreate
    }).then(res => {
        if (loadingOverlay) loadingOverlay.style.display = 'none';
        alert("🎉 " + res.data.message);
        bootstrap.Modal.getInstance(document.getElementById('createUserModal')).hide();
        document.getElementById('createUserForm').reset();
        fetchDashboardData();
    }).catch(err => {
        if (loadingOverlay) loadingOverlay.style.display = 'none';
        alert("❌ " + (err.response?.data?.message || "Error creating user"));
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
    }).catch(err => alert("❌ " + (err.response?.data?.message || "Error assigning task")));
});

window.logout = () => { localStorage.clear(); window.location.href = '/login'; };