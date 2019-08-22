import re

def is_valid_email(addr):
    return re.match(r'[0-9a-zA-Z\.]+@[0-9a-zA-Z]+\.[0-9a-zA-Z]+',addr)

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
print(is_valid_email('mr-bob@example.com'))

def name_of_email(addr):
    temp=re.match(r'<([a-zA-Z\s]+)>\s[a-zA-Z0-9]+@[0-9a-zA-Z]+\.[0-9a-zA-Z]+',addr)
    return temp.group(1) if temp else re.match(r'([0-9a-zA-Z\.]+)@[0-9a-zA-Z]+\.[0-9a-zA-Z]+',addr).group(1)

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')