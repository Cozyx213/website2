// Define a variable to store the selected sorting column
let selectedColumn = null;

// Function to update the user scores table
function updateUserscoresTable() {
    // Build the URL for the AJAX request based on the selected column
    let url = "/EnrolleesJSON";
    if (selectedColumn) {
        url += `?sort=${selectedColumn}`;
    }

    // Make an AJAX request to the Flask endpoint to get the updated enrollees data
    fetch(url)
        .then(response => response.json())
        .then(data => {
            // Clear the current table content
            document.getElementById("userscores-table").innerHTML = "";

             // Update the table with the new data and calculate ranking
             let ranking = 1; // Initialize the ranking
            data.forEach(userscore => {
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td>${ranking}</td>
                    <td>${userscore.name}</td>
                    <td>${userscore.score}</td>
                    <td>${userscore.time}</td>
                    <td>${userscore.date}</td>
                `;
                ranking ++;
                document.getElementById("userscores-table").appendChild(row);
            });
        });
}

// Add event listeners for sorting buttons
const sortNameButton = document.getElementById('sortNameButton');
const sortScoreButton = document.getElementById('sortScoreButton');
const sortTimeButton = document.getElementById('sortTimeButton');
const sortDateButton = document.getElementById('sortDateButton');

sortNameButton.addEventListener('click', () => {
    sortTableByColumn('name');
});
sortScoreButton.addEventListener('click', () => {
    sortTableByColumn('score');
});
sortTimeButton.addEventListener('click', () => {
    sortTableByColumn('time');
});
sortDateButton.addEventListener('click', () => {
    sortTableByColumn('date');
});

// Function to sort the table data by the chosen column
function sortTableByColumn(column) {
    // Set the selected column
    selectedColumn = column;
    // Update the table immediately after selecting a sorting column
    updateUserscoresTable();
}

// Update the table initially and then periodically (e.g., every 5 seconds)
updateUserscoresTable(); // Initial update
setInterval(() => updateUserscoresTable(), 5000); // Periodic update every 5 seconds
