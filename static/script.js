function hideAll() {
    $('.navmenu-element').each(function () {
        $(this).removeClass('active')
    });
    $('.organic-class').each(function () {
        $(this).hide();
    });
}

hideAll();

$(document).ready(function(){
    $('.navmenu-element').click(function(){
        hideAll();
         $(this).addClass('active');
        $('#organic-class'+$(this).attr('id')).show();
    });
});