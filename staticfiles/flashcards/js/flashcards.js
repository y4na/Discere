const profileMenuButton = document.getElementById('profile-menu-button');
const profilePopup = document.getElementById('profile-popup');

profileMenuButton.addEventListener('click', () => {
    profilePopup.classList.toggle('hidden');
});

window.addEventListener('click', (event) => {
    if (!profileMenuButton.contains(event.target) && !profilePopup.contains(event.target)) {
        profilePopup.classList.add('hidden');
    }
});