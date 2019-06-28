import urllib.request
import sys
import zipfile

addOns = {
    "BigWigs Bossmods" : "https://www.curseforge.com/wow/addons/big-wigs/download",
    "LittleWigs" : "https://www.curseforge.com/wow/addons/little-wigs/download",
    "BigWigs_Voice" : "https://www.curseforge.com/wow/addons/bigwigs_voice/download/",
    "Bigwigs Voice - Chinese voicepack (VV)" : "https://www.curseforge.com/wow/addons/bigwigs-voice-chinese-voicepack-vv/download/",
    "Details! Damage Meter" : "https://www.curseforge.com/wow/addons/details/download/",
    "Quartz" : "https://www.wowace.com/projects/quartz/files/latest",
    "Bagnon" : "https://www.curseforge.com/wow/addons/bagnon/download/",
    "CompactRaid" : "https://www.curseforge.com/wow/addons/compactraid/download/",
    "Immersion" : "https://www.curseforge.com/wow/addons/immersion/download/",
    "Mapster" : "https://www.wowace.com/projects/mapster/files/latest",
    "OmniCC" : "https://www.curseforge.com/wow/addons/omni-cc/download/",
    "Postal" : "https://www.wowace.com/projects/postal/files/latest",
    "KuiNameplates" : "https://www.curseforge.com/wow/addons/kuinameplates/download/",
    "Garrison Mission Manager" : "https://www.curseforge.com/wow/addons/garrison-mission-manager/download",
    "World Quests List" : "https://www.curseforge.com/wow/addons/world-quests-list/download",
    "Scrap (Junk Seller)" : "https://www.curseforge.com/wow/addons/scrap/download/",
    "TinyInspect" : "https://www.curseforge.com/wow/addons/itemlevel-anywhere/download/",
    "BonusRollPreview" : "https://www.curseforge.com/wow/addons/bonusrollpreview/download/",
    "KeystoneHelper" : "https://www.curseforge.com/wow/addons/keystonehelper/download/",
    "Angry Keystones" : "https://www.wowace.com/projects/angry-keystones/files/latest", 
    "Can I Mog It?" : "https://www.curseforge.com/wow/addons/can-i-mog-it/download/",
    "alaChat" : "https://www.curseforge.com/wow/addons/alachat/download/",
    "EnhancedChatFilterMODFix" : "https://www.curseforge.com/wow/addons/ecfmodfix/download/", 
    "AzeriteTooltip" : "https://www.curseforge.com/wow/addons/azeritetooltip/download/",
    "BFAInvasionTimer" : "https://www.curseforge.com/wow/addons/bfainvasiontimer/download/",
    "WeakAuras 2" : "https://www.wowace.com/projects/weakauras-2/files/latest",
    "Shadowed Unit Frames" : "https://www.wowace.com/projects/shadowed-unit-frames/files/latest",
    "Talent Set Manager" : "https://www.curseforge.com/wow/addons/talent-set-manager/download/",
    "Nameplate Scrolling Combat Text" : "https://www.curseforge.com/wow/addons/nameplate-scrolling-combat-text/download/",
    "AllTheIDs" : "https://www.curseforge.com/wow/addons/alltheids/download",
    "Instance Portals" : "https://www.curseforge.com/wow/addons/instance-portals/download",
    "Astral Keys" : "https://www.curseforge.com/wow/addons/astral-keys/download",
    "BugGrabber" : "https://www.wowace.com/projects/bug-grabber/files/latest",
    "BugSack" : "https://www.wowace.com/projects/bugsack/files/latest",
    "MythicPlusTimer" : "hhttps://www.curseforge.com/wow/addons/mythicplustimer/download", 
    "LibGroupInSpecT" : "https://www.wowace.com/projects/libgroupinspect/files/latest",
    "LibGetFrame" : "https://www.curseforge.com/wow/addons/libgetframe/download/",
    # "HandyNotes" : "https://www.wowace.com/projects/handynotes/files/latest",
    # "HandyNotes_DraenorTreasures" : "https://wow.curseforge.com/projects/handynotes_draenortreasures/files/latest",
    "SavedInstances" : "https://www.wowace.com/projects/saved_instances/files/latest",
    "AdvancedInterfaceOptions" : "https://www.wowace.com/projects/advancedinterfaceoptions/files/latest",
    "TinyTooltip" : "https://www.curseforge.com/wow/addons/tinytooltip/download",
    "Auctionator" : "https://www.curseforge.com/wow/addons/auctionator/download",
    "Bartender4" : "https://www.wowace.com/projects/bartender4/files/latest",
}

def parseCurseForge(file):
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if "If your download doesn't start automatically, click" in line:
                start = line.index('"') + 1
                end = line.index('"', start)
                return "https://www.curseforge.com" + line[start : end]
    return None

def dlAddOn(url):
    def progresshook(chunk, chunkSize, totalSize):
        size = min(chunk * chunkSize, totalSize)
        sys.stdout.write("%d KB / %d KB\r" % (size / 1024, totalSize / 1024))
        sys.stdout.flush()

    file, _ = urllib.request.urlretrieve(url, reporthook=progresshook)
    if "www.curseforge.com" in url:
        url = parseCurseForge(file)
        print("[%s] -> [%s]" % (file, url))
        file, _ = urllib.request.urlretrieve(url, reporthook=progresshook)

    return file

def unZip(file, folder = '.'):
    with zipfile.ZipFile(file, 'r') as f:
        f.extractall(folder)

if __name__ == '__main__':
    folder = 'D:/Games/World of Warcraft/_retail_/Interface/AddOns'
    use_proxy = True
    
    proxy = urllib.request.ProxyHandler({'http': 'http://raspberrypi:8118', 'https': 'http://raspberrypi:8118'})
    if use_proxy:
        opener = urllib.request.build_opener(proxy)
    else:
        opener = urllib.request.build_opener()

    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0')]
    urllib.request.install_opener(opener)
    
    for k in addOns:
        try:
            url = addOns[k]
            print("Downloading [%s] from [%s] ..." % (k, url))
            file = dlAddOn(url)
            print("\nExtracting [%s] to [%s] ..." % (file, folder))
            unZip(file, folder)
        except Exception as err:
            print("Failed to get [%s]: %r" % (k, err))
            
