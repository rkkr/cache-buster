import webapp2
from google.appengine.api import urlfetch

class MainPage(webapp2.RequestHandler):
    def get(self):
        if 'url' not in self.request.GET.keys():
            self.response.status = '400 Bad Request'
            self.response.write('Invalid url')
            return

        url = self.request.GET['url']
        remote = urlfetch.fetch(url=url, method=urlfetch.GET, headers=self.request.headers)
        #Cache-Control: no-cache header added by default
        self.response.status_int = remote.status_code
        for name, value in remote.headers.iteritems():
            self.response.headers[name] = value
        self.response.write(remote.content)

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
