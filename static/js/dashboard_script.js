//home.js
// const menuButton = document.querySelector('#menu-button');
// const sidebarMenuButton = document.querySelector('#sidebar-menu-button');
// const sidebar = document.querySelector('#sidebar');
// const backdrop = document.querySelector('#backdrop');

// const toggleSidebar = () => {
//     sidebar.classList.toggle('-translate-x-full');
//     //backdrop.classList.toggle('hidden');
// };

// menuButton.addEventListener('click', toggleSidebar);
// sidebarMenuButton.addEventListener('click', toggleSidebar);
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


    const studySetsButton = document.querySelector('#study-sets');
    const examsButton = document.querySelector('#exams');
    const activeBar = document.querySelector('.active-bar');
    const studySetsContent = document.getElementById('study-sets-content');
    const examsContent = document.getElementById('exams-content');
    const openModalBtn = document.getElementById('open-modal');
    const createStudySetModal = document.getElementById('create-study-set-modal');
    const createExamModal = document.getElementById('create-exam-modal');
    const closeModalBtn = document.getElementById('close-modal');
    const closeExamModalBtn = document.getElementById('close-exam-modal');

    function toggleMenu(menuId) {
        const menu = document.getElementById(menuId);
        menu.style.display = menu.style.display === 'none' || menu.style.display === '' ? 'block' : 'none';
    }

    function handleAction(action) {
        alert(`Action selected: ${action}`);
        if (action === 'archive') {
            console.log("Adding to Archive...");
        } else if (action === 'favorite') {
            console.log("Adding to Favorites...");
        } else if (action === 'delete') {
            console.log("Deleting Set...");
        }
    }

    // document.addEventListener('click', function(event) {
    //     const menus = document.querySelectorAll('[id^="popupMenu-"]');
    //     const buttons = document.querySelectorAll('[id^="menuButton-"]');

    //     let isClickInside = false;

    //     menus.forEach(menu => {
    //         if (menu.contains(event.target)) isClickInside = true;
    //     });
    //     buttons.forEach(button => {
    //         if (button.contains(event.target)) isClickInside = true;
    //     });

    //     if (!isClickInside) {
    //         menus.forEach(menu => menu.style.display = 'none');
    //     }
    // });

//library.js
document.addEventListener("DOMContentLoaded", function() {
    function setActiveBar(button) {
        activeBar.style.width = `${button.offsetWidth}px`;
        activeBar.style.left = `${button.offsetLeft}px`;
    }

    function setButtonOpacity(activeButton, inactiveButton) {
        activeButton.classList.remove('opacity-50');
        activeButton.classList.add('opacity-100');
        inactiveButton.classList.remove('opacity-100');
        inactiveButton.classList.add('opacity-50');
    }

    function showTab(tab) {
        if (tab === 'study-sets') {
            studySetsContent.classList.remove('hidden');
            examsContent.classList.add('hidden');
            openModalBtn.innerHTML = `
                <img src="/static/icons/plus.svg" alt="icon" class="h-5 w-5 mr-2">
                Create Study Set
            `;
        } else if (tab === 'exams') {
            examsContent.classList.remove('hidden');
            studySetsContent.classList.add('hidden');
            openModalBtn.innerHTML = `
                <img src="/static/icons/plus.svg" alt="icon" class="h-5 w-5 mr-2">
                Create Exam
            `;
        }
    }

    setActiveBar(studySetsButton);
    setButtonOpacity(studySetsButton, examsButton);

    studySetsButton.addEventListener('click', function() {
        setActiveBar(studySetsButton);
        setButtonOpacity(studySetsButton, examsButton);
        showTab('study-sets');
    });

    examsButton.addEventListener('click', function() {
        setActiveBar(examsButton);
        setButtonOpacity(examsButton, studySetsButton);
        showTab('exams');
    });

    // Helper functions to disable and enable scrolling
    function disableScrolling() {
        document.body.style.overflow = 'hidden';
    }

    function enableScrolling() {
        document.body.style.overflow = '';
    }

    openModalBtn.addEventListener('click', function() {
        createStudySetModal.classList.add('hidden');
        createExamModal.classList.add('hidden');

        if (document.getElementById('study-sets').classList.contains('opacity-100')) {
            createStudySetModal.classList.remove('hidden');
        } else {
            createExamModal.classList.remove('hidden');
        }

        disableScrolling();
    });

    closeModalBtn.addEventListener('click', function() {
        createStudySetModal.classList.add('hidden');
        enableScrolling();
    });

    closeExamModalBtn.addEventListener('click', function() {
        createExamModal.classList.add('hidden');
        enableScrolling();
    });

        const manuallyCreateModal = document.getElementById('manually-create-modal');
        const manuallyCreateButton = document.getElementById('manually-create-exam');
        const closeExamModalButton = document.getElementById('close-exam-modal');
        const closeManuallyCreateModalButton = document.getElementById('close-manually-create-modal');

        manuallyCreateButton.addEventListener('click', () => {
            createExamModal.classList.add('hidden');
            manuallyCreateModal.classList.remove('hidden');
        });

        closeExamModalButton.addEventListener('click', () => {
            createExamModal.classList.add('hidden');
        });

        closeManuallyCreateModalButton.addEventListener('click', () => {
            manuallyCreateModal.classList.add('hidden');
            createExamModal.classList.remove('hidden');
        });

    // Color selection function
    function selectColor(element) {
        document.querySelectorAll('.selected-ring').forEach(ring => ring.classList.add('hidden'));
        document.querySelectorAll('.selected-icon').forEach(icon => icon.classList.add('hidden'));
        
        element.querySelector('.selected-ring').classList.remove('hidden');
        element.querySelector('.selected-icon').classList.remove('hidden');
    }

    // Expose selectColor to global scope if needed in HTML onclick
    window.selectColor = selectColor;
});


//user_settings.js

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


document.addEventListener('DOMContentLoaded', function () {
    try {
        const form = document.getElementById('profilePictureForm');
        if (!form) throw new Error('Form with ID "profilePictureForm" not found.');

        const fileInput = form.querySelector('input[type="file"]');
        if (!fileInput) throw new Error('File input not found in the form.');

        fileInput.addEventListener('change', function () {
            form.submit();
        });
    } catch (error) {
        console.error('Error:', error.message);
    }
});



//exam
document.getElementById("create-exam-set-btn").addEventListener("click", async function () {
    // Get form data
    const examSetName = document.getElementById("exam-set-name").value;
    const subject = document.getElementById("subject-exam").value;
    const examType = document.getElementById("exam-type").value;

    // Validate input
    if (examSetName == '' || subject == '' || examType == '') {
        alert("Please fill out all fields.");
        return;
    }

    try {
        const response = await fetch("/save-exam-set/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': document.querySelector('[name=csrf-token]').content // CSRF token for Django
            },
            body: JSON.stringify({
                name: examSetName,
                subject: subject,
                type: examType,
            }),
        });

        const result = await response.json();
        if (result.success) {
                    examsContent.classList.remove('hidden');
                    studySetsContent.classList.add('hidden');
                    openModalBtn.innerHTML = `
                        <img src="/static/icons/plus.svg" alt="icon" class="h-5 w-5 mr-2">
                        Create Exam
                    `;
            
        } else {
            alert("Error saving exam set: " + result.error);
        }
    } catch (error) {
        alert("An error occurred: " + error.message);
    }

    document.getElementById("manually-create-modal").classList.add("hidden");
});

