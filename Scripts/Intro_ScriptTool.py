import arcpy

def print_message(msg):
    print(msg)
    arcpy.AddMessage(msg)

arcpy.env.overwriteOutput = True
# arcpy.env.workspace = r"E:\LPA\Data\Sample.gdb"

# fc = r"E:\LPA\Data\ne_10m_admin_0_countries.shp"
fc = arcpy.GetParameterAsText(0)
if fc == "":
    fc = fc = r"E:\LPA\Data\ne_10m_admin_0_countries.shp"
numFeats = arcpy.GetCount_management(fc)
# print("The feature class, {0}, has {1} feature(s)".format(fc, numFeats))
# arcpy.AddMessage("The feature class, {0}, has {1} feature(s)".format(fc, numFeats))
print_message("The feature class, {0}, has {1} feature(s)".format(fc, numFeats))

##arcpy.CreateFileGDB_management(r"E:\LPA\Data","Sample")
##arcpy.Select_analysis(fc, "Egypt", "NAME = 'Egypt'")

print_message("Script completed!")
