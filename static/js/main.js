document.addEventListener('DOMContentLoaded', () => {
    // Initializing the modules
    if (document.getElementById('changing-text')) {
        const script = document.createElement('script');
        script.src = 'textchange.js';
        document.body.appendChild(script);
    }


    if (document.getElementById('profile')) {
        const script = document.createElement('script');
        script.src = 'profile.js';
        document.body.appendChild(script);
    }

    if (document.getElementById('posts')) {
        const script = document.createElement('script');
        script.src = 'writingzone.js';
        document.body.appendChild(script);
    }

    if (document.getElementById('postImg')) {
        const script = document.createElement('script');
        script.src = 'writingzone.js';
        document.body.appendChild(script);
    }

    if (document.getElementById('likeButton')) {
        const script = document.createElement('script');
        script.src = 'writingzone.js';
        document.body.appendChild(script);
    }

    const scriptTips = document.createElement('script');
    scriptTips.src = 'tips.js';
    document.body.appendChild(scriptTips);

    const scriptResponses = document.createElement('script');
    scriptResponses.src = 'challenges.js';
    document.body.appendChild(scriptResponses);
});
