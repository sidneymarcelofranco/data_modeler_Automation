#!/usr/bin/python
# -*- coding: gbk -*-
import win32com.client

print "point 01"
# ����COM����
scapi = win32com.client.Dispatch('AllFusionERwin.SCAPI')
# conn=win32com.client.Dispatch('ADODB.Connection')
# ������־�װ����ģ�͵�����
# Դ�ļ�
filename = "C:\\111.erwin"
# Ŀ���ļ�
newfilename = "C:\\122.erwin"
scPUnit = scapi.PersistenceUnits.Add(filename, "RDO=yes")
# ������ȡ�ڴ���ģ�����ݵ�����
scSession = scapi.Sessions.Add()
scSession.Open(scPUnit, 0, 0)
# �������
scTranId = scSession.BeginTransaction()
# ��ȡ����Entityģ�Ͷ���
scMObjects = scSession.ModelObjects.Collect(scSession.ModelObjects.Root, 'Entity', 1)
for scObj in scMObjects:
    # ȡDefinition���Ե�ֵ
    try:
        scDefineName = scObj.Properties('Definition').Value
    except Exception, ex:
        scDefineName = ''
    try:
        scName = scObj.Properties('Name').Value
    except Exception, ex:
        scName = ''
# ��������ֵ
    # print "His scName is %s" % scName
    # print "His scDefineName is %s" % scDefineName
    scObj.Properties('Physical_Name').Value = scName
    scObj.Properties('Name').Value = scDefineName
# ��ȡ��Entity������Attribute����
scAttrObjects = scSession.ModelObjects.Collect(scObj, 'Attribute', 1)
for scAttrObj in scAttrObjects:
    # scAttrDefineName = scAttrObj.Properties('Definition').Value
    # scAttrName = scAttrObj.Properties('Name').Value
    try:
        scAttrDefineName = scAttrObj.Properties('Definition').Value
    except Exception, ex:
        scAttrDefineName = ''
    try:
        scAttrName = scAttrObj.Properties('Name').Value
    except Exception, ex:
        scAttrName = ''
# ��������ֵ
    scAttrObj.Properties('Physical_Name').Value = scAttrName
    scAttrObj.Properties('Name').Value = scAttrDefineName
scSession.CommitTransaction(scTranId)
# ����Ϊһ���µ��ļ�
scPUnit.Save(newfilename, 'OVF=yes')
print "The End"