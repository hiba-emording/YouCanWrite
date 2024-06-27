let liked = false;

// Function to load posts data
function loadPosts() {
    const postsData = [
        { title: 'Post Title 1', img: 'images/1.jpg', url: 'post.html?id=1' },
        { title: 'Post Title 2', img: 'images/1.jpg', url: 'post.html?id=2' },
        { title: 'Post Title 3', img: 'images/1.jpg', url: 'post.html?id=3' }
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
        img: 'images/post1.jpg',
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

// Function to handle post delete
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
});

