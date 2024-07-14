document.addEventListener('DOMContentLoaded', function() {
    const changingTextElement = document.getElementById('changing-text');
    const texts = [
        "Join our writing community and get your daily dose of writing inspiration and feedback.",
        "Share your stories and get constructive feedback.",
        "Challenge yourself with daily writing prompts."
    ];
    let currentIndex = 0;

    function changeText() {
        currentIndex = (currentIndex + 1) % texts.length;
        changingTextElement.textContent = texts[currentIndex];
    }

    function fadeOutAndChangeText() {
        changingTextElement.classList.add('fade-out');
        changingTextElement.classList.remove('fade-in');
        changingTextElement.addEventListener('animationend', function() {
            changeText();
            fadeInText();
        }, { once: true });
    }

    function fadeInText() {
        changingTextElement.classList.add('fade-in');
        changingTextElement.classList.remove('fade-out');
        changingTextElement.addEventListener('animationend', function() {
            setTimeout(fadeOutAndChangeText, 2000);
        }, { once: true });
    }

    setTimeout(fadeOutAndChangeText, 2000);
});
