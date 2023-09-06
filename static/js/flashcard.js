document.addEventListener('DOMContentLoaded', function () {
const elementsData = JSON.parse('{{ elements | tojson | safe }}');
const compoundsData = JSON.parse('{{ compounds | tojson | safe }}');
const motivationalPhrases = JSON.parse('{{ phrases | tojson | safe }}');

const elements = elementsData.map(element => ({ ...element, done: false }));
const compounds = compoundsData.map(compound => ({ ...compound, done: false }));
//lets
let currentFlashcardIndex = 0;
let score = 0;
let currentData = elements; // Initially, start with flashcards
let elementsProgress = 0;
let compoundsProgress = 0;
let flashcardActivityStartTime;



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

shareButton.addEventListener('click',  shareScoreToLeaderboards);
// Initial setup
updateFlashcard();

// Functions
window.onload = function () {
    flashcardActivityStartTime = Date.now(); // Store the start time
};
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


function checkAnswer() {
    const origAnswer = currentData[currentFlashcardIndex].element_name;
    const userAnswer = answerInput.value.trim().toLowerCase();
    const correctAnswer = currentData[currentFlashcardIndex].element_name.toLowerCase();

    if (userAnswer === correctAnswer) {
        score++;
        scoreSpan.textContent = score;
        currentData[currentFlashcardIndex].done = true; // Mark flashcard as done
        nextFlashcard();
    } else {
        backDiv.style.display = 'block';
        const randomPhraseIndex = Math.floor(Math.random() * motivationalPhrases.length);
        backDiv.querySelector('p').textContent = motivationalPhrases[randomPhraseIndex];
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
    const name = document.getElementById('name').value;
    const scoreParam = `score=${score}`;
    // Calculate the total time spent on the flashcard activity
    const endTime = Date.now();
    const totalTimeSpent = (endTime - flashcardActivityStartTime) / 1000; // Convert to seconds
    const timeSpentParam = `total_time_spent=${totalTimeSpent}`;
    const nameParam = `name=${name}`;

    // Create a hidden form and submit it with score, time spent, and name
    const form = document.createElement('form');
    form.action = '/leaderboards'; // Replace with your leaderboards endpoint
    form.method = 'post';

    const scoreInput = document.createElement('input');
    scoreInput.type = 'hidden';
    scoreInput.name = 'score';
    scoreInput.value = score;

    const timeSpentInput = document.createElement('input');
    timeSpentInput.type = 'hidden';
    timeSpentInput.name = 'total_time_spent';
    timeSpentInput.value = totalTimeSpent;

    const nameInput = document.createElement('input');
    nameInput.type = 'hidden';
    nameInput.name = 'name';
    nameInput.value = name;

    form.appendChild(scoreInput);
    form.appendChild(timeSpentInput);
    form.appendChild(nameInput);

    document.body.appendChild(form);
    form.submit();
}
});
