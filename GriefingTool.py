import socket
import subprocess
import os
import sys
from threading import Thread
import time
from mcstatus import MinecraftServer
from colorama import *
import random

def clear(): 
    if (os.name == "nt"): 
        os.system('cls') 
    else: 
        os.system('clear') 

def separator():
    print(Fore.YELLOW + "")

def mainMenu():
    clear()
    os.system ("title [ Griefing Tool ]")
    separator()
    print(Fore.LIGHTCYAN_EX)
    print("   _____        _         __  _                ")
    print("  / ____|      (_)       / _|(_)               ")
    print(" | |  __  _ __  _   ___ | |_  _  _ __    __ _  ")
    print(" | | |_ || '__|| | / _ \|  _|| || '_ \  / _` | ")
    print(" | |__| || |   | ||  __/| |  | || | | || (_| | ")
    print("  \_____||_|   |_| \___||_|  |_||_| |_| \__, | ")
    print("                                         __/ | ")
    print("                                        |___/  ")

    separator()

    print(Fore.RESET)
    print("[1] PortScanner")    
    print("[2] Subdomain Scanner")   
    print("[3] Get IP")    
    print("[4] ServerStatus")    
    print("[5] BungeeCord Exploit")    
    print("[6] Plugin Exploit")    
    print("[7] RankManager")   
    print("[8] Griefing Commands")
    print("[9] IP Whitelist Bypass")
    print("[10] Tool Info")
    print(Fore.WHITE)

    separator()
    print()

    try:
        selection = input(Fore.RESET + "Select » " + Fore.LIGHTCYAN_EX)
    except KeyboardInterrupt:
        print(Fore.WHITE)
        sys.exit()

    try:
        selection = int(selection)
    except:
        clear()
        print("Server Not Found!")
        time.sleep(2)
        mainMenu()

    print(Fore.WHITE)
    if (selection == 2):
        subdomain()
    if (selection == 1):
        portscanner()
    if (selection == 3):
        getip()
    if (selection == 4):
        status()
    if (selection == 5):
        bungee()
    if (selection == 6):
        plugin()
    if (selection == 10):
        info()
    if (selection == 9):
        white()
    if (selection == 8):
        grief()
    if (selection == 7):
        rank()
    if (selection == 99):
        clear()
        quit()

def back():
    print()
    if (os.name == "nt"):
        os.system("Pause")    
    mainMenu()

def subdomain():
    domain = input(Fore.RESET + "Server IP [Domain] » " + Fore.LIGHTCYAN_EX)
    
    clear()
    print(Fore.LIGHTCYAN_EX)
    print("   _____        _         __  _                ")
    print("  / ____|      (_)       / _|(_)               ")
    print(" | |  __  _ __  _   ___ | |_  _  _ __    __ _  ")
    print(" | | |_ || '__|| | / _ \|  _|| || '_ \  / _` | ")
    print(" | |__| || |   | ||  __/| |  | || | | || (_| | ")
    print("  \_____||_|   |_| \___||_|  |_||_| |_| \__, | ")
    print("                                         __/ | ")
    print("                                        |___/  ")
    os.system ("title [Subdomain Scanner]")
    print(" Subdomains » " + domain + "")
    time.sleep(2)
    print(Fore.RED)

    subdomains = ["www", "build", "web", "dev", "staff", "mc", "play", "sys", "node1", "node2", "node3", "builder", "developer", "test", "test1", "forum", "bans", "baneos", "ts", "ts3", "sys1", "sys2", "mods", "bungee", "bungeecord", "array", "spawn", "server", "help", "client", "api", "smtp", "s1", "s2", "s3", "s4", "server1", "server2", "jugar", "login", "mysql", "phpmyadmin", "demo", "na", "eu", "us", "es", "fr", "it", "ru", "support", "developing", "discord", "backup", "buy", "buycraft", "go", "dedicado1", "dedi", "dedi1", "dedi2", "dedi3", "minecraft", "prueba", "pruebas", "ping", "register", "cdn", "stats", "store", "serie", "buildteam", "info", "host", "jogar", "proxy", "vps", "ovh", "partner", "partners", "appeals", "appeal", "store-assets"]
    for subdomain in subdomains:
        try:
            fullsub = str(subdomain)+"."+str(domain)
            ipofsub = socket.gethostbyname(str(fullsub))
            print(Fore.LIGHTCYAN_EX + " [GriefTool] " + fullsub + " » " + ipofsub)
        except:
            pass
    
    back()

def getip():

    domain = input(Fore.RESET + "Server IP [Domain] » " + Fore.LIGHTCYAN_EX)

    clear()
    print()
    print(Fore.LIGHTCYAN_EX)
    print("   _____        _         __  _                ")
    print("  / ____|      (_)       / _|(_)               ")
    print(" | |  __  _ __  _   ___ | |_  _  _ __    __ _  ")
    print(" | | |_ || '__|| | / _ \|  _|| || '_ \  / _` | ")
    print(" | |__| || |   | ||  __/| |  | || | | || (_| | ")
    print("  \_____||_|   |_| \___||_|  |_||_| |_| \__, | ")
    print("                                         __/ | ")
    print("                                        |___/  ")
    os.system ("title [Get IP]")
    print(" IP Servers List » " + domain + "")
    time.sleep(2)

    ip_list = []
    ais = socket.getaddrinfo(domain,0,0,0,0)
    for result in ais:
        ip_list.append(result[-1][0])
        ip_list = list(set(ip_list))

    for x in range(len(ip_list)):
        print(Fore.RED)
        print(Fore.LIGHTCYAN_EX + " [GriefTool] » " + ip_list[x])
    
    back()

def portscanner():
    ip = input(Fore.RESET + "Target IP » " + Fore.LIGHTCYAN_EX)
    print("Starting, This May Take A Long Time To Found Ports ")
    time.sleep(3)
    clear()
    print(Fore.LIGHTCYAN_EX)
    print("   _____        _         __  _                ")
    print("  / ____|      (_)       / _|(_)               ")
    print(" | |  __  _ __  _   ___ | |_  _  _ __    __ _  ")
    print(" | | |_ || '__|| | / _ \|  _|| || '_ \  / _` | ")
    print(" | |__| || |   | ||  __/| |  | || | | || (_| | ")
    print("  \_____||_|   |_| \___||_|  |_||_| |_| \__, | ")
    print("                                         __/ | ")
    print("                                        |___/  ")
    os.system ("title [PortScanner]")
    os.system ("nmap -p 1-65535 -T5 -v -A -Pn " + ip)

    back()
    
def info():
    clear()
    print(Fore.LIGHTCYAN_EX)
    print("   _____        _         __  _                ")
    print("  / ____|      (_)       / _|(_)               ")
    print(" | |  __  _ __  _   ___ | |_  _  _ __    __ _  ")
    print(" | | |_ || '__|| | / _ \|  _|| || '_ \  / _` | ")
    print(" | |__| || |   | ||  __/| |  | || | | || (_| | ")
    print("  \_____||_|   |_| \___||_|  |_||_| |_| \__, | ")
    print("                                         __/ | ")
    print("                                        |___/  ")
    os.system ("title [Info]")
    time.sleep(2)
    print("[ Tool Created By Keevo ]")
    time.sleep(2)
    print("[ https://youtube.com/c/Keevo ]")
    
    back()
    
def status():
    ip = input(Fore.RESET + "Server IP » " + Fore.LIGHTCYAN_EX)

    port = 25565
    if (len(ip.split(":")) != 1):
        port = int(ip.split(":")[1])
        ip = ip.split(":")[0]

    print("Connecting")
    server = MinecraftServer(ip, port)
    status = server.status()

    clear()
    print(Fore.LIGHTCYAN_EX)
    print("   _____        _         __  _                ")
    print("  / ____|      (_)       / _|(_)               ")
    print(" | |  __  _ __  _   ___ | |_  _  _ __    __ _  ")
    print(" | | |_ || '__|| | / _ \|  _|| || '_ \  / _` | ")
    print(" | |__| || |   | ||  __/| |  | || | | || (_| | ")
    print("  \_____||_|   |_| \___||_|  |_||_| |_| \__, | ")
    print("                                         __/ | ")
    print("                                        |___/  ")
    os.system ("title [ServerStatus]")
    print("Status » " + ip + "")
    print()

    print("Motd » ", end="")
    print(status.description)
    print("***********************************************")
    print("Players » " + str(status.players.online) + "/" + str(status.players.max))
    print("***********************************************")
    print("Version » " + status.version.name)
    print("***********************************************")
    print("Ping » " + str(status.latency))
    print("***********************************************")

    back()

    print(status.description)
    
def bungee():
    clear()
    print(Fore.LIGHTCYAN_EX)
    print("   _____        _         __  _                ")
    print("  / ____|      (_)       / _|(_)               ")
    print(" | |  __  _ __  _   ___ | |_  _  _ __    __ _  ")
    print(" | | |_ || '__|| | / _ \|  _|| || '_ \  / _` | ")
    print(" | |__| || |   | ||  __/| |  | || | | || (_| | ")
    print("  \_____||_|   |_| \___||_|  |_||_| |_| \__, | ")
    print("                                         __/ | ")
    print("                                        |___/  ")
    os.system ("title [BungeeCord Exploit]")
    print(" ╔═══════════════════════════════════════════════════════════════════════════════╗ ")
    print(" ║                         ======= BUNGEECORD ========                           ║ ")
    print(" ║                                 1. Method                                     ║ ")
    print(" ║                             Join on nick: md_5                                ║ ")
    print(" ║                    Once you join you should have perms                        ║ ")
    print(" ║                         try: /send /alert /server                             ║ ")
    print(" ║                                 2. Method                                     ║ ")
    print(" ║                                 UUID SPOOF                                    ║ ")
    print(" ║                                 3. Method                                     ║ ")
    print(" ║                                Port Checking                                  ║ ")
    print(" ║ Only working if the bungeecord and the other servers are on the same machine! ║ ")
    print(" ╚═══════════════════════════════════════════════════════════════════════════════╝ ")
    
    back()
  
def plugin():
    clear()
    print(Fore.LIGHTCYAN_EX)
    print("   _____        _         __  _                ")
    print("  / ____|      (_)       / _|(_)               ")
    print(" | |  __  _ __  _   ___ | |_  _  _ __    __ _  ")
    print(" | | |_ || '__|| | / _ \|  _|| || '_ \  / _` | ")
    print(" | |__| || |   | ||  __/| |  | || | | || (_| | ")
    print("  \_____||_|   |_| \___||_|  |_||_| |_| \__, | ")
    print("                                         __/ | ")
    print("                                        |___/  ")
    os.system ("title [Plugin Exploit]")
    print()   
    print(" ╔═══════════════════════════════════════════════════════════════════════════════╗")
    print(" ║                         ======= PLUGIN EXPLOIT ========                       ║")
    print(" ║                                 1. Method                                     ║")
    print(" ║           Just try /pl if they are not using plugin to stop that              ║")
    print(" ║                                 2. Method                                     ║")
    print(" ║          Use JigsawClient and go to option exploits and PluginSteal           ║")
    print(" ║                                 3. Method                                     ║")
    print(" ║                  Use SkillClient and go to plugin exploit                     ║")
    print(" ║                                 4. Method                                     ║")
    print(" ║                              / pl [space] [tab]                               ║")
    print(" ║                                / bukkit: help                                 ║")
    print(" ║                                / bukkit: see                                  ║")
    print(" ║                                 / bukkit :?                                   ║")
    print(" ║                              / see [space] [tab]                              ║")
    print(" ║                               or write / [tab]                                ║")
    print(" ╚═══════════════════════════════════════════════════════════════════════════════╝")
   
    back()  
    
def rank():
    clear()
    print(Fore.LIGHTCYAN_EX)
    print("   _____        _         __  _                ")
    print("  / ____|      (_)       / _|(_)               ")
    print(" | |  __  _ __  _   ___ | |_  _  _ __    __ _  ")
    print(" | | |_ || '__|| | / _ \|  _|| || '_ \  / _` | ")
    print(" | |__| || |   | ||  __/| |  | || | | || (_| | ")
    print("  \_____||_|   |_| \___||_|  |_||_| |_| \__, | ")
    print("                                         __/ | ")
    print("                                        |___/  ")
    os.system ("title [RankManager]")
    print()   
    print("GroupManager")
    print("/manuadd <player> <rank>")
    print("**************************************")
    print("UltraPermssions")
    print("/upc addgroup <player> <rank>")
    print("**************************************")
    print("zPermissions")
    print("/zpermissions player <player> set *")
    print("**************************************")
    print("PowerFulPerms")
    print("/pp user <player> setgroup <rank>")
    print("**************************************")
    print("LuckPerms")
    print("/lp user <player> group set <rank>")
    print("**************************************")
    print("PermssionsEx")
    print("/pex user <player> add *")
    print("**************************************")    
   
    back()  
    
def grief():
    clear()
    print(Fore.LIGHTCYAN_EX)
    print("   _____        _         __  _                ")
    print("  / ____|      (_)       / _|(_)               ")
    print(" | |  __  _ __  _   ___ | |_  _  _ __    __ _  ")
    print(" | | |_ || '__|| | / _ \|  _|| || '_ \  / _` | ")
    print(" | |__| || |   | ||  __/| |  | || | | || (_| | ")
    print("  \_____||_|   |_| \___||_|  |_||_| |_| \__, | ")
    print("                                         __/ | ")
    print("                                        |___/  ")
    os.system ("title [Grief Commands]")
    print()   
    print("**************************************")
    print("/ept /sphere 0 10")
    print("**************************************")
    print("/ept /cyl lava 5")
    print("**************************************")
    print("/br sphere 0 5")
    print("**************************************")
    print("/sp area 5")
    print("**************************************")
    print("/fill ~-10 ~-2 ~-10 ~10 ~2 ~10 air")
    print("**************************************")
    print("/fill ~-5 ~-5 ~-5 ~5 ~5 ~5 lava")
    print("**************************************")  
    print("/minecraft:summon PrimedTnt")
    print("**************************************") 
    print("/minecraft:tp @a @p")
    print("**************************************")
    print("/fill ~0 ~30 ~0 ~0 ~30 ~0 anvil")
    print("**************************************")  
    print("/minecraft:execute 0 0 0 @p minecraft:op @p")
    print("**************************************")
    print("/minecraft:op @p")
    print("**************************************")
    
    back()
    
def white():
    clear()
    print(Fore.LIGHTCYAN_EX)
    print("   _____        _         __  _                ")
    print("  / ____|      (_)       / _|(_)               ")
    print(" | |  __  _ __  _   ___ | |_  _  _ __    __ _  ")
    print(" | | |_ || '__|| | / _ \|  _|| || '_ \  / _` | ")
    print(" | |__| || |   | ||  __/| |  | || | | || (_| | ")
    print("  \_____||_|   |_| \___||_|  |_||_| |_| \__, | ")
    print("                                         __/ | ")
    print("                                        |___/  ")
    os.system ("title [IP Whitelist]")
    print()   
    ip = input(Fore.RESET + "IP: " + Fore.LIGHTCYAN_EX)
    port = input(Fore.RESET + "Port: " + Fore.LIGHTCYAN_EX)
    
    print()
    print(f'{Fore.RESET}Connecting to {Fore.LIGHTCYAN_EX}{ip}:{port}{Fore.RESET}...')
    time.sleep(1)
    
    print('Spoofing packets...')
    time.sleep(2)
    
    print('Creating server...')
    print('Starting server...')
    time.sleep(2)

    print()
    print(f'Use Code: {Fore.LIGHTCYAN_EX}127.0.0.1{Fore.RESET}')
    print()
    time.sleep(2)
    back()  
  
if (__name__ == "__main__"):
    mainMenu()

  
