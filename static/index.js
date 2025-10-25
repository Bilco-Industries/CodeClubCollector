// Get a reference to the input and button
const searchInput = document.getElementById('search-text');
const searchButton = document.getElementById('search-button');

// Read the parameters we used when the page loaded so we can pre-populate the search box with it
const parameters = new URLSearchParams(window.location.search);
searchInput.value = parameters.get('name')

// When the search button is clicked
searchButton.onclick = () => {
    // Update our parameters with the value from the search box
    parameters.set("name", searchInput.value);
    window.location.search = parameters.toString();
}