#
def send_mail(from_name, old):
    text = f'Уважаемый, Сергей Балакерев! Я так и не понял, что такое функция. Объясните лучше! {from_name}.' \
           f' И не судите строго, мне всего {old} лет'
    print(text)


send_mail('Nikolay', 36)  # Уважаемый, Сергей Балакерев! Я так и не понял, что такое функция. Объясните лучше!


def weight(kg):
    a = f'Предмет имеет вес: {kg} кг.'
    print(a)


weight(int(input()))