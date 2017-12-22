$(function() {
    init_size();
    init_img();
    init_footer_swiper();
    init_swiper();
    $(window).resize(function() {
        init_size();
    });
});
function init_size() {

    if ($(document).width() <= 768) {
        $('.top_container').height($(window).height());
    } else {
        $('.top_container').height($(window).height()*0.9);
    };
    $('.show_container').height($(window).height());
    $('.video_bg_1').height($('.video_bg_1').width() / 1.5);
    $('.video_bg_2').height($('.video_bg_2').width() / 1.5);
};

function init_img() {
    set_image_src('.top_gululu_talk', 'home_zh_top_icon_1.png');
    set_image_src('.top_hao_are_you', 'home_zh_top_icon_3.png');
    set_image_src('.top_awesome', 'home_zh_top_icon_4.png');
    set_image_src('.top_cup', 'home_zh_top_cup_1.png');

    if ($(document).width() <= 768) {
        // $('.top_swiper_slide_1').remove();
        set_background_img('.top_container', 'home_zh_top_bg.png');
        // set_background_img('.top_swiper_container .top_swiper_slide_2', 'home_img_2_m.jpg');
        set_background_img('.show_container', 'home_img_3_m.jpg');
        set_background_img('.video_container .video_bg_1', 'home_video_bg_1_m.jpg');
        set_background_img('.video_container .video_bg_2', 'home_video_bg_2_m.jpg');
    } else {
        set_background_img('.top_container', 'home_zh_top_bg.png');
        // set_background_img('.top_swiper_container .top_swiper_slide_2', 'home_img_2.jpg');
        set_background_img('.show_container', 'home_img_3.jpg');
        set_background_img('.video_container .video_bg_1', 'home_video_bg_1.jpg');
        set_background_img('.video_container .video_bg_2', 'home_video_bg_2.jpg');
    };

    show_img_with_animation_delay('.top_hao_are_you', 'bounceInUp', 1000);
    show_img_with_animation_delay('.top_awesome', 'bounceInUp', 1500);
};

function show_img_with_animation_delay(class_name, animation_name ,delay_time){
    setTimeout(
        function(){
            $(class_name).show();
            play_animation(class_name, animation_name);
        }, delay_time);
};

function play_animation(class_name, animation_name){
    $(class_name).removeClass('animated ' + animation_name).addClass('animated ' + animation_name).one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend');
};

function set_background_img(class_name, img_file) {
    $(class_name).css({ 'background': getImgUrl(img_file, 'center', 'no-repeat'), 'background-size': 'cover' });
};

function set_image_src(class_name, img_name) {
    $(class_name).attr('src', getImg(img_name));
};

function init_swiper() {
    if ($(document).width() > 768) {
        init_top_swiper();
    }else{
        $('.top_swiper_text').css('opacity','1');
    };
};
function init_top_swiper() {
    var top_swiper_index = 0;

    var top_swiper = new Swiper('.top_swiper_container', {
        effect: 'fade',
        speed: 900,
        loop: true,
        paginationClickable: true,
        pagination: '.top_swiper_pagination',
        onSlideChangeEnd: function(swiper) {
            hide_text(top_swiper_index);
            top_swiper_index = ((swiper.activeIndex + 1) % 2 + 1);
            show_text(top_swiper_index);
        },
        paginationBulletRender: function(swiper, index, className) {
            return '<span style="border-radius:3px;background:#fff;width:20px;height:4px;" class="' + className + '"></span>';
        }
    });
};

function init_footer_swiper() {
    var comment_swiper = new Swiper('.comment_swiper_container', {
        loop: true,
        paginationClickable: true,
        pagination: '.comment_swiper_pagination',
        paginationBulletRender: function(swiper, index, className) {
            return '<span style="background:#fff;" class="' + className + '"></span>';
        }
    });
};

function show_text(index) {
    $('.top_swiper_text_' + index).animate({
        bottom: '300px',
        opacity: '0.8',
    }, 800);
};

function hide_text(index) {
    $('.top_swiper_text_' + index).animate({
        bottom: '100px',
        opacity: '0',
    }, 800);
};

function show_video(item, lang) {
    close_video();
    var video_dialog = $('.video_dialog_container');
    var video_name = 'web_ad_';

    if (item == 1) {
        video_name += 'children_';
    };

    if (item == 2) {
        video_name += 'product_';
    };
    if (lang == 'zh' || lang == 'zh_hant') {
        video_name += 'zh';
    } else {
        video_name += 'en';
    };

    var video_url = getVideo(video_name);

    video_dialog.find('#video_' + item).attr('src', video_url);
    video_dialog.find('#video_' + item).show();
    video_dialog.fadeIn();
    document.getElementById("video_" + item).play();
};

function close_video() {
    document.getElementById("video_1").pause();
    document.getElementById("video_2").pause();
    $('.video_dialog_container').find('video').hide()
    $('.video_dialog_container').hide();
};
