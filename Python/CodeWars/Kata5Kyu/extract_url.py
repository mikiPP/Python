# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
def domain_name(url):
    if url.index(".") < 12:
        url = url.split(".")
        return url[1]
    else:
        start_link = url.find('/')
        start_quote = url.find('/', start_link + 1)
        end_quote = url.find('.', start_quote + 1)
        url = url[start_quote + 1: end_quote]
        return url


if __name__ == '__main__':
    assert domain_name("http://github.com/carbonfive/raygun") == "github"
    assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
    assert domain_name("https://www.cnet.com") == "cnet"
