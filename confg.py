import json
from wx.lib.embeddedimage import PyEmbeddedImage

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

icon_32 = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlw"
    "SFlzAAALEwAACxMBAJqcGAAABHtJREFUWIW1l21M1VUcxz/n/P/3irkBbWKQKAI+Qk2eCgvM"
    "mHOuVj7MTcFWDrW0zbVqvqhe5dab3Hpjrc1Z2uYcW/nK0q0HB4qpQHqRdhEML8htaoTyqMC9"
    "l/PrBd4bCFzvX/H78ncePt9zzv/8fuevcKhTbXUpYlm5IipDKYkHUKJ6RIlPQkFPSXrhTSfz"
    "qVihRtvbUJQpyIre23gxuuLapYbDW9ZsaX8kA5WtnkQs9qDMToV2x2IW4HJ1Dep0jbxWmO8N"
    "Js54PX19eZtjA1V+T4mBIxpSYgUDNJ2pQVWdp2xBBgCDMjzcOzPxw/nlH+yL2UBl+8XtIrJf"
    "a62dwC9X12KdPk/p/HQAZGgQ09mBAF2LFx/K3LF76wMNVLZf3K6UOuAEDNB0pg5VdTay8jAc"
    "kXskxe0JTIxZYZXfUyIi+6ccDiDCk01N5X99t2/X6LGRHahs9SSKTaPTM2/+vQ6pPMvmaPCw"
    "B6DT5RoeWDBv3tJ3PvobRu+AxR6n8CvnLkDVuZjhPUMB6Omz6LpzLBzXMHLPUWanE3jN8ZP8"
    "c+wXyu774KLBg8MGgB89DTmHK0+kRgwYbW9zcs+NMfhqL5BdnMtP1/yO4N939ZG0YY1KnZ/8"
    "ZsQAirLY1w4+bzOvvlTAqhUF1Hd34fX5kEng3aPgP3T1kbRxLYuW5SGMMNVIbrevOzHw8zdH"
    "2L1hJW7bwt/eTmv7dWpPedgcP4NZ06aNgYdGwzetZWFhXmSeUMBK1mJZuU7gxhjsQAC3y8YE"
    "B3k6KYGi/CW8934pFX13kIng3ePhANplcrSIynBiwOdtpmBRGmIMEhqKxC2tyS9ayuXe/gng"
    "68bBATQmU4dLaqy6WnOR4rwsJHB3XNuc1Fkc7e3n+K0uAI5294/An594k0WR4CjXiwh2IIBL"
    "CWJCY9ruDgwxY/o03t2xnrhnMjlw4xYzN62dFB6WPfKYiM2Az9tMwcI0THAgEgsEQ/TfHSQ0"
    "PMxQIEhdYxu1V2+waN3qB8KV0GOLEl+M7xIaTlbzycaVIAZjhP6BQXr67vBHYxstnX2o+Hiy"
    "il/gjdLSmOZTolpsCQU9yn5wDhIRGuu9fN5zm11lq6n2XOFKRzcqPoHs5S+yKn1uTNDRst2q"
    "3i5JL7xZ5b/gBZ0drbO/pY3Of2/zJ/DVrx6ee2XlQ0HDEkNDUUpOhw2A0RVoPos2IDUjjY/3"
    "72XW7OSHho6Rlgq4l4rFBL4FMxS1v6WnDG5gwG3rgxEDJemFNxH19ZTMHoMU8mVRSk5HxABA"
    "3GDgUwFHNeFhZIz4XXHTI8cdMbBs4bJeLaYMw/DjoxOyLEqLk5b0jTMAsGJu/mlRvP24+KLN"
    "1hWpeWdHx8al4pK5uYdE2DqlO2EICeatkjn5h+9vmvzH5Nql5ehQBejZj8Q24rcsSu9feViT"
    "FqOX05ZWxw0EswS+AAYdg2FAkL3uJ6ZnTwaHGItAZWtNMrarXKBMo56N1lcMDWipcNv6YPiq"
    "RVOMdfB//Xa14SntMjkakymKBBipakpUi+1W9bFAR+s/lzwyovCuxWQAAAAASUVORK5CYII=")
