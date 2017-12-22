$(function() {
    init_size();
    init_img();
    $(window).resize(function() {
        init_size();
    });
});

function init_size() {
    $('.img_container').height($(window).height());
    $('.bottom_img_container').height($(window).height() * 2);
    $('.card_div_img').height($('.card_div_img').width());
    $('.show_video_bg').height($('.show_video_bg').width()/1.38);
}

function init_img() {
    if ($(document).width() <= 768) {
        set_background_image('.img_container_1', 'product_img_1.jpg');
        set_background_image('.img_container_1 .show_video_bg', 'product_video_1.png');
        set_background_image('.img_container_2', 'home_img_2.jpg');
        set_background_image('.img_container_3', 'product_img_3.jpg');
        set_background_image('.img_container_4', 'product_img_4.jpg');
        set_background_image('.bottom_img_container', 'product_img_5_m.jpg');
    } else {
        set_background_image('.img_container_1', 'product_img_1.jpg');
        set_background_image('.img_container_1 .show_video_bg', 'product_video_1.png');
        set_background_image('.img_container_2', 'home_img_2.jpg');
        set_background_image('.img_container_3', 'product_img_3.jpg');
        set_background_image('.img_container_4', 'product_img_4.jpg');
        set_background_image('.bottom_img_container', 'product_img_5.jpg');
    };

    for (var i = 1; i < 4; i++) {
        for (var j = 1; j < 4; j++) {
            var obj = '.card_container_' + i + ' .card_div:eq(' + (j - 1) + ') .card_div_img';
            set_background_image(obj, 'product_detail_' + i + '_' + j + '.jpg');
        };
    };

    set_image_src('.bottom_img_container .certifications', 'product_icon_5.svg');
}

function set_background_image(class_name, img_file) {
    $(class_name).css({ 'background': getImgUrl(img_file, 'center', 'no-repeat'), 'background-size': 'cover' });
};

function set_image_src(class_name, img_name) {
    $(class_name).attr('src', getImg(img_name));
};

function show_video(lang) {
    close_video();
    var video_dialog = $('.video_dialog_container');
    var video_name = 'web_ad_product_';

    if (lang == 'zh' || lang == 'zh_hant') {
        video_name += 'zh';
    } else {
        video_name += 'en';
    };

    var video_url = getVideo(video_name);
    video_dialog.find('#video_product').attr('src', video_url);
    video_dialog.fadeIn();
    document.getElementById("video_product").play();
};

function close_video() {
    document.getElementById("video_product").pause();
    $('.video_dialog_container').hide();
};
