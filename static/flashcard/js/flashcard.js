document.addEventListener('DOMContentLoaded', () => {
    const addCardButton = document.querySelector('.add-card-btn');
    const flashcardsContainer = document.getElementById('flashcards');
    const flashcardCounter = document.getElementById('flashcard-counter');
    const modal = document.getElementById('modal');
    const closeModalButton = document.querySelector('.close-btn');

    function updateFlashcardCount() {
        const flashcardCount = flashcardsContainer.querySelectorAll('.flashcard').length;
        flashcardCounter.textContent = flashcardCount;

        const flashcardNumbers = flashcardsContainer.querySelectorAll('.flashcard-number');
        flashcardNumbers.forEach((number, index) => {
            number.textContent = index + 1; 
        });
    }

    updateFlashcardCount();

    addCardButton.addEventListener('click', () => {
        const flashcardToClone = flashcardsContainer.querySelector('.flashcard');

        const newFlashcard = flashcardToClone.cloneNode(true);
        const inputTerms = newFlashcard.querySelectorAll('.input-term');
        const inputDefinitions = newFlashcard.querySelectorAll('.input-definition');

        inputTerms.forEach(input => {
            input.value = '';
        });

        inputDefinitions.forEach(input => {
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
