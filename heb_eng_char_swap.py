from pyperclip import copy, paste

eng_heb_dict = {
    'q': '/', 'w': '\'', 'e': 'ק', 'r': 'ר', 't': 'א', 'y': 'ט', 'u': 'ו', 'i': 'ן', 'o': 'ם', 'p': 'פ',
    'a': 'ש', 's': 'ד', 'd': 'ג', 'f': 'כ', 'g': 'ע', 'h': 'י', 'j': 'ח', 'k': 'ל', 'l': 'ך', ';': 'ף',
    'z': 'ז', 'x': 'ס', 'c': 'ב', 'v': 'ה', 'b': 'נ', 'n': 'מ', 'm': 'צ', ',': 'ת', '.': 'ץ', '\'': ',',
}


def swap_chars(str_to_fix: str) -> str:
    result_str = ''
    for char in str_to_fix:
        if char in eng_heb_dict.keys():
            result_str += eng_heb_dict[char]
        elif char in eng_heb_dict.values():
            result_str += get_key(char)
        else:
            result_str += char
    return result_str


def get_key(val: str) -> str:
    for key, value in eng_heb_dict.items():
        if val == value:
            return key


copy(swap_chars(paste()))
