# me - this DAT
# 
# comp - the USD COMP
# allOps - a list of all the OPs imported from the USD file
# newOps - the list of all OPs newly created from this import
#

def onImport(comp, allOps, newOps):
	
	instance_op = op.ALLOCATOR.op(f'{comp.name[:-3]}/null_{comp.name[-2:]}')
	tex_path = comp.par.file.val[:-18]+f'textures/{comp.name}'

	for c in allOps:
		if c.OPType == 'importselectSOP':
			#Setting the render and display flag off for the importselectSOP
			c.render = False
			c.display = False

			#Adding a polyreduceSOP to reduce the number of points per model to 40% and connecting that to the importselectSOP 
			poly_reduce = c.parent().create(polyreduceSOP, f'polyreduce_{comp.name}')
			c.outputConnectors[0].connect(poly_reduce.inputConnectors[0])
			poly_reduce.nodeX = 200
			poly_reduce.par.percentage = 40
			poly_reduce.par.borderweight = 0.2
			poly_reduce.par.creaseweight = 0.2
			poly_reduce.par.lengthweight = 0.1

			#Adding an attributecreateSOP to compute tangents and connecting that to polyreduce
			attrib_create = c.parent().create(attributecreateSOP, f'attribcreate_{comp.name}')
			poly_reduce.outputConnectors[0].connect(attrib_create)
			attrib_create.nodeX = 400
			attrib_create.par.comptang = True

			#Adding a nullSOP at the end and then setting the render and display flag as on
			null = c.parent().create(nullSOP, f'null_{comp.name}')
			attrib_create.outputConnectors[0].connect(null)
			null.nodeX = 600
			null.render = True
			null.display = True

			#Instancing information for the geometry
			c.parent().par.instancing = True
			c.parent().par.instanceop = instance_op
			c.parent().par.instancetx = 'P(0)'
			c.parent().par.instancety = 'P(1)'
			c.parent().par.instancetz = 'P(2)'
		
		elif c.name == 'root':
			#Resetting the scale of the imported model to 1 
			c.par.sx = 1
			c.par.sy = 1
			c.par.sz = 1
		
		elif c.name == 'materials':
			#creating a reference to the pbrMAT in the materials component and setting the emit color to white
			mat = c.op(f'{comp.name}')
			mat.par.emitr = 1
			mat.par.emitg = 1
			mat.par.emitb = 1

			#Adding the diffuse map, setting it's input space to sRGB, then assigning it to the pbrMAT and setting the anisotropic filter to 4X
			dif = c.create(moviefileinTOP, f'{comp.name}_d')
			dif.par.file = tex_path+'_d.png'
			dif.nodeX = 200
			dif.par.inputsrgb = True
			mat.par.basecolormap = dif.path
			mat.par.basecolormapanisotropy = 2

			#Adding the metalness map, then assigning it to the pbrMAT and setting the anisotropic filter to 4X
			met = c.create(moviefileinTOP, f'{comp.name}_m')
			met.par.file = tex_path+'_m.png'
			met.nodeX = 400
			mat.par.metallicmap = met.path
			mat.par.metalnessmapanisotropy = 2

			#Adding the specular map, then assigning it to the pbrMAT and setting the anisotropic filter to 4X
			spec = c.create(moviefileinTOP, f'{comp.name}_s')
			spec.par.file = tex_path+'_s.png'
			spec.nodeX = 600
			mat.par.specularlevelmap = spec.path
			mat.par.specularlevelmapanisotropy = 2

			#Adding the roughness map, then assigning it to the pbrMAT and setting the anisotropic filter to 4X
			rough = c.create(moviefileinTOP, f'{comp.name}_r')
			rough.par.file = tex_path+'_r.png'
			rough.nodeX = 800
			mat.par.roughnessmap = rough.path
			mat.par.roughnessmapanisotropy = 2

			#Adding the normal map, then assigning it to the pbrMAT and setting the anisotropic filter to 4X
			norm = c.create(moviefileinTOP, f'{comp.name}_n')
			norm.par.file = tex_path+'_n.exr'
			norm.nodeX = 1000
			mat.par.normalmap = norm.path
			mat.par.normalmapanisotropy = 2

			#Adding the emit map, then assigning it to the pbrMAT
			emit = c.create(moviefileinTOP, f'{comp.name}_e')
			emit.par.file = tex_path+'_e.png'
			emit.nodeX = 1200
			mat.par.emitmap = emit.path

	return
	