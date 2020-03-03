import urllib.parse as parse

import tld


def checkUrl(url):
    """Check validity of the URL."""
    _url = patchUrl(str(url))
    _url = parse.urlparse(_url)
    checkDomain = checkService(_url)

    return checkDomain   # Continua...

def patchUrl(url):
    """Fix the URL if the scheme is missing."""
    scheme = 'https://'

    if not url.startswith(scheme):
        patchedUrl = scheme + url

    return patchedUrl

def checkService(url):
    """Check if the URL is from one of the implemented services."""
    services = ['youtube']  # TODO: Grab this automatically from Video class
    res = tld.get_tld(_url.netloc, fix_protocol = True, as_object = True)
    domain = res.domain

    return domain in services
