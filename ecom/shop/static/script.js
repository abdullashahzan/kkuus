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
