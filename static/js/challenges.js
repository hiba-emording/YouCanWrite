function fetchAndDisplayResponses() {
    fetch('/challenges/<challenge_id>/responses')
        .then(response => response.json())
        .then(responses => {
            const responsesList = document.getElementById('responsesList');
            responsesList.innerHTML = '';
            responses.forEach(response => {
                const li = document.createElement('li');
                li.innerHTML = `
                    ${response.text}
                    <button class="editResponse" data-id="${response.id}">Edit</button>
                    <button class="deleteResponse" data-id="${response.id}">Delete</button>
                `;
                responsesList.appendChild(li);
            });
        })
        .catch(error => console.error('Error fetching responses:', error));
}

function editResponse(id) {
    const newText = prompt('Edit your response:');
    if (newText) {
        fetch(`/challenges/<challenge_id>/responses/<response_id>/${id}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: newText })
        })
        .then(response => response.json())
        .then(() => {
            fetchAndDisplayResponses();
        });
    }
}

function deleteResponse(id) {
    if (confirm('Are you sure you want to delete this response?')) {
        fetch(`/challenges/<challenge_id>/responses/<response_id>/${id}`, { method: 'DELETE' })
        .then(response => response.json())
        .then(() => {
            fetchAndDisplayResponses();
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    fetchAndDisplayResponses();
    document.getElementById('submitResponseForm').addEventListener('submit', function(e) {
        e.preventDefault();
        const responseText = document.getElementById('responseText').value;
        fetch('/challenges/<challenge_id>/responses', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ response: responseText }),
        })
        .then(response => response.json())
        .then(data => {
            alert('Response submitted successfully!');
            document.getElementById('responseText').value = '';
        })
        .catch(error => {
            console.error('Error submitting response:', error);
            alert('Failed to submit response.');
        });
    });

    document.getElementById('responsesSection').addEventListener('click', function(e) {
        if (e.target.className === 'editResponse') {
            editResponse(e.target.dataset.id);
        } else if (e.target.className === 'deleteResponse') {
            deleteResponse(e.target.dataset.id);
        }
    });
});

