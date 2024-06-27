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

    const userMenuButton = document.getElementById('user-menu-button');
    const userMenu = document.getElementById('user-menu');

    userMenuButton.addEventListener('click', function() {
        userMenu.classList.toggle('hidden');
    });

    document.addEventListener('click', function(event) {
        if (!userMenuButton.contains(event.target) && !userMenu.contains(event.target)) {
            userMenu.classList.add('hidden');
        }
    });
})

 function showEditProfile() {
            document.getElementById('profile').classList.add('hidden');
            document.getElementById('editProfile').classList.remove('hidden');
        }

        // Function to cancel editing and go back to the profile view
        function cancelEditProfile() {
            document.getElementById('editProfile').classList.add('hidden');
            document.getElementById('profile').classList.remove('hidden');
        }

        // Function to load user profile data
        function loadUserProfile() {
            // Example data, replace with actual data retrieval logic
            const userData = {
                profilePic: 'images/profile.jpg',
                username: 'JohnDoe',
                email: 'john.doe@example.com',
                bio: 'This is a short bio about John Doe.',
                posts: [
                    { title: 'Post Title 1', url: 'post1.html' },
                    { title: 'Post Title 2', url: 'post2.html' },
                    { title: 'Post Title 3', url: 'post3.html' }
                ]
            };

            document.getElementById('profilePic').src = userData.profilePic;
            document.getElementById('username').innerText = userData.username;
            document.getElementById('email').innerText = userData.email;
            document.getElementById('bio').innerText = userData.bio;

            const postsContainer = document.getElementById('posts');
            postsContainer.innerHTML = '';
            userData.posts.forEach(post => {
                const postElement = document.createElement('a');
                postElement.href = post.url;
                postElement.className = 'block text-blue-500 hover:underline mb-2';
                postElement.innerText = post.title;
                postsContainer.appendChild(postElement);
            });
        }

        // Call the function to load user profile data when the page loads
        window.onload = loadUserProfile;

// script.js

// Function to load posts data
function loadPosts() {
    // Example data, replace with actual data retrieval logic
    const postsData = [
        { title: 'Post Title 1', img: 'images/post1.jpg', url: 'viewpost.html?id=1' },
        { title: 'Post Title 2', img: 'images/post2.jpg', url: 'viewpost.html?id=2' },
        { title: 'Post Title 3', img: 'images/post3.jpg', url: 'viewpost.html?id=3' }
    ];

    const postsContainer = document.getElementById('posts');
    postsContainer.innerHTML = '';
    postsData.forEach(post => {
        const postElement = document.createElement('div');
        postElement.className = 'bg-white p-4 rounded-lg shadow-lg';
        postElement.innerHTML = `
            <a href="${post.url}">
                <img src="${post.img}" alt="${post.title}" class="w-full h-48 object-cover rounded mb-4">
                <h3 class="text-xl font-bold">${post.title}</h3>
            </a>
        `;
        postsContainer.appendChild(postElement);
    });
}

// script.js

let liked = false; // Track the like status

// Function to load posts data
function loadPosts() {
    const postsData = [
        { title: 'Post Title 1', img: 'images/post1.jpg', url: 'viewpost.html?id=1' },
        { title: 'Post Title 2', img: 'images/post2.jpg', url: 'viewpost.html?id=2' },
        { title: 'Post Title 3', img: 'images/post3.jpg', url: 'viewpost.html?id=3' }
    ];

    const postsContainer = document.getElementById('posts');
    postsContainer.innerHTML = '';
    postsData.forEach(post => {
        const postElement = document.createElement('div');
        postElement.className = 'bg-white p-4 rounded-lg shadow-lg';
        postElement.innerHTML = `
            <a href="${post.url}">
                <img src="${post.img}" alt="${post.title}" class="w-full h-48 object-cover rounded mb-4">
                <h3 class="text-xl font-bold">${post.title}</h3>
            </a>
        `;
        postsContainer.appendChild(postElement);
    });
}

// Function to load post data for viewing
function loadPost() {
    const postData = {
        img: 'images/1.jpg',
        title: 'Post Title 1',
        content: 'This is the content of post 1.'
    };

    document.getElementById('postImg').src = postData.img;
    document.getElementById('postTitle').textContent = postData.title;
    document.getElementById('postContent').textContent = postData.content;

    loadComments();
}

// Function to load comments
function loadComments() {
    const commentsData = [
        { author: 'User 1', text: 'Great post!' },
        { author: 'User 2', text: 'Thanks for sharing.' }
    ];

    const commentsContainer = document.getElementById('comments');
    commentsContainer.innerHTML = '';
    commentsData.forEach(comment => {
        const commentElement = document.createElement('div');
        commentElement.className = 'mb-2';
        commentElement.innerHTML = `
            <p class="text-sm"><strong>${comment.author}</strong>: ${comment.text}</p>
        `;
        commentsContainer.appendChild(commentElement);
    });
}

// Function to handle comment submission
function submitComment() {
    const commentInput = document.getElementById('commentInput');
    const newComment = commentInput.value;
    if (newComment) {
        const commentsContainer = document.getElementById('comments');
        const commentElement = document.createElement('div');
        commentElement.className = 'mb-2';
        commentElement.innerHTML = `
            <p class="text-sm"><strong>You</strong>: ${newComment}</p>
        `;
        commentsContainer.appendChild(commentElement);
        commentInput.value = '';
    }
}

// Function to handle post edit
function editPost() {
    window.location.href = 'editpost.html?id=1';
}

function deletePost() {
            if (confirm('Are you sure you want to delete this post?')) {
                // Handle post deletion logic here
                alert('Post deleted.');
                window.location.href = 'dashboard.html';
            }
        }


// Function to handle like/unlike button
function toggleLike() {
    const likeButton = document.getElementById('likeButton');
    const likeIcon = document.getElementById('likeIcon');
    const likeText = document.getElementById('likeText');

    if (liked) {
        likeIcon.className = 'fas fa-thumbs-up';
        likeText.textContent = 'Like';
        likeButton.classList.replace('bg-red-500', 'bg-blue-500');
        liked = false;
    } else {
        likeIcon.className = 'fas fa-thumbs-down';
        likeText.textContent = 'Unlike';
        likeButton.classList.replace('bg-blue-500', 'bg-red-500');
        liked = true;
    }
}

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

// Event listeners
document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('posts')) {
        loadPosts();
    }
    if (document.getElementById('postImg')) {
        loadPost();
    }
    if (document.getElementById('submitComment')) {
        document.getElementById('submitComment').addEventListener('click', submitComment);
    }
    if (document.getElementById('likeButton')) {
        document.getElementById('likeButton').addEventListener('click', toggleLike);
    }
    fetchTips();
});
