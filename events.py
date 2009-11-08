#SECURITY NOTE: anything in here can be created simply by sending the 
# class name over the network.  This is a potential vulnerability
# I wouldn't suggest letting any of these classes DO anything, especially
# things like file system access, or allocating huge amounts of memory

class Event:
	"""this is a superclass for any events that might be generated by an
	object and sent to the EventManager"""
	def __init__(self):
		self.name = "Generic Event"

class TickEvent(Event):
	def __init__(self):
		self.name = "CPU Tick Event"

class QuitEvent(Event):
	def __init__(self):
		self.name = "Program Quit Event"

class MapBuiltEvent(Event):
	def __init__(self, map):
		self.name = "Map Finished Building Event"
		self.map = map

class GameStartRequest(Event):
	def __init__(self):
		self.name = "Game Start Request"

class GameStartedEvent(Event):
	def __init__(self, game):
		self.name = "Game Started Event"
		self.game = game

class CharactorMoveRequest(Event):
	def __init__(self, direction):
		self.name = "Charactor Move Request"
		self.direction = direction

class CharactorMoveEvent(Event):
	def __init__(self, charactor):
		self.name = "Charactor Move Event"
		self.charactor = charactor

class CharactorPlaceEvent(Event):
	"""this event occurs when a Charactor is *placed* in a sector, 
	ie it doesn't move there from an adjacent sector."""
	def __init__(self, charactor):
		self.name = "Charactor Placement Event"
		self.charactor = charactor

class ServerConnectEvent(Event):
	def __init__(self, serverReference):
		self.name = "Network Server Connection Event"
		self.server = serverReference

class ClientConnectEvent(Event):
	"""this event is generated by the Server whenever a client connects
	to it"""
	def __init__(self, client):
		self.name = "Network Client Connection Event"
		self.client = client


from twisted.spread import pb
class CopyableTickEvent(TickEvent, pb.Copyable, pb.RemoteCopy):
	def __init__(self, obj ):
		pass

class CopyableQuitEvent(QuitEvent, pb.Copyable, pb.RemoteCopy):
	def __init__(self, obj ):
		pass

class CopyableMapBuiltEvent(MapBuiltEvent, pb.Copyable, pb.RemoteCopy):
	def __init__(self, obj ):
		pass

class CopyableGameStartRequest(GameStartRequest, pb.Copyable, pb.RemoteCopy):
	def __init__(self, obj ):
		pass

class CopyableGameStartedEvent(GameStartedEvent, pb.Copyable, pb.RemoteCopy):
	def __init__(self, obj ):
		self.game = id( obj.game )

class CopyableCharactorMoveRequest(CharactorMoveRequest, pb.Copyable, pb.RemoteCopy):
	def __init__(self, obj ):
		CharactorMoveRequest.__init__(self, obj.direction)

class CopyableCharactorMoveEvent(CharactorMoveEvent, pb.Copyable, pb.RemoteCopy):
	def __init__(self, obj ):
		CharactorMoveEvent.__init__(self, obj.charactor)

class CopyableCharactorPlaceEvent(CharactorPlaceEvent, pb.Copyable, pb.RemoteCopy):
	def __init__(self, obj ):
		self.charactor = id( obj.charactor )

class CopyableServerConnectEvent(ServerConnectEvent, pb.Copyable, pb.RemoteCopy):
	def __init__(self, obj ):
		ServerConnectEvent.__init__(self, obj.server)

class CopyableClientConnectEvent(ClientConnectEvent, pb.Copyable, pb.RemoteCopy):
	def __init__(self, obj ):
		ClientConnectEvent.__init__(self, obj.client)
