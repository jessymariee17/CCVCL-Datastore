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

class DeleteSpecificMessageById(webapp2.RequestHandler):
	def get(self):
		message=Message.get_by_id(int(self.request.get('id')))
		message.key.delete()
		self.response.write("specific 'id' deleted")

class DeleteAllMessageById(webapp2.RequestHandler):
	def get(self):
		message_list=Message.query()
		for message in message_list:
			message.key.delete()
		self.response.write('all input deleted')
        
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
            
class Rotation(ndb.Model):
    rotX = ndb.FloatProperty() 
    rotY = ndb.FloatProperty() 
    rotW = ndb.FloatProperty() 
    rotZ = ndb.FloatProperty()
    seqid = ndb.IntegerProperty()
    timestamp = ndb.StringProperty()
    
class AddRotation(webapp2.RequestHandler):
    def post(self):
        rotation = Rotation()
        rotation.rotX = float(self.request.get("rotX"))
        rotation.rotY= float(self.request.get("rotY"))
        rotation.rotZ = float(self.request.get('rotZ'))
        rotation.rotW = float(self.request.get('rotW'))
        rotation.seqid = int(self.request.get('seqid'))
        rotation.timestamp = self.request.get('timestamp')
        key = rotation.put()
        self.response.write(key.id())
        
class GetRotationById(webapp2.RequestHandler):
    def get(self):
        rotation= Rotation.get_by_id(int(self.request.get('id')))
        self.response.write(rotation.rotX)
        self.response.write(",")
        self.response.write(rotation.rotY)
        self.response.write(",")
        self.response.write(rotation.rotZ)
        self.response.write(",")
        self.response.write(rotation.rotW)
        self.response.write(",")
        self.response.write(rotation.seqid)
        self.response.write(",")
        self.response.write(rotation.timestamp)

class GetAllRotation(webapp2.RequestHandler):
    def get(self):
        rotation_list = Rotation.query().order(Rotation.seqid)
        for rotation in rotation_list: 
            self.response.write(rotation.rotX)
            self.response.write(",")
            self.response.write(rotation.rotY)
            self.response.write(",")
            self.response.write(rotation.rotZ)
            self.response.write(",")
            self.response.write(rotation.rotW)
            self.response.write(",")
            self.response.write(rotation.seqid)
            self.response.write(",")
            self.response.write(rotation.timestamp)
            self.response.write("\n")

class LinearAcceleration(ndb.Model):
    linaccX = ndb.FloatProperty() 
    linaccY = ndb.FloatProperty() 
    linaccZ = ndb.FloatProperty()
    seqid = ndb.IntegerProperty()
    timestamp = ndb.StringProperty()
    
class AddLinearAcceleration(webapp2.RequestHandler):
    def post(self):
        linear_acceleration = LinearAcceleration()
        linear_acceleration.linaccX = float(self.request.get("linaccX"))
        linear_acceleration.linaccY= float(self.request.get("linaccY"))
        linear_acceleration.linaccZ = float(self.request.get('linaccZ'))
        linear_acceleration.seqid = int(self.request.get('seqid'))
        linear_acceleration.timestamp = self.request.get('timestamp')
        key = linear_acceleration.put()
        self.response.write(key.id())
        
class GetLinearAccelerationById(webapp2.RequestHandler):
    def get(self):
        linear_acceleration= LinearAcceleration.get_by_id(int(self.request.get('id')))
        self.response.write(linear_acceleration.linaccX)
        self.response.write(",")
        self.response.write(linear_acceleration.linaccY)
        self.response.write(",")
        self.response.write(linear_acceleration.linaccZ)
        self.response.write(",")
        self.response.write(linear_acceleration.seqid)
        self.response.write(",")
        self.response.write(linear_acceleration.timestamp)

class GetAllLinearAcceleration(webapp2.RequestHandler):
    def get(self):
        linear_acceleration_list = LinearAcceleration.query().order(LinearAcceleration.seqid)
        for linear_acceleration in linear_acceleration_list: 
            self.response.write(linear_acceleration.linaccX)
            self.response.write(",")
            self.response.write(linear_acceleration.linaccY)
            self.response.write(",")
            self.response.write(linear_acceleration.linaccZ)
            self.response.write(",")
            self.response.write(linear_acceleration.seqid)
            self.response.write(",")
            self.response.write(linear_acceleration.timestamp)
            self.response.write("\n")
            
class Compass(ndb.Model):
    comX = ndb.FloatProperty() 
    comY = ndb.FloatProperty() 
    comZ = ndb.FloatProperty()
    seqid = ndb.IntegerProperty()
    timestamp = ndb.StringProperty()
    
class AddCompass(webapp2.RequestHandler):
    def post(self):
        compass = Compass()
        compass.comX = float(self.request.get("comX"))
        compass.comY= float(self.request.get("comY"))
        compass.comZ = float(self.request.get('comZ'))
        compass.seqid = int(self.request.get('seqid'))
        compass.timestamp = self.request.get('timestamp')
        key = compass.put()
        self.response.write(key.id())
        
class GetCompassById(webapp2.RequestHandler):
    def get(self):
        compass= Compass.get_by_id(int(self.request.get('id')))
        self.response.write(compass.comX)
        self.response.write(",")
        self.response.write(compass.comY)
        self.response.write(",")
        self.response.write(compass.comZ)
        self.response.write(",")
        self.response.write(compass.seqid)
        self.response.write(",")
        self.response.write(compass.timestamp)

class GetAllCompass(webapp2.RequestHandler):
    def get(self):
        compass_list = Compass.query().order(Compass.seqid)
        for compass in compass_list: 
            self.response.write(compass.comX)
            self.response.write(",")
            self.response.write(compass.comY)
            self.response.write(",")
            self.response.write(compass.comZ)
            self.response.write(",")
            self.response.write(compass.seqid)
            self.response.write(",")
            self.response.write(compass.timestamp)
            self.response.write("\n")
                                
app = webapp2.WSGIApplication([
    ('/', MainHandler),    
    ('/add', AddMessage),
    ('/get', GetMessageById),
    ('/getall', GetAll),    
    ('/addpoint', AddPoint),
    ('/getpoint', GetPointById),
    ('/getallpoints', GetAllPoint),
    ('/addrotation', AddRotation),
    ('/getrotation', GetRotationById),
    ('/getallrotations', GetAllRotation),
    ('/addlinacc', AddLinearAcceleration),
    ('/getlinacc', GetLinearAccelerationById),
    ('/getalllinaccs', GetAllLinearAcceleration),
    ('/addcom', AddCompass),
    ('/getcom', GetCompassById),
    ('/getallcoms', GetAllCompass),
    ('/deletespecific',DeleteSpecificMessageById),
    ('/deleteall',DeleteAllMessageById)

], debug=True)
