# -*- coding: utf-8 -*-
# @Author: Lorenzo
# @Date:   2017-10-03 10:56:02
# @Last Modified by:   Lorenzo
# @Last Modified time: 2018-09-03 18:08:10

import json
from microchip.ateccx08a import ateccx08a

def load_from_resource(mresource):
    mstream = open(mresource)
    barray = bytearray()
    while True:
        rd = mstream.read(1)
        if not rd:
            barray.append(0x0)
            break
        barray.append(rd[0])
    return barray

def load_thing_conf():
    confstream = open('resource://thing.conf.json')
    conf = ''
    while True:
        line = confstream.readline()
        if not line:
            break
        conf += line
    return json.loads(conf)

conf2atecctype = {
    'ATECC508A': ateccx08a.DEV_ATECC508A,
    'ATECC608A': ateccx08a.DEV_ATECC608A
}

conf2ateccclass = {
    'ATECC508A': ateccx08a.ATECC508A,
    'ATECC608A': ateccx08a.ATECC608A
}