# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
# 
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.

def onValueChange(par, prev):
	# use par.eval() to get current value
	return

# Called at end of frame with complete list of individual parameter changes.
# The changes are a list of named tuples, where each tuple is (Par, previous value)
def onValuesChanged(changes):
	for c in changes:
		# use par.eval() to get current value
		par = c.par
		prev = c.prev
	return

def onPulse(par):
    if par.name == 'Rebuild':
        op.CITY.BuildCity()
    if par.name == 'Updateseeds':
        op.CITY.AllocateInstanceGroups()
    if par.name == 'Clearmodels':
        debug('Clearing City')
        op.AUDIO.par.Pause.pulse()
        op.LOADING.op('switch1').par.index = 0
        op.BUILDINGS.op('timer1').par.maxcycles.val = 10
        op.BUILDINGS.op('timer1').par.initialize.pulse()
        op.BUILDINGS.op('timer1').par.start.pulse()
    if par.name == 'Importmodels':
        debug('Importing Models')
        op.LOADING.op('switch1').par.index = 1
        op.BUILDINGS.op('timer1').par.maxcycles.val = 21
        op.BUILDINGS.op('timer1').par.initialize.pulse()
        op.BUILDINGS.op('timer1').par.start.pulse()
    return

def onExpressionChange(par, val, prev):
	return

def onExportChange(par, val, prev):
	return

def onEnableChange(par, val, prev):
	return

def onModeChange(par, val, prev):
	return
	