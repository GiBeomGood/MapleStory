import pandas as pd

def reader(path):
    with open(path, 'rb') as f:
        file = f.read()
        file = file.decode('utf-8')
        file = file.replace('<br>', '\n')

        first_index = file.index('\n') - 1
        file = file[first_index:-4]
        file = file.replace('false', 'False')
        file = file.replace('true', 'True')
        file = eval(file)['cube_histories']
    
    return file


def option_preprocessor(history):
    for result_dict in history:
        del result_dict['before_potential_options']
        del result_dict['before_additional_potential_options']
        del result_dict['after_additional_potential_options']
        del result_dict['additional_potential_option_grade']
        del result_dict['upgradeguarantee'], result_dict['upgradeguaranteecount'], result_dict['item_upgrade_result']
        del result_dict['id'], result_dict['character_name'], result_dict['miracle_time_flag']
        temp = result_dict['after_potential_options']
        temp = [option_dict['value'] for option_dict in temp]
        result_dict['after_potential_option_1'] = temp[0]
        result_dict['after_potential_option_2'] = temp[1]
        result_dict['after_potential_option_3'] = temp[2]
        del result_dict['after_potential_options']
    
    history = pd.DataFrame(history)
    history.create_date = pd.to_datetime(history.create_date)
    history = history.sort_values(by='create_date').reset_index(drop=True)

    return history