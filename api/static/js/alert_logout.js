document.getElementById('logout-button').addEventListener('click', function(event) {
    event.preventDefault();
    Swal.fire({
        title: 'Are you sure?',
        text: "You will lose your current session",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, log out',
        cancelButtonText: 'Cancel'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = "/logout/";
        }
    });
});