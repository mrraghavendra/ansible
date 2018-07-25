#!/usr/bin/python
from __future__ import print_function

from uuid import uuid4

import velocloud
from velocloud.rest import ApiException
# If SSL verification disabled (e.g. in a development environment)
import urllib3
urllib3.disable_warnings()
velocloud.configuration.verify_ssl=False
from copy import deepcopy
import json
import velocloud.models


class FilterModule(object):
    def filters(self):
        return {
            'updateDeviceSettings': self.updateDeviceSettings,
            'updateQOS': self.updateQOS
            #'another_filter': self.b_filter
        }
 
    def updateDeviceSettings(self, a_variable,b_variable):
        velocloud.configuration.verify_ssl=False
        client = velocloud.ApiClient()
	client.authenticate("user@velocloud.net", "p4ssword", operator=True)
	api = velocloud.AllApi(client)

        try:
	  configuration = api.configurationGetConfiguration({ "enterpriseId":a_variable,"configurationId":b_variable,"with": ["modules"] })
          devicesettings_module = None
          result= None
          print("processing started")
          for module in configuration.modules:
	    if module.name == "deviceSettings":
              devicesettings_module = module
	      break
          
          devicesettings_module.description = "updated desc"
          vlanids=[3,4]
          newDeviceSettingsDataModelsVirtualLanInterfaces = velocloud.models.DeviceSettingsDataModelsVirtualLanInterfaces( "", "lan1", "", "","Trunc Port","true","", "",vlanids)
          DeviceSettingsDataModelsVirtualLanInterfaces=[]
          DeviceSettingsDataModelsVirtualLanInterfaces.append(newDeviceSettingsDataModelsVirtualLanInterfaces)
          newDeviceSettingsDataModelsVirtualLan=velocloud.models.DeviceSettingsDataModelsVirtualLan(DeviceSettingsDataModelsVirtualLanInterfaces)
          newDeviceSettingsDataModelsVirtual=velocloud.models.DeviceSettingsDataModelsVirtual("",newDeviceSettingsDataModelsVirtualLan)
          newDeviceSettingsDataModels=velocloud.models.DeviceSettingsDataModels(newDeviceSettingsDataModelsVirtual)
          newDeviceSettingsDataVpn=velocloud.models.DeviceSettingsDataVpn("true","","","","false","true")
          # lan=None, ospf=None, bgp=None, dns=None, authentication=None, softwareUpdate=None, radioSettings=None, netflow=None, vqm=None, snmp=None, multiSourceQos=None, models=None, vpn=None
          newDeviceSettingsData=velocloud.models.DeviceSettingsData("","","","","","","","","","","",newDeviceSettingsDataModels,newDeviceSettingsDataVpn)
          devicesettings_module.data=newDeviceSettingsData
        except ApiException as e:
          print("Error in configuration_get_configuration")
        try:
          result = api.configurationUpdateConfigurationModule({ "id": devicesettings_module.id,"_update": devicesettings_module })
          #configuration = api.configurationGetConfiguration({ "enterpriseId": 123,"configurationId":3,"with": ["modules"] })
          #print("updated module")
        except ApiException as e:
          print("Error in configuration_update_configuration_module")
	  print(e)          
        return result
		
    def updateQOS(self, enterpriseID,configurationId,QOS):
        velocloud.configuration.verify_ssl=False
        client = velocloud.ApiClient()
        client.authenticate("user@velocloud.net", "p4ssword", operator=True)
        api = velocloud.AllApi(client)

        try:
          configuration = api.configurationGetConfiguration({ "enterpriseId":enterpriseID,"configurationId":configurationId,"with": ["modules"] })
          qos_module = None
          result= None
          print("updateQOS perocessing started")
          for module in configuration.modules:
            if module.name == "QOS":
              qos_module = module
              break
        except ApiException as e:
          print("Error in configuration_get_configuration")
        
        highbulkcosmappingvalue=velocloud.CosMappingValue("15","true")
        normalbulkcosmappingvalue=velocloud.CosMappingValue("5","true")
        lowbulkcosmappingvalue=velocloud.CosMappingValue("1","true")
        newbulkCos=velocloud.models.CosMapping(highbulkcosmappingvalue,normalbulkcosmappingvalue,lowbulkcosmappingvalue)

        highrealtimecosmappingvalue=velocloud.CosMappingValue("35","true")
        normalrealtimecosmappingvalue=velocloud.CosMappingValue("15","true")
        lowrealtimecosmappingvalue=velocloud.CosMappingValue("1","true")
        newrealtimeCos=velocloud.models.CosMapping(highrealtimecosmappingvalue,normalrealtimecosmappingvalue,lowrealtimecosmappingvalue)

        hightransactionalcosmappingvalue=velocloud.CosMappingValue("20","true")
        normaltransactionalcosmappingvalue=velocloud.CosMappingValue("7","true")
        lowtransactionalcosmappingvalue=velocloud.CosMappingValue("1","true")
        newtransactionalCos=velocloud.models.CosMapping(hightransactionalcosmappingvalue,normaltransactionalcosmappingvalue,lowtransactionalcosmappingvalue)

        newedgeQosDatacosMapping=velocloud.models.EdgeQOSDataCosMapping("",newbulkCos,newrealtimeCos,newtransactionalCos)
        newedgeQosData=velocloud.models.EdgeQOSData("","","","",newedgeQosDatacosMapping)
        qos_module.data=newedgeQosData
        #print(newedgeQosData)
	try:
          result = api.configurationUpdateConfigurationModule({ "id": qos_module.id,"_update": qos_module })
          #configuration = api.configurationGetConfiguration({ "enterpriseId": 123,"configurationId":3,"with": ["modules"] })
          #print("updated module")
        except ApiException as e:
          print("Error in configuration_update_configuration_module")
          print(e)
        return result
