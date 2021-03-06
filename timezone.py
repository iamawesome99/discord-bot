import re

# dictionary of timezone abbreviations
timezone_abbreviations = zoneList = {
    "A": 1.0, "ACDT": 10.5, "ACST": 9.5, "ACT": -5.0, "ACWST": 8.75, "ADT": 4.0, "AEDT": 11.0, "AEST": 10.0,
    "AET": 10.0, "AFT": 4.5, "AKDT": -8.0, "AKST": -9.0, "ALMT": 6.0, "AMST": -3.0, "AMT": -4.0, "ANAST": 12.0,
    "ANAT": 12.0, "AQTT": 5.0, "ART": -3.0, "AST": 3.0, "AT": -4.0, "AWDT": 9.0, "AWST": 8.0, "AZOST": 0.0,
    "AZOT": -1.0, "AZST": 5.0, "AZT": 4.0, "AoE": -12.0, "B": 2.0, "BNT": 8.0, "BOT": -4.0, "BRST": -2.0, "BRT": -3.0,
    "BST": 1.0, "BTT": 6.0, "C": 3.0,  "CAST": 8.0, "CAT": 2.0, "CCT": 6.5, "CDT": -5.0, "CEST": 2.0, "CET": 1.0,
    "CHADT": 13.75, "CHAST": 12.75, "CHOST": 9.0, "CHOT": 8.0, "CHUT": 10.0, "CIDST": -4.0, "CIST": -5.0, "CKT": -10.0,
    "CLST": -3.0, "CLT": -4.0, "COT": -5.0, "CST": -6.0, "CT": -6.0, "CVT": -1.0, "CXT": 7.0, "ChST": 10.0, "D": 4.0,
    "DAVT": 7.0, "DDUT": 10.0, "E": 5.0, "EASST": -5.0, "EAST": -6.0, "EAT": 3.0, "ECT": -5.0, "EDT": -4.0, "EEST": 3.0,
    "EET": 2.0, "EGST": 0.0, "EGT": -1.0, "EST": -5.0, "ET": -5.0, "F": 6.0, "FET": 3.0, "FJST": 13.0, "FJT": 12.0,
    "FKST": -3.0, "FKT": -4.0, "FNT": -2.0, "G": 7.0, "GALT": -6.0, "GAMT": -9.0, "GET": 4.0, "GFT": -3.0, "GILT": 12.0,
    "GMT": 0.0, "GST": 4.0, "GYT": -4.0, "H": 8.0, "HDT": -9.0, "HKT": 8.0, "HOVST": 8.0, "HOVT": 7.0, "HST": -10.0,
    "I": 9.0, "ICT": 7.0, "IDT": 3.0, "IOT": 6.0, "IRDT": 4.5, "IRKST": 9.0, "IRKT": 8.0, "IRST": 3.5, "IST": 5.5,
    "JST": 9.0, "K": 10.0, "KGT": 6.0, "KOST": 11.0, "KRAST": 8.0, "KRAT": 7.0, "KST": 9.0, "KUYT": 4.0, "L": 11.0,
    "LHDT": 11.0, "LHST": 10.5, "LINT": 14.0, "M": 12.0, "MAGST": 12.0, "MAGT": 11.0, "MART": -8.5, "MAWT": 5.0,
    "MDT": -6.0, "MHT": 12.0, "MMT": 6.5, "MSD": 4.0, "MSK": 3.0, "MST": -7.0, "MT": -7.0, "MUT": 4.0, "MVT": 5.0,
    "MYT": 8.0, "N": -1.0, "NCT": 11.0, "NDT": -1.5, "NFT": 11.0, "NOVST": 7.0, "NOVT": 7.0, "NPT": 5.75, "NRT": 12.0,
    "NST": -2.5, "NUT": -11.0, "NZDT": 13.0, "NZST": 12.0, "O": -2.0, "OMSST": 7.0, "OMST": 6.0, "ORAT": 5.0, "P": -3.0,
    "PDT": -7.0, "PET": -5.0, "PETST": 12.0, "PETT": 12.0, "PGT": 10.0, "PHOT": 13.0, "PHT": 8.0, "PKT": 5.0,
    "PMDT": -2.0, "PMST": -3.0, "PONT": 11.0, "PST": -8.0, "PT": -8.0, "PWT": 9.0, "PYST": -3.0, "PYT": -4.0,
    "Q": -4.0, "QYZT": 6.0, "R": -5.0, "RET": 4.0, "ROTT": -3.0, "S": -6.0, "SAKT": 11.0, "SAMT": 4.0, "SAST": 2.0,
    "SBT": 11.0, "SCT": 4.0, "SGT": 8.0, "SRET": 11.0, "SRT": -3.0, "SST": -11.0, "SYOT": 3.0, "T": -7.0, "TAHT": -10.0,
    "TFT": 5.0, "TJT": 5.0, "TKT": 13.0, "TLT": 9.0, "TMT": 5.0, "TOST": 14.0, "TOT": 13.0, "TRT": 3.0, "TVT": 12.0,
    "U": -8.0, "ULAST": 9.0, "ULAT": 8.0, "UYST": -2.0, "UYT": -3.0, "UZT": 5.0, "V": -9.0, "VET": -4.0, "VLAST": 11.0,
    "VLAT": 10.0, "VOST": 6.0, "VUT": 11.0, "W": -10.0, "WAKT": 12.0, "WARST": -3.0, "WAST": 2.0, "WAT": 1.0,
    "WEST": 1.0, "WET": 0.0, "WFT": 12.0, "WGST": -2.0, "WGT": -3.0, "WIB": 7.0,  "WIT": 9.0, "WITA": 8.0, "WST": 14.0,
    "WT": 0.0, "X": -11.0, "Y": -12.0, "YAKST": 10.0, "YAKT": 9.0, "YAPT": 10.0, "YEKST": 6.0, "YEKT": 5.0,
    "CDST": 10.5,  "ADST": -3.0, "HAA": -3.0, "EDST": 11.0, "AMDT": 5.0, "HNA": -4.0, "WDT": 9.0, "AZODT": 0.0,
    "BDT": 8.0, "BT": -3.0, "BDST": 1.0, "NACDT": -5.0, "HAC": -5.0, "CEDT": 2.0, "ECST": 2.0, "MESZ": 2.0, "MEZ": 1.0,
    "CHODT": 9.0, "CHODST": 9.0, "CIT": -5.0, "CLDT": -3.0, "NACST": -6.0, "HNC": -6.0, "EADT": -5.0, "NAEDT": -4.0,
    "HAE": -4.0, "EEDT": 3.0, "OESZ": 3.0, "OEZ": 2.0, "NAEST": -5.0, "HNE": -5.0, "FJDT": 13.0, "FKDT": -3.0,
    "GT": 0.0, "HADT": -9.0, "HOVDT": 8.0, "HOVDST": 8.0, "HAST": -10.0, "IT": 3.5, "KT": 9.0, "SAMST": 4.0,
    "MDST": -6.0, "NAMDT": -6.0, "HAR": -6.0, "MCK": 3.0, "NAMST": -7.0, "HNR": -7.0, "HAT": -1.5, "HNT": -2.5,
    "PDST": -7.0, "NAPDT": -7.0, "HAP": -7.0, "NAPST": -8.0, "HNP": -8.0, "KIT": 5.0, "HLV": -4.0, "EFATE": 11.0,
    "WEDT": 1.0, "WESZ": 1.0, "WEZ": 0.0, "ST": 14.0}

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
TIMEZONES = ["UTC+0", "UTC+1", "UTC+2", "UTC+3"]


# parses the timezone through inp,
def parse_timezone(inp): 
    # search for "UTC" or "GMT" plus an additional but optional character and then numbers,
    # and then an optional colon and more numbers
    ret = re.search(r'((UTC)|(GMT))(?P<sign>[+-])(?P<first>\d+)(: (?P<second>\d+))?', inp, re.IGNORECASE)
    # if it it exists
    if ret: 
        sign = 1
        if ret.group('sign') == "-": 
            sign = -1
        # if a second number exist
        if ret.group('second'): 
            # add the first number to the second number/60
            return (int(ret.group('first')) + int(ret.group('second'))/60)*sign
        # otherwise
        elif ret.group('first'): 
            # return the first number
            return int(ret.group('first'))*sign
    # search for it in our timezone_abrreviations dict
    try: 
        # return the found value if found
        return timezone_abbreviations[inp.upper()]
    except KeyError: 
        # otherwise, return false
        return False


if __name__ == "__main__": 
    print(parse_timezone("UTC+7: 30"))
    print(parse_timezone("UTC-7: 30"))
    print(parse_timezone("EST"))
