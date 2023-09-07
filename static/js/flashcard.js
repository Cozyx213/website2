fetch('/chemistryData') 
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const contentType = response.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
            return response.json();
        } else {
            throw new TypeError('Response is not in JSON format');
        }
    })
    .then(data=>{ 
    const elementsData = data.elements;
    const compoundsData = data.compounds;
    const motivationalPhrases = data.phrases;
    const elements = elementsData.map(element => ({ ...element, done: false }));
    const compounds = compoundsData.map(compound => ({ ...compound, done: false }));
    //lets
    let currentFlashcardIndex = 0;
    let score = 0;
    let currentData = elements; // Initially, start with flashcards
    let elementsProgress = 0;
    let compoundsProgress = 0;
    let flashcardActivityStartTime = null;
    // DOM elements
    const flashcardSymbol = document.getElementById('flashcard-symbol');
    const answerInput = document.getElementById('answer');
    const scoreSpan = document.getElementById('score');
    const descriptionDiv = document.querySelector('.description');
    const backDiv = document.querySelector('.back');
    const checkButton = document.getElementById('checkButton');
    const nextButton = document.getElementById('nextButton');
    const shuffleButton = document.getElementById('shuffleButton');
    const toggleDescriptionButton = document.getElementById('toggleDescriptionButton');
    const toggleDataButton = document.getElementById('toggleDataButton'); // New button
    const toggleAnswerButton = document.getElementById('showAnswer');
    const promptText = document.querySelector('.content');
    const shareButton = document.getElementById('share');
    const usernameInput = document.getElementById('username')
    // Event listeners
    answerInput.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            checkAnswer();
        }
    });
    //buttons
    checkButton.addEventListener('click', () => checkAnswer());
    nextButton.addEventListener('click', () => nextFlashcard());
    shuffleButton.addEventListener('click', () => shuffleFlashcards());
    toggleDescriptionButton.addEventListener('click', () => toggleDescription());
    toggleDataButton.addEventListener('click', () => toggleData()); // New event listener
    toggleAnswerButton.addEventListener('click', () => toggleAnswer());
    shareButton.addEventListener('click', shareScoreToLeaderboards);
    answerInput.addEventListener('input', () => {
        // Start the timer if the score is greater than 0 and the timer has not started
        if ( flashcardActivityStartTime === null) {
            flashcardActivityStartTime = Date.now();
        }
    });
    // Initial setup
    updateFlashcard();
    // Functions
    
     // Store the start time
    
    function redirectToEnrollmentPage() {
        const scoreParam = `score=${score}`;
        const enrollmentURL = "/Enroll?" + scoreParam; // Replace with the actual URL of your enrollment page
        window.location.href = enrollmentURL;
    }
    function updatePrompt(currentData) {
        const textPrompt = promptText.querySelector('p');
        if (currentData === elements) {
            textPrompt.textContent = "Guess the element:";
        }
        else if (currentData === compounds) {
            textPrompt.textContent = "Guess the compound:";
        }
    }
    function updateFlashcard() {
        const flashcard = currentData[currentFlashcardIndex];
        flashcardSymbol.textContent = flashcard.element_symbol;
        answerInput.value = '';
        descriptionDiv.textContent = flashcard.other_info;
        backDiv.style.display = 'none';
    }
    function handleCorrectAnswer(){
        score++;
        scoreSpan.textContent = score;
        currentData[currentFlashcardIndex].done = true; // Mark flashcard as done
        
        nextFlashcard();
    }
    function handleIncorrectAnswer(){
        backDiv.style.display = 'block';
        const randomPhraseIndex = Math.floor(Math.random() * motivationalPhrases.length);
        backDiv.querySelector('p').textContent = motivationalPhrases[randomPhraseIndex];
    }
    function checkAnswer() {
        const origAnswer = currentData[currentFlashcardIndex].element_name;
        const userAnswer = answerInput.value.trim().toLowerCase();
        const correctAnswer = currentData[currentFlashcardIndex].element_name.toLowerCase();
        if (userAnswer === correctAnswer) {
            handleCorrectAnswer();
        } else {
            handleIncorrectAnswer();
        }
        
    }
    function nextFlashcard() {
        // Find the next undone flashcard
        let nextIndex = currentFlashcardIndex + 1;
        while (nextIndex < currentData.length && currentData[nextIndex].done) {
            nextIndex++;
        }
        if (nextIndex < currentData.length) {
            currentFlashcardIndex = nextIndex;
            updateFlashcard();
        } else {
            alert("You've completed all the flashcards!");
        }
    }
    function shuffleFlashcards() {
        for (let i = currentData.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [currentData[i], currentData[j]] = [currentData[j], currentData[i]];
        }
        // Find the first undone flashcard after shuffling
        let firstUndoneIndex = 0;
        while (firstUndoneIndex < currentData.length && currentData[firstUndoneIndex].done) {
            firstUndoneIndex++;
        }
        if (firstUndoneIndex < currentData.length) {
            currentFlashcardIndex = firstUndoneIndex;
            updateFlashcard();
        } else {
            alert("You've completed all the flashcards!");
        }
    }
    function toggleDescription() {
        descriptionDiv.style.display = (descriptionDiv.style.display === 'none') ? 'block' : 'none';
    }
    function toggleData() {
        if (currentData === elements) {
            // Switching from elements to compounds
            compoundsProgress = currentFlashcardIndex;
            currentData = compounds;
            currentFlashcardIndex = compoundsProgress;
        } else {
            // Switching from compounds to elements
            elementsProgress = currentFlashcardIndex;
            currentData = elements;
            currentFlashcardIndex = elementsProgress;
        }
        updatePrompt(currentData);
        updateFlashcard();
    }
    function toggleAnswer() {
        const flashcard = currentData[currentFlashcardIndex];
        const answerParagraph = backDiv.querySelector('p')
        if (backDiv.style.display === 'none') {
            backDiv.style.display = 'block';
            answerParagraph.textContent = `The answer is ${flashcard.element_name}`
        }
        else {
            backDiv.style.display = 'none';
            answerParagraph.textContent = 'So you give up huh... It\'s Okay';
        }
    }
    function shareScoreToLeaderboards() {
        const endTime = Date.now();
        const totalTimeSpent = (endTime - flashcardActivityStartTime) / 1000; // Convert to seconds
        const timeSpentParam = totalTimeSpent;
        const name = prompt("Please enter your username to put in the leaderboards:");
        if (name !== null) { // User pressed OK in the prompt
            const scoreParam = score; // Assuming score is a global variable
            // Calculate the total time spent on the flashcard activity
            // Set the form field values
            document.getElementById('scoreInput').value = scoreParam;
            document.getElementById('timeSpentInput').value = timeSpentParam;
            document.getElementById('nameInput').value = name;
            // Trigger the form submission
            document.getElementById('leaderboardForm').submit();
        }
    } })
