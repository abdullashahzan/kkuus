function openModalParameter(item_id) {
    document.getElementById('myModal').style.display = 'block';
    var item_id = item_id.trim();
    console.log(item_id);
    document.querySelector('.redirect_link').action = `/myShop/renew/${item_id}`;
}

function openModal(){
    document.getElementById('myModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('myModal').style.display = 'none';
}

document.addEventListener("DOMContentLoaded", function() {
    var forms = document.querySelectorAll("form");

    forms.forEach(function(form) {
        form.addEventListener("submit", function(event) {
            var submitButton = form.querySelector("button[type='submit']");
            submitButton.disabled = true;
            
            // Optional: Display a loading indicator
            submitButton.innerHTML = "Please wait...";
            
            // Prevent the default form submission behavior
            event.preventDefault();
            
            // Manually submit the form after a short delay (optional)
            setTimeout(function() {
                form.submit();
            }, 200); // Adjust the delay as needed
        });
    });
});