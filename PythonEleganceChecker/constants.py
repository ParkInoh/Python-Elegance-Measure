# import re
#
#
# # x, y, z, w, i, j, k, l are allowed in variable names or indices
# REGEX_VAR_NAME_ERROR = [
#                           re.compile(r'([A-H]|[M-V]|[a-h]|[m-v])'),
#                           re.compile(r'([A-Z]|[a-z]){2}')
# ]
#
# # Regex for camelCase to snake_case.
# REGEX_CAMEL_TO_SNAKE1 = re.compile(r'([A-Z]+)([A-Z][a-z])')
# REGEX_CAMEL_TO_SNAKE2 = re.compile(r'([a-z\d])([A-Z])')

# flake8 default style guide
# recommended set of rules by sider
# https://github.com/sider/runners/blob/bdc863bd5faf78f820fc05dcfad7cd5a27613f78/images/flake8/sider_recommended_flake8.ini
IGNORE = ['E121', 'E126', 'E127', 'E128', 'E203',
          'E225', 'E226', 'E231', 'E241', 'E251',
          'E261', 'E265', 'E302', 'E303', 'E305',
          'E402', 'E501', 'E741', 'W291', 'W292',
          'W293', 'W391', 'W503', 'W504', 'F403',
          'B007', 'B950']
MAX_LINE_LENGTH = 200
