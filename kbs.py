from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# 1 курс
def get_kb_course() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('1 курс')],
        [KeyboardButton('2 курс')],
        [KeyboardButton('3 курс')],
        [KeyboardButton('4 курс')]
    ])
    return kb

def get_kb_directions() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('Бизнес информатика')],
        [KeyboardButton('Прикладная математика и информатика')],
        [KeyboardButton('Прикладная математика')],
        [KeyboardButton('Фундаментальная информатика и информационные технологии')],
        [KeyboardButton('Информационная безопасность')],
        [KeyboardButton('Прикладная информатика')],
        [KeyboardButton('Информационные системы и технологии')]
    ])
    return kb

def get_kb_groups_1_Biz_Inf() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-201')],
        [KeyboardButton('09-202')],
        [KeyboardButton('09-203')]
    ])
    return kb

def get_kb_groups_1_PMI() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-211')],
        [KeyboardButton('09-212')],
        [KeyboardButton('09-213')]
    ])
    return kb

def get_kb_groups_1_PM() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-221')],
        [KeyboardButton('09-222')]
    ])
    return kb

def get_kb_groups_1_FIIT() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-231')],
        [KeyboardButton('09-232')]
    ])
    return kb

def get_kb_groups_1_Info_Bez() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-241')],
        [KeyboardButton('09-242')]
    ])
    return kb

def get_kb_groups_1_PI() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-251')],
        [KeyboardButton('09-252')],
        [KeyboardButton('09-253')]
    ])
    return kb

def get_kb_groups_1_IST() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-261')],
        [KeyboardButton('09-262')],
        [KeyboardButton('09-263')]
    ])
    return kb

#2 курс
def get_kb_groups_2_Biz_Inf() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-101')],
        [KeyboardButton('09-102')]
    ])
    return kb

def get_kb_groups_2_PMI() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-111')],
        [KeyboardButton('09-112')],
        [KeyboardButton('09-113')]
    ])
    return kb

def get_kb_groups_2_PM() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-121')],
        [KeyboardButton('09-122')]
    ])
    return kb

def get_kb_groups_2_FIIT() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-131')],
        [KeyboardButton('09-132')]
    ])
    return kb

def get_kb_groups_2_Info_Bez() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-141')],
        [KeyboardButton('09-142')]
    ])
    return kb

def get_kb_groups_2_PI() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-151')],
        [KeyboardButton('09-152')],
        [KeyboardButton('09-153')]
    ])
    return kb

def get_kb_groups_2_IST() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-161')],
        [KeyboardButton('09-162')],
        [KeyboardButton('09-163')]
    ])
    return kb

#3 курс
def get_kb_groups_3_Biz_Inf() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-001')],
        [KeyboardButton('09-002')]
    ])
    return kb

def get_kb_groups_3_PMI() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-011')],
        [KeyboardButton('09-012')],
        [KeyboardButton('09-013')]
    ])
    return kb

def get_kb_groups_3_PM() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-021')],
        [KeyboardButton('09-022')]
    ])
    return kb

def get_kb_groups_3_FIIT() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-031')],
        [KeyboardButton('09-032')],
        [KeyboardButton('09-033')],
    ])
    return kb

def get_kb_groups_3_Info_Bez() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-041')]
    ])
    return kb

def get_kb_groups_3_PI() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-051')],
        [KeyboardButton('09-052')],
        [KeyboardButton('09-053')]
    ])
    return kb

def get_kb_groups_3_IST() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-061')],
        [KeyboardButton('09-062')],
        [KeyboardButton('09-063')]
    ])
    return kb

# 4 курс
def get_kb_groups_4_Biz_Inf() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-901')],
        [KeyboardButton('09-902')]
    ])
    return kb

def get_kb_groups_4_PMI() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-911')],
        [KeyboardButton('09-912')],
        [KeyboardButton('09-913')]
    ])
    return kb

def get_kb_groups_4_PM() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-921')],
        [KeyboardButton('09-922')]
    ])
    return kb

def get_kb_groups_4_FIIT() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-931')],
        [KeyboardButton('09-932')],
        [KeyboardButton('09-933')]
    ])
    return kb

def get_kb_groups_4_Info_Bez() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-941')]
    ])
    return kb

def get_kb_groups_4_PI() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-951')],
        [KeyboardButton('09-952')]
    ])
    return kb

def get_kb_groups_4_IST() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('09-961')],
        [KeyboardButton('09-962')]
    ])
    return kb

def get_kb_subgroups() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('1')],
        [KeyboardButton('2')]
    ])
    return kb