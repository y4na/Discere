
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


document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('profilePictureForm');
    const fileInput = form.querySelector('input[type="file"]');
    
    fileInput.addEventListener('change', function() {
        form.submit();
    });
});