function updateUserscoresTable() {
    // Make an AJAX request to the Flask endpoint to get the updated enrollees data
    fetch("/EnrolleesJSON")
        .then(response => response.json())
        .then(data => {
            // Clear the current table content
            document.getElementById("userscores-table").innerHTML = "";

            // Update the table with the new data
            data.forEach(userscore => {
                const row = document.createElement("tr");
                row.innerHTML = `
                    
                    <td>${userscore.name}</td>
                    <td>${userscore.score}</td>
                    <td>${userscore.time}</td>
                    <td>${userscore.date}</td>
                    <!--<td>
                        <form action="/Deregister" method="post">
                            <input name="id" type="hidden" value="${userscore.id}">
                            <input type="submit" value="Deregister">
                        </form>
                        --></td>
                `;
                document.getElementById("userscores-table").appendChild(row);
            });
        });
}

// Update the table initially and then periodically (e.g., every 5 seconds)
updateUserscoresTable();
setInterval(updateUserscoresTable, 5000); // Adjust the interval as needed