from controllers import Arduino


def main(name):
    print(f'Hi, {name}')
    Arduino.connect()
    message_to_arduino = '1'
    result = Arduino.send_order(message_to_arduino)
    Arduino.disconnect()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('Arduino')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
