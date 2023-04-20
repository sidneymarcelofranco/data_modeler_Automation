import win32com.client
scapi = win32com.client.Dispatch('AllFusionERwin.SCAPI')
filePath = "C:\\temp\\eMovies.erwin"
Definition = input("Digite a Definition: ")
# newfilename = "C:\\122.erwin"
scPUnit = scapi.PersistenceUnits.Add(filePath, "RDO=No")
scSession = scapi.Sessions.Add()
scSession.Open(scPUnit, 0, 0)
scTranId = scSession.BeginTransaction()
scMObjects = scSession.ModelObjects.Collect(scSession.ModelObjects.Root, 'Entity', 1)
for scObj in scMObjects:
    print(scObj.Properties('Name').Value)
    print(scObj.Properties('Comment').Value)
    print(scObj.Properties('Definition').Value)
    # print(scObj.Properties('Pii').Value)
# for scObj in scMObjects:
#     print (f"Definition Before {scObj.Properties('Definition').Value} ")
# for scObj in scMObjects:
#     scObj.Properties('Definition').Value = f"{scObj.Properties('Name').Value} {Definition}"
#     print (f"Definition After {scObj.Properties('Definition').Value} ")
scSession.CommitTransaction(scTranId)
scPUnit.Save(filePath, "RDO=NO;OVM=YES;OVF=Yes;DGM=YES;TRC=NO")