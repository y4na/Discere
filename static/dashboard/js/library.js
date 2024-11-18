document.addEventListener("DOMContentLoaded", function() {
    const studySetsButton = document.querySelector('#study-sets');
    const examsButton = document.querySelector('#exams');
    const activeBar = document.querySelector('.active-bar');

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

    setActiveBar(studySetsButton);
    setButtonOpacity(studySetsButton, examsButton);

    studySetsButton.addEventListener('click', function() {
        setActiveBar(studySetsButton);
        setButtonOpacity(studySetsButton, examsButton);
    });

    examsButton.addEventListener('click', function() {
        setActiveBar(examsButton);
        setButtonOpacity(examsButton, studySetsButton);
    });
});

//create study set
document.addEventListener("DOMContentLoaded", function() {
    const openModalButton = document.getElementById('open-modal');
    const closeModalButton = document.getElementById('close-modal');
    const modal = document.getElementById('create-study-set-modal');

    openModalButton.addEventListener('click', function() {
        modal.classList.remove('hidden');
    });

    closeModalButton.addEventListener('click', function() {
        modal.classList.add('hidden');
    });

    modal.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.classList.add('hidden');
        }
    });
});
//select color
function selectColor(element) {
    document.querySelectorAll('.selected-ring').forEach(ring => ring.classList.add('hidden'));
    document.querySelectorAll('.selected-icon').forEach(icon => icon.classList.add('hidden'));
    
    element.querySelector('.selected-ring').classList.remove('hidden');
    element.querySelector('.selected-icon').classList.remove('hidden');
}


//tabs
function showTab(tab) {
    const studySetsContent = document.getElementById('study-sets-content');
    const examsContent = document.getElementById('exams-content');

    if (tab === 'study-sets') {
        studySetsContent.classList.remove('hidden');
        examsContent.classList.add('hidden');
        document.getElementById('study-sets').classList.add('opacity-100');
        document.getElementById('exams').classList.remove('opacity-100');
        document.getElementById('exams').classList.add('opacity-50');
    } else if (tab === 'exams') {
        examsContent.classList.remove('hidden');
        studySetsContent.classList.add('hidden');
        document.getElementById('exams').classList.add('opacity-100');
        document.getElementById('study-sets').classList.remove('opacity-100');
        document.getElementById('study-sets').classList.add('opacity-50');
    }
}
