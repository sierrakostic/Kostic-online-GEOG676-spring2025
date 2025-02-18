# Create a geodatabase
import arcpy

arcpy.env.workspace = r'H:\Grad School\GEOG 676\Kostic-online-GEOG676-spring2025\Lab_4'
folder_path = r'H:\Grad School\GEOG 676\Kostic-online-GEOG676-spring2025\Lab_4'
gdb_name = '6-0Campus.gdb'
gdb_path = folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

csv_path = r'H:\Grad School\GEOG 676\Kostic-online-GEOG676-spring2025\Lab_4\garages.csv'
garage_layer_name = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)


input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + '\\' + garage_layer_name

# Copy the Structures feature class into your geodatabase

campus = r'H:\Grad School\GEOG 676\Kostic-online-GEOG676-spring2025\Lab_4\--0Campus.gdb'
buildings_campus = campus + '\Structures'
buildings = gdb_path + '\\' + 'Buildings'
arcpy.Copy_management(buildings_campus,buildings)


# Re-projection
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + '\Garage_Points_reprojected', spatial_ref)

# Buffer Garages
garageBuffered = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_reprojected', gdb_path + '\Garage_Points_buffered', 150)

# Intersect buffer with the buildings
arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path +'\Garage_Building_Intersection', 'ALL')
arcpy.TableToTable_conversion(gdb_path + '\Garage_Building_Intersection.dbf',
            r'H:\Grad School\GEOG 676\Kostic-online-GEOG676-spring2025\Lab_4', 
            'nearbyBuilding.csv')