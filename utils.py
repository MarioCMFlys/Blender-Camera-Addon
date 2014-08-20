import bpy

def setTrackTo(child, trackTo):
	deselectAll()
	child.select = True
	setActive(trackTo)
	bpy.ops.object.track_set(type = "TRACKTO")   

def setParent(child, parent):
	deselectAll()
	child.select = True
	setActive(parent)
	bpy.ops.object.parent_set(type = "OBJECT", keep_transform = True)
	
def setCustomProperty(object, propertyName, value, min = -100000000.0, max = 100000000.0):
	object[propertyName] = value
	object["_RNA_UI"] = { propertyName: {"min": min, "max": max} } 
	
def newDriver(object, dataPath, index = -1, type = "SCRIPTED"):
	fcurve = object.driver_add(dataPath, index)
	driver = fcurve.driver
	driver.type = type
	return driver

def linkFloatPropertyToDriver(driver, name, id, dataPath):
	driverVariable = driver.variables.new()
	driverVariable.name = name
	driverVariable.type = "SINGLE_PROP"
	driverVariable.targets[0].id = id
	driverVariable.targets[0].data_path = '["' + dataPath + '"]'
	
def deselectAll():
	bpy.ops.object.select_all(action = "DESELECT")
	
def setActive(object):
	bpy.context.scene.objects.active = object
	
def deleteSelectedObjects():
	bpy.ops.object.delete(use_global=False)
		
		
		
def lockCurrentLocalLocation(object, xAxes = True, yAxes = True, zAxes = True):
	setActive(object)
	constraint = object.constraints.new(type = "LIMIT_LOCATION")
	constraint.owner_space = "LOCAL"
	
	setConstraintLimitData(constraint, object.location)
	
	constraint.use_min_x = xAxes
	constraint.use_max_x = xAxes
	constraint.use_min_y = yAxes
	constraint.use_max_y = yAxes
	constraint.use_min_z = zAxes
	constraint.use_max_z = zAxes
	
def lockCurrentLocalRotation(object, xAxes = True, yAxes = True, zAxes = True):
	setActive(object)
	constraint = object.constraints.new(type = "LIMIT_ROTATION")
	constraint.owner_space = "LOCAL"
	
	setConstraintLimitData(constraint, object.rotation_euler)
	
	constraint.use_limit_x = xAxes
	constraint.use_limit_y = yAxes
	constraint.use_limit_z = zAxes
	
def lockCurrentLocalScale(object, xAxes = True, yAxes = True, zAxes = True):
	setActive(object)
	constraint = object.constraints.new(type = "LIMIT_SCALE")
	constraint.owner_space = "LOCAL"
	
	setConstraintLimitData(constraint, object.scale)
	
	constraint.use_min_x = xAxes
	constraint.use_max_x = xAxes
	constraint.use_min_y = yAxes
	constraint.use_max_y = yAxes
	constraint.use_min_z = zAxes
	constraint.use_max_z = zAxes
	
def setConstraintLimitData(constraint, vector):
	(x, y, z) = vector
	constraint.min_x = x
	constraint.max_x = x
	constraint.min_y = y
	constraint.max_y = y
	constraint.min_z = z
	constraint.max_z = z
	