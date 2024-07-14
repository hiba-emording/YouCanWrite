function toggleEdit(editMode) {
    const display = document.getElementById('profileDisplay');
    const editForm = document.getElementById('profileEditForm');
    if (editMode) {
        display.style.display = 'none';
        editForm.style.display = '';
    } else {
        display.style.display = '';
        editForm.style.display = 'none';
    }
}

function updateProfilePicture(url) {
    document.getElementById('profile-picture').src = url;
}