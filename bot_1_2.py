from lib import *
from superdriver import SuperDriver

def main(bot_num=1, pause_time=10, max_users=100, device=None):
    terminal = Terminal()
    d = SuperDriver(driver_start(device))

    persons = read_file('urls.txt')
    for i in range(len(persons)):
        temp = persons[i]
        temp = temp[:temp.rfind('/')+1]
        persons[i] = temp
        print(persons[i])

    authorization(d)

    if bot_num == 1:
        button_path = '//ul/li[2]/a'
        file_path = 'Подписчики.txt'
    elif bot_num == 2:
        button_path = '//ul/li[3]/a'
        file_path = 'Подписки.txt'

    for person in persons:
        d.get(person)
        el = d.element_by_xpath(button_path)
        d.click(el)
        sleepr(5,7)
        scroll_page(d, pause_time, max_users) # * +12 users each iteration

        # get users urls
        users_links = []
        users = d.elements_by_xpath('//li//a[@title]')
        for user in users:
            users_links.append(user.get_attribute('href'))
            print(users_links[-1])

        write_file(file_path, users_links)
        # print([user for user in users_links])


    terminal.ok('\nDone\n')
    d.driver.quit()

if __name__ == "__main__":
    try:
        terminal = Terminal()
        main()
    except:
        terminal.print_except()
            
# 1. сбор подписчиков по списку
# берет из специального файла url акк, 
# заходит на них и парсит всех подписчиков исходя из лимитов.
# если не успел, запоминает где остановился и продолжает снова через паузу.
# результат сохраняет в специальный файл добавлением.

# 2. сбор подписок по списку
# берет из специального файла url акк, заходит 
# на них и парсит все подписки исходя из лимитов.
# если не успел, запоминает где остановился и продолжает снова через паузу.
# результат сохраняет в специальный файл добавлением.