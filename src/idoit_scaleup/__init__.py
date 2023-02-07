from .object import IDoitObject
from . import consts
from pprint import pprint
from .cat_access import IDoitAccess
from .cat_connector import IDoitConnector
from .cat_cpu import IDoitCpu
from .cat_ip import IDoitIP
from .cat_location import IDoitLocation
from .cat_memory import IDoitMemory
from .cat_network import IDoitNetwork
from .cat_networkport import IDoitNetworkPort
from .cat_power_consumer import IDoitPowerConsumer
from .cat_racktables import Racktables
from .cat_vlan import IDoitVlan
from .category import IDoitCategory
from .conditional_read import IDoitConditionalRead
from .dialog import IDoitDialog
from .search import IDoitSearch
from .cat_storage_device import IDoitStorageDevice


def createApiCall(cfg, category):
    if category == consts.C__CATG__ACCESS:
        return IDoitAccess(cfg)
    if category == consts.C__CATG__CONNECTOR:
        return IDoitConnector(cfg)
    if category == consts.C__CATG__CUSTOM_FIELDS_RACKTABLES:
        return Racktables(cfg)
    if category == consts.C__CATG__IP:
        return IDoitIP(cfg)
    if category == consts.C__CATG__LOCATION:
        return IDoitLocation(cfg)
    if category == consts.C__CATG__MEMORY:
        return IDoitMemory(cfg)
    if category == consts.C__CATG__NETWORK_PORT:
        return IDoitNetworkPort(cfg)
    if category == consts.C__CATG__POWER_CONUMER:
        return IDoitPowerConsumer(cfg)
    if category == consts.C__CATG__CPU:
        return IDoitCpu(cfg)
    if category == consts.C__CATG__STORAGE_DEVICE:
        return IDoitStorageDevice(cfg)
    if category == consts.C__CATS__NET:
        return IDoitNetwork(cfg)
    if category == consts.C__CATS__LAYER2_NET:
        return IDoitVlan(cfg)
    if category.startswith('C__OBJTYPE__'):
        return IDoitObject(cfg, category)
    if category.startswith('C__CATS__') or category.startswith('C__CATG__'):
        return IDoitCategory(cfg, category)
    return None


def createApiCalls(cfg):
    rtn = {}
    for varname in consts.__dict__.keys():
        if not (varname in rtn.keys()):
            rtn[varname] = createApiCall(cfg, varname)
    return rtn


def createApiDialogs(cfg, category, field):
    if 'dialogs' not in cfg.keys():
        cfg['dialogs'] = {}
    if category not in cfg['dialogs'].keys():
        cfg['dialogs'][category] = {}
    if field not in cfg['dialogs'][category].keys():
        cfg['dialogs'][category][field] = IDoitDialog(cfg, category, field)
    return cfg['dialogs'][category][field]


def search(cfg):
    return IDoitSearch(cfg, 'no_type')


def conditional_read(cfg):
    return IDoitConditionalRead(cfg, 'no_type')
