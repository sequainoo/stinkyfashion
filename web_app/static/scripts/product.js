document.addEventListener('DOMContentLoaded', function() {
    // Get all thumbnail images
    const thumbnails = document.querySelectorAll('.thumbnail-images img');

    // Get the main product image
    const mainImage = document.querySelector('.main-image img');

    // Loop through each thumbnail image
    thumbnails.forEach(thumbnail => {
        // Add click event listener to each thumbnail
        thumbnail.addEventListener('click', function() {
            // Get the src attribute of the clicked thumbnail
            const newImageSrc = thumbnail.src;

            // Update the src attribute of the main product image
            mainImage.src = newImageSrc;

            // Apply a visual indication (e.g., border or opacity) to the selected thumbnail
            // You can customize this to match your desired styling
            removeBorderFromThumbnails();
            thumbnail.style.border = '2px solid #007bff'; // Example: Highlight selected thumbnail
        });
    });

    // Function to remove border from all thumbnails
    function removeBorderFromThumbnails() {
        thumbnails.forEach(thumbnail => {
            thumbnail.style.border = 'none';
        });
    }
});
