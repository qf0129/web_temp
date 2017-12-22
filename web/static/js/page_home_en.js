$(function() {
    init_size();
    // init_shop_href();
    init_img();
    init_footer_swiper();
    init_swiper();
    $(window).resize(function() {
        init_size();
    });
});

function init_size() {
    var w = $(window).width(), h =$(window).height();

    if ($(document).width() <= 768) {
        $('.top_swiper_container').height(h);
        $('.top_swiper_1').height(h);

        $(".star_text1,.star_text2").css({"text-align":"center","font-size":"12px"});
        $(".start_user").css({"font-size":"12px"});

    }else{
        $('.top_swiper_container').height(h*0.9);
        $('.top_swiper_1').height(h*0.9);


    };
    // $('.video_container').height(w).height(w * 758 / 1920);
    // $('.show_container').height(w).height(w * 760 / 1920);
    // $('.video_bg_1').width(300).height(162);
    // $('.video_bg_2').width(300).height(162);
    $('.show_container').height($(window).height());
    $('.video_bg_1').height($('.video_bg_1').width() / 1.5);
    $('.video_bg_2').height($('.video_bg_2').width() / 1.5);

};

function init_shop_href(){
    if (Math.round(Math.random()) == 0){
        $('.top_btn').html('Available at Amazon');
        $('.top_btn_a').attr('href','/shop/amazon?from=home_top')
        $('.menu_right_container .btn_shop').attr("onclick", "window.open('/shop/amazon?from=nav_right','_blank')");
    }else{
        $('.top_btn').html('BUY NOW');
        $('.top_btn_a').attr('href','/shop/shopify?from=home_top')
        $('.menu_right_container .btn_shop').attr("onclick", "window.open('/shop/shopify?from=nav_right','_blank')");
    };
};

function init_img() {


    // $(".slide_page .slice_img img").eq(0).attr("src","home_en_2-13.jpg")
    // $('.cup_function .fun .figure img').eq(0).attr("src","home_en_2-01.jpg");
    // $('.cup_function .fun .figure img').eq(1).attr("src","home_en_2-02.jpg");
    // $('.cup_function .fun .figure img').eq(2).attr("src","home_en_2-03.jpg");
    // $('.cup_function .fun .figure img').eq(3).attr("src","home_en_2-04.jpg");
    // $('.buy_link .left_img img').eq(0).attr("src","home_en_2-05.jpg");


    set_image_src('.video_div_img', 'home_en_video_1.jpg');

    set_image_src('.slide_page .slice_img img', 'home_en_2-13.jpg');
    set_image_src('.cup_function .figure img:eq(0)', 'home_en_2-01.jpg');
    set_image_src('.cup_function .figure img:eq(1)', 'home_en_2-02.jpg');
    set_image_src('.cup_function .figure img:eq(2)', 'home_en_2-03.jpg');
    set_image_src('.cup_function .figure img:eq(3)', 'home_en_2-04.jpg');
    set_image_src('.buy_link .left_img img', 'home_en_2-05.jpg');


    // $(".five_start").attr("src","home_en_2-12.jpg");
    // $(".yin").attr("src","home_en_2-13.jpg");
    // $(".cup_img").attr("src","home_en_2-11.jpg");
    // $(".img_1").attr("src","home_en_2-06.jpg");
    // $(".img_2").attr("src","home_en_2-07.jpg");
    // $(".img_3").attr("src","home_en_2-14.jpg");

    set_image_src('.five_start', 'home_en_2-12.jpg');
    set_image_src('.yin', 'home_en_2-13.jpg');
    set_image_src('.cup_img', 'home_en_2-11.jpg');

    set_image_src('.img_1', 'home_en_2-06.jpg');
    set_image_src('.img_2', 'home_en_2-07.jpg');
    set_image_src('.img_3', 'home_en_2-14.jpg');

    set_background_img('.Buy_now', 'home_en_2-09.jpg');
    set_background_img('.Urls', 'home_en_2-15.jpg');
    set_background_img('.blue_bg', 'home_en_2-08.jpg');

    var img_class_normal = {".top_swiper_1":"home_en_1.jpg",
                            ".show_container":"home_img_3.jpg",
                            ".video_bg_1":"home_video_bg_1.jpg",
                            ".video_bg_2":"home_video_bg_2.jpg"};
    var img_class_small = {".top_swiper_1":"home_en_1.jpg",
                            ".show_container":"home_img_3_m.jpg",
                            ".video_bg_1":"home_video_bg_1_m.jpg",
                            ".video_bg_2":"home_video_bg_2_m.jpg"};

    if ($(document).width() <= 768) {
        for (var i in img_class_small) { set_background_img(i, img_class_small[i]);};
    } else {
        for (var i in img_class_normal) { set_background_img(i, img_class_normal[i]);};
    };
    
    for (var i=1;i<4;i++){
        set_image_src('.top_pet_'+i, 'home_en_top_pet_'+i+'.png');
        set_image_src('.top_cup_'+i, 'home_en_top_cup_'+i+'.png');
    };

    var i = document.getElementsByClassName("float_div"), len = i.length, loaded = 0;
    for(var j=0;j<len;j++){
        i[j].onload = (function(){
                loaded ++;
                if(loaded == len){
                    show_img_with_animation_delay('.top_cup_1', 'bounceInDown', 100);
                    show_img_with_animation_delay('.top_cup_3', 'fadeInUp', 500);
                    show_img_with_animation_delay('.top_cup_2', 'fadeInUp', 900);
                    show_img_with_animation_delay('.top_pet_1', 'zoomInUp', 1000);
                    show_img_with_animation_delay('.top_pet_3', 'slideInDown', 1500);
                    show_img_with_animation_delay('.top_pet_2', 'wobble', 2000);
                    // show_img_with_animation_delay('.top_cup_2,.top_cup_3', 'bounceInDown', 700);
                    // show_img_with_animation_delay('.top_pet_2,.top_pet_3', 'bounceInDown', 700);
                    show_img_with_animation_delay('.top_text_div', 'fadeIn', 1600);
                    setTimeout(function(){
                        listen_mouse_move();
                    },2500);
                };
        })(j);
    }

    $('.top_btn_div').click(function(){
    });
};

function listen_mouse_move(){

    listen_mouse_move_div('.top_pet_1',1,2);
    listen_mouse_move_div('.top_pet_2',-1,-2);
    listen_mouse_move_div('.top_pet_3',1,-5);
    listen_mouse_move_div('.top_cup_1',-1,1);
    listen_mouse_move_div('.top_cup_2',0.5,1);
    listen_mouse_move_div('.top_cup_3',-1,1);
    listen_mouse_move_div('.top_text_div',0.3,1);
   
};

function listen_mouse_move_div(class_name, rate ,zoom){
    var opt = $(class_name);
    var old_left = opt.position().left;
    var old_top = opt.position().top;
    var old_w = opt.width();
 
    $('.top_swiper_container').on('mousemove', function(e) {
        opt.css('left',old_left + (e.clientX)/50*rate).css('top',old_top + (e.clientY)/50*rate);
        opt.css('width',old_w + (e.clientY)/70*rate*zoom);
    });

    $('.top_swiper_container').on('mouseleave', function(e) {
        opt.animate({left:old_left, top:old_top, width:old_w});
    });
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

    var mySwiper = new Swiper('.swiper-container', {
        autoplay: 3000,
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        loop: true,
        autoplayDisableOnInteraction: false
    })


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
        video_name += '60s_';
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
