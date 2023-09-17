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
    .then(data => {
        const elementsData = data.elements;
        const compoundsData = data.compounds;
        const ionsData = data.ions;
        const acidsData = data.acids;
        const motivationalPhrases = data.phrases;
        const elements = elementsData.map(element => ({ ...element, done: false }));
        const compounds = compoundsData.map(compound => ({ ...compound, done: false }));
        const acids = acidsData.map(acid => ({ ...acid, done: false }));
        const ions = ionsData.map(ion => ({ ...ion, done: false }));
        //lets
        let currentFlashcardIndex = 0;
        let score = 0;
        let currentData = elements; // Initially, start with flashcards
        let elementsProgress = 0;
        let compoundsProgress = 0;
        let acidsProgress = 0;
        let ionsProgress = 0;
        let flashcardActivityStartTime = null;
        let isFormulaMode = false;

        // DOM elements
        const flashcardSymbol = document.getElementById('flashcard-symbol');
        const answerInput = document.getElementById('answer');
        const scoreSpan = document.getElementById('score');
        const descriptionDiv = document.querySelector('.description');
        const backDiv = document.querySelector('.back');
        const pastDiv = document.querySelector('.past');
        const acidButton = document.getElementById('acidButton');
        const nextButton = document.getElementById('nextButton');
        const shuffleButton = document.getElementById('shuffleButton');
        const toggleDescriptionButton = document.getElementById('toggleDescriptionButton');
        const toggleDataButton = document.getElementById('toggleDataButton'); // New button
        const toggleAnswerButton = document.getElementById('showAnswer');
        const promptText = document.querySelector('.content');
        const shareButton = document.getElementById('share');
        const usernameInput = document.getElementById('username');
        const resetButton = document.getElementById('resetButton');
        const swapButton = document.getElementById('swapAnswer')
        // Event listeners
        answerInput.addEventListener('keydown', (event) => {
            if (event.key === 'Enter') {
                checkAnswer();
            }
        });
        //buttons
        swapButton.addEventListener('click', () =>formulaMode());
        nextButton.addEventListener('click', () => nextFlashcard());
        shuffleButton.addEventListener('click', () => shuffleFlashcards());
        toggleDescriptionButton.addEventListener('click', () => toggleDescription());
        toggleDataButton.addEventListener('click', () => toggleData()); // New event listener
        toggleAnswerButton.addEventListener('click', () => toggleAnswer());
        shareButton.addEventListener('click', shareScoreToLeaderboards);
        answerInput.addEventListener('input', () => {
            // Start the timer if the score is greater than 0 and the timer has not started
            if (flashcardActivityStartTime === null) {
                flashcardActivityStartTime = Date.now();
            }
        });

        resetButton.addEventListener('click', () => {
            // Reset the flashcards to their initial state
            currentFlashcardIndex = 0;
            score = 0;
            elementsProgress = 0;
            compoundsProgress = 0;
            acidsProgress = 0;
            ionsProgress =0;
            flashcardActivityStartTime = null;

            // Mark all flashcards as not done
            elements.forEach(element => (element.done = false));
            compounds.forEach(compound => (compound.done = false));
            acids.forEach(acid => (acid.done = false));

            // Shuffle the flashcards if needed (uncomment the line below)
            // shuffleFlashcards();

            // Update the UI to display the first flashcard
            updateFlashcard();
        });
        // Initial setup
        updateFlashcard();
        // Functions

        // Store the start time
        function formulaMode(){
            isFormulaMode = isFormulaMode ? false : true;
            updateFlashcard();
        }
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
            else if (currentData === ions) {
                textPrompt.textContent = "Guess the ion:";
            }
            else if (currentData === compounds) {
                textPrompt.textContent = "Guess the Polyatomic ion:";
            }
            else if (currentData === acids) {
                textPrompt.textContent = "Guess the acid:";
            }
        }
        function compoundSubscript(formula) {
            // Regular expression to match element symbols and counts
            const regex = /([A-Z][a-z]*)(\d*)(\^([\d+]?[+-]?))?/g;

            // Replace element counts and superscripts
            const formulaWithSubscripts = formula.replace(regex, (match, element, count, _, superscript) => {
                if (count === '') {
                    // If no count is specified, return the element with superscript if present
                    return element + (superscript ? `<sup>${superscript}</sup>` : '');
                } else {
                    // Use individual characters as subscripts for count, and superscript if present
                    const subscriptedCount = count.split('').map(digit => `<sub>${digit}</sub>`).join('');
                    return element + subscriptedCount + (superscript ? `<sup>${superscript}</sup>` : '');
                }
            });

            return formulaWithSubscripts;
        }

        // Example usage:
        const formula = "H2O";
        const formulaWithSubscripts = compoundSubscript(formula);
        console.log(formulaWithSubscripts); // Output: "H<sub>2</sub>O"



        function updateFlashcard() {
            if (isFormulaMode) {
                const flashcard = currentData[currentFlashcardIndex];
                flashcardSymbol.innerHTML = compoundSubscript(flashcard.element_name);
                answerInput.value = '';
                descriptionDiv.textContent = flashcard.other_info;
                hideAnswer();
            }
            else {
                const flashcard = currentData[currentFlashcardIndex];
                flashcardSymbol.innerHTML = compoundSubscript(flashcard.element_symbol);
                answerInput.value = '';
                descriptionDiv.textContent = flashcard.other_info;
                hideAnswer();
            }

        }
        function handleCorrectAnswer(correctAnswer) {
            const answer = correctAnswer;
            if (currentData === compounds && currentData === acids) {
                score += 5
            }
            else {
                score += 3
            }

            scoreSpan.textContent = score;
            currentData[currentFlashcardIndex].done = true; // Mark flashcard as done
            pastDiv.style.display = 'block';
            console.log(answer)
            pastDiv.querySelector('p').textContent = answer;
            nextFlashcard();
        }
        function handleIncorrectAnswer() {
            backDiv.style.display = 'block';
            const randomPhraseIndex = Math.floor(Math.random() * motivationalPhrases.length);
            backDiv.querySelector('p').textContent = motivationalPhrases[randomPhraseIndex];
        }
        function checkAnswer() {
            if (isFormulaMode) {
                const origAnswer = currentData[currentFlashcardIndex].element_symbol;
                const userAnswer = answerInput.value.trim().toLowerCase();
                const correctAnswer = currentData[currentFlashcardIndex].element_symbol.toLowerCase();
                if (userAnswer === correctAnswer) {
                     
                    handleCorrectAnswer(origAnswer);
                }
                else if (userAnswer === "show") {
                    showAnswer();
                    answerInput.value = '';
                }
                else {
                    handleIncorrectAnswer();
                }
            }
            else {
                const origAnswer = currentData[currentFlashcardIndex].element_name;
                const userAnswer = answerInput.value.trim().toLowerCase();
                const correctAnswer = currentData[currentFlashcardIndex].element_name.toLowerCase();
                if (userAnswer === correctAnswer) {
                    handleCorrectAnswer(origAnswer);
                }
                else if (userAnswer === "show") {
                    showAnswer();
                    answerInput.value = '';
                }
                else {
                    handleIncorrectAnswer();
                }
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
                currentData = ions;
                currentFlashcardIndex = ionsProgress;
            }

            else if (currentData === ions) {
                acidsProgress = currentFlashcardIndex;
                currentData = compounds;
                currentFlashcardIndex = compoundsProgress;
            }
            else if (currentData === compounds){
                // Switching from compounds to elements
                elementsProgress = currentFlashcardIndex;
                currentData = acids;
                currentFlashcardIndex = acidsProgress;
            }
            else if (currentData === acids){
                // Switching from compounds to elements
                elementsProgress = currentFlashcardIndex;
                currentData = elements;
                currentFlashcardIndex = elementsProgress;
            }

            updatePrompt(currentData);
            updateFlashcard();
        }

        function showAnswer() {
            if (isFormulaMode) {
                const flashcard = currentData[currentFlashcardIndex];
                score = score - 10;
                const answerParagraph = backDiv.querySelector('p')
                answerParagraph.textContent = `The answer is ${flashcard.element_symbol}`
                backDiv.style.display = 'block';
            }else{
                const flashcard = currentData[currentFlashcardIndex];
                score = score - 10;
                const answerParagraph = backDiv.querySelector('p')
                answerParagraph.textContent = `The answer is ${flashcard.element_name}`
                backDiv.style.display = 'block';
            }
            
        }

        function hideAnswer() {
            backDiv.style.display = 'none';
        }

        function toggleAnswer() {
            const flashcard = currentData[currentFlashcardIndex];
            const answerParagraph = backDiv.querySelector('p')
            answerParagraph.textContent = `The answer is ${flashcard.element_name}`
            showAnswer();
        }

        function shareScoreToLeaderboards() {
            const endTime = Date.now();
            const totalTimeSpent = (endTime - flashcardActivityStartTime) / 1000; // Convert to seconds
            const timeSpentParam = totalTimeSpent;
            const name = prompt("Please enter username to place in the leaderboards:");
            const scoreParam = score; // Assuming score is a global variable

            document.getElementById('scoreInput').value = scoreParam;
            document.getElementById('timeSpentInput').value = timeSpentParam;// Calculate the total time spent on the flashcard activity
            document.getElementById('nameInput').value = name;

            if (name !== null && name.trim() !== "") { // User pressed OK in the prompt
                if (name.length > 11) {
                    alert("Username can't be more than 10 characters")
                } else {
                    document.getElementById('leaderboardForm').submit();
                }
            } else {
                alert("Please enter a valid username.");
            }
        }
    })
