#########################################
###  Convert arabic number to roman  ###
#########################################

#######################################################################################
# https://pt.wikipedia.org/wiki/Numera%C3%A7%C3%A3o_romana
# https://s1.static.brasilescola.uol.com.br/iframes/conversor-romano/?site=brasilescola
# text-decoration: overline;
# max roman number: 3999999
#######################################################################################

ROMAN_NUMBERS = {
    1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX',
    10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC',
    100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM',
    1000: 'M', 2000: 'MM', 3000: 'MMM', 4000: 'IV', 5000: 'V', 6000: 'VI', 700: 'VII', 8000: 'VIII', 9000: 'IX',
    10000: 'X', 20000: 'XX', 30000: 'XXX', 40000: 'XL', 50000: 'L', 60000: 'LX', 70000: 'LXX', 80000: 'LXXX', 90000: 'XC',
    100000: 'C', 200000: 'CC', 300000: 'CCC', 400000: 'CD', 500000: 'D', 600000: 'DC', 700000: 'DCC', 800000: 'DCCC', 900000: 'CM',
    1000000: 'M', 2000000: 'MM', 3000000: 'MMM'
}

OVERLINE_ROMAN_NUMBER = {
  'I': 'I̅', 'V':  'V̅', 'X': 'X̅', 'L': 'L̅', 'C': 'C̅', 'D': 'D̅', 'M': 'M̅'
}


class ArabicToRoman():

    def enter_number(self):
        given_number = input("Enter your number lass then 4000000: ")
        given_number = int(given_number)
        if given_number <= 3999999:
            self.get_print_result(given_number)
    
    def format_number(self, num: int):
        num = str(num)
        while True:
            if num.startswith('0'):
                num = num[1: len(num)]
            else:
                break
        return num
    
    def str_split(self, str_num: str):
        tmp = ''
        parts = []
        count = 0
        for num in str_num[::-1]:
            tmp += num
            count += 1
            if count >= 3:
                parts.append(tmp[::-1])
                tmp = ''
                count = 0
        if count > 0:
            parts.append(tmp[::-1])
        return list(reversed(parts))
    
    def get_list_index(self, num, count):
        for _ in range(0, count):
            num += '0'
        return num
    
    def change_to_overline(self, numbers: str):
        for num in numbers:
            numbers = numbers.replace(num, OVERLINE_ROMAN_NUMBER[num])
        return numbers

    def convert(self, num: str, overline='default'):
        new_num = ''
        str_num = num
        str_split = self.str_split(str_num)
        str_zero_len = len(str_split) - 1
        count_parts = len(str_split)

        for part in self.str_split(str_num):
            is_first_number = True
            count = 0

            for part_num in part:
                count += 1
                dict_key = self.get_list_index(part_num, len(part) - count)
                if is_first_number:
                    if str_zero_len > 0:
                        for _ in range(0, str_zero_len):
                            dict_key += '000'
                        str_zero_len -= 1
                        is_first_number = False
                dict_key = int(dict_key)
                if dict_key > 0:
                    new_num += ROMAN_NUMBERS[dict_key]
            
            count_parts -= 1
            if count_parts == 1 and int(num) >= 4000:
                if overline == 'default':
                    new_num = self.change_to_overline(new_num)
                else:
                    new_num += overline
        
        return new_num
    
    def get_web_overline_result(self, num: int):
        num = self.format_number(num)
        result = self.convert(num)
        if result.__contains__('_'):
            parts = result.split('_')
            result = f'<span style="text-decoration: overline;">{parts[0]}</span>{parts[1]}'
        return result
    
    def get_clean_result(self, num: int):
        return self.convert(self.format_number(num))
    
    def get_print_result(self, num: int):
        num = self.format_number(num)
        hashtags = "################################################"
        hashtags_len = len(hashtags)
        result = num + " -> " + self.convert(num)
        result_len = len(result)
        spaces_len = (hashtags_len - result_len) - 4
        half_space_len = int(((hashtags_len - result_len) - 2) / 2)
        formated_result = '##'

        for space in range(0, spaces_len):
            if space == half_space_len:
                formated_result += result
            else:
                formated_result += ' '
        
        formated_result += ' ##'
        
        print(hashtags)
        print(formated_result)
        print(hashtags)