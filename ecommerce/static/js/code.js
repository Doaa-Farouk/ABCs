// Hamburger Menu 
hamburger = document.getElementById('hamburger');
closeHamMenu = document.getElementById('close');
hamburgerMenu = document.getElementsByClassName('categories_ul');
hamburger.onclick = ()=> hamburgerMenu[0].classList.add('shown');
closeHamMenu.onclick = ()=> hamburgerMenu[0].classList.remove('shown');

// search label
searchCategoriesLabel = document.getElementById('search_categories_label');
searchCategoriesinput = document.getElementById('search_categories');
function check() {
    if(searchCategoriesinput.value != '') {
        searchCategoriesLabel.children[0].classList.replace("fa-search", "fa-times")
    }
    else {
        searchCategoriesLabel.children[0].classList.replace("fa-times", "fa-search")
    }
}
searchCategoriesinput.oninput = function(){
    check();
}
searchCategoriesinput.onclick = function(){
    check();
    searchCategoriesLabel.onclick = ()=> searchCategoriesinput.value = '';
}

$(document).ready(function(){
    $("#hero .owl-carousel").owlCarousel();
});

$('#hero .owl-carousel').owlCarousel({
    rtl:true,
    responsive:{
        0:{
            items:1
        }
    },
    autoplay:true,
    autoplayTimeout:1500,
    autoplayHoverPause:true,
    loop: true
})

$('.owl-carousel.second-slider').owlCarousel({
    margin: 10,
    responsive:{
        0:{
            items: 2
        },

        576:{
            items: 4
        },

        768:{
            items: 6
        }
    },
    autoplay: true,
    autoplayTimeout:1500,
    autoplayHoverPause:true,
    loop: true,
    // rtl: true
})


$(document).ready(function(){
    $(".prodcut-page-container > .img").owlCarousel();
});


$('.prodcut-page-container > .img').owlCarousel({
    responsive:{
        0:{
            items: 1
        },
    },
    rtl: true,
    loop: true,
})


// Start Categories;

// activiting categories
const categoriesFilters = Array.from(document.querySelectorAll('#filters .categories_filters img'));
const products = Array.from(document.querySelectorAll('.procucts_grid .product'));
let activeCtg;
categoriesFilters.forEach((categoryBtn,_,array) => {
    categoryBtn.onclick = (e)=>{
        array.forEach(element => element.classList.remove('active'));
        e.target.classList.add('active');
        activeCtg = e.target.dataset.categoryName;
        // filtering the objects according to category;
        let visibleProducts = products.filter((product) => product.dataset.category == activeCtg);
        // hiding and showing the objects according to the filtertion;
        products.forEach((product) => {
            if(activeCtg != 'all') product.style.display = 'none';
            else {product.style.display = 'flex'}
        });
        visibleProducts.forEach((visibleProduct) => visibleProduct.style.display = 'flex');
    };
});