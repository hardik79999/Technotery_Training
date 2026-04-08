document.addEventListener("DOMContentLoaded", function() {
    const urlParams = new URLSearchParams(window.location.search);
    const token = urlParams.get('token');

    if (token) {
        try {
            const payload = JSON.parse(atob(token.split('.')[1]));
            
            if (payload.email) {
                document.getElementById('email').value = payload.email;
                document.getElementById('password').focus(); 
                
                // Mast Success Message dikhao
                const errorDiv = document.getElementById('error-msg');
                errorDiv.classList.remove('d-none', 'alert-danger');
                errorDiv.classList.add('alert-success');
                errorDiv.innerText = "✅ Secure link verified! Enter your password to continue.";
            }
        } catch (e) {
            console.log("Invalid or Expired Token");
        }
    }
});

document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault(); 

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const errorDiv = document.getElementById('error-msg');
    
    if (errorDiv) {
        errorDiv.classList.add('d-none');
        errorDiv.classList.remove('alert-success');
        errorDiv.classList.add('alert-danger');
        errorDiv.innerText = "";
    }

    axios.post('/login', {
        email: email,
        password: password
    })
    .then(function (response) {
        const data = response.data;
        
        localStorage.setItem('token', data.token);
        localStorage.setItem('role', data.role);
        localStorage.setItem('username', data.username || "User"); 
        
        window.location.href = '/dashboard'; 
    })
    .catch(function (error) {
        if (errorDiv) {
            errorDiv.classList.remove('d-none');
            errorDiv.innerText = error.response?.data?.message || "Server Error. Check terminal or database connection!";
        } else {
            alert("Login Failed: " + (error.response?.data?.message || "Server Issue"));
        }
    });
});