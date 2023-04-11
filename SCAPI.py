
import win32com.client

scapi = win32com.client.Dispatch('AllFusionERwin.SCAPI')
filePath = "C:\\temp\eMovies.erwin"
newfilename = "C:\\temp\eMovies2.erwin"

oModel = scapi.PersistenceUnits.Add(filePath, "RDO=Yes")


# scPUnit = scapi.PersistenceUnits.Add(filePath, "RDO=Yes")


# oBag.Add("Hidden_Model", False)
# oModel.PropertyBag = oBag
scSession = scapi.Sessions.Add()
# print(scSession)
scSession.Open(oModel, 0, 0)
print(scSession)

scTranId = scSession.BeginTransaction()
print(scSession.Name)
scMObjects = scSession.ModelObjects.Collect(scSession.ModelObjects.Root, 'Entity', 1)
for scObj in scMObjects:
    try:
        scDefineName = scObj.Properties('Definition').Value
    except Exception:
        scDefineName = ''
    try:
        # scName = scObj.Properties('Name').Value
        print(scObj.Properties('Name').Value)
    except Exception:
        scName = ''
    scObj.Properties('Physical_Name').Value = scName
    scObj.Properties('Name').Value = scDefineName
scAttrObjects = scSession.ModelObjects.Collect(scObj, 'Attribute', 1)
for scAttrObj in scAttrObjects:
    try:
        scAttrDefineName = scAttrObj.Properties('Definition').Value
    except Exception:
        scAttrDefineName = ''
    try:
        scAttrName = scAttrObj.Properties('Name').Value
    except Exception:
        scAttrName = ''
    scAttrObj.Properties('Physical_Name').Value = scAttrName
    scAttrObj.Properties('Name').Value = scAttrDefineName
scSession.CommitTransaction(scTranId)
scPUnit.Save(newfilename, 'OVF=yes')
print ("The End")