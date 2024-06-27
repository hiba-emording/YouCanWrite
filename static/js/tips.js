function fetchTips() {
    fetch('/api/tips')
        .then(response => response.json())
        .then(data => {
            const tipsContainer = document.getElementById('tipsContainer');
            tipsContainer.innerHTML = '';
            data.forEach(tip => {
                const tipElement = document.createElement('div');
                tipElement.classList.add('mb-4');
                tipElement.innerHTML = `
                    <p class="text-lg text-gray-700">Content: ${tip.content}</p>
                    <p class="text-sm text-gray-500">Date: ${new Date(tip.date).toLocaleDateString()}</p>
                `;
                tipsContainer.appendChild(tipElement);
            });
        })
        .catch(error => {
            console.error('Error fetching tips:', error);
            document.getElementById('tipsContainer').innerHTML = '<p class="text-lg text-red-500">Failed to load tips.</p>';
        });
}

function fetchDailyTip() {
    fetch('/api/tips/daily')
        .then(response => response.json())
        .then(data => {
            document.getElementById('tipContent').textContent = data.content;
        })
        .catch(error => {
            console.error('Error fetching daily tip:', error);
            document.getElementById('tipContent').textContent = 'Failed to load daily tip.';
        });
}

document.addEventListener('DOMContentLoaded', () => {
    fetchTips();
    fetchDailyTip();
});

