from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import render_to_response
import os
from .. import settings
def status_views(request):
    #return render(request, 'log/nginxacc.html')
    #return render_to_response('log/nginxacc.html')
    url = ""
    response = HttpResponse()
    if "srverr" in str(request):
        print("error log")
        url=os.path.join (settings.STATICFILES_DIRS[0],'log','nginxerr.html')
        newurl=url[:-5]+"or.html"
        replacements=[('"Hit"','"Error"'), ('"Valid Requests"', '"Denied Requests"'),(" Dashboard", " Error Dashboard"), ('"Hits"','"Miss"'), ('"hit"','"miss"'), ('"hits"','"miss"')]
        with open(url) as infile, open(newurl, 'w') as outfile:
            for line in infile:
                for src, target in replacements:
                    line = line.replace(src, target)
                outfile.write(line)
        url = newurl
    else:
        url=os.path.join (settings.STATICFILES_DIRS[0],'log','nginxacc.html')
    file = open(url, "rb")
    return HttpResponse(file.read())
