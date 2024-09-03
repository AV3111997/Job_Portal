
document.getElementById('radiusSlider').addEventListener('input', function() {
    document.getElementById('radiusValue').textContent = this.value + ' miles';
});

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

