import arcpy, os, itertools


MXDs = r"M:\West_Palm_Beach\Guam\Maps\Mxd\Missions\2016_08_02\Zoning"
EXPORTs= r"M:\West_Palm_Beach\Guam\Maps\Pdf\Missions\2016_08_02\Zoning"


#Create lists of input and output file locations, can have multiple folders in list if needed
all_folders_list = [MXDs]
all_export_folders = [EXPORTs]


#set the pdf overwrite = TRUE
arcpy.env.overwriteOutput = True


#iterate through the lists of the input/output locations simultaneously
for ws, exportlocn in itertools.izip(all_folders_list, all_export_folders):

    #setting the input mxd workspace
    arcpy.env.workspace = ws

    #getting all the mxds in the workspace and put in list
    mxd_list = arcpy.ListFiles("*.mxd")

    print "Opening mxds in CURRENT WORKSPACE: " + str(ws)
    print "mxd_list: " + str(len(mxd_list)) + " items in this folder" + '\n'

    #loop through the list of mxds in the list
    for mxd in mxd_list:

        #get the file path of the current mxd
        current_mxd = arcpy.mapping.MapDocument(str(ws) + '\\' + str(mxd))
        print str(ws) + '\\' + str(mxd)

        #create the file path to export the pdf
        pdf_name = exportlocn + '\\' + mxd[:-4] + '.pdf'
        print "exporting item:  " + pdf_name


        #export the input mxd to the export pdf location        
        arcpy.mapping.ExportToPDF(current_mxd, pdf_name, 'PAGE_LAYOUT', 2550, 3000, '600')

        #close the mxd
        del mxd
        
    print '\n'

print "Done"
