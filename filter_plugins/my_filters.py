#!/usr/bin/python
# coding=utf-8

from __future__ import print_function
from uuid import uuid4
from velocloud.rest import ApiException
from copy import deepcopy
import json
import velocloud.models
import velocloud
import urllib3
import ast
from jinja2 import Environment
from jinja2 import FileSystemLoader
urllib3.disable_warnings()
velocloud.configuration.verify_ssl = False


class FilterModule(object):

    def filters(self):
        return {'updateDeviceSettings': self.updateDeviceSettings,
                'updateQOS': self.updateQOS,
                'json_formatUtil': self.json_formatUtil,
                'segRulesfilter': self.segRulesfilter
               }

    def updateDeviceSettings(self, a_variable, b_variable):
        velocloud.configuration.verify_ssl = False
        client = velocloud.ApiClient()
        client.authenticate('user@velocloud.net', 'p4ssword',
                            operator=True)
        api = velocloud.AllApi(client)

        try:
            configuration = \
                api.configurationGetConfiguration({'enterpriseId': a_variable,
                    'configurationId': b_variable, 'with': ['modules']})
            devicesettings_module = None
            result = None
            print('processing started')
            for module in configuration.modules:
                if module.name == 'deviceSettings':
                    devicesettings_module = module
                    break

            devicesettings_module.description = 'updated desc'
            vlanids = [3, 4]
            newDeviceSettingsDataModelsVirtualLanInterfaces = \
                velocloud.models.DeviceSettingsDataModelsVirtualLanInterfaces(
                '',
                'lan1',
                '',
                '',
                'Trunc Port',
                'true',
                '',
                '',
                vlanids,
                )
            DeviceSettingsDataModelsVirtualLanInterfaces = []
            DeviceSettingsDataModelsVirtualLanInterfaces.append(newDeviceSettingsDataModelsVirtualLanInterfaces)
            newDeviceSettingsDataModelsVirtualLan = \
                velocloud.models.DeviceSettingsDataModelsVirtualLan(DeviceSettingsDataModelsVirtualLanInterfaces)
            newDeviceSettingsDataModelsVirtual = \
                velocloud.models.DeviceSettingsDataModelsVirtual('',
                    newDeviceSettingsDataModelsVirtualLan)
            newDeviceSettingsDataModels = \
                velocloud.models.DeviceSettingsDataModels(newDeviceSettingsDataModelsVirtual)
            newDeviceSettingsDataVpn = \
                velocloud.models.DeviceSettingsDataVpn(
                'true',
                '',
                '',
                '',
                'false',
                'true',
                )

          # lan=None, ospf=None, bgp=None, dns=None, authentication=None, softwareUpdate=None, radioSettings=None, netflow=None, vqm=None, snmp=None, multiSourceQos=None, models=None, vpn=None

            newDeviceSettingsData = velocloud.models.DeviceSettingsData(
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                newDeviceSettingsDataModels,
                newDeviceSettingsDataVpn,
                )
            devicesettings_module.data = newDeviceSettingsData
        except ApiException, e:
            print('Error in configuration_get_configuration')
        try:
            result = \
                api.configurationUpdateConfigurationModule({'id': devicesettings_module.id,
                    '_update': devicesettings_module})
        except ApiException, e:

          # configuration = api.configurationGetConfiguration({ "enterpriseId": 123,"configurationId":3,"with": ["modules"] })
          # print("updated module")

            print('Error in configuration_update_configuration_module')
            print(e)
        return result

    def updateQOS(
        self,
        enterpriseID,
        configurationId,
        QOS,
        ):
        velocloud.configuration.verify_ssl = False
        client = velocloud.ApiClient()
        client.authenticate('user@velocloud.net', 'p4ssword',
                            operator=True)
        api = velocloud.AllApi(client)

        try:
            configuration = \
                api.configurationGetConfiguration({'enterpriseId': enterpriseID,
                    'configurationId': configurationId,
                    'with': ['modules']})
            qos_module = None
            result = None
            print('updateQOS perocessing started')
            for module in configuration.modules:
                if module.name == 'QOS':
                    qos_module = module
                    break
        except ApiException, e:
            print('Error in configuration_get_configuration')

        highbulkcosmappingvalue = velocloud.CosMappingValue('15', 'true'
                )
        normalbulkcosmappingvalue = velocloud.CosMappingValue('5',
                'true')
        lowbulkcosmappingvalue = velocloud.CosMappingValue('1', 'true')
        newbulkCos = \
            velocloud.models.CosMapping(highbulkcosmappingvalue,
                normalbulkcosmappingvalue, lowbulkcosmappingvalue)

        highrealtimecosmappingvalue = velocloud.CosMappingValue('35',
                'true')
        normalrealtimecosmappingvalue = velocloud.CosMappingValue('15',
                'true')
        lowrealtimecosmappingvalue = velocloud.CosMappingValue('1',
                'true')
        newrealtimeCos = \
            velocloud.models.CosMapping(highrealtimecosmappingvalue,
                normalrealtimecosmappingvalue,
                lowrealtimecosmappingvalue)

        hightransactionalcosmappingvalue = \
            velocloud.CosMappingValue('20', 'true')
        normaltransactionalcosmappingvalue = \
            velocloud.CosMappingValue('7', 'true')
        lowtransactionalcosmappingvalue = velocloud.CosMappingValue('1'
                , 'true')
        newtransactionalCos = \
            velocloud.models.CosMapping(hightransactionalcosmappingvalue,
                normaltransactionalcosmappingvalue,
                lowtransactionalcosmappingvalue)

        newedgeQosDatacosMapping = \
            velocloud.models.EdgeQOSDataCosMapping('', newbulkCos,
                newrealtimeCos, newtransactionalCos)
        newedgeQosData = velocloud.models.EdgeQOSData('', '', '', '',
                newedgeQosDatacosMapping)
        qos_module.data = newedgeQosData

        # print(newedgeQosData)

        try:
            result = \
                api.configurationUpdateConfigurationModule({'id': qos_module.id,
                    '_update': qos_module})
        except ApiException, e:

          # configuration = api.configurationGetConfiguration({ "enterpriseId": 123,"configurationId":3,"with": ["modules"] })
          # print("updated module")

            print('Error in configuration_update_configuration_module')
            print(e)
        return result

    def json_formatUtil(self, a_variable):
        print('in json_formatUtil')
        c = a_variable[0:len(a_variable) - 2] + '}'
        b = c.split('-')
        a_newvariable = '['
        i = 0
        print('length of list is ' + str(len(b)))
        for temp in b:
            a_newvariable = a_newvariable + str(temp)
            i = i + 1
            if i < len(b):
                a_newvariable = a_newvariable + ','

        a_newvariable = a_newvariable + ']'
        print(a_newvariable)
        return a_newvariable
        
    def segRulesfilter(self, a_variable):
        j2_env = Environment(loader=FileSystemLoader('./files'), trim_blocks=True)
        template = j2_env.get_template('rulestemplate.json')
        segmenttemplate = j2_env.get_template('SegmenQOStemplate.json')
        insertqostemplate = j2_env.get_template('insert_QOS.json')
        jsonDataStr = str(a_variable)
        print("test:" + jsonDataStr)
        jsonDataStr = jsonDataStr.replace("'", '"').replace('u"', '"')
        print("test2:" + jsonDataStr)
       
        i = 0
        print("obj_json1")
        # obj_json = json.dumps(json.loads(a_variable))
        # jsonStr = a_variable.decode("utf-8")
        jsonData = json.dumps(jsonDataStr)
        obj_json = json.loads(jsonData)
        ruletem = ""
        print("obj_json2" + obj_json)
        segtemplate = '{"segments":['
        print("obj_json3"+jsonDataStr["velo_edge_id"])
        #type(obj_json)
        noofsegments = len(obj_json['segments'])
        print(noofsegments)
        j = 0
        for temp in obj_json['segments']:
            j = j + 1
            ruletem = '['
            noofrules = len(temp['rules'])
            print("obj_json:" + j)
            i = 0
            for a_rule in temp['rules']:
                # jinjainput ="ruleName='"+a_rule['name']+"',"+"desination_ip='"+a_rule['dip']+"',"+"desination_port='"+a_rule['dport']+"',"+"protocol_id='"+a_rule['protocol']+"',"+"priority='"+a_rule['priority']+"',"+"traffic_class='"+a_rule['traffic_class']+"'"
                i = i + 1
                context = dict()
                context['ruleName'] = a_rule['ruleName']
                context['desination_ip'] = a_rule['destAppIP']
                context['desination_port'] = a_rule['destAppPort']
                context['protocol_id'] = a_rule['protocol'].get('id')
                context['priority'] = a_rule['priorityID']
                context['traffic_class'] = a_rule['serviceClass']
                context['hostname'] = a_rule['destApp']
                # print(context)
                # print(jinjainput)
                ruletemplate = template.render(**context)
                if i < noofrules: 
                    ruletem = ruletem + ruletemplate + ","
                else:
                    ruletem = ruletem + ruletemplate
            
            ruletem = ruletem + ']' 
            segcontext = dict()
            segcontext['segment_id'] = temp['segmentid']
            segcontext['segment_name'] = temp['segment']
            segcontext['rules'] = ruletem
            segment = segmenttemplate.render(**segcontext)
            if j < noofsegments:
                segtemplate = segtemplate + segment + ','
            else:
                segtemplate = segtemplate + segment + "]}"
        
        qoscontext = dict()
        qoscontext['tempsegment'] = segtemplate
        qoscontext['velo_edge_config_id'] = obj_json['velo_edge_id'] 
        insertqos = insertqostemplate.render(**qoscontext)
        return insertqos 