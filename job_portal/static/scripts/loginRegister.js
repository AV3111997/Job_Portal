
function getCookie(name) {
    let cookieValue = null
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';')
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim()
            if (cookie.substring(0, name.length + 1) === name + '=') {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                break
            }
        }
    }
    return cookieValue
}

  


function submitForm(formId, url, error_id) {
    const form = document.getElementById(formId)
    form.addEventListener('submit', function (event) {
        event.preventDefault()
        const formData = new FormData(form) // Collect form data
        const csrfToken = getCookie('csrftoken') // Get CSRF token from the cookie
        const div = document.getElementById(error_id)

        div.classList.add('d-none')

        fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken, // Include CSRF token in the request headers
                'X-Requested-With': 'XMLHttpRequest' // Optional: Indicate that this is an AJAX request
            },
            body: formData
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.success) {
                    div.classList.remove('d-none')
                    div.classList.add('text-primary-emphasis')
                    div.classList.add('bg-primary-subtle')
                    div.textContent = data.message
                    if (data.redirect_url) { 
                        window.location.href = data.redirect_url
                    }

                } else {
                    div.classList.remove('d-none')
                    div.classList.add('bg-warning-subtle')
                    div.classList.add('text-warning-emphasis')
                    div.textContent = data.error
                }
            })
            .catch((error) => {
                console.error('Error:', error)
            })
    })
}

// Example usage
