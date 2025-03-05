import arcpy

#assign bands
source = r"H:\Grad School\GEOG 676\Kostic-online-GEOG676-spring2025\Lab_7"
band1 = arcpy.sa.Raster(source + r"\Band1.TIF") # blue
band2 = arcpy.sa.Raster(source + r"\Band2.TIF") # green
band3 = arcpy.sa.Raster(source + r"\Band3.TIF") # red 
band4 = arcpy.sa.Raster(source + r"\Band4.TIF") # NIR
combined = arcpy.CompositeBands_management([band1, band2, band3, band4], source + r"\output_combined.tif" )

# Hillshade

azimuth = 315
altitude = 45
shadows = 'NO_SHADOWS'
z_factor = 1
arcpy.ddd.HillShade(source + r"\DEM.tif", source + r"\output_Hillshaded.tif", azimuth, altitude, shadows, z_factor)

# Slope
output_measurement = "DEGREE"
z_factor = 1
arcpy.ddd.Slopee(source + r"\DEM.tif", source + r"\output_Slope.tif", output_measurement, z_factor)

print("success!")
