import win32com.client
ObjApi = win32com.client.Dispatch('AllFusionERwin.SCAPI')
objPropertyBag = win32com.client.Dispatch('AllFusionERwin.SCAPI.PropertyBag')
objPropertyBag.Add("Model_Type", "Combined")
conexao_arquivo = "C:\\temp\\eMovies.erwin"
ObjPU = ObjApi.PersistenceUnits.Create(objPropertyBag)
ObjPU = ObjApi.PersistenceUnits.Add(conexao_arquivo, "RDO=Yes")
if ObjApi.Sessions.Count > 0:
    ObjApi.Sessions.Clear()

sessao_M0 = ObjApi.Sessions.Add()
sessao_M1 = ObjApi.Sessions.Add()
intRetOper =  sessao_M0.Open(ObjPU,0 )
intRetOper =  sessao_M1.Open(ObjPU,1 )
entity_definition = "Teste Definition Value"

root = sessao_M0.ModelObjects.Root

entities = sessao_M0.ModelObjects.Collect(root, "Entity", 1)

print(entities.count)
for entity in entities:
    print(entity.Name)
    if entity.Name =='CUSTOMER': 
        print(entity.Properties["Definition"].Value)
    attributes = sessao_M0.ModelObjects.Collect(entity, "Attribute", 1)
    for attribute in attributes:
        print(attribute.Name)
        try:
            print(attribute.Properties["Definition"].Value)
            print(sessao_M0.Properties["Name"].Value)
            print(sessao_M0.Properties["tag_Udp_Owner_Type"].Value)
            print(sessao_M0.Properties["tag_Is_Logical"].Value)
            print(sessao_M0.Properties["tag_Is_Physical"].Value)
            print(sessao_M0.Properties["tag_Udp_Data_Type"].Value)
            print(sessao_M0.Properties["tag_Order"].Value)
            print(sessao_M0.Properties["tag_Udp_Values_List"].Value)
            print(sessao_M0.Properties["tag_Udp_Default_Value"].Value)
            print(sessao_M0.Properties["tag_Udp_Values_List"].Value)
        except Exception:
            print('Definition None')
    
# for entity in entities:
    
#     if entity.Name =='CUSTOMER': 
#         transIdAlter = sessao_M0.BeginNamedTransaction("ALTER PROP")
#         entity.Properties["Definition"].Value = entity_definition
#         sessao_M0.CommitTransaction(transIdAlter)
# ObjPU.Save(conexao_arquivo, "RDO=NOOVM=YESOVF=YesDGM=YES")
    

#SessaoM1.CommitTransaction(transIdCreate)