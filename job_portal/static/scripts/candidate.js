
function updateSlider(value) {
    const slider = document.getElementById('radiusSlider');
    const max = slider.max;
    const percentage = (value / max) * 100;

    // Update the gradient background to fill up to the current slider value
    slider.style.background = `linear-gradient(to right, #007bff ${percentage}%, #ddd ${percentage}%)`;

    // Update the displayed radius value
    document.getElementById('radiusValue').textContent = `${value} miles`;
}

document.addEventListener('DOMContentLoaded', (event) => {
    const slider = document.getElementById('slider');
    slider.addEventListener('input', function () {
        console.log('Slider value:', this.value); // Log current value to console
    });
});

document.getElementById("showMoreBtn").addEventListener("click", function () {
    document.getElementById("showMoreBtn").style.display = "none";
    document.getElementById("showLessBtn").style.display = "inline";
    // Add your logic here to show more content
});

document.getElementById("showLessBtn").addEventListener("click", function () {
    document.getElementById("showLessBtn").style.display = "none";
    document.getElementById("showMoreBtn").style.display = "inline";
    // Add your logic here to show less content
});

document.getElementById("viewProfileButton").addEventListener("click", function () {
    this.classList.toggle("clicked");
});
document.getElementById('radiusSlider').addEventListener('input', function () {
    document.getElementById('radiusValue').textContent = this.value + ' miles';
});


    function toggleBookmark(element) {
        // Add the 'loading' class to show the spinner
        element.classList.add('loading');

        // Simulate an asynchronous operation (e.g., bookmarking via an API call)
        setTimeout(() => {
            // Remove the loading state after a delay (simulate a successful API response)
            element.classList.remove('loading');
            alert("Please login as Employer to add shortlist");
        }, 2000); // Simulate 2 seconds delay
    }

