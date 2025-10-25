// Store the url of the current page in a variable
const currentUrl = window.location.origin;

// When the loading state changes
document.onreadystatechange = () => {

    // If we have finished loading
    if (document.readyState === 'complete') {

        // Get all the elements on the page that have a class="replaceUrl"
        document.querySelectorAll('.replaceUrl')
            // For each element that has the replaceUrl class
            .forEach((elementWithReplaceUrlClass) => {

                // Update the text and replace all instances of {url} with the url of the current page 
                elementWithReplaceUrlClass.innerText = elementWithReplaceUrlClass.innerText
                    .replace('{url}', currentUrl)
            })
    }
};