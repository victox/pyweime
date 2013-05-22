'''
Created on 2013-5-22

@author: luojie
'''

import defs
from xml.etree.ElementTree import iterparse

def md5(data):
    import hashlib
    h = hashlib.md5()
    h.update(data)
    return h.hexdigest()

def mac_address():
    import uuid
    node = uuid.getnode()
    mac = uuid.UUID(int = node).hex[-12:]
    return '-'.join([mac[x:x+2] for x in range(0, len(mac), 2)])

def device_id():
    devid = mac_address()
    return devid

def signed_device_id(devid = None):
    devid = devid or device_id()
    devid = defs.DEVICE_KEY + devid
    return md5(devid)

def elem2dict(elem):
    d = {}
    children = elem.getchildren()
    if not children:
        return elem.text
    else:
        for child in children:
            d[child.tag] = elem2dict(child)
        return d

def xml2dict(xml):
    ret = {}
    stack = [ret]
    for event, node in iterparse(xml, ['start', 'end']):
        if event == 'start':
            last = stack[len(stack)-1]
            if node.getchildren():
                d = {}
                last[node.tag] = d
                stack.append(d)
            else:
                last[node.tag] = node.text
                stack.append('')
            
        elif event == 'end':
            stack.pop()
    return ret
            
    
    