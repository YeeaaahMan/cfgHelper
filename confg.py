import json

def create_config():
    c = json.loads("""{
    "wot": {
        "path": "D:\\\\Games\\\\World_Of_Tanks\\\\WoTLauncher.cfg",
        "versions": {
            "launcher_ver": "unknown",
            "locale_ver": "unknown",
            "client_ver": "unknown",
            "sdcontent_ver": "unknown",
            "hdcontent_ver": "unknown",
            "selected_target": "sandbox",
            "lang": "ru"
        }
    },
    "wows": {
        "path": "D:\\\\Games\\\\World_of_Warships\\\\WoWSLauncher.cfg",
        "versions": {
            "launcher_ver": "unknown",
            "sdcontent_ver": "unknown",
            "locale_ver": "unknown",
            "selected_target": "full",
            "client_ver": "unknown"
        }
    },
    "wowp": {
        "path": "D:\\\\Games\\\\World_of_Warplanes\\\\WoWPLauncher.cfg",
        "versions": {
            "selected_target": "sd",
            "launcher_ver": "unknown",
            "hdcontent_ver": "unknown",
            "client_ver": "unknown",
            "content_ver": "unknown"
        }
    },
    "output": "D:\\\\"
}
    """)
    write_config(c)

def read_config():
    try:
        CFG = json.load( open("cfgHelper.json") )
    except:
        create_config()
        CFG = json.load( open("cfgHelper.json") )

    return CFG

def write_config(settings):
    fw = open("cfgHelper.json", "w")
    json.dump(settings, fw, indent=4)
    fw.close()