import urllib.request
import sys
import zipfile

addOns = {
    "BigWigs Bossmods" : "https://www.curseforge.com/wow/addons/big-wigs/download/2730395/file",
    "LittleWigs" : "https://www.curseforge.com/wow/addons/little-wigs/download/2730396/file",
    "BigWigs_Voice" : "https://www.curseforge.com/wow/addons/bigwigs_voice/download/2730444/file",
    "Bigwigs Voice - Chinese voicepack (VV)" : "https://www.curseforge.com/wow/addons/bigwigs-voice-chinese-voicepack-vv/download/2701838/file",
    "Details! Damage Meter" : "https://www.curseforge.com/wow/addons/details/download/2730880/file",
    "Quartz" : "https://www.wowace.com/projects/quartz/files/latest",
    "Bagnon" : "https://www.curseforge.com/wow/addons/bagnon/download/2731027/file",
    "CompactRaid" : "https://www.curseforge.com/wow/addons/compactraid/download/2625311/file",
    "Immersion" : "https://www.curseforge.com/wow/addons/immersion/download/2665099/file",
    "Mapster" : "https://www.wowace.com/projects/mapster/files/latest",
    "OmniCC" : "https://www.curseforge.com/wow/addons/omni-cc/download/2729472/file",
    "Postal" : "https://www.wowace.com/projects/postal/files/latest",
    "KuiNameplates" : "https://www.curseforge.com/wow/addons/kuinameplates/download/2730194/file",
    "Garrison Mission Manager" : "https://www.curseforge.com/wow/addons/garrison-mission-manager/download/2669426/file",
    "World Quests List" : "https://www.curseforge.com/wow/addons/world-quests-list/download/2729754/file",
    "Scrap (Junk Seller)" : "https://www.curseforge.com/wow/addons/scrap/download/2674885/file",
    "TinyInspect" : "https://www.curseforge.com/wow/addons/itemlevel-anywhere/download/2729100/file",
    "BonusRollPreview" : "https://www.curseforge.com/wow/addons/bonusrollpreview/download/2670624/file",
    "KeystoneHelper" : "https://www.curseforge.com/wow/addons/keystonehelper/download/2587171/file",
    "Angry Keystones" : "https://www.wowace.com/projects/angry-keystones/files/latest", 
    "Can I Mog It?" : "https://www.curseforge.com/wow/addons/can-i-mog-it/download/2729861/file",
    "alaChat" : "https://www.curseforge.com/wow/addons/alachat/download/2731106/file",
    "EnhancedChatFilterMODFix" : "https://www.curseforge.com/wow/addons/ecfmodfix/download/2731070/file", 
    "AzeriteTooltip" : "https://www.curseforge.com/wow/addons/azeritetooltip/download/2686571/file",
    "BFAInvasionTimer" : "https://www.curseforge.com/wow/addons/bfainvasiontimer/download/2730468/file",
    "WeakAuras 2" : "https://www.wowace.com/projects/weakauras-2/files/latest",
    "Shadowed Unit Frames" : "https://www.wowace.com/projects/shadowed-unit-frames/files/latest",
    "Talent Set Manager" : "https://www.curseforge.com/wow/addons/talent-set-manager/download/2688116/file",
    "Nameplate Scrolling Combat Text" : "https://www.curseforge.com/wow/addons/nameplate-scrolling-combat-text/download/2723430/file",
    "AllTheIDs" : "https://www.curseforge.com/wow/addons/alltheids/download/2584848/file",
    "Instance Portals" : "https://www.curseforge.com/wow/addons/instance-portals/download/2699553/file",
    "Astral Keys" : "https://www.curseforge.com/wow/addons/astral-keys/download/2730239/file",
    "BugGrabber" : "https://www.wowace.com/projects/bug-grabber/files/latest",
    "BugSack" : "https://www.wowace.com/projects/bugsack/files/latest",
    "MythicPlusTimer" : "hhttps://www.curseforge.com/wow/addons/mythicplustimer/download/2712277/file", 
    "LibGroupInSpecT" : "https://www.wowace.com/projects/libgroupinspect/files/latest",
    "LibGetFrame" : "https://www.curseforge.com/wow/addons/libgetframe/download/2708105/file",
    # "HandyNotes" : "https://www.wowace.com/projects/handynotes/files/latest",
    # "HandyNotes_DraenorTreasures" : "https://wow.curseforge.com/projects/handynotes_draenortreasures/files/latest",
    "SavedInstances" : "https://www.wowace.com/projects/saved_instances/files/latest",
    "AdvancedInterfaceOptions" : "https://www.wowace.com/projects/advancedinterfaceoptions/files/latest",
    "TinyTooltip" : "https://www.curseforge.com/wow/addons/tinytooltip/download/2729101/file",
    "Auctionator" : "https://www.curseforge.com/wow/addons/auctionator/download/2649069/file",
    "Bartender4" : "https://www.wowace.com/projects/bartender4/files/latest",
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
            
