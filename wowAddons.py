import urllib.request
import sys
import zipfile
import socks
import sockshandler

addOns = {
    "Quartz" : "https://www.wowace.com/projects/quartz/files/latest",
    "Deadly Boss Mods (DBM)" : "https://wow.curseforge.com/projects/deadly-boss-mods/files/latest",
    "Bagnon" : "https://wow.curseforge.com/projects/bagnon/files/latest",
    "CompactRaid" : "https://wow.curseforge.com/projects/compactraid/files/latest",
    "Garrison Mission Manager" : "https://wow.curseforge.com/projects/garrison-mission-manager/files/latest",
    "Immersion" : "https://wow.curseforge.com/projects/immersion/files/latest",
    "Mapster" : "https://www.wowace.com/projects/mapster/files/latest",
    "OmniCC" : "https://wow.curseforge.com/projects/omni-cc/files/latest",
    "Postal" : "https://www.wowace.com/projects/postal/files/latest",
    "Skada" : "https://www.wowace.com/projects/skada/files/latest",
    "World Quests List" : "https://wow.curseforge.com/projects/world-quests-list/files/latest",
    "Scrap (Junk Seller)" : "https://wow.curseforge.com/projects/scrap/files/latest"
}

useProxy = False

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
    if useProxy:
        proxy = sockshandler.SocksiPyHandler(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1080)
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener)
    folder = 'D:/Games/World of Warcraft/Interface/AddOns'
    for k in addOns:
        url = addOns[k]
        print("Downloading %s from %s ..." % (k, url))
        file = dlAddOn(url)
        print("\nExtracting %s to %s ..." % (file, folder))
        unZip(file, folder)
