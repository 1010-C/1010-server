from split_settings.tools import include

base_settings = [
    'components/common.py',
    'components/database.py'
]

include(*base_settings)
