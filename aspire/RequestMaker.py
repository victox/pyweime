'''
Created on 2013-5-22

@author: luojie
'''

import defs
import urllib2
import urllib

class RequestMaker(object):
    '''
    classdocs
    '''
    

    def __init__(self, appkey, devid, sign, json = False):
        self.appkey = appkey
        self.devid = devid
        self.sign = sign
        self.json = json
    
    def headers(self):
        return {}
    
    def requestWithParams(self, params):
        
        action = params.pop('action')
        url = defs.SERVER_URL + action + ('.json' if self.json else '.xml')
        request = urllib2.Request(url)
        
        for k, v in self.headers():
            request.add_header(k, v)
        
        params['app_key'] = self.appkey
        params['device_id'] = self.devid
        params['sign'] = self.sign
        
        enc_params = urllib.urlencode(params)
        request.add_data(enc_params)
        
        rsp = urllib2.urlopen(request)
        return rsp