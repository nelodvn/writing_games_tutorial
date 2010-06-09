#SECURITY NOTE: anything in here can be created simply by sending the 
# class name over the network.  This is a potential vulnerability
# I wouldn't suggest letting any of these classes DO anything, especially
# things like file system access, or allocating huge amounts of memory

class Event:
	"""this is a superclass for any events that might be generated by an
	object and sent to the EventManager"""
	def __init__(self):
		self.name = "Generic Event"
	def __str__(self):
		return '<%s %s>' % (self.__class__.__name__,
		                    id(self))
	    

class TickEvent(Event):
	def __init__(self):
		self.name = "CPU Tick Event"

class SecondEvent(Event):
	def __init__(self):
		self.name = "Clock One Second Event"

class QuitEvent(Event):
	def __init__(self):
		self.name = "Program Quit Event"

class FatalEvent(Event):
	def __init__(self, *args):
		self.name = "Fatal Error Event"
		self.args = args

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
	def __init__(self, player, charactor, direction):
		self.name = "Charactor Move Request"
		self.player = player
		self.charactor = charactor
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
	"""the client generates this when it detects that it has successfully
	connected to the server"""
	def __init__(self, serverReference):
		self.name = "Network Server Connection Event"
		self.server = serverReference

class ClientConnectEvent(Event):
	"""this event is generated by the Server whenever a client connects
	to it"""
	def __init__(self, client, avatarID):
		self.name = "Network Client Connection Event"
		self.client = client
		self.avatarID = avatarID

class ClientDisconnectEvent(Event):
	"""this event is generated by the Server when it finds that a client 
	is no longer connected"""
	def __init__(self, avatarID):
		self.name = "Network Client Disconnection Event"
		self.avatarID = avatarID

class GameSyncEvent(Event):
	"""..."""
	def __init__(self, game):
		self.name = "Game Synched to Authoritative State"
		self.game = game

class PlayerJoinRequest(Event):
	"""..."""
	def __init__(self, playerDict):
		self.name = "Player Joining Game Request"
		self.playerDict = playerDict

class PlayerJoinEvent(Event):
	"""..."""
	def __init__(self, player):
		self.name = "Player Joined Game Event"
		self.player = player

class CharactorPlaceRequest(Event):
	"""..."""
	def __init__(self, player, charactor, sector):
		self.name = "Charactor Placement Request"
		self.player = player
		self.charactor = charactor
		self.sector = sector
