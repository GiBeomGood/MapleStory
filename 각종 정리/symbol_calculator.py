from datetime import datetime, timedelta


days = ['월', '화', '수', '목', '금', '토', '일']
today = datetime.today()
today_year = today.year
today_month = today.month
today_date = today.day
today_day_index = today.weekday()
today_day = days[today_day_index]
today_string = f'{today_year}. {today_month}. {today_date}.({today_day})'

def cumsum_symbol(level):  # level means the last level for summation
    return 11 * level + level * (level+1) * (2*level+1) // 6

total_req = cumsum_symbol(19)

def additional_day_calculator(level, count):
    current_total = cumsum_symbol(level-1) + count
    current_rest = total_req - current_total

    if current_rest <= 20*(6-today_day_index):
        total_add_day = (current_rest-1) // 20 + 1

    else:
        total_add_day = 6-today_day_index  # defined
        current_rest -= 20 * total_add_day
        
        total_add_day += (current_rest // 185) * 7  # added
        last_week_rest = current_rest % 185

        if last_week_rest == 0:
            add_day = 0

        elif last_week_rest <= 65:
            add_day = 1

        else:
            add_day = (last_week_rest - 66) // 20 + 2

        total_add_day += add_day  # added

    return total_add_day


check = None
print('매주 주간 퀘스트를 수행하는 것을 기준으로 하며, 오늘 일퀘와 이번 주 주퀘는 이미 수행되었다고 가정합니다.\
      확인하셨으면 다음 문구를 정확히 입력해주세요:')
while True:
    check = input('\n관련 사항을 확인했습니다.\n')
    if check == '관련 사항을 확인했습니다.':
        break
    else:
        print('\n정확히 입력하지 않았습니다. 다음 문구를 똑바로 입력하세요:')

level = int(input('\n아케인심볼의 레벨을 입력하세요: '))
count = int(input('보유 중인 아케인심볼을 입력하세요: '))

print(f'\n오늘은 {today_string}입니다.')
print(f'아케인 심볼 정보: {level:2d}레벨, {count}/{11+level**2}')

total_add_day = additional_day_calculator(level=level, count=count)
end_day = today + timedelta(days=total_add_day)
end_year = end_day.year
end_month = end_day.month
end_date = end_day.day
end_day_index = end_day.weekday()
end_day = days[end_day_index]
end_day_string = f'{end_year}. {end_month}. {end_date}.({end_day})'

print(f'\n만렙을 찍기까지 총 {total_add_day:3d}일이 남았습니다.')
print(f'심볼 만렙을 찍는 날은 {end_day_string}입니다.')
