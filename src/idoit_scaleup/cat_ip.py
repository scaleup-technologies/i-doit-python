from .consts import C__CATG__IP
from .category import IDoitCategory


class IDoitIP(IDoitCategory):

    CATEGORY = C__CATG__IP

    def __init__(self, cfg):
        super().__init__(cfg, self.CATEGORY)

    def convert_field_with_name_primary(self, data):
        if data['primary']['value']==None:
            return False
        return int(data['primary']['value'])

    def convert_field_with_name_active(self, data):
        if data['active']['value']==None:
            return False
        return int(data['active']['value'])

    def convert_field_with_name_use_standard_gateway(self, data):
        if data['use_standard_gateway']['value']==None:
            return False
        return int(data['use_standard_gateway']['value'])

    def convert_field_with_name_ipv4_address(self, data):
        return data['ipv4_address']['ref_title']

    def convert_field_with_name_ipv6_address(self, data):
        return data['ipv6_address']['ref_title']

    def convert_field_with_name_assigned_port(self,data):
        return data['assigned_port']['title']

    def convert_field_with_name_dns_domain(self, data):
        rtn=[]
        if 'dns_domain' in data and data['dns_domain'] is not None:
            for ele in data['dns_domain']:
                rtn.append(ele['title'])
        return rtn
