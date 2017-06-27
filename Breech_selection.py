import arcpy
from arcpy import env
import time

start = time.time()

HOLDINGS = "C:\\Database_connections\\GIS101Delivery_Restricted.sde\\GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS"
holdings_Select = 'in_memory/holding_all'
proposed_run = 'B:\\Breech_Methodology\\Final_Breachdatabase.gdb\\NTLLS_NPWS_2017_proposed_FINAL'
actual_run = 'B:\\Breech_Methodology\\Final_Breachdatabase.gdb\\Actual_Completed_run_2017'
arcpy.Select_analysis(HOLDINGS,holdings_Select)

Holding_lyr = arcpy.MakeFeatureLayer_management(HOLDINGS,'holdings_Layer')
arcpy.SelectLayerByLocation_management(Holding_lyr, 'INTERSECT', proposed_run ,'REMOVE_FROM_SELECTION' )
arcpy.SelectLayerByLocation_management(Holding_lyr, 'WITHIN_A_DISTANCE', actual_run, '11 Metres' )
arcpy.FeatureClassToFeatureClass_conversion(holdings_Select,'B:\\Breech_Methodology\\Final_Breachdatabase.gdb\\potential_breech2017')
rint('Time: ' + str(time.time() - start))
