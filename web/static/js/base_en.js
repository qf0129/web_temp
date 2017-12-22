$(function() {
    // autoNavBg();
    initLanguageBar();
    autoContentHeight();
document.body.addEventListener('touchstart', function () {});
});

function autoContentHeight() {
    var min_content_height = $(window).height() - $('.root_footer_bar').height() - $('.root_nav_bar').height();
    if ($('.root_content_bar').height() < min_content_height) {
        $('.root_content_bar').height(min_content_height);
    };
};

function initLanguageBar() {
    $('.lang_container span').html($('.lang_container .active a').html());
};

function autoNavBg() {
    $('.nav_empty').height($('.nav_root').height());
    // setNavBg();
    // $(window).scroll(function() {
    //     $('.nav_menu_ul').hide();
    //     setNavBg();
    // });
    // $('.nav_menu_btn').click(function(){
    //     $('.nav_menu_ul').toggle();
    // });
};

function setNavBg() {
    if ($(window).scrollTop() > 50) {
        $('.nav_root').css('background', '#fafafa');
        $('.nav_root').css('box-shadow', '0 1px 2px #eee');
    };
    if ($(window).scrollTop() <= 50) {
        $('.nav_root').css('background', 'none');
        $('.nav_root').css('box-shadow', 'none');
    };
};

// var img_url = "http://qn.mygululu.com/img/";
var img_url = "/static/img/";

var video_url = "http://qn.mygululu.com/video/";


function getVideo(filename) {
    return video_url + filename;
};

function getImg(filename) {
    return img_url + filename;
};

function getImgUrl(filename) {
    var returnUrl = "url(" + img_url + arguments[0] + ")";

    if (arguments.length == 1) {
        return returnUrl;
    };

    if (arguments.length > 1) {
        for (var i in arguments) {
            if (i > 0) {
                returnUrl += ' ' + arguments[i];
            };
        };
        return returnUrl;
    };
};
