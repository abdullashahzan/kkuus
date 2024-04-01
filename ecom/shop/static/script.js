function openModalParameter(item_id) {
    document.getElementById('myModal').style.display = 'block';
    var item_id = item_id.trim();
    console.log(item_id);
    document.querySelector('.redirect_link').action = `/myShop/renew/${item_id}`;
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
    let cards = document.querySelector('.card')
    cards.style.filter = "blur(2px)";
}

function openModal() {
    document.getElementById('myModal').style.display = 'block';
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
    let cards = document.querySelector('.card')
    cards.style.filter = "blur(2px)";
}

function closeModal() {
    document.getElementById('myModal').style.display = 'none';
    let cards = document.querySelector('.card')
    cards.style.filter = "blur(0)";
}

let lastScrollTop = 0;
const hiddenDiv = document.getElementById("hiddenDiv");

window.addEventListener("scroll", function () {
    let currentScroll = window.scrollY;
    if (currentScroll > lastScrollTop) {
        // Scroll down
        hiddenDiv.classList.remove("animate__slideInUp");
        hiddenDiv.classList.add("animate__slideOutDown");
        hiddenDiv.addEventListener("animationend", function () {
            hiddenDiv.classList.remove("d-none");
            hiddenDiv.classList.add("d-block");
        });
    } else {
        // Scroll up
        hiddenDiv.classList.remove("animate__slideOutDown");
        hiddenDiv.classList.add("animate__slideInUp");
    }
    lastScrollTop = currentScroll;
});

document.addEventListener("DOMContentLoaded", function () {
    var forms = document.querySelectorAll("form");

    forms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            var submitButton = form.querySelector("button[type='submit']");
            submitButton.disabled = true;

            // Optional: Display a loading indicator
            submitButton.innerHTML = "Please wait...";

            // Prevent the default form submission behavior
            event.preventDefault();

            // Manually submit the form after a short delay (optional)
            setTimeout(function () {
                form.submit();
            }, 200); // Adjust the delay as needed
        });
    });
});

window.addEventListener('scroll', revealCards);

function revealCards() {
    const cards = document.querySelectorAll('.item-card');
    
    cards.forEach(card => {
        const cardTop = card.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
        
        if (cardTop < windowHeight * 0.9) {
            card.classList.add('visible');
        } else {
            card.classList.remove('visible');
        }
    });
}

