import os 

test = input("is it IOT or WEB: ")

if test == "IOT":
    os.system('clear')
    target = input("Targets IP to scan: ")
    os.system('sudo nmap -sV --script vulners ' + target + ' -O -o IOT_SCAN.txt')

if test == "WEB":
    os.system('clear')
    SITE = input("What website are we scanning: ")
    os.system('sudo nmap -sV --script banner ' + SITE + ' -O -o WEB_NMAP_SCAN.txt')
    os.system('sudo nikto -host '+ SITE + ' -o WEB_NIKTO_SCAN.txt')
