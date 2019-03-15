import urllib.request
import sys
import zipfile

addOns = {
    "Deadly Boss Mods (DBM)" : "https://wow.curseforge.com/projects/deadly-boss-mods/files/latest",
    "Details! Damage Meter" : "https://wow.curseforge.com/projects/details/files/latest",
    "Skada Damage Meter" : "https://www.wowace.com/projects/skada/files/latest",
    "Quartz" : "https://www.wowace.com/projects/quartz/files/latest",
    "Bagnon" : "https://wow.curseforge.com/projects/bagnon/files/latest",
    "CompactRaid" : "https://wow.curseforge.com/projects/compactraid/files/latest",
    "Immersion" : "https://wow.curseforge.com/projects/immersion/files/latest",
    "Mapster" : "https://www.wowace.com/projects/mapster/files/latest",
    "OmniCC" : "https://wow.curseforge.com/projects/omni-cc/files/latest",
    "Postal" : "https://www.wowace.com/projects/postal/files/latest",
    "KuiNameplates" : "https://wow.curseforge.com/projects/kuinameplates/files/latest",
    "Garrison Mission Manager" : "https://wow.curseforge.com/projects/garrison-mission-manager/files/latest",
    "AzeritePowerWeights" : "https://wow.curseforge.com/projects/azeritepowerweights/files/latest",
    "World Quests List" : "https://wow.curseforge.com/projects/world-quests-list/files/latest",
    "Scrap (Junk Seller)" : "https://wow.curseforge.com/projects/scrap/files/latest",
    "TinyInspect" : "https://wow.curseforge.com/projects/itemlevel-anywhere/files/latest",
    "Pa'ku Totems" : "https://wow.curseforge.com/projects/paku-totems/files/latest",
    "BonusRollPreview" : "https://wow.curseforge.com/projects/bonusrollpreview/files/latest",
    "KeystoneHelper" : "https://wow.curseforge.com/projects/keystonehelper/files/latest",
    "Angry Keystones" : "https://www.wowace.com/projects/angry-keystones/files/latest", 
    "Can I Mog It?" : "https://wow.curseforge.com/projects/can-i-mog-it/files/latest",
    "alaChat" : "https://wow.curseforge.com/projects/alachat/files/latest",
    "EnhancedChatFilterMODFix" : "https://wow.curseforge.com/projects/ecfmodfix/files/latest", 
    "AzeriteTooltip" : "https://wow.curseforge.com/projects/azeritetooltip/files/latest",
    "BFAInvasionTimer" : "https://wow.curseforge.com/projects/bfainvasiontimer/files/latest",
    "Quest Completist" : "https://wow.curseforge.com/projects/quest_completist/files/latest",
    "WeakAuras 2" : "https://www.wowace.com/projects/weakauras-2/files/latest",
    "Shadowed Unit Frames" : "https://www.wowace.com/projects/shadowed-unit-frames/files/latest",
}

def dlAddOn(url):
    def progresshook(chunk, chunkSize, totalSize):
        size = min(chunk * chunkSize, totalSize)
        sys.stdout.write("%d KB / %d KB\r" % (size / 1024, totalSize / 1024))
        sys.stdout.flush()

    file, _ = urllib.request.urlretrieve(url, reporthook=progresshook)

    return file

def unZip(file, folder = '.'):
    with zipfile.ZipFile(file, 'r') as f:
        f.extractall(folder)

if __name__ == '__main__':
    folder = 'D:/Games/World of Warcraft/_retail_/Interface/AddOns'
    use_proxy = True
    
    proxy = urllib.request.ProxyHandler({'http': 'raspberrypi:8118'})
    if use_proxy:
        opener = urllib.request.build_opener(proxy)
    else:
        opener = urllib.request.build_opener()

    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0')]
    urllib.request.install_opener(opener)
    
    for k in addOns:
        try:
            url = addOns[k]
            print("Downloading %s from %s ..." % (k, url))
            file = dlAddOn(url)
            print("\nExtracting %s to %s ..." % (file, folder))
            unZip(file, folder)
        except Exception as err:
            print("Failed to get %s: %r" % (k, err))
            
