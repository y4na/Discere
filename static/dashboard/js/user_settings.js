
function showChangePassword() {
    document.getElementById('confirm-password-section').classList.add('hidden');
    document.getElementById('change-password-section').classList.remove('hidden');
}


function openModal(modalId) {
    document.getElementById(modalId).classList.remove("hidden");
    document.body.style.overflow = 'hidden';
}

function closeModal(modalId) {
    document.getElementById(modalId).classList.add("hidden");
    document.body.style.overflow = '';

    // Reset sections to default
    document.getElementById('confirm-password-section').classList.remove('hidden');
    document.getElementById('change-password-section').classList.add('hidden');
}

document.addEventListener("DOMContentLoaded", function () {
    //Current Password
    const toggleCurrentPassword = document.getElementById("toggle-password-current");
    const currentPasswordInput = document.getElementById("current-password");

    toggleCurrentPassword.addEventListener("click", function () {
        if (currentPasswordInput.type === "password") {
            currentPasswordInput.type = "text";
            toggleCurrentPassword.src = "/static/icons/eye-off.svg";
        } else {
            currentPasswordInput.type = "password";
            toggleCurrentPassword.src = "/static/icons/eye.svg";
        }
    });

    //New Password
    const toggleNewPassword = document.getElementById("toggle-password-new");
    const newPasswordInput = document.getElementById("new-password");

    toggleNewPassword.addEventListener("click", function () {
        if (newPasswordInput.type === "password") {
            newPasswordInput.type = "text";
            toggleNewPassword.src = "/static/icons/eye-off.svg";
        } else {
            newPasswordInput.type = "password";
            toggleNewPassword.src = "/static/icons/eye.svg";
        }
    });

    //Confirm New Password
    const toggleConfirmPassword = document.getElementById("toggle-password-confirm");
    const confirmPasswordInput = document.getElementById("confirm-new-password");

    toggleConfirmPassword.addEventListener("click", function () {
        if (confirmPasswordInput.type === "password") {
            confirmPasswordInput.type = "text";
            toggleConfirmPassword.src = "/static/icons/eye-off.svg";
        } else {
            confirmPasswordInput.type = "password";
            toggleConfirmPassword.src = "/static/icons/eye.svg";
        }
    });

    // Handle the Change Password modal submission
    document.getElementById('change-password-modal').querySelector('form').addEventListener('submit', function (e) {
        e.preventDefault();

        const newPassword = document.getElementById('new-password').value;
        const confirmPassword = document.getElementById('confirm-password').value;

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
    document.getElementById('change-email-modal').querySelector('form').addEventListener('submit', function (e) {
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
    document.getElementById('change-username-modal').querySelector('form').addEventListener('submit', function (e) {
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

    document.getElementById('change-email-modal').querySelector('form').addEventListener('submit', function (e) {
        e.preventDefault();
    
        const newEmail = document.getElementById('new-email').value;
        const confirmPasswordEmail = document.getElementById('password').value;
    
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
                window.location.href = "/confirm-email-change/";
            } else {
                alert('Error: ' + data.error);
            }
        });
    });    
});