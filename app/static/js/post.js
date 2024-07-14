

// Function to handle post edit visibility
function toggleEdit(show) {
    const postDisplay = document.getElementById('postDisplay');
    const postEditForm = document.getElementById('postEditForm');
    if (show) {
        postDisplay.style.display = 'none';
        postEditForm.style.display = 'block';
    } else {
        postDisplay.style.display = 'block';
        postEditForm.style.display = 'none';
    }
}



// Function to handle updating post image preview
function updatePostImage(url) {
    const postImage = document.getElementById('postImage');
    postImage.src = url;
    postImage.style.display = 'block';
}

// Function to handle post deletion
function deletePost(postId) {
    if (confirm('Are you sure you want to delete this post?')) {
        fetch(`/posts/${postId}`, {
            method: 'DELETE',
        })
        .then(response => response.json())
        .then(data => {
            window.location.href = '/writing_zone'; // Redirect to writing zone after deletion
        })
        .catch(error => console.error('Error:', error));
    }
}


// Function to handle comment submission
function submitComment(postId) {
    const commentInput = document.getElementById('commentInput').value;
    fetch(`/posts/${postId}/comments`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ content: commentInput }),
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Failed to submit comment');
        }
    })
    .then(data => {
        // Reload the page to show the submitted comment
        window.location.reload();
    })
    .catch(error => console.error('Error:', error));
}

// Function to handle editing a comment
function toggleCommentEdit(commentId, show) {
    const commentEditForm = document.getElementById(`commentEditForm-${commentId}`);
    const commentDisplay = document.getElementById(`commentDisplay-${commentId}`);
    if (show) {
        commentDisplay.style.display = 'none';
        commentEditForm.style.display = 'block';
    } else {
        commentDisplay.style.display = 'block';
        commentEditForm.style.display = 'none';
    }
}

function editComment(commentId) {
    toggleCommentEdit(commentId, true);
}

function updateComment(commentId) {
    const content = document.getElementById(`commentEditInput-${commentId}`).value;
    fetch(`/comments/${commentId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ content: content }),
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Failed to update comment');
        }
    })
    .then(data => {
        if (data.success) {
          
            const commentContent = document.getElementById(`commentDisplay-${commentId}`);
            commentContent.textContent = data.content;
            toggleCommentEdit(commentId, false);
            window.location.reload();
        } else {
            console.error('Failed to update comment:', data.message);
        }
    })
    .catch(error => console.error('Error:', error));
}



// Function to handle comment deletion
function deleteComment(commentId, postId) {
    if (confirm('Are you sure you want to delete this comment?')) {
        fetch(`/comments/${commentId}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => {
            if (response.ok) {
                window.location.href = `/posts/${postId}`; // Redirect to the post after comment deletion
            } else {
                return response.json().then(data => {
                    throw new Error(data.message || 'Failed to delete comment');
                });
            }
        })
        .catch(error => console.error('Error:', error));
    }
}

document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.save-comment').forEach(button => {
        button.addEventListener('click', function () {
            const commentId = this.dataset.id;
            const content = document.getElementById(`comment-content-${commentId}`).value;

            fetch(`/comments/${commentId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ content: content })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Update the comment display
                    const commentDisplay = document.getElementById(`comment-display-${commentId}`);
                    commentDisplay.innerText = content;
                    
                    // Toggle edit/save buttons visibility
                    document.getElementById(`edit-comment-${commentId}`).style.display = 'inline';
                    document.getElementById(`save-comment-${commentId}`).style.display = 'none';

                    // Hide the text area
                    document.getElementById(`comment-content-${commentId}`).style.display = 'none';
                } else {
                    alert('Failed to update comment.');
                }
            });
        });
    });
});


    document.addEventListener('DOMContentLoaded', (event) => {
        document.querySelectorAll('.like-btn').forEach(button => {
            button.addEventListener('click', function() {
                const postId = this.closest('[data-post-id]').getAttribute('data-post-id');
                fetch(`/posts/${postId}/like`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': '{{ csrf_token() }}'  // Include CSRF token if needed
                    }
                })
                .then(response => response.json())
                .then(data => {
                    if (data.liked) {
                        this.classList.add('liked');  // Optionally add a class to show the button as liked
                    } else {
                        this.classList.remove('liked');  // Optionally remove the class to show the button as unliked
                    }
                    this.querySelector('.like-count').textContent = data.likes_count;

                    // Update the list of users who liked the post
                    const likedUsersList = this.closest('.post').querySelector('.liked-users');
                    likedUsersList.innerHTML = '';
                    data.liked_users.forEach(user => {
                        const userItem = document.createElement('li');
                        userItem.textContent = user.username;
                        likedUsersList.appendChild(userItem);
                    });
                })
                .catch(error => console.error('Error:', error));
            });
        });
    });



