from django.test import SimpleTestCase, Client
from django.core.urlresolvers import reverse
from django.utils.translation import activate
import requests

TENCENT_STORE = "http://a.app.qq.com/o/simple.jsp?pkgname=com.bowhead.gululu";
APPLE_STORE = "https://itunes.apple.com/bt/app/gululu/id1067167648";
GOOGLE_STORE = "https://play.google.com/store/apps/details?id=com.bowhead.gululu&hl=en";

TMALL_SHOP = "https://gululumy.tmall.com"
YOUZAN_SHOP = "https://shop18465506.youzan.com"
SHOPLINE_SHOP = "https://www.gululushop.com/"
AMAZON_SHOP = "https://www.amazon.com/dp/B06X1BX37R"


iphone_ua_string = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'
ipad_ua_string = 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10'
long_ua_string = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.3; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)'

class URLTestCases(SimpleTestCase):


    def test_url_download(self):
        client = Client()
        #url = "https://www.mygululu.com//"
        #headers = {"Accept-Language": "en-US,en;q=0.5"}
        #r = requests.get(url, headers=headers)
        response = self.client.get('/app/download/gululu/')
        self.assertEqual(response.status_code, 302)
        response.close()

        response = self.client.get('/app/download/gululu/', follow=True)
        chain = response.redirect_chain
        self.assertIs(len(chain)>0, True)
        response.close()
        self.assertIs(chain[0][0]==GOOGLE_STORE, True)
        print(chain[0])

    def test_url_download2(self):

        client = Client()
        response = self.client.get('/app/download/gululu/',HTTP_USER_AGENT='Mozilla/5.0')
        self.assertEqual(response.status_code, 302)
        response.close()

        response = self.client.get('/app/download/gululu/', follow=True)
        chain = response.redirect_chain
        self.assertIs(len(chain)>0, True)
        self.assertIs(chain[0][0]==GOOGLE_STORE, True)
        response.close()

    def test_url_download3(self):
        client = Client()
        response = self.client.get('/app/download/gululu/')
        self.assertEqual(response.status_code, 302)
        response.close()
        response = self.client.get('/app/download/gululu/',HTTP_USER_AGENT='micromessenger', follow=True)
        chain = response.redirect_chain
        self.assertIs(len(chain)>0, True)
        self.assertIs(chain[0][0]==TENCENT_STORE, True)
        print(str(chain[0][0]))
        response.close()

    def test_url_download4(self):

        client = Client()
        response = self.client.get('/app/download/gululu/')
        self.assertEqual(response.status_code, 302)
        response.close()
        response = self.client.get('/app/download/gululu/', HTTP_USER_AGENT=iphone_ua_string, follow=True)
        chain = response.redirect_chain
        self.assertIs(len(chain)>0, True)
        self.assertIs(chain[0][0]==APPLE_STORE, True)
        
    def test_url_download5(self):

        client = Client(HTTP_USER_AGENT='Ophone')
        response = self.client.get('/app/download/gululu/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/app/download/gululu/', HTTP_USER_AGENT="OMG", follow=True)
        chain = response.redirect_chain
        self.assertIs(len(chain)>0, True)
        self.assertIs(chain[0][0]==GOOGLE_STORE, True)


    def test_url_download6(self):
        client = Client()
        response = self.client.get('/app/download/gululu/',HTTP_USER_AGENT=ipad_ua_string,HTTP_ACCEPT_LANGUAGE='fr')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/app/download/gululu/',HTTP_USER_AGENT=ipad_ua_string,HTTP_ACCEPT_LANGUAGE='fr', follow=True)
        chain = response.redirect_chain
        self.assertIs(len(chain)>0, True)
        self.assertIs(chain[0][0]==APPLE_STORE, True)

    def test_url_download7(self):
        client = Client(HTTP_USER_AGENT=long_ua_string,HTTP_ACCEPT_LANGUAGE='zh')
        response = self.client.get('/app/download/gululu/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/app/download/gululu/',HTTP_USER_AGENT=long_ua_string,HTTP_ACCEPT_LANGUAGE='zh', follow=True)
        chain = response.redirect_chain
        self.assertIs(len(chain)>0, True)
        self.assertIs(chain[0][0]==TENCENT_STORE, True)
        
    def test_url_download8(self):

        client = Client(HTTP_USER_AGENT='iphone')
        response = self.client.get('/app/download/gululu/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/app/download/gululu/', HTTP_USER_AGENT='iphone',HTTP_ACCEPT_LANGUAGE='fr', follow=True)
        chain = response.redirect_chain
        self.assertIs(len(chain)>0, True)
        self.assertIs(chain[0][0]==APPLE_STORE, True)
        response.close()

        client = Client(HTTP_USER_AGENT='iphone')
        response = self.client.get('/app/download/gululu/')
        self.assertEqual(response.status_code, 302)
        response.close()
        response = self.client.get('/app/download/gululu/', HTTP_USER_AGENT='iphone', HTTP_ACCEPT_LANGUAGE='zh-cn', follow=True)
        chain = response.redirect_chain
        self.assertIs(len(chain)>0, True)
        self.assertIs(chain[0][0]==APPLE_STORE, True)
        response.close()

        client = Client(HTTP_USER_AGENT='iphone')
        response = self.client.get('/app/download/gululu/')
        self.assertEqual(response.status_code, 302)
        response.close()

        response = self.client.get('/app/download/gululu/', HTTP_USER_AGENT='iphone', HTTP_ACCEPT_LANGUAGE='fr', follow=True)
        chain = response.redirect_chain
        self.assertIs(len(chain)>0, True)
        self.assertIs(chain[0][0]==APPLE_STORE, True)
        response.close()

    def test_url_download9(self):

        client = Client(HTTP_USER_AGENT='android')
        response = self.client.get('/app/download/gululu/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/app/download/gululu/', HTTP_ACCEPT_LANGUAGE='zh-cn', follow=True)
        chain = response.redirect_chain
        self.assertIs(len(chain)>0, True)
        self.assertIs(chain[0][0]==TENCENT_STORE, True)

        client = Client(HTTP_USER_AGENT='android')
        response = self.client.get('/app/download/gululu/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/app/download/gululu/', HTTP_ACCEPT_LANGUAGE='en', follow=True)
        chain = response.redirect_chain
        self.assertIs(len(chain)>0, True)
        self.assertIs(chain[0][0]==GOOGLE_STORE, True)

        client = Client(HTTP_USER_AGENT='android')
        response = self.client.get('/app/download/gululu/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/app/download/gululu/', HTTP_ACCEPT_LANGUAGE='zh-hant', follow=True)
        chain = response.redirect_chain
        self.assertIs(len(chain)>0, True)
        self.assertIs(chain[0][0]==GOOGLE_STORE, True)



    def test_url_shop(self):
        client = Client()
        activate('en')
        response = self.client.get('/shop/',HTTP_USER_AGENT='android',  HTTP_ACCEPT_LANGUAGE='en', follow=True)
        chain = response.redirect_chain
        self.assertIs(len(chain)>0, True)
        self.assertIs(chain[0][0]==AMAZON_SHOP, True)
        response.close()

    def test_url_shop_ms(self):
        client = Client()
        response = self.client.get('/shop/', HTTP_USER_AGENT="micromessenger;android", HTTP_ACCEPT_LANGUAGE='zh', follow=True)
        activate('zh-cn')
        chain = response.redirect_chain
        self.assertIs(len(chain)>0, True)
        self.assertIs(chain[0][0]==YOUZAN_SHOP, True)
        response.close()

        client = Client(HTTP_USER_AGENT="android")
        response = self.client.get('/shop/',  follow=True)
        activate('zh-cn')

        chain = response.redirect_chain
        self.assertIs(len(chain)>0, True)
        self.assertIs(chain[0][0]==TMALL_SHOP, True)
        response.close()

    def test_url_shop_android(self):

        client = Client()
        activate('en')
        response = self.client.get('/shop/', HTTP_USER_AGENT="android", HTTP_ACCEPT_LANGUAGE='en', follow=True)
        chain = response.redirect_chain
        self.assertIs(len(chain)>0, True)
        self.assertIs(chain[0][0]==AMAZON_SHOP, True)
        response.close()

        activate('zh-hant')
        response = self.client.get('/shop/',  HTTP_ACCEPT_LANGUAGE='en', follow=True)
        chain = response.redirect_chain
        self.assertIs(len(chain)>0, True)
        self.assertIs(chain[0][0]==SHOPLINE_SHOP, True)
        response.close()



        #other tests
