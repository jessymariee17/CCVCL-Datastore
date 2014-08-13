import webapp2
from google.appengine.ext import ndb

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Welcome to the CCVCLAB Datastore!')

class Message(ndb.Model):
    data = ndb.StringProperty()    

class AddMessage(webapp2.RequestHandler):
    def post(self):
        message = Message()
        message.data = self.request.get('data')
        key = message.put()
        self.response.write(key.id())
        
class GetMessageById(webapp2.RequestHandler):
    def get(self):
        message = Message.get_by_id(int(self.request.get('id')))
        self.response.write(message.data)
        
class GetAll(webapp2.RequestHandler):
    def get(self):
        message_list = Message.query()
        for message in message_list: 
            self.response.write(message.data)
            self.response.write("\n")
                        
class Point(ndb.Model):
    x = ndb.FloatProperty() 
    y = ndb.FloatProperty() 
    z = ndb.FloatProperty() 

class AddPoint(webapp2.RequestHandler):
    def post(self):
        point = Point()
        point.x = float(self.request.get("x"))
        point.y = float(self.request.get("y"))
        point.z = float(self.request.get('z'))
        key = point.put()
        self.response.write(key.id())
        
class GetPointById(webapp2.RequestHandler):
    def get(self):
        point= Point.get_by_id(int(self.request.get('id')))
        self.response.write(point.x)
        self.response.write(",")
        self.response.write(point.y)
        self.response.write(",")
        self.response.write(point.z)

class GetAllPoint(webapp2.RequestHandler):
    def get(self):
        point_list = Point.query()
        for point in point_list: 
            self.response.write(point.x)
            self.response.write(",")
            self.response.write(point.y)
            self.response.write(",")
            self.response.write(point.z)
            self.response.write("\n")
#hello jane
                        
app = webapp2.WSGIApplication([
    ('/', MainHandler),    
    ('/add', AddMessage),
    ('/get', GetMessageById),
    ('/getall', GetAll),    
    ('/addpoint', AddPoint),
    ('/getpoint', GetPointById),
    ('/getallpoints', GetAllPoint)

], debug=True)
