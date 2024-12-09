document.addEventListener('DOMContentLoaded', function () {
    const stepOneForm = document.getElementById('step-one-form');
    const stepTwoForm = document.getElementById('step-two-form');
    const nextBtn = document.querySelector('.next-btn');

    stepTwoForm.style.display = 'none';
	//stepTwoForm.style.display = 'block';

    nextBtn.addEventListener('click', function (event) {
        event.preventDefault();

        stepOneForm.style.display = 'none';
        stepTwoForm.style.display = 'block';
    });
});
