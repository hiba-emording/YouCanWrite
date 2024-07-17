// Handle close btn for flash msg
document.addEventListener("DOMContentLoaded", function() {
    const closeButtons = document.querySelectorAll('.close-button');
  
    closeButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            const flashMessage = this.parentElement;
            flashMessage.style.display = 'none';
            event.stopPropagation();
        });
    });

    // Auto-close after a few seconds
    setTimeout(function() {
        let flashMessages = document.querySelectorAll('.flash-message');
        flashMessages.forEach(function(message) {
            message.style.display = 'none';
        });
    }, 3000);
});
