# me - this DAT.
# 
# dat - the changed DAT
# rows - a list of row indices
# cols - a list of column indices
# cells - the list of cells that have changed content
# prev - the list of previous string contents of the changed cells
# 
# Make sure the corresponding toggle is enabled in the DAT Execute DAT.
# 
# If rows or columns are deleted, sizeChange will be called instead of row/col/cellChange.
pars = op('constant_pars')


def onTableChange(dat):
	current_folder = int(pars['folder'])+1
	if int(pars['clear']) == 0:
		for index, row in enumerate(dat.rows()):
			new_node = op(f'building_{current_folder:02d}').create(usdCOMP, f'{row[0].val}')
			new_node.nodeX = 0
			new_node.nodeY = -200 * index
			new_node.par.file = row[1].val + f'/{row[0].val}.usd'
			new_node.par.callbacks = op('usd_all_imports_callbacks').path
			new_node.par.imp.pulse()
	elif int(pars['clear']) == 1:
		found_leftovers = op(f'building_{current_folder:02d}').findChildren(type = usdCOMP)
		for old in found_leftovers:
			old.destroy()
	return

def onRowChange(dat, rows):
	return

def onColChange(dat, cols):
	return

def onCellChange(dat, cells, prev):
	return

def onSizeChange(dat):
	return
	