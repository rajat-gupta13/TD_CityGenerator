# me - this DAT
# 
# frame - the current frame
# state - True if the timeline is paused
# 
# Make sure the corresponding toggle is enabled in the Execute DAT.

def onStart():
    debug('Project Started, importing all models')
    op.CITY.OnStart()
    return

def onCreate():
	return

def onExit():
	debug('Project closed, clearing all models')
	op.CITY.ClearModels()
	return

def onFrameStart(frame):
	return

def onFrameEnd(frame):
	return

def onPlayStateChange(state):
	return

def onDeviceChange():
	return

def onProjectPreSave():
	return

def onProjectPostSave():
	return

	