#Enter Url to looking for technology
import webtech as webtech

url="https://35000usdperwwekpodf.blogspot.com/?p=9swghttps://35000usdperwwekpodf.blogspot.co.il?o%3D0hnd"
try:
    wt = webtech.WebTech(options={'json': True})
    print('Crawlering -- >' + url)
    # scan a single website
    report = wt.start_from_url(url)
    print(report)
except:

    print("")