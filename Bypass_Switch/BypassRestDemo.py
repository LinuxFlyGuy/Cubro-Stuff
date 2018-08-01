#Python2.7 Cubro Copper Bypass Switch REST API demo.

#!/usr/bin/python

#Import necessary libraries
from bypassswitch_rest import BypassSwitch

def set_ip():
    """Set the management IP address of Bypass Switch to manage."""
    fail_count = 0
    while fail_count < 3:
        address = raw_input('Enter the IP Address of the Bypass Switch you want to manage: ')
        try:
            ip_address = re.findall('\A(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', address)
            address = ip_address[0]
            return address
        except:
            print "That is not a valid IPv4 address."
            fail_count += 1
    print "That is not a valid IPv4 address.  Exiting"
    exit()

if __name__ == '__main__':
    #Print welcome statement
    print 'Welcome to the Cubro Bypass Switch REST Demo\n'
    #Define IP address of the Bypass Switch
    address = set_ip()
    bypass = BypassSwitch(address)

    def menu():
        """Menu for Bypass Switch management options."""
        global address, bypass
        print '\nWorking with Bypass Switch at %s \n' % address
        print '''Make Selection:
                1 - Engage Bypass
                2 - Disengage Bypass
                3 - Timeout
                4 - Set Management Configuration
                5 - Change working device
                6 - Quit\n'''
        choice = raw_input('Enter the number of your selection: ')
        #Evaluate user selection
        if int(choice) == 1:
            on = bypass.engage()
            print on
            menu()
        elif int(choice) == 2:
            off = bypass.disengage()
            print off
            menu()
        elif int(choice) == 3:
            timeout = bypass.timeout()
            print timeout
            menu()
        elif int(choice) == 4:
            mgmt = bypass.set_config_guided()
            print mgmt
            menu()
        elif int(choice) == 5:
            address = set_ip()
            bypass = BypassSwitch(address)
            menu()
        elif int(choice) == 6:
            print 'Goodbye'
            exit()
        else:
            print "That is not a valid choice"
        menu()

    menu()
