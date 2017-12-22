$(function() {
    init_size();
    init_img();
    $(window).resize(function() {
        init_size();
    });
});

function init_size() {

}

function init_img() {
    set_icon('.customer_icon', 'contact_us_img_1.jpg');
    set_icon('.marketing_icon', 'contact_us_img_2.jpg');
    set_icon('.opportunity_icon', 'contact_us_img_3.jpg');
}

function set_icon(icon_type, icon_file) {
    $(icon_type).css({ 'background': getImgUrl(icon_file, 'center', 'no-repeat'), 'background-size': 'cover' });
}