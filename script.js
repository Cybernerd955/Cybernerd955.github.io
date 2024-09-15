function fetchLastLine() {
    fetch('data.txt')
        .then(response => response.text())
        .then(data => {
            // Split the file content by lines
            const lines = data.trim().split('\n');
            
            // Get the last line
            const lastLine = lines[lines.length - 1];
            
            // Display the last line in the output
            document.getElementById('output').textContent = `Last Line: ${lastLine}`;
        })
        .catch(error => {
            console.error('Error reading file:', error);
        });
}

// Set interval to fetch data every 1 second (1000 milliseconds)
setInterval(fetchLastLine, 1000);
