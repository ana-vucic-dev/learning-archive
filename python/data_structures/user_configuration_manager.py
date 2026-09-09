test_settings = {
    'language': 'English',
    'theme': 'dark',
    'brightness': 'automatic',
    'resolution': 'smart',
    'layout': 'standard',
    'text': 'normal',
    'notifications': 'enabled',
}


def add_setting(settings: dict, new_setting: tuple) -> str:
    input_key, input_value = new_setting
    key = input_key.lower()
    value = input_value.lower()

    if key in settings:
        return f'{key.capitalize()} setting already exists.'
    else:
        settings[key] = value
        return f'{key.capitalize()} setting added and set to {value}.'


def update_setting(settings: dict, setting_to_update: tuple) -> str:
    input_key, input_value = setting_to_update
    key = input_key.lower()
    value = input_value.lower()

    if key in settings:
        settings[key] = value
        return f'{key.capitalize()} updated to {value}.'
    else:
        return f'{key.capitalize()} setting does not exist.'


def delete_setting(settings: dict, setting_to_delete: str) -> str:
    key = setting_to_delete.lower()

    if key in settings:
        del settings[key]
        return f'{key.capitalize()} setting deleted.'
    else:
        return f'{key.capitalize()} setting not found.'


def view_settings(settings: dict) -> str:
    if not settings:
        return 'No settings available.'

    user_settings = 'Current User Settings:\n'
    for key, value in settings.items():
        user_settings += f'{key.capitalize()}: {value}\n'
    return user_settings


assert add_setting(test_settings, ('volume', 'medium')) == (
    'Volume setting added and set to medium.'
)

assert test_settings['volume'] == 'medium'

assert add_setting(test_settings, ('theme', 'dark')) == (
    'Theme setting already exists.'
)
