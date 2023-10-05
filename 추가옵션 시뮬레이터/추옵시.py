from random import sample, choices
from math import ceil


armor_options = ['STR', 'DEX', 'LUK', 'INT', ['STR', 'DEX'], ['STR', 'INT'], ['STR', 'LUK'], ['DEX', 'INT'], ['DEX', 'LUK'], ['INT', 'LUK'], '올스탯', '최대 HP', '최대 MP', '착용 레벨 감소', '방어력', '공격력', '마력', '이동속도', '점프력']
weapon_options = ['STR', 'DEX', 'LUK', 'INT', ['STR', 'DEX'], ['STR', 'INT'], ['STR', 'LUK'], ['DEX', 'INT'], ['DEX', 'LUK'], ['INT', 'LUK'], '올스탯', '최대 HP', '최대 MP', '착용 레벨 감소', '방어력', '공격력', '마력', '보스 몬스터 공격 시 데미지', '데미지']


armor_divisions = {0: ['STR', 'DEX', 'LUK', 'INT', '방어력'],
                   1: [['STR', 'DEX'], ['STR', 'INT'], ['STR', 'LUK'], ['DEX', 'INT'], ['DEX', 'LUK'], ['INT', 'LUK']],
                   2: ['최대 HP', '최대 MP'],
                   3: ['착용 레벨 감소'],
                   4: ['공격력', '마력', '올스탯', '이동속도', '점프력']}
weapon_divisions = {0: ['STR', 'DEX', 'LUK', 'INT', '방어력'],
                    1: [['STR', 'DEX'], ['STR', 'INT'], ['STR', 'LUK'], ['DEX', 'INT'], ['DEX', 'LUK'], ['INT', 'LUK']],
                    2: ['공격력', '마력'],
                    3: ['보스 몬스터 공격 시 데미지'],
                    4: ['최대 HP', '최대 MP'],
                    5: ['착용 레벨 감소'],
                    6: ['올스탯', '데미지']}


def Simulator(level, kind, basic_atkmgc, item = '강환불'):
    print_orders = ['STR', 'DEX', 'INT', 'LUK', '최대 HP', '최대 MP', '착용 레벨 감소', '공격력', '마력', '방어력']
    options_indices = sample(range(19), 4)
    
    data = [3, 4, 5, 6, 7]
    if level == 150:
        data = [[8* grade for grade in data],
                [4*grade for grade in data]]
    elif level == 160:
        data = [[9* grade for grade in data],
                [5*grade for grade in data]]
    elif level == 200:
        data = [[11* grade for grade in data],
                [6*grade for grade in data]]

    if kind == '무기':
        if level == 150:
            data += [[ceil(basic_atkmgc * weight) for weight in [0.12, 0.176, 0.242, 0.32, 0.41]]]
        elif level == 160:
            data += [[ceil(basic_atkmgc * weight) for weight in [0.15, 0.22, 0.3025, 0.4, 0.5125]]]
        elif level == 200:
            data += [[ceil(basic_atkmgc * weight) for weight in [0.18, 0.264, 0.363, 0.479, 0.615]]]
        data += [[6, 8, 10, 12, 14]]
        
        options = [weapon_options[i] for i in options_indices]
        divisions = weapon_divisions
        print_orders += ['보스 몬스터 공격 시 데미지', '데미지', '올스탯']
        
    elif kind == '방어구':
        options = [armor_options[i] for i in options_indices]
        divisions = armor_divisions
        print_orders += ['이동속도', '점프력', '올스탯']

    data += [[3*level*grade for grade in [3, 4, 5, 6, 7]],
             [-15, -20, -25, -30, -35],
             [3, 4, 5, 6, 7]]
    
    
    if item == '강환불':
        probs = [0.2, 0.3, 0.36, 0.14, 0]
    elif item == '영환불':
        probs = [0, 0.29, 0.45, 0.25, 0.01]
    
    options_kinds = [(options[i], key) for key, value in divisions.items() for i in range(4) if options[i] in value]
    final_result = dict()
    
    for i in range(4):
        option_name = options_kinds[i][0]; option_kind = options_kinds[i][1]
        options_grade = choices(population = [0, 1, 2, 3, 4], weights = probs, k = 1)[0]
        option = data[option_kind][options_grade]
        
        if type(option_name) == list:
            for j in range(2):
                temp_option_name = option_name[j]
                if temp_option_name in final_result.keys():
                    final_result[temp_option_name] += option
                else:
                    final_result[temp_option_name] = option
        else:
            if option_name in final_result.keys():
                final_result[option_name] += option
            else:
                final_result[option_name] = option
    
    
    for option_name in print_orders:
        if option_name in final_result.keys():
            if option_name in ['보스 몬스터 공격 시 데미지', '데미지', '올스탯']:
                percent = '%'
            else:
                percent = ''
            print('{} : {:+}{}'.format(option_name, final_result[option_name], percent))
    
    return final_result


level = int(input('레벨을 입력하세요: '))
kind = str(input('아이템의 종류를 입력하세요 [방어구/무기]: '))
if kind == '무기':
    basic_atkmgc = int(input('무기의 기본 공격력/마력을 입력하세요: '))
elif kind == '방어구':
    basic_atkmgc = None
item = str(input('환생의 불꽃의 종류를 입력하세요 [강환불/영환불]: '))
print('\n')

while True:
    final_result = Simulator(level = level, kind = kind, item = item, basic_atkmgc = basic_atkmgc)
    keep_going = str(input('\n계속 진행하시겠습니까? [y/n] \n'))
    if keep_going == 'n':
        break