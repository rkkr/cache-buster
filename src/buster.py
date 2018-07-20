import webapp2
import datetime
from google.appengine.api import urlfetch

class MainPage(webapp2.RequestHandler):
    def get(self):
        if 'url' not in self.request.GET.keys():
            self.response.status = '400 Bad Request'
            self.response.write('Invalid url')
            return

        url = self.request.GET['url']
        remote = urlfetch.fetch(url=url, method=urlfetch.GET, headers=self.request.headers)
        self.response.status_int = remote.status_code
        expires = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        self.response.headers['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
        for name, value in remote.headers.iteritems():
            #Cache-Control: no-cache header added by default
            if name.lower() in ['content-type', 'etag', 'expires', 'last-modified']:
                self.response.headers[name.lower()] = value
        self.response.write(remote.content)

app = webapp2.WSGIApplication([
    ('/.*', MainPage),
], debug=True)
