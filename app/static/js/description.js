// Function to show a description element
function showDescription(descId) {
    document.getElementById(descId).style.display = 'block';
}

// Function to hide a description element
function hideDescription(descId) {
    document.getElementById(descId).style.display = 'none';
}

// Function for typing animation
const textElement = document.querySelector('.typing-animation');
const text = "This website is still under construction, but hey, at least it's under construction! (We're making progress... slowly. Even developers get writer's block, believe it or not! Coding can hit a wall just like writing text.";
let index = 0;

const typeWriter = () => {
  if (index < text.length) {
    textElement.textContent += text.charAt(index);
    index++;
    setTimeout(typeWriter, 50);
  } else {
    setTimeout(eraseText, 5000);
  }
};

const eraseText = () => {
  const eraseInterval = setInterval(() => {
    if (textElement.textContent.length > 0) {
      textElement.textContent = textElement.textContent.substring(0, textElement.textContent.length - 1);
    } else {
      clearInterval(eraseInterval);
      index = 0;
      setTimeout(typeWriter, 500);
    }
  }, 30);
};

typeWriter();


