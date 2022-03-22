class AudioEXT:
	
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.op = ownerComp

		#Grabbing the trigger chop to pulse the deck item index
		self.deck_a_trigger = op('trigger_a')		
		self.deck_b_trigger = op('trigger_b')

		#grabbing the audio file in chop to enable play and pause
		self.audio_a = op('audiofilein_a')
		self.audio_b = op('audiofilein_b')

		#used to store the current deck
		self.deck_constant = op('constant_deck')


	#Returns which deck we are in
	def GetCurrentDeck(self):
		if self.deck_constant.par.value0 == -1:
			return 'a'
		elif self.deck_constant.par.value0 == 1:
			return 'b'

	#Disables the pulse button on the component and then starts the transition
	def TransitionAudio(self):
		op.AUDIO.par.Nextsong.enable = False
		op.NEXTSONG.par.enable = False
		if self.GetCurrentDeck() == 'a':
			self.audio_b.par.cuepulse.pulse()
			self.audio_b.par.play = True
		elif self.GetCurrentDeck() == 'b':
			self.audio_a.par.cuepulse.pulse()
			self.audio_a.par.play = True

		self.deck_constant.par.value0 *= -1

	#Enables the pulse button on the component and then sets up the non playing deck to hold the next audio file in the folder
	def TransitionComplete(self):
		op.AUDIO.par.Nextsong.enable = True
		op.NEXTSONG.par.enable = True
		if self.GetCurrentDeck() == 'a':
			self.audio_b.par.play = False
			self.deck_b_trigger.par.triggerpulse.pulse()
		elif self.GetCurrentDeck() == 'b':
			self.audio_a.par.play = False
			self.deck_a_trigger.par.triggerpulse.pulse()
	
	#Starts playback of the current deck
	def PlayAudio(self):
		if self.GetCurrentDeck() == 'a':
			self.audio_a.par.play = True
		elif self.GetCurrentDeck() == 'b':
			self.audio_b.par.play = True
	
	#Stops playback of the current deck
	def PauseAudio(self):
		if self.GetCurrentDeck() == 'a':
			self.audio_a.par.play = False
		elif self.GetCurrentDeck() == 'b':
			self.audio_b.par.play = False
		