// profile popup
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

// flashcard clone
document.addEventListener('DOMContentLoaded', () => {
    const addCardButton = document.querySelector('.add-card-btn');
    const flashcardsContainer = document.getElementById('flashcards');
    const flashcardCounter = document.getElementById('flashcard-counter');
    const modal = document.getElementById('modal');
    const closeModalButton = document.querySelector('.close-btn');

    function updateFlashcardCount() {
        const flashcards = flashcardsContainer.querySelectorAll('.flashcard');
        flashcardCounter.textContent = flashcards.length;

        flashcards.forEach((flashcard, index) => {
            flashcard.querySelector('.flashcard-number').textContent = index + 1;

            flashcard.querySelector('.input-term').setAttribute('name', `term_${index + 1}`);
            flashcard.querySelector('.input-definition').setAttribute('name', `definition_${index + 1}`);
        });
    }

    updateFlashcardCount();

    addCardButton.addEventListener('click', () => {
        const flashcardToClone = flashcardsContainer.querySelector('.flashcard');
        const newFlashcard = flashcardToClone.cloneNode(true);

        newFlashcard.querySelectorAll('input').forEach(input => {
            input.value = '';
        });

        flashcardsContainer.appendChild(newFlashcard);
        updateFlashcardCount();
    });

    flashcardsContainer.addEventListener('click', (event) => {
        if (event.target.closest('.delete-btn')) {
            const flashcard = event.target.closest('.flashcard');
            const flashcardCount = flashcardsContainer.querySelectorAll('.flashcard').length;

            if (flashcardCount === 1) {
                modal.style.display = 'block';
            } else {
                flashcardsContainer.removeChild(flashcard);
                updateFlashcardCount();
            }
        }
    });

    closeModalButton.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    window.addEventListener('click', (event) => {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
});