import urllib.parse as parse

import tld


def checkUrl(url):
    """Check validity of the URL."""
    _url = patchUrl(str(url))
    _url = parse.urlparse(_url)
    validTypes = {'youtube': ('watch', 'playlist')}    # TODO: Grab this automatically from Video class
    domain = getDomain(_url)
    checkDomain = checkService(_url)
    if not checkDomain:
        return checkDomain
    else:
        return _url.path.lstrip('/') in validTypes[domain]

def patchUrl(url):
    """Fix the URL if the scheme is missing."""
    schemes = ('https://', 'http://')
    scheme = schemes[0]

    if not any(map(url.startswith, (scheme))):
        return scheme + url
    else:
        return url

def getDomain(url):
    """Get the domain from the URL."""
    res = tld.get_tld(url.netloc, fix_protocol = True, as_object = True)
    return res.domain

def checkService(url):
    """Check if the URL is from one of the implemented services."""
    services = ['youtube']  # TODO: Grab this automatically from Video class
    domain = getDomain(url)
    return domain in services
