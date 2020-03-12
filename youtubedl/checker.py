import urllib.parse as parse

import tld

from helpers import logger

from tld.exceptions import TldBadUrl, TldDomainNotFound

def checkUrl(url):
    """Check validity of the URL."""
    _url = patchUrl(str(url))
    _url = parse.urlparse(_url)
    validTypes = {'youtube': ('watch', 'playlist')}    # TODO: Grab this automatically from Video class
    domain = getDomain(_url)
    if not domain:
        return False
    checkDomain = checkService(_url)
    if not checkDomain:
        return checkDomain
    else:
        return _url.path.lstrip('/') in validTypes[domain]

def patchUrl(url):
    """Fix the URL if the scheme is missing."""
    schemes = ('https://', 'http://')
    scheme = schemes[0]
    url = str(url)

    if not any(map(url.startswith, (scheme))):
        return scheme + url
    else:
        return url

def getDomain(url):
    """Get the domain from the URL.

    Arguments:
        url: ParseResult (urllib.parse.parseurl)
    """
    res = None
    try:
        res = tld.get_tld(url.netloc, fix_protocol = True, as_object = True)
    except (TldBadUrl, TldDomainNotFound):
        return False
    except AttributeError:
        return False
    except Exception as errorMessage:
        # Catches any other unexpected error
        exceptionName = errorMessage.__class__.__name__
        logger.error(f"Invalid Domain Error Caught: {exceptionName}")
        logger.error(f"{errorMessage}")
        error = f"{exceptionName}:\n{errorMessage}"
    return res.domain

def checkService(url):
    """Check if the URL is from one of the implemented services.

    Arguments:
        url: ParseResult (urllib.parse.parseurl)
    """
    services = {'youtube'}  # TODO: Grab this automatically from Video class
    domain = getDomain(url)
    if domain:
        return domain in services
    else:
        return False
