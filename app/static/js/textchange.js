// Function to cycle through changing text on the homepage
document.addEventListener('DOMContentLoaded', function() {
    const changingTextElement = document.getElementById('changing-text');
    const texts = [
        "Join our writing community and get your daily dose of writing inspiration and feedback.",
        "Share your stories and get constructive feedback.",
        "Challenge yourself with daily writing prompts.",
        "Explore daily writing tips to improve your skills."
    ];
    let currentIndex = 0;

    function changeText() {
        // Increment the current index to switch to the next text
        currentIndex = (currentIndex + 1) % texts.length;
        changingTextElement.textContent = texts[currentIndex];
    }

    function fadeOutAndChangeText() {
        // Add fade-out animation class and remove fade-in class
        changingTextElement.classList.add('fade-out');
        changingTextElement.classList.remove('fade-in');
        changingTextElement.addEventListener('animationend', function() {
            // Once fade-out animation ends, change text and fade it in
            changeText();
            fadeInText();
        }, { once: true });
    }

    function fadeInText() {
        // Add fade-in animation class and remove fade-out class
        changingTextElement.classList.add('fade-in');
        changingTextElement.classList.remove('fade-out');
        changingTextElement.addEventListener('animationend', function() {
            // Set timeout to start fade-out and change text process after 2 seconds
            setTimeout(fadeOutAndChangeText, 2000);
        }, { once: true });
    }
    // Start the cycle of fading out and changing text after 2 seconds of page load
    setTimeout(fadeOutAndChangeText, 2000);
});
