import os
import webapp2

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from polls.models import Poll

class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
	a =Poll.objects.all()[0].question
        self.response.write(a)

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)

test var = "i'm not gonna use this. 	This is a line with >80 chars to make pep8 linter unhappy.      "



def main():
    from paste import httpserver                                        
    httpserver.serve(app, host='127.0.0.1', port='8080')
                                         
if __name__== '__main__':
    main()
