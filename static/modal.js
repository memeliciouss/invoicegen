// Variable to store the form that needs to be submitted
let formToSubmit = null;

function showConfirmModal(form) {
    // We store the form instance here
    formToSubmit = form;
    const modal = document.getElementById('confirmModal');
    modal.style.display = 'flex';
}

function hideConfirmModal() {
    // Clear the stored form when the modal is hidden
    formToSubmit = null;
    const modal = document.getElementById('confirmModal');
    modal.style.display = 'none';
}

// New function to submit the form
function submitModalForm() {
    if (formToSubmit) {
        formToSubmit.submit();
    }
}