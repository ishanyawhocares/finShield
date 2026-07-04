document.addEventListener('DOMContentLoaded', function() {
    // 1. Get the URL of the current tab
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        let currentUrl = tabs[0].url;
        document.getElementById('url-display').innerText = currentUrl;

        // 2. Send URL to Python Backend
        fetch('http://127.0.0.1:5000/scan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: currentUrl })
        })                                     
        .then(response => response.json())
        .then(data => {
            // 3. Update UI based on response
            const box = document.getElementById('result-box');
            box.innerText = data.status + "\n" + data.message;
            box.style.backgroundColor = data.color;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('result-box').innerText = "Server Error. Is Python running?";
            document.getElementById('result-box').style.backgroundColor = "#333";
        });
    });
});