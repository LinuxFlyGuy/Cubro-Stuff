#Packetmaster EX device class for REST API interaction,  Use with firmware version 2.1.x or newer.

import requests, json, re
from requests.exceptions import ConnectionError
from getpass import getpass

#TO-DO Add code to handle case and verify input in all areas where needed
#add_rule_guided requires many input checks
#Add code to validate input for IPv6 as well as IPv4

#Add code to check and handle HTTPS for URIs
class PacketmasterEX(object):

    def __init__(self, address, username=None, password=None):
        self.address = address
        self.username = username
        self.password = password
        #self.https = False
        self.hardware_generation()
        self.get_port_count()
    #check whether web interface is using HTTP or HTTPS
    #def check_https(self):
        #try:
            # uri = 'http://' + self.address + '/rest/device/imageversion'
            # response = requests.get(uri, auth=(self.username, self.password))
            # r = response.status_code
            # if r == '200':
                #self.https = False

        #except:
    def get_port_count(self):
        uri = 'http://' + self.address + '/rest/ports/config?'
        ports = list()
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            r = response.content
            data = json.loads(r)
            count = 0
            for port in data['port_config']:
                ports.append(data['port_config'][count]['if_name'])
                count += 1
            self.ports = len(ports)
            return len(ports)
        except ConnectionError as e:
            raise e

    #Retrieve firmware version
    def firmware_version(self):
        uri = 'http://' + self.address + '/rest/device/imageversion?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            self.firmware = data['version']
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve IP configuration
    def ip_config(self):
        uri = 'http://' + self.address + '/rest/device/ipconfig?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            self.netmask = data['current_netmask']
            self.gateway = data['current_gateway']
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve Packetmaster model
    def device_model(self):
        uri = 'http://' + self.address + '/rest/device/model?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            self.model = data['model']
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e
        self.model = data['model']

    #Retrieve Packetmaster name
    def device_name(self):
        uri = 'http://' + self.address + '/rest/device/name?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            self.name = data['name']
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve Packetmaster Name plus Notes
    def device_label(self):
        uri = 'http://' + self.address + '/rest/device/customident?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            self.name = data['name']
            self.notes = data['notes']
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve hardware generation of the device
    def hardware_generation(self):
        uri = 'http://' + self.address + '/rest/device/generation?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            self.hardware = data['generation']
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve Packetmaster serial number
    def serial_number(self):
        uri = 'http://' + self.address + '/rest/device/serialno?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            self.serial = data['serial']
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve current port configuration
    def port_config(self):
        uri = 'http://' + self.address + '/rest/ports/config?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve port information
    def port_info(self):
        uri = 'http://' + self.address + '/rest/ports/info?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve port counters
    def port_statistics(self):
        uri = 'http://' + self.address + '/rest/ports/stats?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve SFP information
    def sfp_info(self):
        uri = 'http://' + self.address + '/rest/ports/sfpstatus?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            result = data['result']
            return json.dumps(result, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve active rules
    def rules_active(self):
        uri = 'http://' + self.address + '/rest/rules/all?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve active groups
    def groups_active(self):
        uri = 'http://' + self.address + '/rest/groups/all?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #List all available apps
    def device_apps(self):
        uri = 'http://' + self.address + '/rest/apps?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve running apps
    def apps_active(self):
        uri = 'http://' + self.address + '/rest/apps/running?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve hash algorithm information
    def hash_algorithms(self):
        uri = 'http://' + self.address + '/rest/device/grouphash?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve rule permanence mode
    def rule_permanence(self):
        uri = 'http://' + self.address + '/rest/device/permanentrulesmode?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve rule storage mode
    def storage_mode(self):
        uri = 'http://' + self.address + '/rest/device/rulestoragemode?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve environment information
    def env_info(self):
        uri = 'http://' + self.address + '/rest/device/environment?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve deice ID LED status_code
    def id_led(self):
        uri = 'http://' + self.address + '/rest/device/idled?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve load information
    def load_info(self):
        uri = 'http://' + self.address + '/rest/device/loadaverage?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve the maximum and currently used TCAM flows
    def tcam(self):
        uri = 'http://' + self.address + '/rest/flownumbers'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve memory usage
    def mem_free(self):
        uri = 'http://' + self.address + '/rest/device/memoryusage?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve cch machinery server revision
    def server_revision(self):
        uri = 'http://' + self.address + '/rest/device/serverrevision?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #List all save points
    def save_points(self):
        uri = 'http://' + self.address + '/rest/savepoints?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve Web Log
    def web_log(self):
        uri = 'http://' + self.address + '/rest/weblog'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve all users
    def get_users(self):
        uri = 'http://' + self.address + '/rest/users?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve User Authentication settings
    def user_uac(self):
        uri = 'http://' + self.address + '/rest/users/uac?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve RADIUS settings
    def get_radius(self):
        uri = 'http://' + self.address + '/rest/users/radius?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve DNS settings
    def get_dns(self):
        uri = 'http://' + self.address + '/rest/device/nameresolution?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Retrieve telnet service status_code
    def get_telnet(self):
        uri = 'http://' + self.address + '/rest/device/telnet?'
        try:
            response = requests.get(uri, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Change the management IP configuration with guided options
    def set_ip_config_guided(self):
        uri = 'http://' + self.address + '/rest/device/ipconfig?'
        newip = raw_input('Enter IP Address (e.g. 192.168.0.200): ').strip()
        newmask = raw_input('Enter Subnet Mask (e.g. 255.255.255.0): ').strip()
        newgate = raw_input('Enter gateway (e.g. 192.168.0.1): ').strip()
        #Implement checks to validate IP input
        params = {'ip': newip, 'mask': newmask, 'gw': newgate}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Change the management IP configuration with arguments
    def set_ip_config(self, address, netmask, gateway):
        uri = 'http://' + self.address + '/rest/device/ipconfig?'
        newip = address.strip()
        newmask = netmask.strip()
        newgate = gateway.strip()
        #Implement checks to validate IP input
        params = {'ip': newip, 'mask': newmask, 'gw': newgate}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Change the device name
    def set_name_guided(self):
        uri = 'http://' + self.address + '/rest/device/name?'
        newname = raw_input('Enter device name: ')
        params = {'name': newname}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    def set_name(self, name):
        uri = 'http://' + self.address + '/rest/device/name?'
        params = {'name': name}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    def set_label_guided(self):
        uri = 'http://' + self.address + '/rest/device/customident?'
        newname = raw_input('Enter device name: ')
        newnotes = raw_input('Enter device notes: ')
        params = {'name': newname,
                  'notes': newnotes}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    def set_label(self, name, notes):
        uri = 'http://' + self.address + '/rest/device/customident?'
        params = {'name': name,
                  'notes': notes}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Change the configuration of a port
    def set_port_config_guided(self):
        #Add additional parameters, add function to change multiple ports without exiting
        #Add provision to handle devices which require reboot for speed change e.g. EX2 (10G is XG)
        #Add shutdown true/false parameter for EX2 (more?)
        uri = 'http://' + self.address + '/rest/ports/config?'
        interface = raw_input('Enter the interface name of the port you want to change: ').strip()
        port_no = re.findall('[1-9][0-9/]*', interface)
        if len(port_no) == 1:
            interface = 'eth-0-' + port_no[0]
        else:
            error = 'that is not a valid port number; please try again'
            return error
        speed = raw_input('Enter the desired interface speed; options are  "10", "100", "1000", "10G", "40G", "100G", or "auto": ').strip()
        if speed.lower() == 'auto':
            speed = 'auto'
        else:
            speed = speed.upper() #More checks needed here
        duplex = raw_input('Enter the Duplex of the interface; options are "full", "half, or "auto": ').strip()
        if duplex.lower() =='auto' or duplex.lower() == 'full' or duplex.lower() == 'half':
            duplex = duplex.lower()
        else:
            print "That is not a valid duplex; defaulting to auto"
            duplex = 'auto'
        forcetx = raw_input('Force TX?  Enter "true" for yes and "false" for no: ').strip()
        forcetx = forcetx.lower()
        check = raw_input('Perform CRC check?  Enter "true" for yes and "false" for no: ').strip()
        check = check.lower()
        recalc = raw_input('Perform CRC recalculation?  Enter "true" for yes and "false" for no: ').strip()
        recalc = recalc.lower
        params = {
            'if_name': interface,
            'speed': speed,
            'duplex': duplex,
            'unidirectional': forcetx,
            'crc_check': check,
            'crc_recalculation': recalc }
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    def set_port_config(self, interface, speed='auto', duplex='auto', forcetx='true', check='false', recalc='false'):
        uri = 'http://' + self.address + '/rest/ports/config?'
        if_name = str(interface).strip()
        port_no = re.findall('[1-9][0-9/]*', if_name)
        if len(port_no) == 1:
            interface = 'eth-0-' + port_no[0]
        else:
            error = 'that is not a valid port number; please try again'
            return error
        if speed.lower() == 'auto':
            speed = 'auto'
        else:
            speed = speed.upper()
        if duplex.lower() =='auto' or duplex.lower() == 'full' or duplex.lower() == 'half':
            duplex = duplex.lower()
        else:
            print "That is not a valid duplex; defaulting to auto"
            duplex = 'auto'
        forcetx = forcetx.lower()
        check = check.lower()
        recalc = recalc.lower()
        params = {
            'if_name': interface,
            'speed': speed,
            'duplex': duplex,
            'unidirectional': forcetx,
            'crc_check': check,
            'crc_recalculation': recalc }
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Activate or deactivate a port
    def port_on_off_guided(self):
        uri = 'http://' + self.address + '/rest/ports/config?'
        interface = raw_input('Enter the interface name of the port you want to change: ').strip()
        port_no = re.find('[1-9][0-9/]*', interface)
        interface = 'eth-0-' + port_no
        updown = raw_input('Enter "true" to shut port down; Enter "false" to activate port [false]: ').lower()
        if updown == 'true':
            updown = True
        else:
            updown = False
        params = {'if_name': interface, 'shutdown': updown}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Reset Port Counters
    def delete_counters(self):
        uri = 'http://' + self.address + '/rest/ports/counters?'
        try:
            requests.delete(uri, auth=(self.username, self.password))
            success = 'Counters deleted successfully'
            return success
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Reset Rule Counters
    def reset_rule_counters(self):
        uri = 'http://' + self.address + '/rest/rules/counters?'
        try:
            requests.delete(uri, auth=(self.username, self.password))
            success = 'Counters deleted successfully'
            return success
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Add a rule with guided options
    def add_rule_guided(self):
        uri = 'http://' + self.address + '/rest/rules?'
        params = {}
        rulename = raw_input('Enter a name for the rule [none]: ')
        if rulename != '':
            params['name'] = rulename
        ruledescrip = raw_input('Enter a description for the rule [none]: ')
        if ruledescrip != '':
            params['description'] = ruledescrip
        priority = raw_input('Enter the priority level of the rule; 0 - 65535 higher number = higher priority [32768]: ')
        if priority != '':
            params['priority'] = int(priority)
        else:
            params['priority'] = 32768
        portin = raw_input('Enter the port number or numbers for incoming traffic; multiple ports separated by a comma: ')
        params['match[in_port]'] = portin
        print '''\nMatch VLAN tag?
                1 - No, match all tagged and untagged traffic
                2 - No, match only untagged traffic
                3 - Yes, match a VLAN tag \n'''
        trafmatch = raw_input('Enter the number of your selection [1]: ')
        if trafmatch == '' or int(trafmatch) == 1:
            pass
        elif int(trafmatch) == 2:
            params['match[vlan]'] = 'neg_match'
        elif int(trafmatch) == 3:
            params['match[vlan]'] = 'match'
            matchid = raw_input('Enter the VLAN ID to filter on: ')
            params['match[vlan_id]'] = matchid
            vpri = raw_input('Enter the VLAN priority (Enter 0-7) [0]: ')
            if vpri == '':
                params['match[vlan_priority]'] = '0'
            else:
                vpri != ''
                try:
                    if int(vpri) >= 0 or int(vpri) <= 7:
                        params['match[vlan_priority]'] = vpri
                    else:
                        print "That is not a valid selection; VLAN priority defaulting to '0'"
                        params['match[vlan_priority]'] = '0'
                except:
                    print "That is not a valid selection; VLAN priority defaulting to '0'"
                    params['match[vlan_priority]'] = '0'
        else:
            error = 'That is not a valid selection; please try again \n'
            return error
        macsrc = raw_input('Filter by source MAC address?  Leave blank for no or enter MAC address: ')
        if macsrc != '':
            params['dl_src'] = macsrc
        macdst = raw_input('Filter by destination MAC address?  Leave blank for no or enter MAC address: ')
        if macdst != '':
            params['dl_dst'] = macdst
        print '''\nFilter on protocol?
                1 - No Protocol Filtering
                2 - ip
                3 - tcp
                4 - udp
                5 - sctp
                6 - icmp
                7 - arp
                8 - Enter Ethertype\n'''
        proto = raw_input('Enter the number of your selection [1]: ')
        if proto == '' or int(proto) == 1:
            pass
        elif int(proto) == 2:
            params['match[protocol]'] = 'ip'
            nwsrc = raw_input('Filter on source IP address?  Leave blank for no or enter IP address: ')
            if nwsrc != '':
                try:
                    nwsrc = re.findall('\A(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', nwsrc)
                    params['match[nw_src]'] = nwsrc[0]
                except:
                    return "That is not a valid IP address, canceling add rule."
            nwdst = raw_input('Filter on destination IP address?  Leave blank for no or enter IP address: ')
            if nwdst != '':
                try:
                    nwdst = re.findall('\A(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', nwdst)
                    params['match[nw_dst]'] = nwdst[0]
                except:
                    return "That is not a valid IP address, canceling add rule."
        elif int(proto) == 3:
            params['match[protocol]'] = 'tcp'
            nwsrc = raw_input('Filter on source IP address?  Leave blank for no or enter IP address: ')
            if nwsrc != '':
                try:
                    nwsrc = re.findall('\A(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', nwsrc)
                    params['match[nw_src]'] = nwsrc[0]
                except:
                    return "That is not a valid IP address, canceling add rule."
            nwdst = raw_input('Filter on destination IP address?  Leave blank for no or enter IP address: ')
            if nwdst != '':
                try:
                    nwdst = re.findall('\A(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', nwdst)
                    params['match[nw_dst]'] = nwdst[0]
                except:
                    return "That is not a valid IP address, canceling add rule."
            tcpsrc = raw_input('Filter on source port?  Leave blank for no or enter port number: ')
            if tcpsrc != '':
                params['match[tcp_src]'] = tcpsrc
            tcpdst = raw_input('Filter on destination port?  Leave blank for no or enter port number: ')
            if tcpdst != '':
                params['match[tcp_dst]'] = tcpdst
        elif int(proto) == 4:
            params['match[protocol]'] = 'udp'
            nwsrc = raw_input('Filter on source IP address?  Leave blank for no or enter IP address: ')
            if nwsrc != '':
                try:
                    nwsrc = re.findall('\A(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', nwsrc)
                    params['match[nw_src]'] = nwsrc[0]
                except:
                    return "That is not a valid IP address, canceling add rule."
            nwdst = raw_input('Filter on destination IP address?  Leave blank for no or enter IP address: ')
            if nwdst != '':
                try:
                    nwdst = re.findall('\A(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', nwdst)
                    params['match[nw_dst]'] = nwdst[0]
                except:
                    return "That is not a valid IP address, canceling add rule."
            udpsrc = raw_input('Filter on source port?  Leave blank for no or enter port number: ')
            if udpsrc != '':
                params['match[udp_src]'] = udpsrc
            udpdst = raw_input('Filter on destination port?  Leave blank for no or enter port number: ')
            if udpdst != '':
                params['match[udp_dst]'] = udpdst
        elif int(proto) == 5:
            params['match[protocol]'] = 'sctp'
            nwsrc = raw_input('Filter on source IP address?  Leave blank for no or enter IP address: ')
            if nwsrc != '':
                try:
                    nwsrc = re.findall('\A(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', nwsrc)
                    params['match[nw_src]'] = nwsrc[0]
                except:
                    return "That is not a valid IP address, canceling add rule."
            nwdst = raw_input('Filter on destination IP address?  Leave blank for no or enter IP address: ')
            if nwdst != '':
                try:
                    nwdst = re.findall('\A(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', nwdst)
                    params['match[nw_dst]'] = nwdst[0]
                except:
                    return "That is not a valid IP address, canceling add rule."
            sctpsrc = raw_input('Filter on source port?  Leave blank for no or enter port number: ')
            if sctpsrc != '':
                params['match[sctp_src]'] = sctpsrc
            sctpdst = raw_input('Filter on destination port?  Leave blank for no or enter port number: ')
            if sctpdst != '':
                params['match[sctp_dst]'] = sctpdst
        elif int(proto) == 6:
            params['match[protocol]'] = 'icmp'
            nwsrc = raw_input('Filter on source IP address?  Leave blank for no or enter IP address: ')
            if nwsrc != '':
                try:
                    nwsrc = re.findall('\A(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', nwsrc)
                    params['match[nw_src]'] = nwsrc[0]
                except:
                    return "That is not a valid IP address, canceling add rule."
            nwdst = raw_input('Filter on destination IP address?  Leave blank for no or enter IP address: ')
            if nwdst != '':
                try:
                    nwdst = re.findall('\A(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', nwdst)
                    params['match[nw_dst]'] = nwdst[0]
                except:
                    return "That is not a valid IP address, canceling add rule."
            icmpt = raw_input('Flter on ICMP type?  Leave blank for no or enter ICMP type number: ')
            if icmpt != '':
                params['match[icmp_type]'] = icmpt
            icmpc = raw_input('Flter on ICMP code?  Leave blank for no or enter ICMP code number: ')
            if icmpc != '':
                params['match[icmp_code]'] = icmpc
        elif int(proto) == 7:
            params['match[protocol]'] = 'arp'
        elif int(proto) == 8:
            params['match[protocol]'] = 'custom'
            ether = raw_input('Enter Ethertype e.g. 0x800: ')
            if ether != '':
                params['match[dl_type]'] = ether
            nwproto = raw_input('Enter protocol number (protocol number in IPv4, header type in IPv6, opcode in ARP) or leave blank for none: ')
            if nwproto != '':
                params['match[nw_proto]'] = nwproto
        else:
            error = 'That is not a valid selection; please try again \n'
            return error
        print '''\nAdd Custom Extra Match?
        e.g. hard_timeout, idle_timeout, tcp_flags, Q in Q
        Leave blank for none
        Improper syntax will cause Add Rule to fail \n'''
        extra = raw_input('Enter Extra Custom Match String: ')
        if extra != '':
            params['match[extra]'] = extra
        ruleaction = raw_input('Enter the desired output actions separated by commas; order matters - improper syntax will cause add rule to fail: ')
        params['actions'] = ruleaction
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Add rule by providing all parameters
    def add_rule(self, params):
        uri = 'http://' + self.address + '/rest/rules?'
        if type(params) != 'dict':
            return "That is not a valid format for rule; please provide a dictionary object with valid rule parameters."
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Add a group with guided options
    def add_group_guided(self):
        uri = 'http://' + self.address + '/rest/groups?'
        name = raw_input("Enter the group ID: ")
        try:
            input_check = int(name)
        except:
            return "That is not a valid group ID, canceling Add Group."
        existing = []
        all_groups = self.groups_active()
        json_groups = json.loads(all_groups)
        count = 0
        for group in json_groups['groups']:
            existing.append(json_groups['groups'][count]['group_id'])
            count +=1
        if name in existing:
            return "A group with this group ID already exists; use Modify Group or select a different group ID. Canceling Add Group"
        description = raw_input("Enter the group description: ")
        group_type = raw_input(""" Select the group type:
                                1 - All
                                2 - Select
                                3 - Fast Failover
                                Enter the number of your selection: """)
        try:
            group_type = int(group_type)
        except:
            return "That is not a valid group type selection; canceling Add Group."
        if group_type == 1:
            type_group = 'all'
        elif group_type == 2:
            type_group = 'select'
        elif group_type == 3:
            type_group = 'ff'
        else:
            return "That is not a valid group type selection; canceling Add Group."
        bucket_list = []
        buckets = raw_input("How many buckets in this port group?  Must be at least 2 and no more than 16: ")
        try:
            buckets = int(buckets)
        except:
            return "That is not a valid bucket number; canceling Add Group."
        if buckets >= 2 and buckets <= 16:
            for bucket in xrange(buckets):
                print "\nConfigure settings for bucket %s" % bucket
                #Add check against number of ports on device
                output = raw_input("Output on which port: ")
                try:
                    input_check = int(output)
                    output = 'output:' + output
                except:
                    return "That is not a valid port number; canceling Add Group"
                actions = output
                if self.hardware != '4':
                    watch = raw_input("Set watch port to: ")
                    try:
                        input_check = int(watch)
                    except:
                        return "That is not a valid port number; canceling Add Group"
                push_vlan = raw_input('Push VLAN ID to outout traffic? Enter VLAN ID or leave blank for no: ').strip()
                if push_vlan != '':
                    try:
                        vlan = str(int(push_vlan) + 4096)
                        vlan = 'push_vlan:0x8100,set_field:' + vlan + '->vlan_vid,'
                        actions = vlan + actions
                    except:
                        return "That is not a valid VLAN ID, canceling Add Group."
                else:
                    mod_vlan = raw_input('Modify VLAN ID of output traffic? Enter VLAN ID or leave blank for no: ').strip()
                    if mod_vlan != '':
                        try:
                            vlan = str(int(mod_vlan) + 4096)
                            vlan = 'set_field:' + vlan + '->vlan_vid,'
                            actions = vlan + actions
                        except:
                            return "That is not a valid input for VLAN ID, canceling Add Group."
                    else:
                        strip_vlan = raw_input('Strip VLAN ID from output traffic?  Y or N [N]: ').lower()
                        if strip_vlan == 'y' or strip_vlan == 'yes':
                            actions = 'strip_vlan,' + actions
                if self.hardware == '4':
                    pop_l2 = raw_input('Pop all L2 information from packet?  Y or N [N]: ').lower()
                    if pop_l2 == 'y' or pop_l2 == 'yes':
                        actions = 'pop_l2,' + actions
                if self.hardware == '4':
                    pop_mpls = raw_input('Pop MPLS tags? In most cases you should also push L2.  Y or N [N]: ').lower()
                    if pop_mpls == 'y' or pop_mpls == 'yes':
                        actions = 'pop_all_mpls,' + actions
                if self.hardware == '4':
                    push_l2 = raw_input('Push L2 information to output packets?  Y or N [N]: ').lower()
                    if push_l2 == 'y' or push_l2 == 'yes':
                        print "Be sure to modify destination MAC when prompted or an error will occur."
                        actions = 'push_l2,' + actions
                src_mac = raw_input('Modify source MAC address?  Enter new MAC address or leave blank for no: ').strip()
                if src_mac != '':
                    ations = 'set_field:' + src_mac + '->eth_src,' + actions
                dst_mac = raw_input('Modify destination MAC address?  Enter new MAC address or leave blank for no: ').strip()
                if dst_mac != '':
                    ations = 'set_field:' + dst_mac + '->eth_dst,' + actions
                dst_ip = raw_input('Modify destination IP address?  Enter new IP address or leave blank for no: ').strip()
                if dst_ip != '':
                    try:
                        dstip = re.findall('\A(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', dst_ip)
                        actions = 'set_field:' + dstip[0] + '->ip_dst,' + actions
                    except:
                        return "That is not a valid input for IP address, canceling Add Group."
                if self.hardware == '4':
                    src_udp = raw_input('Modify source UDP port?  Enter new port number or leave blank for no: ').strip()
                    if src_udp != '':
                        try:
                            test_input = int(src_udp)
                            actions = 'set_field:' + src_udp + '->udp_src,' + actions
                        except:
                            return "That is not a valid input for port number; canceling Add Group."
                dst_udp = raw_input('Modify destination UDP port?  Enter new port number or leave blank for no: ').strip()
                if dst_udp != '':
                    try:
                        test_input = int(dst_udp)
                        actions = 'set_field:' + dst_udp + '->udp_dst,' + actions
                    except:
                        return "That is not a valid input for port number; canceling Add Group."
                if self.hardware == '4':
                    src_tcp = raw_input('Modify source TCP port?  Enter new port number or leave blank for no: ').strip()
                    if src_tcp != '':
                        try:
                            test_input = int(src_tcp)
                            actions = 'set_field:' + src_tcp + '->tcp_src,' + actions
                        except:
                            return "That is not a valid input for port number; canceling Add Group."
                dst_tcp = raw_input('Modify destination TCP port?  Enter new port number or leave blank for no: ').strip()
                if dst_tcp != '':
                    try:
                        test_input = int(dst_tcp)
                        actions = 'set_field:' + dst_tcp + '->tcp_dst,' + actions
                    except:
                        return "That is not a valid input for port number; canceling Add Group."
                if self.hardware != '4':
                    bucket_params = {'actions': actions,
                                     'watch_port': watch}
                else:
                    bucket_params = {'actions': actions}
                bucket_list.append(bucket_params)
        else:
            return "That is not a valid bucket number; canceling Add Group."
        params = { 'buckets': bucket_list,
                   'group_id': name,
                   'type': type_group,
                   'description': description
                 }
        params_json = json.dumps(params)
        try:
            response = requests.post(uri, json=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Add a group with arguments
    def add_group(self, gid, json_app):
        uri = 'http://' + self.address + '/rest/groups?'
        try:
            input_check = int(gid)
        except:
            return "That is not a valid group ID, canceling Add Group."
        existing = []
        all_groups = self.groups_active()
        json_groups = json.loads(all_groups)
        count = 0
        for group in json_groups['groups']:
            existing.append(json_groups['groups'][count]['group_id'])
            count +=1
        if gid in existing:
            return "A group with this group ID already exists; use Modify Group or select a different group ID. Canceling Add Group"
        try:
            input_check = json.loads(json_app)
        except:
            return "That is not a valid JSON object for Add Group.  Canceling Add Group."
        try:
            response = requests.post(uri, json=json_app, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Modify a group with guided options
    def modify_group_guided(self):
        uri = 'http://' + self.address + '/rest/groups?'
        name = raw_input("Enter the group ID of the group you would like to modify: ")
        try:
            input_check = int(name)
        except:
            return "That is not a valid group ID, canceling Modify Group."
        existing = []
        all_groups = self.groups_active()
        json_groups = json.loads(all_groups)
        count = 0
        for group in json_groups['groups']:
            existing.append(json_groups['groups'][count]['group_id'])
            count +=1
        if name not in existing:
            return "A group with this group ID does not exist; use Add Group. Canceling Modify Group"
        description = raw_input("Enter the new group description or leave blank to retain original: ")
        bucket_list = []
        buckets = raw_input("How many buckets in this port group?  Must be at least 2 and no more than 16: ")
        try:
            buckets = int(buckets)
        except:
            return "That is not a valid bucket number; canceling Modify Group."
        if buckets >= 2 and buckets <= 16:
            for bucket in xrange(buckets):
                print "\nConfigure settings for bucket %s" % bucket
                #Add check against number of ports on device
                output = raw_input("Output on which port: ")
                try:
                    input_check = int(output)
                    output = 'output:' + output
                except:
                    return "That is not a valid port number; canceling Modify Group"
                actions = output
                if self.hardware != '4':
                    watch = raw_input("Set watch port to: ")
                    try:
                        input_check = int(watch)
                    except:
                        return "That is not a valid port number; canceling Modify Group"
                push_vlan = raw_input('Push VLAN ID to outout traffic? Enter VLAN ID or leave blank for no: ').strip()
                if push_vlan != '':
                    try:
                        vlan = str(int(push_vlan) + 4096)
                        vlan = 'push_vlan:0x8100,set_field:' + vlan + '->vlan_vid,'
                        actions = vlan + actions
                    except:
                        return "That is not a valid VLAN ID, canceling Modify Group."
                else:
                    mod_vlan = raw_input('Modify VLAN ID of output traffic? Enter VLAN ID or leave blank for no: ').strip()
                    if mod_vlan != '':
                        try:
                            vlan = str(int(mod_vlan) + 4096)
                            vlan = 'set_field:' + vlan + '->vlan_vid,'
                            actions = vlan + actions
                        except:
                            return "That is not a valid input for VLAN ID, canceling Modify Group."
                    else:
                        strip_vlan = raw_input('Strip VLAN ID from output traffic?  Y or N [N]: ').lower()
                        if strip_vlan == 'y' or strip_vlan == 'yes':
                            actions = 'strip_vlan,' + actions
                if self.hardware == '4':
                    pop_l2 = raw_input('Pop all L2 information from packet?  Y or N [N]: ').lower()
                    if pop_l2 == 'y' or pop_l2 == 'yes':
                        actions = 'pop_l2,' + actions
                if self.hardware == '4':
                    pop_mpls = raw_input('Pop MPLS tags? In most cases you should also push L2.  Y or N [N]: ').lower()
                    if pop_mpls == 'y' or pop_mpls == 'yes':
                        actions = 'pop_all_mpls,' + actions
                if self.hardware == '4':
                    push_l2 = raw_input('Push L2 information to output packets?  Y or N [N]: ').lower()
                    if push_l2 == 'y' or push_l2 == 'yes':
                        print "Be sure to modify destination MAC when prompted or an error will occur."
                        actions = 'push_l2,' + actions
                src_mac = raw_input('Modify source MAC address?  Enter new MAC address or leave blank for no: ').strip()
                if src_mac != '':
                    ations = 'set_field:' + src_mac + '->eth_src,' + actions
                dst_mac = raw_input('Modify destination MAC address?  Enter new MAC address or leave blank for no: ').strip()
                if dst_mac != '':
                    ations = 'set_field:' + dst_mac + '->eth_dst,' + actions
                dst_ip = raw_input('Modify destination IP address?  Enter new IP address or leave blank for no: ').strip()
                if dst_ip != '':
                    try:
                        dstip = re.findall('\A(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', dst_ip)
                        actions = 'set_field:' + dstip[0] + '->ip_dst,' + actions
                    except:
                        return "That is not a valid input for IP address, canceling Modify Group."
                if self.hardware == '4':
                    src_udp = raw_input('Modify source UDP port?  Enter new port number or leave blank for no: ').strip()
                    if src_udp != '':
                        try:
                            test_input = int(src_udp)
                            actions = 'set_field:' + src_udp + '->udp_src,' + actions
                        except:
                            return "That is not a valid input for port number; canceling Modify Group."
                dst_udp = raw_input('Modify destination UDP port?  Enter new port number or leave blank for no: ').strip()
                if dst_udp != '':
                    try:
                        test_input = int(dst_udp)
                        actions = 'set_field:' + dst_udp + '->udp_dst,' + actions
                    except:
                        return "That is not a valid input for port number; canceling Modify Group."
                if self.hardware == '4':
                    src_tcp = raw_input('Modify source TCP port?  Enter new port number or leave blank for no: ').strip()
                    if src_tcp != '':
                        try:
                            test_input = int(src_tcp)
                            actions = 'set_field:' + src_tcp + '->tcp_src,' + actions
                        except:
                            return "That is not a valid input for port number; canceling Modify Group."
                dst_tcp = raw_input('Modify destination TCP port?  Enter new port number or leave blank for no: ').strip()
                if dst_tcp != '':
                    try:
                        test_input = int(dst_tcp)
                        actions = 'set_field:' + dst_tcp + '->tcp_dst,' + actions
                    except:
                        return "That is not a valid input for port number; canceling Modify Group."
                if self.hardware != '4':
                    bucket_params = {'actions': actions,
                                     'watch_port': watch}
                else:
                    bucket_params = {'actions': actions}
                bucket_list.append(bucket_params)
        else:
            return "That is not a valid bucket number; canceling Modify Group."
        params = { 'buckets': bucket_list,
                   'group_id': name,
                   'type': type_group,
                   'description': description
                 }
        params_json = json.dumps(params)
        try:
            response = requests.put(uri, json=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Modify a group with arguments
    def modify_group(self, gid, json_app):
        uri = 'http://' + self.address + '/rest/groups?'
        try:
            input_check = int(gid)
        except:
            return "That is not a valid group ID, canceling Modify Group."
        existing = []
        all_groups = self.groups_active()
        for item in all_groups['groups']:
            if item == 'group_id':
                existing.append(item[0])
        if gid not in existing:
            return "A group with this group ID does not exist; use Add Group. Canceling Modify Group"
        try:
            input_check = json.loads(json_app)
        except:
            return "That is not a valid JSON object for Modify Group.  Canceling Modify Group."
        try:
            response = requests.put(uri, json=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Delete all active groups
    def delete_groups_all(self):
        uri = 'http://' + self.address + '/rest/groups/all?'
        try:
            response = requests.delete(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Make a port save point active
    def set_port_savepoint_guided(self):
        uri = 'http://' + self.address + '/rest/savepoints/activeportsavepoint?'
        savename = raw_input('What is the name of the port save point to make active?: ')
        params = {'name': savename}
        try:
            response = requests.put(uri, data=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Make a rule save point active
    def set_rule_savepoint_guided(self):
        uri = 'http://' + self.address + '/rest/savepoints/activerulesavepoint?'
        savename = raw_input('What is the name of the rule save point to make active?: ')
        params = {'name': savename}
        try:
            response = requests.put(uri, data=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Set a save point as the default boot configuration
    def set_boot_savepoint_guided(self):
        uri = 'http://' + self.address + '/rest/savepoints/defaultrulesavepoint?'
        savename = raw_input('What is the name of the save point to make the default at boot configuration?: ')
        params = {'name': savename}
        try:
            response = requests.put(uri, data=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Export a save point from the Packetmaster This still needs worked out; Packetmaster returns empty save points
    def export_savepoint_guided(self):
        uri = 'http://' + self.address + '/rest/savepoints/export?'
        rspname = raw_input('What is the name of the rule save point to export? (leave blank for none): ')
        pspname = raw_input('What is the name of the port save point to export? (leave blank for none): ')
        params = {'rule_save_point_names': rspname, 'port_save_point_names': pspname}
        try:
            response = requests.get(uri, data=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            filename = raw_input("Enter a file name for the savepoint: ")
            try:
                with open(filename, "w") as f:
                    f.write(r)
            except:
                print "Invalid filename\n"
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Modify a port save point
    def modify_port_savepoint_guided(self):
        uri = 'http://' + self.address + '/rest/savepoints/modportsavepoint?'
        oldname = raw_input("What is the name of the save point you would like to modify?")
        newname = raw_input("What would you like to rename this save point to?")
        desc = raw_input("What is the description of the save point?")
        saveports = raw_input('Hit enter to save the current active ports to this save point; type "false" to not save them (This overwrites port configuration of the save point): ')
        params = {'oldname': oldname, 'newname': newname, 'description': desc, 'saveports': saveports}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Modify a rule save point
    def modify_rule_savepoint_guided(self):
        uri = 'http://' + self.address + '/rest/savepoints/modrulesavepoint?'
        oldname = raw_input("What is the name of the save point you would like to modify?")
        newname = raw_input("What would you like to rename this save point to?")
        desc = raw_input("What is the description of the save point?")
        saverules = raw_input('Hit enter to save the current active rules to this save point; type "false" to not save them (This overwrites rule configuration of the save point): ')
        params = {'oldname': oldname, 'newname': newname, 'description': desc, 'saverules': saverules}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Create a port save point from current configuration
    def create_port_savepoint_guided(self):
        uri = 'http://' + self.address + '/rest/savepoints/portsavepoint?'
        name = raw_input("What would you like to name the port save point?")
        desc = raw_input("Enter a description for the port save point")
        params = {'name': name, 'description': desc}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Create a quicksave point of current configuration
    def create_quick_savepoint(self):
        uri = 'http://' + self.address + '/rest/savepoints/quicksaverules?'
        try:
            response = requests.put(uri, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Create a rule save point from current configuration
    def create_rule_savepoint_guided(self):
        uri = 'http://' + self.address + '/rest/savepoints/rulesavepoint?'
        name = raw_input("What would you like to name the rule save point?")
        desc = raw_input("Enter a description for the rule save point")
        params = {'name': name, 'description': desc}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Delete a port save point
    def delete_port_savepoint_guided(self):
        uri = 'http://' + self.address + '/rest/savepoints/portsavepoint?'
        name = raw_input("What is the name of the port save point you would like to delete? ")
        params = {'name': name}
        try:
            response = requests.delete(uri, data=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Delete a rule save point
    def delete_rule_savepoint_guided(self):
        uri = 'http://' + self.address + '/rest/savepoints/rulesavepoint?'
        name = raw_input("What is the name of the rule save point you would like to delete? ")
        params = {'name': name}
        try:
            response = requests.delete(uri, data=params, auth=(self.username, self.password))
            # print response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    # Call a custom app action with guided options
    def call_app_action_guided(self):
        uri = 'http://' + self.address + '/rest/apps/action?'
        pid = raw_input('Enter the PID of the app instance: ')
        try:
            pid = int(pid)
        except:
            return "That is not a valid PID; canceling call app action."
        name = raw_input('Enter the name of the custom app action: ')
        params = {'pid': pid,
                  'action_name': name}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    # Call a custom app action with arguments
    def call_app_action(self, pid, name):
        uri = 'http://' + self.address + '/rest/apps/action?'
        try:
            pid = int(pid)
        except:
            return "That is not a valid PID; canceling call app action."
        params = {'pid': pid,
                  'action_name': name}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Change group hash algorithms with guided options
    def set_hash_algorithms_guided(self):
        uri = 'http://' + self.address + '/rest/device/grouphash?'
        macsa = raw_input('Type "true" to use MAC source address; type "false" to ignore [true]: ').lower()
        if macsa == 'false':
            macsa = False
        else:
            macsa = True
        macda = raw_input('Type "true" to use MAC destination address; type "false" to ignore [true]: ').lower()
        if macda == 'false':
            macda = False
        else:
            macda = True
        ether = raw_input('Type "true" to use ether type; type "false" to ignore [true]: ').lower()
        if ether == 'false':
            ether = False
        else:
            ether = True
        ipsa = raw_input('Type "true" to use IP source address; type "false" to ignore [true]: ').lower()
        if ipsa == 'false':
            ipsa = False
        else:
            ipsa = True
        ipda = raw_input('Type "true" to use IP destination address; type "false" to ignore [true]: ').lower()
        if ipda == 'false':
            ipda = False
        else:
            ipda = True
        proto = raw_input('Type "true" to use IP protocol; type "false" to ignore [true]: ').lower()
        if proto == 'false':
            proto = False
        else:
            proto = True
        src = raw_input('Type "true" to use source port; type "false" to ignore [true]: ').lower()
        if src == 'false':
            src = False
        else:
            src = True
        dst = raw_input('Type "true" to use destination port; type "false" to ignore [true]: ').lower()
        if dst == 'false':
            dst = False
        else:
            dst = True
        params = {'macsa': macsa,
                  'macda': macda,
                  'ether_type': ether,
                  'ipsa': ipsa,
                  'ipda': ipda,
                  'ip_protocol': proto,
                  'src_port': src,
                  'dst_port': dst}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Change group hash algorithms with arguments
    def set_hash_algorithms(self, macsa, madca, ether, ipsa, ipda, proto, src, dst):
        uri = 'http://' + self.address + '/rest/device/grouphash?'
        macsa = macsa.lower()
        if macsa == 'false':
            macsa = False
        else:
            macsa = True
        macda = macda.lower()
        if macda == 'false':
            macda = False
        else:
            macda = True
        ether = ether.lower()
        if ether == 'false':
            ether = False
        else:
            ether = True
        ipsa = ipsa.lower()
        if ipsa == 'false':
            ipsa = False
        else:
            ipsa = True
        ipda = ipda.lower()
        if ipda == 'false':
            ipda = False
        else:
            ipda = True
        proto = proto.lower()
        if proto == 'false':
            proto = False
        else:
            proto = True
        src = src.lower()
        if src == 'false':
            src = False
        else:
            src = True
        dst = dst.lower()
        if dst == 'false':
            dst = False
        else:
            dst = True
        params = {'macsa': macsa,
                  'macda': macda,
                  'ether_type': ether,
                  'ipsa': ipsa,
                  'ipda': ipda,
                  'ip_protocol': proto,
                  'src_port': src,
                  'dst_port': dst}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Change rule mode permanence with guided options
    def set_rule_permanence_guided(self):
        uri = 'http://' + self.address + '/rest/device/permanentrulesmode?'
        perm = raw_input('type "true" to turn on permanent rules; type "false" to turn them off [false]: ').lower()
        if perm == 'true':
            perm = True
        else:
            perm = False
        params = {'state': perm}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Change rule mode permanence with arguments
    def set_rule_permanence(self, permanence):
        uri = 'http://' + self.address + '/rest/device/permanentrulesmode?'
        perm = permanence.lower()
        if perm == 'true':
            perm = True
        else:
            perm == False
        params = {'state': perm }
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Set rule storage mode with guided options
    def set_storage_mode_guided(self):
        uri = 'http://' + self.address + '/rest/device/rulestoragemode?'
        mode = raw_input('''Select the rule storage mode:
                        1 - Simple
                        2 - IPv6
                        Enter the number of your selection: ''')
        try:
            mode = int(mode)
        except:
            return "That is not a valid selection; canceling set rule storage mode."
        if mode == 1:
            params = {'mode' : 'simple'}
        elif mode == 2:
            params = {'mode': 'ipv6'}
        else:
            return "That is not a valid selection; canceling set rule storage mode."
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Set rule storage mode
    def set_storage_mode(self, mode):
        uri = 'http://' + self.address + '/rest/device/rulestoragemode?'
        try:
            mode = mode.lower()
        except:
            return "That is not a valid setting; canceling set rule storage mode."
        if mode == 'simple':
            params = {'mode': 'simple'}
        elif mode == 'ipv6':
            params = {'mode': 'ipv6'}
        else:
            return "That is not a valid selection; canceling set rule storage mode."
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Add a user with guided option
    def add_user_guided(self):
        uri = 'http://' + self.address + '/rest/users?'
        username = raw_input('Enter a username: ').strip()
        if username == '':
            return "That is not a valid username; canceling add user."
        user_list = []
        active_users = self.get_users()
        json_users = json.loads(active_users)
        for user in json_users:
            user_list.append(json_users[user]['username'])
        if username in user_list:
            return "That username is already in use; use Modify User; canceling Add User."
        access_level = raw_input("""Choose an access level for the user:
                                1 - Read only
                                7 - Write
                               31 - Super User
                               Enter the numeric value for the access level: """).strip()
        try:
            access_level = int(access_level)
        except:
            return "That is not a valid user access level; canceling Add User."
        if access_level not in (1, 7, 31):
            return "That is not a valid user access level; canceling Add User."
        passwd = raw_input("Enter a password for the user: ")
        description = raw_input("Add a description for this user: ")
        rad = raw_input("Use RADIUS authentication?  Y or N [N]: ").lower()
        if rad == 'y' or rad == 'yes':
            rad = True
        else:
            rad = False
        params = {'username': username,
                  'accesslevel': access_level,
                  'password': passwd,
                  'description': description,
                  'radius': rad}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Add a user
    def add_user(self, username, access_level, passwd, description='', rad=False):
        uri = 'http://' + self.address + '/rest/users?'
        user_list = []
        active_users = self.get_users()
        json_users = json.loads(active_users)
        for user in json_users:
            user_list.append(json_users[user]['username'])
        if username in user_list:
            return "That username is already in use; use Modify User; canceling Add User."
        try:
            access_level = int(access_level)
        except:
            return "That is not a valid user access level; canceling Add User."
        if access_level not in (1, 7, 31):
            return "That is not a valid user access level; canceling Add User."
        if rad in (True, 'true', 'True', 'Y', 'Yes', 'y', 'yes'):
            rad = True
        else:
            rad = False
        params = {'username': username,
                  'accesslevel': access_level,
                  'password': passwd,
                  'description': description,
                  'radius': rad}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Modify a user with guided options
    def mod_user_guided(self):
        uri = 'http://' + self.address + '/rest/users?'
        cur_name = raw_input('What is the username you would like to modify: ')
        user_list = []
        active_users = self.get_users()
        json_users = json.loads(active_users)
        for user in json_users:
            user_list.append(json_users[user]['username'])
        if cur_name not in user_list:
            return "That username does not exist; please use Add User.  Canceling Modify User."
        new_name = raw_input('Enter a new username: ')
        if new_name in user_list:
            return "The newly entered user name is already in use; canceling Modify User."
        description = raw_input("Enter a new description; this will overwrite the old description: ")
        access_level = raw_input("""Choose an access level for the user:
                                1 - Read only
                                7 - Write
                               31 - Super User
                               Enter the numeric value for the access level: """).strip()
        try:
            access_level = int(access_level)
        except:
            return "That is not a valid user access level; canceling Modify User."
        if access_level not in (1, 7, 31):
            return "That is not a valid user access level; canceling Modify User."
        passwd = raw_input("Enter a new password for the user: ")
        rad = raw_input("Use RADIUS authentication?  Y or N [N]: ").lower()
        if rad in ('y', 'yes'):
            rad = True
        else:
            rad = False
        params = {'username': cur_name,
                  'new_username': new_name,
                  'accesslevel': access_level,
                  'password': passwd,
                  'description': description,
                  'radius': rad}
        try:
            response = requests.put(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Modify a user
    def mod_user(self, cur_name, new_name, access_level, passwd, description='', rad=False ):
        uri = 'http://' + self.address + '/rest/users?'
        user_list = []
        active_users = self.get_users()
        json_users = json.loads(active_users)
        for user in json_users:
            user_list.append(json_users[user]['username'])
        if cur_name not in user_list:
            return "That username does not exist; please use Add User.  Canceling Modify User."
        if new_name in user_list:
            return "The newly entered user name is already in use; canceling Modify User."
        try:
            access_level = int(access_level)
        except:
            return "That is not a valid user access level; canceling Modify User."
        if access_level not in (1, 7, 31):
            return "That is not a valid user access level; canceling Modify User."
        if rad in (True, 'true', 'True', 'Y', 'Yes', 'y', 'yes'):
            rad = True
        else:
            rad = False
        params = {'username': cur_name,
                  'new_username': new_name,
                  'accesslevel': access_level,
                  'password': passwd,
                  'description': description,
                  'radius': rad}
        try:
            response = requests.put(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Delete a user with guided options
    def delete_user_guided(self):
        uri = 'http://' + self.address + '/rest/users?'
        username = raw_input('What is the user name to delete: ')
        user_list = []
        active_users = self.get_users()
        json_users = json.loads(active_users)
        for user in json_users:
            user_list.append(json_users[user]['username'])
        if username not in user_list:
            return "That username does not exist"
        params = {'name': username}
        try:
            response = requests.delete(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Delete a user
    def delete_user(self, username):
        uri = 'http://' + self.address + '/rest/users?'
        user_list = []
        active_users = self.get_users()
        json_users = json.loads(active_users)
        for user in json_users:
            user_list.append(json_users[user]['username'])
        if username not in user_list:
            return "That username does not exist"
        params = {'name': username}
        try:
            response = requests.delete(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Turn mandatory user authentication on or off with guided options
    def set_uac_guided(self):
        uri = 'http://' + self.address + '/rest/users/uac?'
        access = raw_input('type "true" to turn on UAC; type "false" to turn it off [false]: ').lower()
        if access == 'true':
            access = True
        else:
            access = False
        params = {'state': access }
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Turn mandatory user authentication on or off with arguments
    def set_uac(self, uac):
        uri = 'http://' + self.address + '/rest/users/uac?'
        access = uac.lower()
        if access == 'true':
            access = True
        else:
            access = False
        params = {'state': access }
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Set RADIUS settings with guided options
    def set_radius_guided(self):
        uri = 'http://' + self.address + '/rest/users/radius?'
        server = raw_input('Enter the IP address of the RADIUS server: ').strip()
        port = raw_input('Enter the UDP port of the RADIUS server [1812]: ')
        if port == '':
            port = 1812
        try:
            port = int(port)
        except:
            return "That is not a valid port input; canceling RADIUS settings call."
        print "Enter the RADIUS secret."
        secret = getpass()
        level = raw_input('''Enter the RADIUS login level.
        Determines the user access level that a user has logging in via RADIUS but without a local user account.
                             0 - no access
                             1 - read access
                             7 - write access
                            31 - super user access
                            [0]: ''')
        try:
            level = int(level)
        except:
            return "That is not a valid input for login level; canceling RADIUS settings call."
        print level
        if level == 0 or level == 1 or level == 7 or level == 31:
            level = level
        else:
            print "That is not a valid input for login level; setting RADIUS login level to 0"
            level = 0
        refresh = raw_input("Enter the refresh rate of the RADIUS session in seconds: ")
        try:
            refresh = int(refresh)
        except:
            return "That is not a valid input for refresh rate; canceling RADIUS settings call."
        params = {'server': server,
                  'port': port,
                  'secret': secret,
                  'radius_login_level': level,
                  'refresh_rate': refresh}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Set RADIUS settings with arguments
    def set_radius(self, server=None, port=1812, secret=None, level=None, refresh=None):
        uri = 'http://' + self.address + '/rest/users/radius?'
        server = server.strip()
        try:
            port = int(port)
        except:
            return "That is not a valid port input; canceling RADIUS settings call."
        try:
            level = int(level)
        except:
            return "That is not a valid input for login level; canceling RADIUS settings call."
        if level == 0 or level == 1 or level == 7 or level == 31:
            level = level
        else:
            print "That is not a valid input for login level; setting RADIUS login level to 0"
            level = 0
        try:
            refresh = int(refresh)
        except:
            return "That is not a valid input for refresh rate; canceling RADIUS settings call."
        params = {'server': server,
                  'port': port,
                  'secret': secret,
                  'radius_login_level': level,
                  'refresh_rate': refresh}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Turn HTTPS secure web interface on or off with guided options
    def set_https_guided(self):
        uri = 'http://' + self.address + '/rest/device/https?'
        enabled = raw_input('Type "true" to enable HTTPS on web interface; type "false" to turn it off [false]: ').lower()
        if enabled == 'true':
            enabled = True
            print ("Please enter the SSL password")
            ssl = getpass()
        else:
            enabled = False
            ssl = 'none'
        params = {'https_enabled': enabled,
                  'ssl_password': ssl}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = "No Response"
            raise e

    #Turn HTTPS secure web interface on or off with arguments
    def set_https(self, enabled=False, ssl=None):
        uri = 'http://' + self.address + '/rest/device/https?'
        if enabled.lower() == 'true':
            enabled = True
        else:
            enabled = False
        params = {'https_enabled': enabled,
                  'ssl_password': ssl}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = "No Response"
            raise e

    #Turn Telnet service on or off with guided options
    def set_telnet_guided(self):
        uri = 'http://' + self.address + '/rest/device/telnet?'
        enabled = raw_input('Type "true" to enable Telnet; type "false" to turn it off [false]: ').lower()
        if enabled == 'true':
            enabled = True
        else:
            enabled = False
        params = {'activated': enabled}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = "No Response"
            raise e

    #Turn Telnet service on or off with arguments
    def set_telnet(self, enabled=False):
        uri = 'http://' + self.address + '/rest/device/telnet?'
        if enabled.lower() == 'true':
            enabled = True
        else:
            enabled = False
        params = {'activated': enabled}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = "No Response"
            raise e

    #Delete Web Logs
    def del_web_log(self):
        uri = 'http://' + self.address + '/rest/weblog?'
        try:
            response = requests.delete(uri, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Set DNS server settings with guided options
    def set_dns_guided(self):
        uri = 'http://' + self.address + '/rest/device/nameresolution?'
        params = {}
        print 'You may set up to three DNS servers.'
        dns1 = raw_input('Enter the IP address of the first DNS server or leave blank for none [none]: ').strip()
        if dns1 != '':
            params['dns1'] = dns1
        dns2 = raw_input('Enter the IP address of the second DNS server or leave blank for none [none]: ').strip()
        if dns2 != '':
            params['dns2'] = dns2
        dns3 = raw_input('Enter the IP address of the third DNS server or leave blank for none [none]: ').strip()
        if dns3 != '':
            params['dns3'] = dns3
        if len(params) > 0:
            try:
                response = requests.post(uri, data=params, auth=(self.username, self.password))
                code = response.status_code
                r = response.content
                data = json.loads(r)
                return json.dumps(data, indent=4)
            except ConnectionError as e:
                r = 'No Response'
                raise e
        else:
            return 'No valid DNS server addresses given'

    #Set DNS server settings
    def set_dns(self, dns1=None, dns2=None, dns3=None):
        uri = 'http://' + self.address + '/rest/device/nameresolution?'
        params = {}
        if dns1 != '':
            params['dns1'] = dns1
        if dns2 != '':
            params['dns2'] = dns2
        if dns3 != '':
            params['dns3'] = dns3
        if len(params) > 0:
            try:
                response = requests.post(uri, data=params, auth=(self.username, self.password))
                code = response.status_code
                r = response.content
                data = json.loads(r)
                return json.dumps(data, indent=4)
            except ConnectionError as e:
                r = 'No Response'
                raise e
        else:
            return 'No valid DNS server addresses given'

    #Turn the ID LED on or off with guided options
    def set_id_led_guided(self):
        uri = 'http://' + self.address + '/rest/device/idled?'
        led = raw_input('type "true" to turn the ID LED on; type "false" to turn it off [false]: ').lower()
        if led == 'true':
            led = True
        else:
            led = False
        params = {'activated': led}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Turn the ID LED on or off with arguments
    def set_id_led(self, led):
        uri = 'http://' + self.address + '/rest/device/idled?'
        led = led.lower()
        if led == 'true':
            led = True
        else:
            led = False
        params = {'activated': led}
        try:
            response = requests.post(uri, data=params, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Restart Web Server without rebooting the device
    def restart_webserver(self):
        uri = 'http://' + self.address + '/rest/device/restartwebserver'

        try:
            response = requests.post(uri, auth=(self.username, self.password))
            code = response.status_code
            r = response.content
            data = json.loads(r)
            return json.dumps(data, indent=4)
        except ConnectionError as e:
            r = 'No Response'
            raise e

    #Reboot the Packetmaster
    def reboot(self):
        uri = 'http://' + self.address + '/rest/device/reboot?'

        try:
            requests.post(uri, auth=(self.username, self.password))
            message = 'Device is rebooting...please allow 2 to 3 minutes for it to complete'
            return message
        except ConnectionError as e:
            r = 'No Response'
            raise e
