$(document).ready(function() {
    $('.menu, .overlay').click(function () {
        $('.menu').toggleClass('clicked');

        $('#nav').toggleClass('show');

    });    
});
