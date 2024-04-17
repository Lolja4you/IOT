import re

class RegexDispatch(object):
    def __init__(self, urls:list):
        self.urls = urls

    def __call__(self, environ, start_response):
        path_info = environ.get('PATH_INFO', '')
        for prefix, app in self.urls.items():
            if path_info == prefix or path_info == prefix+'/':
                return app(environ, start_response)
            match = re.match(prefix, path_info) or\
                re.match(prefix, path_info+'/')
            if match and match.groupdict():
                environ['url_params'] = match.groupdict()
                return app(environ, start_response)
        start_response('404 Not Found', [('content-type', 'text/plain')])
        return 'not found'