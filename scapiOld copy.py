import win32com.client
scapi = win32com.client.Dispatch('AllFusionERwin.SCAPI')
filePath = "C:\\temp\\eMovies.erwin"

# newfilename = "C:\\122.erwin"
scPUnit = scapi.PersistenceUnits.Add(filePath, "RDO=No")
scSession = scapi.Sessions.Add()
scSession.Open(scPUnit, 0, 0)
scTranId = scSession.BeginTransaction()
scMObjects = scSession.ModelObjects.Collect(scSession.ModelObjects.Root, 'Entity', 1)
for scObj in scMObjects:
    # print(str(scObj.Properties('Definition').Value))
    # print(str(scObj.Properties('Name').Value))
    print (f"{scObj.Properties('Name').Value} Teste Definition")
    scObj.Properties('Definition').Value = f"{scObj.Properties('Name').Value} Teste Definition"
scSession.CommitTransaction(scTranId)
scPUnit.Save(filePath, 'OVF=yes')    
  




# for scObj in scMObjects:
#     try:
#         # scDefineName = scObj.Properties('Definition').Value
#         definition = scObj.Properties('Definition').Value
#     except Exception:
#         definition = ''
#     try:
#         entityName = scObj.Properties('Name').Value
#     except Exception:
#         entityName = ''
#     scObj.Properties('Definition').Value = definition
#     # scObj.Properties('Name').Value = entityName
# # scAttrObjects = scSession.ModelObjects.Collect(scObj, 'Attribute', 1)
# # for scAttrObj in scAttrObjects:
# #     try:
# #         scAttrDefineName = scAttrObj.Properties('Definition').Value
# #     except Exception:
# #         scAttrDefineName = ''
# #     try:
# #         scAttrName = scAttrObj.Properties('Name').Value
# #     except Exception:
# #         scAttrName = ''
# #     scAttrObj.Properties('Physical_Name').Value = scAttrName
# #     scAttrObj.Properties('Name').Value = scAttrDefineName
# scSession.CommitTransaction(scTranId)
# scPUnit.Save(filePath, 'OVF=yes')
