import math


def find_zone_by_village(village_name):
    zones = {
        "N1": "ບ້ານ ທ່າດ່ານ, ບ້ານ ດອນຫວາຍ ແລະ ບ້ານ ນາພານ.",
        "N2": "ບ້ານ ບຸ່ງນາດິ, ບ້ານ ຫົວຫາດ, ບ້ານ ສົມສະອາດ ແລະ ບ້ານ ທ່າໂພ.",
        "N3": "ບ້ານ ສົມສະອາດ, ບ້ານ ຄຳແຮ້ງ, ບ້ານ ນໍ້າພູ, ບ້ານ ດົງໂພສີ,\
            ບ້ານ ນາໂດນ, ບ້ານ ຂົວດຳ ແລະ ບ້ານ ຄຳຊັນ.",
        "N4": "ບ້ານ ຂົວດຳ ແລະ ບ້ານ ຄຳຊັນ.",
        "N5": "ບ້ານ ມ່ວງໄຂ່, ບ້ານ ນໍ້າພູ, ບ້ານ ດົງໂພສີ ແລະ ບ້ານ ດົງໜາກໄຟ.",
        "N6": "ບ້ານ ດອນຕູມ, ບ້ານ ດົງໜາກໄຟ, ບ້ານ ສີສະຫວ່າງເໝືອ ແລະ ບ້ານ ໂພນທາດ.",
        "N7": "ບ້ານ ດົງໜາກໄຟ, ບ້ານ ຫອມມາລາ ແລະ ບ້ານ ສີສະຫວ່າງເໝືອ.",
        "N8": "ບ້ານ ພູມມະເຈດີ, ບ້ານ ໂພນທາດ, ບ້ານ ນາຄຳ, ບ້ານ ນາລະໂອ່ງ ແລະ ບ້ານ ໂພສີແກ້ວ.",
        "N9": "ບ້ານ ນາໜາກເກືອ, ບ້ານ ໂພນສົ້ມໂຮງ ແລະ ບ້ານ ຕາກແດດ.",
        "N10": "ບ້ານ ຄັນນາຈານ, ບ້ານ ເວີນຄູນ ແລະ ບ້ານ ເຫຼົ່າໜາກຫູດ.",
        "N11": "ບ້ານ ໂພນທັນ, ບ້ານ ຫ້ວຍຂະຫຍອງ ແລະ ບ້ານ ຄຳແສນໄຊ ( ຄຸ້ມໜອງກຸງ ).",
        "N12": "ບ້ານ ໂພສີແກ້ວ, ບ້ານ ນາລະໂອງ ແລະ ບ້ານ ຄຳແສນໄຊ.",
        "N13": "ບ້ານ ຫ້ວຍມ່ວງ, ບ້ານ ດົງດອກໄມ້ ແລະ ບ້ານ ເຮືອນຫີນ.",
        "N14": "ບ້ານ ນາບໍ່,​ ບ້ານ ນາຈານ, ບ້ານ ນາຕູ່, ບ້ານ ນາໂມງ ແລະ ບ້ານ ສີສະຫວ່າງໃຕ້.",
    }
    for key, value in zones.items():
        if village_name in value:
            return key
    return None

def get_road_type_value(key):
    road_types = {
        "ທາງຮ່ອມ": "ຖະໜົນສາຍແຍກ",
        "ທາງ": "ຖະໜົນສາຍເຊື່ອມຕໍ່",
        math.nan: "ທາງດັ້ງເດີມ/ບໍ່ມີທາງ"
    }
    # Handle NaN keys
    if isinstance(key, float) and math.isnan(key):
        key = math.nan
    
    return road_types.get(key, "ທາງດັ້ງເດີມ/ບໍ່ມີທາງ")

def get_land_type(key):
    if "ປຸກສ້າງ" in key:
        return 2
    return 1

def get_land_subtype(key):
    if "ສວນ" in key:
        return 3
    elif "ນາ" in key:
        return 1
    elif "ໄຮ່" in key:
        return 2
    elif "ສັດ" in key:
        return 4
    elif "ສ້າງ" in key:
        return 4
    return 5

def get_land_zone(key):
    if "ອາ" in key:
        return 1
    elif "ເປົ່າ" in key:
        return 4
    elif "ໂຮງ" in key:
        return 2
    elif "ຮ້ານ" in key:
        return 3
    elif "ກະ" in key:
        return 2
    return 4