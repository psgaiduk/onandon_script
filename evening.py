from usual_func import countdown, next_step


def start_evening():
    print('Вечер начало')
    countdown(50, 'Обучение программированию')
    countdown(15, 'Рисование')
    next_step('SmartProgess заполнение отчёта')
    next_step('Заполни дневник, пишу, почему сегодня я лучше чем вчера')
    countdown(30, 'Чтение')
    next_step('Чистка зубов, водные процедуры, открыть окно не забудь')


if __name__ == '__main__':
    start_evening()
