document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault(); 

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const errorDiv = document.getElementById('error-msg');
    
    // Naya click karne pe purana error hata do
    if (errorDiv) {
        errorDiv.classList.add('d-none');
        errorDiv.innerText = "";
    }

    // Axios POST request
    axios.post('/login', {
        email: email,
        password: password
    })
    .then(function (response) {
        const data = response.data;
        
        // Save saara data
        localStorage.setItem('token', data.token);
        localStorage.setItem('role', data.role);
        localStorage.setItem('username', data.username || "User"); // 🚀 Safe fallback
        
        // Redirect
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