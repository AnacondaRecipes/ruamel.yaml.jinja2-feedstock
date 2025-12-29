import sys

with open('setup.py', 'r') as f:
    content = f.read()

# Add Python 3.14 compatibility
py314_import = '''if sys.version_info >= (3, 14):
    from ast import Constant
    Str = Num = Bytes = NameConstant = Constant
el'''

content = content.replace(
    'if sys.version_info >= (3, 8):',
    py314_import + 'if sys.version_info >= (3, 8):'
)

# Fix _convert to handle Constant.value
old_convert_start = '''    def _convert(node):
        if isinstance(node, Str):'''

new_convert_start = '''    def _convert(node):
        if sys.version_info >= (3, 14) and isinstance(node, Constant):
            return node.value
        if isinstance(node, Str):'''

content = content.replace(old_convert_start, new_convert_start)

with open('setup.py', 'w') as f:
    f.write(content)
