// Portfolio show more functionality
document.getElementById('toggleMore').addEventListener('click', function() {
    var extraImages = document.getElementById('extraImages');

    // Check the current display style of the extra images section
    if (extraImages.style.display === "none" || extraImages.style.display === "") {
        extraImages.style.display = "flex"; // Show the hidden images by setting the display to flex
        this.style.display = "none"; // Hide the "+4" button after it is clicked
    }
});