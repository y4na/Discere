const menuButton = document.querySelector('#menu-button');
const sidebarMenuButton = document.querySelector('#sidebar-menu-button');
const sidebar = document.querySelector('#sidebar');
const backdrop = document.querySelector('#backdrop');

const toggleSidebar = () => {
    sidebar.classList.toggle('-translate-x-full');
    //backdrop.classList.toggle('hidden');
};

menuButton.addEventListener('click', toggleSidebar);
sidebarMenuButton.addEventListener('click', toggleSidebar);
//backdrop.addEventListener('click', toggleSidebar);

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

document.addEventListener('DOMContentLoaded', function () {
    feather.replace(); 
});

