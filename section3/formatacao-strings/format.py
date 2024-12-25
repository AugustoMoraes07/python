name = input('What\'s your name? ')
job = input('What\'s your job? ')
city = input('Are you from ? ')
msg = 'I\'m {0}, my job is {1}. I live in {2}'
format_msg = msg.format(name,job,city)
print(format_msg)