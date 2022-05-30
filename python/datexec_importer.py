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

# stores the current cycle value and the current status of the process
pars = op('constant_pars')

def onTableChange(dat):

	# adding 1 to the current cycle value to create the appropriate prefix
	current_folder = int(pars['folder'])+1
	
	# check if we are in the loading phase of the process
	if int(pars['clear']) == 0:
		for index, row in enumerate(dat.rows()):
			# creating a usdCOMP in the respective geometryCOMP using the table contents
			new_node = op(f'building_{current_folder:02d}').create(usdCOMP, f'{row[0].val}')

			# aligning the newly created operator on the network
			new_node.nodeX = 0
			new_node.nodeY = -200 * index

			# assigning the respective .usd to the file parameter of the usdCOMP using the path and file name from the folderDAT
			new_node.par.file = row[1].val + f'/{row[0].val}.usd'

			# assigning a callbacks script to the newly created usdCOMP to finish the rest of the setup
			new_node.par.callbacks = op('usd_all_imports_callbacks').path

			# pulse the import button to import the asset associated with the usd file
			new_node.par.imp.pulse()
	
	# check if we are in the clearing phase of the process
	elif int(pars['clear']) == 1:

		# find and destroy any usdCOMPs in the geometryCOMPs
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
	