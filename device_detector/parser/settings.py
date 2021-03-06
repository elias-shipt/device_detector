AVAILABLE_ENGINES = {
    'WebKit',
    'Blink',
    'Trident',
    'Text-based',
    'Dillo',
    'iCab',
    'Elektra',
    'Presto',
    'Gecko',
    'KHTML',
    'NetFront',
    'Edge',
    'NetSurf',
    'Servo',
    'Goanna',
}
AVAILABLE_ENGINES_LOWER_CASE = {engine.lower(): engine for engine in AVAILABLE_ENGINES}

AVAILABLE_BROWSERS = {
    '2B': '2345 Browser',
    '36': '360 Phone Browser',
    '3B': '360 Browser',
    'AA': 'Avant Browser',
    'AB': 'ABrowse',
    'AF': 'ANT Fresco',
    'AG': 'ANTGalio',
    'AL': 'Aloha Browser',
    'AH': 'Aloha Browser Lite',
    'AM': 'Amaya',
    'AO': 'Amigo',
    'AN': 'Android Browser',
    'AD': 'AOL Shield',
    'AR': 'Arora',
    'AV': 'Amiga Voyager',
    'AW': 'Amiga Aweb',
    'AS': 'Avast Secure Browser',
    'VG': 'AVG Secure Browser',
    'AZ': 'Avast SafeZone',
    'AT': 'Atomic Web Browser',
    'BA': 'Beaker Browser',
    'BM': 'Beamrise',
    'BB': 'BlackBerry Browser',
    'BD': 'Baidu Browser',
    'BS': 'Baidu Spark',
    'BI': 'Basilisk',
    'BE': 'Beonex',
    'BH': 'BlackHawk',
    'BJ': 'Bunjalloo',
    'BL': 'B-Line',
    'BR': 'Brave',
    'BK': 'BriskBard',
    'BX': 'BrowseX',
    'CA': 'Camino',
    'CL': 'CCleaner',
    'CC': 'Coc Coc',
    'CD': 'Comodo Dragon',
    'CE': 'CM Browser',
    'C1': 'Coast',
    'CX': 'Charon',
    'CF': 'Chrome Frame',
    'HC': 'Headless Chrome',
    'CH': 'Chrome',
    'CI': 'Chrome Mobile iOS',
    'CK': 'Conkeror',
    'CM': 'Chrome Mobile',
    'CN': 'CoolNovo',
    'CO': 'CometBird',
    'CB': 'COS Browser',
    'CP': 'ChromePlus',
    'CR': 'Chromium',
    'CY': 'Cyberfox',
    'CS': 'Cheshire',
    'CT': 'Crusta',
    'CU': 'Cunaguaro',
    'CV': 'Chrome Webview',
    'DB': 'dbrowser',
    'DD': 'DuckDuckGo Privacy Browser',
    'DE': 'Deepnet Explorer',
    'DT': 'Delta Browser',
    'DF': 'Dolphin',
    'DO': 'Dorado',
    'DL': 'Dooble',
    'DI': 'Dillo',
    'EC': 'Ecosia',
    'EI': 'Epic',
    'EL': 'Elinks',
    'EB': 'Element Browser',
    'EZ': 'eZ Browser',
    'EU': 'EUI Browser',
    'EP': 'GNOME Web',
    'ES': 'Espial TV Browser',
    'FA': 'Falkon',
    'FX': 'Faux Browser',
    'F1': 'Firefox Mobile iOS',
    'FB': 'Firebird',
    'FD': 'Fluid',
    'FE': 'Fennec',
    'FF': 'Firefox',
    'FK': 'Firefox Focus',
    'FY': 'Firefox Reality',
    'FR': 'Firefox Rocket',
    'FL': 'Flock',
    'FM': 'Firefox Mobile',
    'FW': 'Fireweb',
    'FN': 'Fireweb Navigator',
    'FU': 'FreeU',
    'GA': 'Galeon',
    'GE': 'Google Earth',
    'HA': 'Hawk Turbo Browser',
    'HO': 'hola! Browser',
    'HJ': 'HotJava',
    'HU': 'Huawei Browser',
    'IB': 'IBrowse',
    'IC': 'iCab',
    'I2': 'iCab Mobile',
    'I1': 'Iridium',
    'I3': 'Iron Mobile',
    'I4': 'IceCat',
    'ID': 'IceDragon',
    'IV': 'Isivioo',
    'IW': 'Iceweasel',
    'IE': 'Internet Explorer',
    'IM': 'IE Mobile',
    'IR': 'Iron',
    'JS': 'Jasmine',
    'JI': 'Jig Browser',
    'JO': 'Jio Browser',
    'KB': 'K.Browser',
    'KI': 'Kindle Browser',
    'KM': 'K-meleon',
    'KO': 'Konqueror',
    'KP': 'Kapiko',
    'KN': 'Kinza',
    'KW': 'Kiwi',
    'KY': 'Kylo',
    'KZ': 'Kazehakase',
    'LB': 'Cheetah Browser',
    'LF': 'LieBaoFast',
    'LG': 'LG Browser',
    'LI': 'Links',
    'LO': 'Lovense Browser',
    'LU': 'LuaKit',
    'LS': 'Lunascape',
    'LX': 'Lynx',
    'M1': 'mCent',
    'MB': 'MicroB',
    'MC': 'NCSA Mosaic',
    'MZ': 'Meizu Browser',
    'ME': 'Mercury',
    'MF': 'Mobile Safari',
    'MI': 'Midori',
    'MO': 'Mobicip',
    'MU': 'MIUI Browser',
    'MS': 'Mobile Silk',
    'MN': 'Minimo',
    'MT': 'Mint Browser',
    'MX': 'Maxthon',
    'NB': 'Nokia Browser',
    'NO': 'Nokia OSS Browser',
    'NV': 'Nokia Ovi Browser',
    'NX': 'Nox Browser',
    'NE': 'NetSurf',
    'NF': 'NetFront',
    'NL': 'NetFront Life',
    'NP': 'NetPositive',
    'NS': 'Netscape',
    'NT': 'NTENT Browser',
    'OC': 'Oculus Browser',
    'O1': 'Opera Mini iOS',
    'OB': 'Obigo',
    'OD': 'Odyssey Web Browser',
    'OF': 'Off By One',
    'OE': 'ONE Browser',
    'OX': 'Opera GX',
    'OG': 'Opera Neon',
    'OH': 'Opera Devices',
    'OI': 'Opera Mini',
    'OM': 'Opera Mobile',
    'OP': 'Opera',
    'ON': 'Opera Next',
    'OO': 'Opera Touch',
    'OS': 'Ordissimo',
    'OR': 'Oregano',
    'OY': 'Origyn Web Browser',
    'OV': 'Openwave Mobile Browser',
    'OW': 'OmniWeb',
    'OT': 'Otter Browser',
    'PL': 'Palm Blazer',
    'PM': 'Pale Moon',
    'PP': 'Oppo Browser',
    'PR': 'Palm Pre',
    'PU': 'Puffin',
    'PW': 'Palm WebPro',
    'PA': 'Palmscape',
    'PX': 'Phoenix',
    'PO': 'Polaris',
    'PT': 'Polarity',
    'PS': 'Microsoft Edge',
    'Q1': 'QQ Browser Mini',
    'QQ': 'QQ Browser',
    'QT': 'Qutebrowser',
    'QZ': 'QupZilla',
    'QM': 'Qwant Mobile',
    'QW': 'QtWebEngine',
    'RE': 'Realme Browser',
    'RK': 'Rekonq',
    'RM': 'RockMelt',
    'SB': 'Samsung Browser',
    'SA': 'Sailfish Browser',
    'SC': 'SEMC-Browser',
    'SE': 'Sogou Explorer',
    'SF': 'Safari',
    'SW': 'SalamWeb',
    'SH': 'Shiira',
    'S1': 'SimpleBrowser',
    'SK': 'Skyfire',
    'SS': 'Seraphic Sraf',
    'SL': 'Sleipnir',
    'SN': 'Snowshoe',
    'SO': 'Sogou Mobile Browser',
    'S2': 'Splash',
    'SI': 'Sputnik Browser',
    'SR': 'Sunrise',
    'SP': 'SuperBird',
    'SU': 'Super Fast Browser',
    'S0': 'START Internet Browser',
    'ST': 'Streamy',
    'SX': 'Swiftfox',
    'SZ': 'Seznam Browser',
    'TO': 't-online.de Browser',
    'TA': 'Tao Browser',
    'TF': 'TenFourFox',
    'TB': 'Tenta Browser',
    'TZ': 'Tizen Browser',
    'TS': 'TweakStyle',
    'TV': 'TV Bro',
    'UB': 'UBrowser',
    'UC': 'UC Browser',
    'UM': 'UC Browser Mini',
    'UT': 'UC Browser Turbo',
    'UZ': 'Uzbl',
    'VI': 'Vivaldi',
    'VV': 'vivo Browser',
    'VB': 'Vision Mobile Browser',
    'WI': 'Wear Internet Browser',
    'WP': 'Web Explorer',
    'WE': 'WebPositive',
    'WF': 'Waterfox',
    'WH': 'Whale Browser',
    'WO': 'wOSBrowser',
    'WT': 'WeTab Browser',
    'YA': 'Yandex Browser',
    'YL': 'Yandex Browser Lite',
    'XI': 'Xiino'
}

# flip Abbrev / Brand for fast membership testing
BROWSER_TO_ABBREV = {browser.lower(): abbrev for abbrev, browser in AVAILABLE_BROWSERS.items()}

BROWSER_FAMILIES = {
    'Android Browser': ('AN', 'MU'),
    'BlackBerry Browser': ('BB',),
    'Baidu': ('BD', 'BS'),
    'Amiga': ('AV', 'AW'),
    'Chrome': (
        'AS',
        'AZ',
        'BA',
        'CH',
        'BR',
        'CC',
        'CD',
        'CM',
        'CI',
        'CF',
        'CN',
        'CR',
        'CP',
        'IR',
        'RM',
        'AO',
        'TB',
        'TS',
        'VI',
        'PT',
        'AD',
        'SB',
        'WP',
        'I3',
        'CV',
        'WH',
        'SZ',
        'QW',
        'LF',
        'KW',
        '2B',
        'CE',
        'EC',
        'MT',
        'MS',
        'HA',
        'OC',
        'MZ',
        'BM',
        'KN',
        'SW',
        'M1',
        'FA',
        'TA',
        'AH',
        'CL',
        'SU',
        'EU',
        'UB',
        'LO',
        'VG',
        'TV',
    ),
    'Firefox': (
        'FF',
        'FE',
        'FM',
        'SX',
        'FB',
        'PX',
        'MB',
        'EI',
        'WF',
        'CU',
        'TF',
        'QM',
        'FR',
        'I4',
        'GZ',
        'MO',
        'F1',
        'BI',
        'MN',
        'BH',
        'TO',
        'OS',
        'FY',
    ),
    'Internet Explorer': ('IE', 'IM', 'PS'),
    'Konqueror': ('KO',),
    'NetFront': ('NF',),
    'NetSurf': ('NE',),
    'Nokia Browser': ('NB', 'NO', 'NV', 'DO'),
    'Opera': ('OP', 'OM', 'OI', 'ON', 'OO', 'OG', 'OH', 'O1', 'OX'),
    'Safari': ('SF', 'MF', 'SO'),
    'Sailfish Browser': ('SA',),
}

MOBILE_ONLY_BROWSERS = {
    '36',
    'OC',
    'PU',
    'SK',
    'MF',
    'OI',
    'OM',
    'DD',
    'DB',
    'ST',
    'BL',
    'IV',
    'FM',
    'C1',
    'AL',
    'SA',
    'SB',
    'FR',
    'WP',
    'HA',
    'NX',
    'HU',
    'VV',
    'RE',
    'CB',
    'MZ',
    'UM',
    'FK',
    'FX',
    'WI',
    'MN',
    'M1',
    'AH',
    'SU',
    'EU',
    'EZ',
    'UT',
    'DT',
    'S0',
}

# Fast membership testing
BROWSER_FAMILIES_LOWER = {browser.lower() for browser in BROWSER_FAMILIES.keys()}

# Crufty name/version prefixes too generic to be meaningful Client names
# iOS/12.1, CFNetwork/975.0.3, Android/7.0
CRUFT_NAMES = {
    'afma-sdk-a',
    '1.0,win',
    'alamofire',
    'applewebkit',
    'carrier',
    'cfnetwork',
    'client',
    'client-protocol',
    'configuration',
    'darwin',
    'dalvik',
    'j2me',
    'mozilla',
    'mozzila',
    'user-agent:mozilla',
    'android mozilla',
    'mobile',
    'ios',
    'android',
    'ipad',
    'iphone',
    'okhttp',
    'os',
    'opera mobi',
    'profile',
    'scale',
    'sdk',
    'sparkle',
    'ss',
    'winsparkle',
    'symbian',
    'unknown',
    'urbanairshiplib',
    'urbanairshiplib-android',
    'windows',
    'windows nt',
    'win64',
    'wow64',
}

# These keys may provide meaningful information,
# but should never be considered app names.
METADATA_NAMES = {
    'app.webview',
    'app.webview app.webview',
    'build',
    'device',
    'ioswebview',
    'linux',
    'version',
    'wfappid',
    'wfexperience',
}

# When parsing UA strings generically, multiple name/version pairs may be found.
# Ignore the uninteresting ones
# Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaN8-00/014.002; Profile/MIDP-2.1 Configuration/CLDC-1.1; en-us) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.4 3gpp-gba
SKIP_PREFIXES = set(AVAILABLE_ENGINES_LOWER_CASE.keys()) | \
                BROWSER_FAMILIES_LOWER | \
                CRUFT_NAMES | \
                set(BROWSER_TO_ABBREV.keys())

CHECK_PAIRS = {
    'Android Browser',
    'Mobile Safari',
    'Chrome Mobile',
    'Chrome',
}

__all__ = (
    'AVAILABLE_ENGINES',
    'AVAILABLE_BROWSERS',
    'BROWSER_FAMILIES',
    'BROWSER_TO_ABBREV',
    'CRUFT_NAMES',
    'METADATA_NAMES',
    'MOBILE_ONLY_BROWSERS',
    'SKIP_PREFIXES',
)
