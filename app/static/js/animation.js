const textElement = document.querySelector('.typing-animation');
const textList = [
 "Feeling writer's block? Don't worry, even squirrels forget where they bury their nuts sometimes. Take a break and come back inspired!",
 "Did you know Stephen King used to write 2,000 words a day, no matter what? Talk about dedication! How many words will your post unleash today?",
 "Mark Twain once said, 'The difference between the almost right word and the right word is the difference between the lightning bug and the lightning.' Choose your words wisely, and your post will truly shine!",
 "Proofreading? More like 'procrastinating by finding typos nobody else will notice'. We've all been there. Just hit publish already!",
 "Feeling intimidated by the blank page? Think of it as your personal canvas - unleash your creativity and paint a masterpiece with words!",
 "Agatha Christie, queen of the whodunnit, used to write in ten-minute bursts with a timer! Maybe that's the secret to her killer plot twists. Will your post keep readers on the edge of their seats?",
 "J.K. Rowling got rejected by 12 publishers before Harry Potter. Now it's one of the best-selling books of all time! Don't be discouraged by setbacks, keep writing your story!",
 "Did you know Ernest Hemingway once wrote a whole story in just six words? Talk about keeping it concise! (Yeah, I know what you're thinking... don't insult this website with a post shorter than a grocery list. Time to unleash your inner wordsmith and craft something worthy of this digital canvas!)"
];

let index = 0;
let currentIndex = 0;

function shuffle(array) {
let currentIndex = array.length, temporaryValue, randomIndex;
while (0 !== currentIndex) {
randomIndex = Math.floor(Math.random() * currentIndex);
currentIndex -= 1;
temporaryValue = array[currentIndex];
array[currentIndex] = array[randomIndex];
array[randomIndex] = temporaryValue;
}
return array;
}

let shuffledTextList = shuffle(textList.slice());

const typeWriter = () => {
if (currentIndex < shuffledTextList.length) {
const currentText = shuffledTextList[currentIndex];
if (index < currentText.length) {
textElement.textContent += currentText.charAt(index);
index++;
setTimeout(typeWriter, 50);
} else {
setTimeout(eraseText, 5000);
index = 0;
currentIndex++;
}
} else {
shuffledTextList = shuffle(textList.slice());
currentIndex = 0;
setTimeout(typeWriter, 5000);
}
};

const eraseText = () => {
const eraseInterval = setInterval(() => {
if (textElement.textContent.length > 0) {
textElement.textContent = textElement.textContent.substring(0, textElement.textContent.length - 1);
} else {
clearInterval(eraseInterval);
typeWriter();
}
}, 15);
};

typeWriter();
