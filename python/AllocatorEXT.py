import random
# Accessing the Point interface object
Point = mod('text_point_interface').Point


class AllocatorEXT:
	"""
	AllocatorEXT used to dynamically allocate points to various groups
	"""
	def __init__(self, my_op):

		self._me = my_op
		
		# Accessing the GridSOP
		self.grid = op('grid1')

		# Basic information about the grid
		self.num_points = self.grid.numPoints		# Total number of points on the grid
		self.num_cols = self.grid.par.cols			# Number of columns in the grid
		self.num_rows = self.grid.par.rows			# Number of rows in the grid
		
		self.plots_area = self._me.par.Gridsizex.eval() * self._me.par.Gridsizey.eval() # Number of usable plot points
		self.block_height = int(self._me.par.Blocksizey.eval()) 	# Height of the block used for road spacing
		self.block_width = int(self._me.par.Blocksizex.eval())		# Width of the block used for road spacing

		
		# Custom parameters of the plots including sizes(read only) and counts
		self.monolith_size = [int(self._me.par.Monolithsizex), int(self._me.par.Monolithsizey)]
		self.monolith_area = 4.6875
		self.monolith_count = int(round(0.01 * self.monolith_area * self.plots_area / (self.monolith_size[0]*self.monolith_size[1])))

		self.large1_size = [int(self._me.par.Large1sizex), int(self._me.par.Large1sizey)]
		self.large1_area = 28.125
		self.large1_count = int(round(0.01 * self.large1_area * self.plots_area / (self.large1_size[0]*self.large1_size[1])))

		self.large2_size = [int(self._me.par.Large2sizex), int(self._me.par.Large2sizey)]
		self.large2_area = 10.546875
		self.large2_count = int(round(0.01 * self.large2_area * self.plots_area / (self.large2_size[0]*self.large2_size[1])))

		self.large3_size = [int(self._me.par.Large3sizex), int(self._me.par.Large3sizey)]
		self.large3_area = 10.546875
		self.large3_count = int(round(0.01 * self.large3_area * self.plots_area / (self.large3_size[0]*self.large3_size[1])))

		self.medium1_size = [int(self._me.par.Medium1sizex), int(self._me.par.Medium1sizey)]
		self.medium1_area = 12.5
		self.medium1_count = int(round(0.01 * self.medium1_area * self.plots_area / (self.medium1_size[0]*self.medium1_size[1])))

		self.medium2_size = [int(self._me.par.Medium2sizex), int(self._me.par.Medium2sizey)]
		self.medium2_area = 6.445312
		self.medium2_count = int(round(0.01 * self.medium2_area * self.plots_area / (self.medium2_size[0]*self.medium2_size[1])))

		self.medium3_size = [int(self._me.par.Medium3sizex), int(self._me.par.Medium3sizey)]
		self.medium3_area = 6.445312
		self.medium3_count = int(round(0.01 * self.medium3_area * self.plots_area / (self.medium3_size[0]*self.medium3_size[1])))
		
		self.small1_size = [int(self._me.par.Small1sizex), int(self._me.par.Small1sizey)]
		self.small1_area = 3.662109
		self.small1_count = int(round(0.01 * self.small1_area * self.plots_area / (self.small1_size[0]*self.small1_size[1])))

		self.small2_size = [int(self._me.par.Small2sizex), int(self._me.par.Small2sizey)]
		self.small2_area = 1.953125
		self.small2_count = int(round(0.01 * self.small2_area * self.plots_area / (self.small2_size[0]*self.small2_size[1])))

		self.small3_size = [int(self._me.par.Small3sizex), int(self._me.par.Small3sizey)]
		self.small3_area = 1.953125
		self.small3_count = int(round(0.01 * self.small3_area * self.plots_area / (self.small3_size[0]*self.small3_size[1])))


		# Creating empty list attributes to store the various point allocations
		self.all_points = []
		self.road_points = []

		self.monolith_list = []
		self.monolith_points = []

		self.large1_list = []
		self.large1_points = []

		self.large2_list = []
		self.large2_points = []

		self.large3_list = []
		self.large3_points = []

		self.medium1_list = []
		self.medium1_points = []

		self.medium2_list = []
		self.medium2_points = []

		self.medium3_list = []
		self.medium3_points = []

		self.small1_list = []
		self.small1_points = []

		self.small2_list = []
		self.small2_points = []

		self.small3_list = []
		self.small3_points = []

		self.small4_points = []

		#self.BuildCity()


	def ClearPoints(self):
		'''
			Clears out all the points in the list
			Called before starting of build city
		'''
		self.all_points.clear()
		self.road_points.clear()
		self.monolith_list.clear()
		self.monolith_points.clear()
		self.large1_list.clear()
		self.large1_points.clear()
		self.large2_list.clear()
		self.large2_points.clear()
		self.large3_list.clear()
		self.large3_points.clear()
		self.medium1_list.clear()
		self.medium1_points.clear()
		self.medium2_list.clear()
		self.medium2_points.clear()
		self.medium3_list.clear()
		self.medium3_points.clear()
		self.small1_list.clear()
		self.small1_points.clear()
		self.small2_list.clear()
		self.small2_points.clear()
		self.small3_list.clear()
		self.small3_points.clear()
		self.small4_points.clear()

	def UpdatePars(self):
		# Basic information about the grid
		self.num_points = self.grid.numPoints		# Total number of points on the grid
		self.num_cols = self.grid.par.cols			# Number of columns in the grid
		self.num_rows = self.grid.par.rows			# Number of rows in the grid
		
		self.plots_area = self._me.par.Gridsizex.eval() * self._me.par.Gridsizey.eval() # Number of usable plot points
		self.block_height = int(self._me.par.Blocksizey.eval()) 	# Height of the block used for road spacing
		self.block_width = int(self._me.par.Blocksizex.eval())		# Width of the block used for road spacing

		
		# Custom parameters of the plots including sizes(read only) and counts
		self.monolith_size = [int(self._me.par.Monolithsizex), int(self._me.par.Monolithsizey)]
		self.monolith_count = int(round(0.01 * self.monolith_area * self.plots_area / (self.monolith_size[0]*self.monolith_size[1])))

		self.large1_size = [int(self._me.par.Large1sizex), int(self._me.par.Large1sizey)]
		self.large1_count = int(round(0.01 * self.large1_area * self.plots_area / (self.large1_size[0]*self.large1_size[1])))

		self.large2_size = [int(self._me.par.Large2sizex), int(self._me.par.Large2sizey)]
		self.large2_count = int(round(0.01 * self.large2_area * self.plots_area / (self.large2_size[0]*self.large2_size[1])))

		self.large3_size = [int(self._me.par.Large3sizex), int(self._me.par.Large3sizey)]
		self.large3_count = int(round(0.01 * self.large3_area * self.plots_area / (self.large3_size[0]*self.large3_size[1])))

		self.medium1_size = [int(self._me.par.Medium1sizex), int(self._me.par.Medium1sizey)]
		self.medium1_count = int(round(0.01 * self.medium1_area * self.plots_area / (self.medium1_size[0]*self.medium1_size[1])))

		self.medium2_size = [int(self._me.par.Medium2sizex), int(self._me.par.Medium2sizey)]
		self.medium2_count = int(round(0.01 * self.medium2_area * self.plots_area / (self.medium2_size[0]*self.medium2_size[1])))

		self.medium3_size = [int(self._me.par.Medium3sizex), int(self._me.par.Medium3sizey)]
		self.medium3_count = int(round(0.01 * self.medium3_area * self.plots_area / (self.medium3_size[0]*self.medium3_size[1])))
		
		self.small1_size = [int(self._me.par.Small1sizex), int(self._me.par.Small1sizey)]
		self.small1_count = int(round(0.01 * self.small1_area * self.plots_area / (self.small1_size[0]*self.small1_size[1])))

		self.small2_size = [int(self._me.par.Small2sizex), int(self._me.par.Small2sizey)]
		self.small2_count = int(round(0.01 * self.small2_area * self.plots_area / (self.small2_size[0]*self.small2_size[1])))

		self.small3_size = [int(self._me.par.Small3sizex), int(self._me.par.Small3sizey)]
		self.small3_count = int(round(0.01 * self.small3_area * self.plots_area / (self.small3_size[0]*self.small3_size[1])))

	def OnStart(self):
		self.BuildCity()
		self.ImportModels()

	def ImportModels(self):
		debug('Importing models')
		op.LOADING.op('switch1').par.index = 1
		op.BUILDINGS.op('timer1').par.maxcycles.val = 21
		op.BUILDINGS.op('timer1').par.initialize.pulse()
		op.BUILDINGS.op('timer1').par.start.pulse()

	def ClearModels(self):
		debug('Clearing City')
		op.LOADING.op('switch1').par.index = 0
		op.BUILDINGS.op('timer1').par.maxcycles.val = 10
		op.BUILDINGS.op('timer1').par.initialize.pulse()
		op.BUILDINGS.op('timer1').par.start.pulse()

	def BuildCity(self):
		'''
			Clear out all points in existing lists
			Creating a list of all Point objects to track which points have been allocated and which havent
			Setup city
		'''
		
		self.ClearPoints()
		self.UpdatePars()
		for i in range(self.num_points):
			self.all_points.append(Point(i))

		self.SetupCity()
		self.AllocateInstanceGroups()

	def SetupCity(self):
		"""
		Generate the city in a linear fashion. First roads and then the biggest to smallest plots.
		"""

		self.AssignRoads()
		self.Assign(group_names=['group_monoliths', 'group_monolith_instance'], 
		group_properties={
			'count': self.monolith_count,
			'size': self.monolith_size,
			'plot_points': self.monolith_points,
			'plot_list': self.monolith_list})
		self.Assign(group_names=['group_large1', 'group_large1_instance'], 
		group_properties={
			'count': self.large1_count,
			'size': self.large1_size,
			'plot_points': self.large1_points,
			'plot_list': self.large1_list})
		self.Assign(group_names=['group_large2', 'group_large2_instance'], 
		group_properties={
			'count': self.large2_count,
			'size': self.large2_size,
			'plot_points': self.large2_points,
			'plot_list': self.large2_list})
		self.Assign(group_names=['group_large3', 'group_large3_instance'], 
		group_properties={
			'count': self.large3_count,
			'size': self.large3_size,
			'plot_points': self.large3_points,
			'plot_list': self.large3_list})
		self.Assign(group_names=['group_medium1', 'group_medium1_instance'], 
		group_properties={
			'count': self.medium1_count,
			'size': self.medium1_size,
			'plot_points': self.medium1_points,
			'plot_list': self.medium1_list})
		self.Assign(group_names=['group_medium2', 'group_medium2_instance'], 
		group_properties={
			'count': self.medium2_count,
			'size': self.medium2_size,
			'plot_points': self.medium2_points,
			'plot_list': self.medium2_list})
		self.Assign(group_names=['group_medium3', 'group_medium3_instance'], 
		group_properties={
			'count': self.medium3_count,
			'size': self.medium3_size,
			'plot_points': self.medium3_points,
			'plot_list': self.medium3_list})
		self.Assign(group_names=['group_small1', 'group_small1_instance'], 
		group_properties={
			'count': self.small1_count,
			'size': self.small1_size,
			'plot_points': self.small1_points,
			'plot_list': self.small1_list})
		self.Assign(group_names=['group_small2', 'group_small2_instance'], 
		group_properties={
			'count': self.small2_count,
			'size': self.small2_size,
			'plot_points': self.small2_points,
			'plot_list': self.small2_list})
		self.Assign(group_names=['group_small3', 'group_small3_instance'], 
		group_properties={
			'count': self.small3_count,
			'size': self.small3_size,
			'plot_points': self.small3_points,
			'plot_list': self.small3_list})
		self.AssignSmall4()


	def AllocateInstanceGroups(self):
		op('building_01/text_create_instance_groups').run()
		op('building_02/text_create_instance_groups').run()
		op('building_03/text_create_instance_groups').run()
		op('building_04/text_create_instance_groups').run()
		op('building_05/text_create_instance_groups').run()
		op('building_06/text_create_instance_groups').run()
		op('building_07/text_create_instance_groups').run()
		op('building_08/text_create_instance_groups').run()
		op('building_09/text_create_instance_groups').run()
		op('building_10/text_create_instance_groups').run()
		op('building_11/text_create_instance_groups').run()

	def AssignRoadsEW(self):
		'''
		Assigns the roads going from East to west based on the block height to find spacing between them
		'''
		numRoadsEW = int(self.num_rows / self.block_height - 1)
		row_start = []
		for i in range(1, numRoadsEW+1):
			row_start.append(self.num_cols*((i*self.block_height)+i-1))

		for i in range(len(row_start)):
			for j in range(row_start[i], row_start[i] + self.num_cols):
				if not self.all_points[j].Allocated():
					self.all_points[j].Allocate()
					self.road_points.append(self.all_points[j])

	def AssignRoadsNS(self):
		'''
		Assigns the roads going from North to South based on the block width to find spacing between them
		'''
		numRoadsNS = int(self.num_cols / self.block_width - 1)
		col_start = []
		for i in range(1, numRoadsNS+1):
			col_start.append((i*self.block_width)+i-1)
		
		for i in range(len(col_start)):
			for j in range(int(self.num_rows)):
				if col_start[i] >= self.num_cols:
					continue
				index = int(col_start[i]+j*self.num_cols)
				if not self.all_points[index].Allocated():
					self.all_points[index].Allocate()
					self.road_points.append(self.all_points[index])

	def AssignRoads(self):
		'''
		Assigns the roads, first E<->W and then N<->S and then assigns those values to the groupSop
		'''
		self.AssignRoadsEW()
		self.AssignRoadsNS()
		
		self.SetGroupValue('group_roads', self.road_points)

	def GetPlotPoints(self, point, plot_size):
		'''
		Fetches the potential points in the plot based on the size of the plot and the input point which is considered to be the bottom left point of the plot(origin for instancing).
		'''
		
		points_contained = []

		bottom_left = point

		for y in range(plot_size[1]):
			for x in range(plot_size[0]):
				points_contained.append(bottom_left + x)
			
			bottom_left = bottom_left + self.num_cols
		
		return points_contained

	def CheckPointsExist(self, points_list):
		'''
		Checks if the points selected for the potential plot exist on the grid. 
		If the point index is greater than the total number of points, then it doesn't exist.
		'''
		for p in points_list:
			if p >= self.num_points:
				return False
		return True

	def CheckFit(self, points_list, plot_size):
		'''
		Checks if the points in potential plot are not already allocated
		Also checks to make sure that the indices of the plot don't wrap to the other side of the grid
		'''
		for p in points_list:
			if self.all_points[p].Allocated():
				return False
		# Checks to make sure that the z coordinate of the top left point and the top right point are same 
		# If they are not the same, then the plot is wrapping around the grid from the left edge to the right edge
		if self.grid.points[points_list[plot_size[0]*(plot_size[1]-1)]].y != self.grid.points[points_list[(plot_size[0]*plot_size[1])-1]].y:
			return False
		return True

	def CheckOverlap(self, points_list, plot_points):
		'''
		Check to make sure that any of the potential plot points are not already alloted to a previous plot in the same group
		'''
		for p in points_list:
			if p in plot_points:
				return False
		return True

	def AssignPlots(self, plot_count, plot_size):
		'''
		Randomly assigns the points in a plot based on the number of plots and the plot size
		Returns 2 lists: 
			1. The plot_list is the list of points where the plot will be instanced and 
			2. The plot_points is the list of all the points in the group 
		'''
		option = range(self.num_points)
		plot_list = []
		plot_points = []
		
		loop_counter = 0

		while len(plot_list) < plot_count:
			
			loop_counter += 1
			# Selected potential point
			potential_placement = random.choice(option)

			# Checking if the selected point has already been allocated
			if self.all_points[potential_placement].Allocated():
				continue

			# Gets the list of points in the potenial plot
			potential_plot = self.GetPlotPoints(potential_placement, plot_size)

			# Checks if the points in the plot exist, fit in the grid and don't overlap and then adds them to the to the lists
			if self.CheckPointsExist(potential_plot) and self.CheckFit(potential_plot, plot_size) and self.CheckOverlap(potential_plot, plot_points):
				plot_points = plot_points + potential_plot
				plot_list.append(potential_placement)

		#print(loop_counter)
		return [plot_list, plot_points]


	def Assign(self, group_names, group_properties):
		'''
		Allocates the points in the group
		Assigns the points in the lists to the respective groupSops

		group_names is a list containing strings of the 2 groupSops
		group_properties is a dictionary containing the properties for that group including the count, size and the 2 lists to store the allocated points and instance locations
		'''
		Plots = self.AssignPlots(group_properties['count'], group_properties['size'])
		for p in Plots[1]:
			self.all_points[p].Allocate()
			group_properties['plot_points'].append(self.all_points[p])

		for p in Plots[0]:
			group_properties['plot_list'].append(self.all_points[p])

		self.SetGroupValue(group_names[0], group_properties['plot_points'])
		self.SetGroupValue(group_names[1], group_properties['plot_list'])
		pass

	def AssignSmall4(self):
		'''
		Allocates the points in the final group of 1x1 buildings
		Assigns the points in the lists to the respective groupSops
		'''
		for i in range(self.num_points):
			if not self.all_points[i].Allocated():
				self.all_points[i].Allocate()
				self.small4_points.append(self.all_points[i])

		self.SetGroupValue('group_small4', self.small4_points)

	def SetGroupValue(self, group_name, group_list):
		'''
		Helper function that sets the contents of the input allocated list to the pattern parameter of the specified groupSop
		'''
		point_list = []
		for i in range(len(group_list)):
			point_list.append(group_list[i].Index())
		
		group_output = ' '.join(map(str, point_list))

		op(group_name).par.pattern.val = group_output