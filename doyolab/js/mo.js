document.addEventListener("DOMContentLoaded", function() {
    // Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll('nav ul li a');
    navLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            window.scrollTo({
                top: targetElement.offsetTop,
                behavior: 'smooth'
            });
        });
    });

    // Example reservation button click event
    const reservationButton = document.querySelector('.hero .btn-cta');
    reservationButton.addEventListener('click', function() {
        alert('予約機能は現在開発中です。しばらくお待ちください。');
    });
});

$(".openbtn").click(function () {
    $(this).toggleClass('active');
});