"""
Created on Jan 2018
@author: LauraMP
"""
import ipaddress
import re
import collections

def exe1():
	while True:
		ip=(raw_input("Enter ip Address: "))

		try:
			ip=unicode(ip, "utf-8")
			ip=ipaddress.ip_address(ip)
			break
		except ValueError:
			print("Invalid ip address format")
		except KeyboardInterrupt:
			print "Abort...."
			exit

	while True:
		try:
			mask=(raw_input("Enter subnet mask in decimal format: "))

			if(int(mask[1:])>30 or int(mask[1:])<0 or mask[0] != '/'):
				raise
			break
		except KeyboardInterrupt:
			print "Abort...."
			exit
		except:
			print("Subnet mask is invalid")

	binmask = list();

	for i in range(32):
		binmask.append((str(int(i<int(mask[1:])))))

	moct1 = binmask[0:8]
	moct2 = binmask[8:16]
	moct3 = binmask[16:24]
	moct4 = binmask[24:32]

	ls=str(ip).split(".")

	oct1 = int(ls[0]) & int(''.join(moct1),2)
	oct2 = int(ls[1]) & int(''.join(moct2),2)
	oct3 = int(ls[2]) & int(''.join(moct3),2)
	oct4 = int(ls[3]) & int(''.join(moct4),2)

	all =str(oct1) +"."+ str(oct2) +"."+ str(oct3) +"."+ str(oct4) + mask 

	all=unicode(all, "utf-8")
	all=ipaddress.ip_network(all)

	print ("network address is: " + (str(all.network_address)))
	print ("broadcast address is: "+ (str(all.broadcast_address)))


"""exe1()
"""

def exe2(file="file"):
    
    try:
        f = open(file, "r")
        
        count=0
        lista = list()
        
        while True:
            line = f.readline()
            if (line == ''):
                break
            m=re.search(r'(?<=switchport trunk allowed vlan )[\d,]+', line)
            
            if(m):
                lista.append(m.group())
                count=count+1
                
        outlist=filter(None, [x for xs in lista for x in xs.split(',')])
        
        common = [item for item, count in collections.Counter(outlist).items() if count == count]
        unique = [item for item, count in collections.Counter(outlist).items() if count == 1]
        
        common = map(int, common)
        unique = map(int, unique)
        
        common = map(str, sorted(common))
        unique = map(str, sorted(unique))
        
        print ("List_1=" + str(common))
        print ("List_2=" + str(unique))
       
        f.close()  

    except IOError:
        print "The file couldn't be open"

"""
exe2("commands.txt")        
"""

def exe3(file="file"):
     
    pattern=re.compile(r'(?P<Pr>\D.*) (?P<Pre>\b\d[\d|\.]+\d\b) (?P<AD>.*) via (?P<Nhop>\b\d[\d|\.]+\d\b).* (?P<LU>\b\d[\d|\:]+\d\b), (?P<Oint>.*)')
    dic={'L':'local', 'C':'connected', 'S':'static', 'R':'RIP', 'M':'Mobile',
         'B':'BGP', 'D':'EIGRP', 'EX':'EIGRP external', 'O':'OSPF', 
         'IA':'OSPF inter area', 'N1':'OSPF NSSA external type 1',
         'N2':'OSPF NSSA external type 2', 'O E2':'OSPF external type 2',
         'i L1':'IS-IS level-1', 'E':'EGP', 'O E1':'OSPF external type 1', 
         'i L2':'IS-IS level-2', 'i':'IS-IS', 'ia':'IS-IS inter area',
         '*':'candidate default', 'U':'per-user static route',
         'o':'ODR', 'P':'periodic downloaded static route', 'H':'NHRP',
         'l':'LISP', 'a':'application route', '+':'replicated route',
         '%':'next hop override'}
    
    try:
        f = open(file, "r")
        
        while True:
            line = f.readline()
            if (line == ''):
                break
            resul = pattern.match(line)
            if(resul):
            	print "\n"
                print "Protocol:\t\t"+dic[resul.group('Pr')]
                print "Prefix:\t\t\t"+resul.group('Pre')
                print "AD/Metric:\t\t"+resul.group('AD')
                print "Next-hop:\t\t"+resul.group('Nhop')
                print "Last Update:\t\t"+resul.group('LU')
                print "Outbound interface:\t"+resul.group('Oint')
                print "\n"
        
    except IOError:
        print "The file couldn't be open"
        
    f.close()

"""
exe3("ShowIpRoute.txt")
"""

def exe4():
    
    access_template = ['switchport mode access',
                       'switchport access vlan {}',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk allowed vlan {}']
    
    while True:
        try:
            
            mode=(raw_input("Enter interface mode (access/trunk): "))
            mode=mode.lower()
            
            if(mode != "access" and mode != "trunk"):
                raise ValueError
            break
        except ValueError:
            print("Enter a valid interface mode")
        except KeyboardInterrupt:
            print "Abort...."
            exit
    
    interface=raw_input("Enter interface type and number: ")
    
    if(mode == "access"):
        vlan=raw_input("Enter VLAN number: ")
        print 
        access_values = access_template
        access_values[1]=access_values[1].format(vlan)
        print "Interface "+ interface
        
        for n in access_values:
            print n
            
    if(mode == "trunk"):
        vlans=raw_input("Enter allowed VLANs: ")
        print 
        trunk_values = trunk_template
        trunk_values[2]=trunk_values[2].format(vlans)
        print "Interface "+ interface
        
        for n in trunk_values:
            print n

"""
exe4()
"""