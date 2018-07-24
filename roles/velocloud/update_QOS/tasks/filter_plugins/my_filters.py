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
   # def b_filter(self, a_variable, another_variable, yet_another_variable):
    #      print("b filter")        
     #   return "test" 
