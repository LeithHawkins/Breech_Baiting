import arcpy
from arcpy import env
import time

arcpy.env.overwriteOutput = True
env.workspace = 'B:\\Breech_Methodology\\Final_Breachdatabase.gdb'
filework = 'B:\\Breech_Methodology\\Final_Breachdatabase.gdb'
proposed_run = 'B:\\Breech_Methodology\\Final_Breachdatabase.gdb\\NTLLS_NPWS_2017_proposed_FINAL'
actual_run = 'B:\\Breech_Methodology\\Final_Breachdatabase.gdb\\Actual_Completed_run_2017'

Buffer_output = 'B:\\Breech_Methodology\\Final_Breachdatabase.gdb\\Buffers'
buffer_10 = Buffer_output + '\\buffer10'
buffer_25 = Buffer_output + '\\buffer25'
buffer_50 = Buffer_output + '\\buffer50'
buffer_100 = Buffer_output + '\\buffer100'
Buffer_10width = '10 Meters'
Buffer_25width = '25 Meters'
Buffer_50width = '50 Meters'
Buffer_100width = '100 Meters'

start = time.time()
def Buffer(Input, Output, BufferLength):
    return arcpy.Buffer_analysis(Input, Output, BufferLength, 'FULL', 'ROUND', 'ALL')

Buffer(proposed_run, buffer_10, Buffer_10width)
Buffer(proposed_run, buffer_25, Buffer_25width)
Buffer(proposed_run, buffer_50, Buffer_50width)
Buffer(proposed_run, buffer_100, Buffer_100width)

clip_output = 'B:\\Breech_Methodology\\Final_Breachdatabase.gdb\\Clip'
clip10 = clip_output + '\\Clip10'
clip25 = clip_output + '\\Clip25'
clip50 = clip_output + '\\Clip50'
clip100 = clip_output + '\\Clip100'
print('Time: ' + str(time.time() - start))
start = time.time()
def Clip_feature(Clip_F, Outputclip):
    return arcpy.Clip_analysis(actual_run, Clip_F, Outputclip)

Clip_feature(buffer_10, clip10)
Clip_feature(buffer_25, clip25)
Clip_feature(buffer_50, clip50)
Clip_feature(buffer_100, clip100)
print('Time: ' + str(time.time() - start))
start = time.time()
def addfield(intable):
    return arcpy.AddField_management(intable, 'Length_km', 'Double', '', '', '', 'Length km', '', '', '')
addfield(clip10)
addfield(clip25)
addfield(clip50)
addfield(clip100)
print('Time: ' + str(time.time() - start))
start = time.time()
def calculate_length(intable):
    return arcpy.CalculateField_management(intable, 'Length_km', '!shape.length@kilometers!', 'PYTHON')
calculate_length(clip10)
calculate_length(clip25)
calculate_length(clip50)
calculate_length(clip100)
print('Time: ' + str(time.time() - start))

start = time.time()
outable10 = filework + '\\Summary10'
outable25 = filework + '\\Summary25'
outable50 = filework + '\\Summary50'
outable100 = filework + '\\Summary100'
def Summary(Intable, outable):
    return arcpy.Statistics_analysis(Intable, outable, [['Length_KM', 'SUM']], '')
Summary(clip10, outable10)
Summary(clip25, outable25)
Summary(clip50, outable50)
Summary(clip100,outable100)

print('Time: ' + str(time.time() - start))



# with arcpy.da.UpdateCursor(dataset_dissolve, ['Max_Distance']) as large:
#                     for row in large:
#                         row[0] = Mval
#                         large.updateRow(row)
#                         print row[0]
#                         print large.updateRow(row)
#                         fields = arcpy.ListFields('in_memory/holding_dissolve')
