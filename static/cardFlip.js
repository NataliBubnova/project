$('.card').click(function(e){
    e.preventDefault();
    $(this).toggleClass('flipped');
})