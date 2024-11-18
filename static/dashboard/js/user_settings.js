// Function to open the modal
function openModal(modalId) {
    document.getElementById(modalId).classList.remove("hidden");
}

// Function to close the modal
function closeModal(modalId) {
    document.getElementById(modalId).classList.add("hidden");
}

// Toggle Password Visibility
document.addEventListener("DOMContentLoaded", function() {
    const toggleNewPassword = document.getElementById("toggle-password-new");
    const newPasswordInput = document.getElementById("new-password");

    toggleNewPassword.addEventListener("click", function() {
        console.log("Toggling New Password Visibility");  
        if (newPasswordInput.type === "password") {
            newPasswordInput.type = "text";
            console.log("Password Visible: eye icon should appear");
            toggleNewPassword.src = "/static/icons/eye-off.svg";  
        } else {
            newPasswordInput.type = "password";
            console.log("Password Hidden: eye-off icon should appear");
            toggleNewPassword.src = "/static/icons/eye.svg"; 
        }
    });

    // Confirm Password Toggle
    const toggleConfirmPassword = document.getElementById("toggle-password-confirm");
    const confirmPasswordInput = document.getElementById("confirm-password");

    toggleConfirmPassword.addEventListener("click", function() {
        console.log("Toggling Confirm Password Visibility");  
        if (confirmPasswordInput.type === "password") {
            confirmPasswordInput.type = "text";
            console.log("Confirm Password Visible: eye icon should appear");
            toggleConfirmPassword.src = "/static/icons/eye-off.svg"; 
        } else {
            confirmPasswordInput.type = "password";
            console.log("Confirm Password Hidden: eye-off icon should appear");
            toggleConfirmPassword.src = "/static/icons/eye.svg"; 
        }
    });
});

// Handle the Change Password modal submission
document.getElementById('change-password-modal').querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault();

    const newPassword = document.getElementById('new-password').value;
    const confirmPassword = document.getElementById('confirm-password').value;

    // Validate passwords
    if (newPassword !== confirmPassword) {
        alert('Passwords do not match!');
        return;
    }

    fetch('/update-user-info/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify({
            password: newPassword
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(data.message);
            closeModal('change-password-modal');
        } else {
            alert('Error: ' + data.error);
        }
    });
});

// Handle the Change Email modal submission
document.getElementById('change-email-modal').querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault();

    const newEmail = document.getElementById('new-email').value;
    const confirmPasswordEmail = document.getElementById('confirm-password-email').value;

    fetch('/update-user-info/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify({
            new_email: newEmail,
            password: confirmPasswordEmail
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(data.message);
            closeModal('change-email-modal');
        } else {
            alert('Error: ' + data.error);
        }
    });
});

// Handle the Change Username modal submission
document.getElementById('change-username-modal').querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault();

    const newUsername = document.getElementById('current-username').value;

    fetch('/update-user-info/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify({
            new_username: newUsername
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(data.message);
            closeModal('change-username-modal');
        } else {
            alert('Error: ' + data.error);
        }
    });
});