def send_email(message, recipient,* , sender = 'university.help@gmail.com'):
    recipient_true = False
    sender_true = False
    if recipient.endswith('.ru') or recipient.endswith('.com') or recipient.endswith('.net'):
        recipient_true = True
    if sender.endswith('.ru') or sender.endswith('.com') or sender.endswith('.net'):
        sender_true = True
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    else:
        if recipient_true and sender_true:
            if sender == 'university.help@gmail.com':
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
            elif '@' not in recipient or '@' not in sender:
                print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
