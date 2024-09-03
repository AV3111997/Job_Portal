
document.getElementById('radiusSlider').addEventListener('input', function() {
    document.getElementById('radiusValue').textContent = this.value + ' miles';
});

function getCsrfToken() {
    const tokenElement = document.querySelector('meta[name="csrf-token"]');
    const token = tokenElement ? tokenElement.getAttribute('content') : '';
    console.log('CSRF Token:', token); // Log CSRF token value
    console.log('CSRF Token Length:', token.length); // Log CSRF token length
    return token;
}

function saveJob(element) {
    const url = element.href;
    const csrfToken = getCsrfToken(); // Use dynamically fetched CSRF token

    console.log('Request URL:', url); // Log request URL
    console.log('CSRF Token:', csrfToken); // Log CSRF token used in the request

    fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
            'X-Requested-With': 'XMLHttpRequest',
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log('Response Data:', data); // Log response data
        if (data.status === 'success') {
            alert(data.message);
            changeIcon(element);
        } else if (data.status === 'exists') {
            alert(data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error); // Log errors
    });
}

function changeIcon(button) {
    var icon = button.querySelector('i');

    if (icon.classList.contains('fa-regular')) {
        icon.classList.remove('fa-regular');
        icon.classList.add('fa-solid');
    } else {
        icon.classList.remove('fa-solid');
        icon.classList.add('fa-regular');
    }
}

// Log the CSRF token on page load
console.log('CSRF Token on Page Load:', getCsrfToken());

