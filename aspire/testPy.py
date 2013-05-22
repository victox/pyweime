'''
Created on 2013-5-21

@author: luojie
'''
import defs
import sys
import utils
import json
from xml.etree import ElementTree
from xml.etree.ElementTree import iterparse

from RequestMaker import RequestMaker

if __name__ == '__main__':
    print sys.version
    
    xml_maker = RequestMaker(defs.APP_KEY, utils.device_id(),
                          utils.signed_device_id())
    try:
        rsp = xml_maker.requestWithParams({'action':'system_config', 'ver':defs.VERSION, 
                             'client':defs.CLIENT, 'active':'0'})
    except:
        print 'request fail'
        sys.exit()
    
    print rsp.info()
#     print rsp.read()
    
#     system_config = ElementTree.parse(rsp).getroot()
#     d =  utils.elem2dict(system_config)
#     print json.dumps(d, indent = 4, ensure_ascii = False)

    d = utils.xml2dict(rsp)
    print json.dumps(d, indent = 2, ensure_ascii = False)
    
    '''
    json_maker = RequestMaker(defs.APP_KEY, utils.device_id(),
                          utils.signed_device_id(), True)
    try:
        rsp = json_maker.requestWithParams({'action':'recommend_user', 'gender':'',
                                   'page':'1', 'size':'3'})
    except:
        print 'request fail'
        sys.exit()
    
    print rsp.info()
    recommend_user = json.load(rsp)
    print recommend_user
#     user_list = recommend_user['data']['recommend_user_list']
#     for uid, info in user_list.items():
#         print uid, info
    '''