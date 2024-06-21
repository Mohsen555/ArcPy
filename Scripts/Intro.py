import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"E:\LPA\Data\Sample.gdb"

fc = r"E:\LPA\Data\ne_10m_admin_0_countries.shp"
numFeats = arcpy.GetCount_management(fc)
print("The feature class, {0}, has {1} feature(s)".format(fc, numFeats))

arcpy.CreateFileGDB_management(r"E:\LPA\Data","Sample")
arcpy.Select_analysis(fc, "Egypt", "NAME = 'Egypt'")

print("Script completed!")
