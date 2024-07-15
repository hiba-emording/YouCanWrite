// Function to toggle between profile display and edit form
function toggleEdit(editMode) {
    const display = document.getElementById('profileDisplay');
    const editForm = document.getElementById('profileEditForm');
    if (editMode) {
        // If editMode is true, hide profile display and show edit form
        display.style.display = 'none';
        editForm.style.display = '';
    } else {
        // If editMode is false, show profile display and hide edit form
        display.style.display = '';
        editForm.style.display = 'none';
    }
}

function updateProfilePicture(url) {
    document.getElementById('profile-picture').src = url;
}