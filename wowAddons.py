import urllib.request
import sys
import zipfile
import csv
import os
import time
import cfscrape

addOns = {
    "BigWigs Bossmods" : "https://www.curseforge.com/wow/addons/big-wigs/download",
    "LittleWigs" : "https://www.curseforge.com/wow/addons/little-wigs/download",
    "BigWigs_Voice" : "https://www.curseforge.com/wow/addons/bigwigs_voice/download/",
    "Bigwigs Voice - Chinese voicepack (VV)" : "https://www.curseforge.com/wow/addons/bigwigs-voice-chinese-voicepack-vv/download/",
    "Details! Damage Meter" : "https://www.curseforge.com/wow/addons/details/download/",
    "Quartz" : "https://www.curseforge.com/wow/addons/quartz/download/",
    "Bagnon" : "https://www.curseforge.com/wow/addons/bagnon/download/",
    # "CompactRaid" : "https://www.curseforge.com/wow/addons/compactraid/download/",
    "Immersion" : "https://www.curseforge.com/wow/addons/immersion/download/",
    "Mapster" : "https://www.curseforge.com/wow/addons/mapster/download",
    "OmniCC" : "https://www.curseforge.com/wow/addons/omni-cc/download/",
    "Postal" : "https://www.curseforge.com/wow/addons/postal/download",
    "KuiNameplates" : "https://www.curseforge.com/wow/addons/kuinameplates/download/",
    "Garrison Mission Manager" : "https://www.curseforge.com/wow/addons/garrison-mission-manager/download",
    "World Quests List" : "https://www.curseforge.com/wow/addons/world-quests-list/download",
    "Scrap (Junk Seller)" : "https://www.curseforge.com/wow/addons/scrap/download/",
    "TinyInspect" : "https://www.curseforge.com/wow/addons/itemlevel-anywhere/download/",
    "BonusRollPreview" : "https://www.curseforge.com/wow/addons/bonusrollpreview/download/",
    "KeystoneHelper" : "https://www.curseforge.com/wow/addons/keystonehelper/download/",
    "Angry Keystones" : "https://www.curseforge.com/wow/addons/angry-keystones/download", 
    "Can I Mog It?" : "https://www.curseforge.com/wow/addons/can-i-mog-it/download/",
    "alaChat" : "https://www.curseforge.com/wow/addons/alachat/download/",
    "EnhancedChatFilterMODFix" : "https://www.curseforge.com/wow/addons/ecfmodfix/download/", 
    "AzeriteTooltip" : "https://www.curseforge.com/wow/addons/azeritetooltip/download/",
    # "BFAInvasionTimer" : "https://www.curseforge.com/wow/addons/bfainvasiontimer/download/",
    "WeakAuras 2" : "https://www.curseforge.com/wow/addons/weakauras-2/download",
    "Shadowed Unit Frames" : "https://www.curseforge.com/wow/addons/shadowed-unit-frames/download",
    "Talent Set Manager" : "https://www.curseforge.com/wow/addons/talent-set-manager/download/",
    "Nameplate Scrolling Combat Text" : "https://www.curseforge.com/wow/addons/nameplate-scrolling-combat-text/download/",
    "AllTheIDs" : "https://www.curseforge.com/wow/addons/alltheids/download",
    "Instance Portals" : "https://www.curseforge.com/wow/addons/instance-portals/download",
    "Astral Keys" : "https://www.curseforge.com/wow/addons/astral-keys/download",
    "BugGrabber" : "https://www.wowace.com/projects/bug-grabber/files/latest",
    "BugSack" : "https://www.wowace.com/projects/bugsack/files/latest",
    "MythicPlusTimer" : "https://www.curseforge.com/wow/addons/mythicplustimer/download", 
    "LibGroupInSpecT" : "https://www.curseforge.com/wow/addons/libgroupinspect/download",
    "LibGetFrame" : "https://www.curseforge.com/wow/addons/libgetframe/download/",
    "SavedInstances" : "https://www.curseforge.com/wow/addons/saved_instances/download",
    "AdvancedInterfaceOptions" : "https://www.curseforge.com/wow/addons/advancedinterfaceoptions/download",
    "TinyTooltip" : "https://www.curseforge.com/wow/addons/tinytooltip/download",
    "Auctionator" : "https://www.curseforge.com/wow/addons/auctionator/download",
    # "Bartender4" : "https://www.wowace.com/projects/bartender4/files/latest",
    "HandyNotes" : "https://www.curseforge.com/wow/addons/handynotes/download",
    # "HandyNotes_DraenorTreasures" : "https://wow.curseforge.com/projects/handynotes_draenortreasures/files/latest",
    "HandyNotes - Nazjatar by TomCat's Tours" : "https://www.curseforge.com/wow/addons/tomcats-tours-nazjatar/download",
    "HandyNotes - Mechagon by TomCat's Tours" : "https://www.curseforge.com/wow/addons/tomcats-tours-mechagon/download",
    "TomCat's Tours" : "https://www.curseforge.com/wow/addons/tomcats/download", 
}

scraper = cfscrape.create_scraper()
def urlretrieve(url, proxies=None, reporthook=None):
    response = scraper.get(url,  proxies=proxies)
    filename = 'tmp'
    with open(filename, 'bw') as f:
        f.write(response.content)
    return filename

def parseCurseForge(file):
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if "If your download doesn't start automatically, click" in line:
                start = line.index('"') + 1
                end = line.index('"', start)
                return "https://www.curseforge.com" + line[start : end]
    return None

def dlAddOn(name, url, proxies, force=False):
    def progresshook(chunk, chunkSize, totalSize):
        size = min(chunk * chunkSize, totalSize)
        sys.stdout.write("%d KB / %d KB\r" % (size / 1024, totalSize / 1024))
        sys.stdout.flush()

    # file, _ = urllib.request.urlretrieve(url, reporthook=progresshook)
    file = urlretrieve(url, proxies=proxies, reporthook=progresshook)
    if "www.curseforge.com" in url:
        url = parseCurseForge(file)
        print("[%s] -> [%s]" % (file, url))
        os.remove(file)
        file = None
        if force or addOns[name]["VERSION"] != url:
            file = urlretrieve(url, reporthook=progresshook)
            addOns[name]["VERSION"] = url

    return file

def unZip(file, folder = '.'):
    with zipfile.ZipFile(file, 'r') as f:
        f.extractall(folder)

if __name__ == '__main__':
    if os.name == 'nt':
        folder = 'D:/Games/World of Warcraft/_retail_/Interface/AddOns'
    else:
        folder = '/Applications/World of Warcraft/_retail_/Interface/AddOns'
    use_proxy = True
    file_name = "addons.csv"

    proxies = {'http': 'http://raspberrypi:8118', 'https': 'http://raspberrypi:8118'}
    proxies = None

    # if use_proxy:
    #     opener = urllib.request.build_opener(proxy)
    # else:
    #     opener = urllib.request.build_opener()

    # urllib.request.install_opener(opener)

    if not os.path.exists(folder):
        os.makedirs(folder)

    if not os.path.exists(file_name):
        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "URL", "VERSION", "TIMESTAMP"])
            for k in addOns:
                url = addOns[k]
                writer.writerow([k, url, '', ''])

    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        header = True
        for row in reader:
            if header:
                header = False
                addOns = {}
            else:
                k = row[0]
                v = { "Name": row[0], "URL" : row[1], "VERSION": row[2], "TIMESTAMP" : row[3] }
                addOns[k] = v             
            
    for k in addOns:
        try:
            url = addOns[k]["URL"]
            print("Downloading [%s] from [%s] ..." % (k, url))
            file = dlAddOn(k, url, proxies, force=True)
            if file is None:
                print('[%s] No updates' % (k))
            else:
                print("Extracting [%s] to [%s] ..." % (file, folder))
                unZip(file, folder)
                os.remove(file)
            addOns[k]["TIMESTAMP"] = time.ctime()
        except Exception as err:
            print("Failed to get [%s]: %r" % (k, err))
            addOns[k]["TIMESTAMP"] = "ERR"

    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "URL", "VERSION", "TIMESTAMP"])
        for k in addOns:
            writer.writerow([addOns[k]["Name"], addOns[k]["URL"], addOns[k]["VERSION"], addOns[k]["TIMESTAMP"]])
            
