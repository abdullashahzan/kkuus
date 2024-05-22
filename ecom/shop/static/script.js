function openModalParameter(item_id) {
    document.getElementById('myModal').style.display = 'block';
    var item_id = item_id.trim();
    document.querySelector('.redirect_link').action = `/myShop/renew/`;
    document.querySelector('.item_id').value = item_id;
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


document.addEventListener("DOMContentLoaded", function () {
    var forms = document.querySelectorAll("form");

    forms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            var submitButton = form.querySelector("button[type='submit']");
            submitButton.disabled = true;
            event.preventDefault();
            setTimeout(function () {
                form.submit();
            }, 200); // Adjust the delay as needed
        });
    });
});

var scroll_left = document.querySelectorAll(".scroll-left");
var scroll_right = document.querySelectorAll(".scroll-right");
var horizontal_scroll_div = document.querySelectorAll(".horizontal-scroll-div");

function scrollRight(item) {
    var scroll_pos = item.scrollLeft + 500;
    item.scrollTo({
        left: scroll_pos,
        behavior: 'smooth'
    })
}

function scrollLeft(item) {
    var scroll_pos = item.scrollLeft - 300;
    item.scrollTo({
        left: scroll_pos,
        behavior: 'smooth'
    })
}

function scrollerRight(item){
    item.addEventListener("click", ()=>{
        horizontal_scroll_div.forEach(scrollRight);
    })
}

function scrollerLeft(item){
    item.addEventListener("click", ()=>{
        horizontal_scroll_div.forEach(scrollLeft);
    })
}

scroll_right.forEach(scrollerRight)
scroll_left.forEach(scrollerLeft)

var imageViewer = document.querySelector(".imageViewer");
imageViewer.addEventListener('click', ()=>{
    imageViewer.classList.remove('d-flex');
    imageViewer.classList.add('d-none');
})

var openImageViewer = document.querySelector(".openImageViewer");
openImageViewer.addEventListener("click", ()=>{
    imageViewer.classList.remove('d-none');
    imageViewer.classList.add('d-flex');
})

