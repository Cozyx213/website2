// Define a variable to store the selected sorting column
let selectedColumn = null;

// Function to update the user scores table
function updateUserscoresTable() {
    // Build the URL for the AJAX request based on the selected column
    let url = "/EnrolleesJSON";
    if (selectedColumn) {
        url += `?sort=${selectedColumn}`;
    }
function secondToTime(seconds){
    if(seconds<60){
        let sec = (seconds).toFixed(2);
        return `${sec}s`
    }else if(seconds<3600){
        let minutes = (seconds/60).toFixed(0);
        let sec = (seconds %60).toFixed(2);
        return `${minutes}m ${sec}s`
    }else{  
        let hours = seconds/3600;
        let roundedHour =Math.floor(hours);
        let minutes = (hours-roundedHour)*60;
        let roundedMin = Math.floor(minutes);
        let sec = (minutes-roundedMin)*60;
        let roundedSec = Math.floor(sec)
        
        return `${roundedHour}h ${roundedMin}m ${roundedSec}s`
    }
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
                let time = secondToTime(userscore.time);
                row.innerHTML = `
                    <td>${ranking}</td>
                    <td>${userscore.name}</td>
                    <td>${userscore.score}</td>
                    <td>${time}</td>
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
