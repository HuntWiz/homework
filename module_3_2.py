def send_email(message, recipient, *, sender="university.help@gmail.com"):

    if recipient.endswith(('.com', '.ru', '.net')) == False or recipient.find('@') == -1 or sender.find('@') == -1 or sender.endswith(('.com', '.ru', '.net')) == False:
        print("Невозможно отправить письмо с адреса {0} на адрес {1}".format(sender, recipient))
        return False
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return False
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса {0} на адрес {1}.".format(sender, recipient))
        return True
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {0} на адрес {1}.".format(sender, recipient))
        return True


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')