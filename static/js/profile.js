function showEditProfile() {
    document.getElementById('profile').classList.add('hidden');
    document.getElementById('editProfile').classList.remove('hidden');
}

function cancelEditProfile() {
    document.getElementById('editProfile').classList.add('hidden');
    document.getElementById('profile').classList.remove('hidden');
}

function loadUserProfile() {
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

window.onload = loadUserProfile;
