from helpers.color import terminalColors

def show_message(message_type, message_text):
    if message_type == 'bold':
        print(terminalColors.BOLD + '[ATENTION]:\t {}'.format(message_text) + terminalColors.CLEAR)
    elif message_type == 'debug':
        print(terminalColors.DEBUG + '[DEBUG   ]:\t {}'.format(message_text) + terminalColors.CLEAR)
    elif message_type == 'error':
        print(terminalColors.FAIL + '[ERROR   ]:\t {}'.format(message_text) + terminalColors.CLEAR)
    elif message_type == 'info':
        print(terminalColors.INFO + '[INFO    ]:\t {}'.format(message_text) + terminalColors.CLEAR)
    elif message_type == 'success':
        print(terminalColors.SUCCESS + '[SUCCESS ]:\t {}'.format(message_text) + terminalColors.CLEAR)
    elif message_type == 'warning':
        print(terminalColors.WARNING + '[WARNING ]:\t {}'.format(message_text) + terminalColors.CLEAR)
    else:
        print(terminalColors.UNDERLINE + '[UKNOW]:\t {}'.format(message_text) + terminalColors.CLEAR)