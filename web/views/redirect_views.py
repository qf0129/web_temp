from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.translation import get_language
import logging

# TENCENT_STORE = "http://a.app.qq.com/o/simple.jsp?pkgname=com.bowhead.gululu";
# APPLE_STORE = "https://itunes.apple.com/bt/app/gululu/id1067167648";
# GOOGLE_STORE = "https://play.google.com/store/apps/details?id=com.bowhead.gululu&hl=en";

# TMALL_SHOP = "https://gululumy.tmall.com"
# YOUZAN_SHOP = "https://shop18465506.youzan.com"
# SHOPLINE_SHOP = "https://www.gululushop.com/"
# AMAZON_SHOP = "https://www.amazon.com/dp/B06X1BX37R"
# SHOPIFY_SHOP = "https://gululustore.myshopify.com/"

app_stores = {
    'qq': 'http://a.app.qq.com/o/simple.jsp?pkgname=com.bowhead.gululu',
    'apple': 'https://itunes.apple.com/bt/app/gululu/id1067167648',
    'google': 'https://play.google.com/store/apps/details?id=com.bowhead.gululu&hl=en'
}

shops = {
    'tmall': 'https://gululumy.tmall.com',
    'amazon': 'https://www.amazon.com/dp/B06X1BX37R', 
    'shopify': 'https://gululustore.myshopify.com', 
    'youzan': 'https://shop18465506.youzan.com', 
    'shopline': 'https://www.gululushop.com'
}

DOWNLOAD_APP_URL_NO_CDN = "http://download.mygululu.com/app/download/"

logger = logging.getLogger('web.views')


def redirect_download_app_no_cdn(request):
    return redirect(DOWNLOAD_APP_URL_NO_CDN)

def redirect_download_app(request):
    lang = ''
    client = ''
    try:
        lang = request.META['HTTP_ACCEPT_LANGUAGE'].split(',')[0].split(';')[0].lower()
    except KeyError:
        logger.error('HTTP_ACCEPT_LANGUAGE size zero!')
        logger.info(str(request.META))
        lang = 'en'

    try:
        client = request.META['HTTP_USER_AGENT'].lower()
    except KeyError:
        logger.error('HTTP_USER_AGENT size zero!')
        logger.info(str(request.META))
        client = ''

    
    if 'micromessenger' in client:
        return redirect(app_stores['qq'])

    if 'iphone' in client or 'ipad' in client or 'ipod' in client:
        return redirect(app_stores['apple'])

    if 'android' in client:
        if lang in ('zh', 'zh-cn'):
            return redirect(app_stores['qq'])

    if lang in ('zh', 'zh-cn'):
        return redirect(app_stores['qq'])
        
    return redirect(app_stores['google'])

def redirect_index(request):
    return redirect('/')

def redirect_faq(request):
    return redirect('/faq')

def redirect_shop(request):

    # Todo: check both localization and ACCEPT LANGUAGE
    # lang = request.META['HTTP_ACCEPT_LANGUAGE'].split(',')[0].split(';')[0].lower()
    client = ''
    try:
        client = request.META['HTTP_USER_AGENT'].lower()
    except:
        logger.error('HTTP_USER_AGENT size zero!')
        logger.error(str(request.META))
        lang = ''

    lang = get_language()

    if lang in ('zh-tw', 'zh-hant', 'zh-Hant'):
        return redirect(shops['shopline'])

    if lang in ('zh', 'zh-cn', 'zh-CN'):
        if 'micromessenger' in client:
            return redirect(shops['youzan'])
        else:
            return redirect(shops['tmall'])

    return redirect(shops['shopify'])

def redirect_shop_channel(request, channel):
    if channel in shops:
        return redirect(shops[channel])
    else:
        return redirect_shop(request)

