from lib import *
from superdriver import SuperDriver

def main(pause_time=4, device=None):
    terminal = Terminal()
    d = SuperDriver(driver_start(device))

    all_persons = read_file('urls.txt')
    persons_for_unsub = []
    for i in range(len(all_persons)):
        temp = all_persons[i]
        if temp.find('Подписался') != -1:
            temp = temp[:temp.rfind('/')+1]
            persons_for_unsub.append(temp)
            print(temp)

    authorization(d)
    iteration = 0

    for person in persons_for_unsub:
        print(f'\nOpen user {person}')
        iteration += 1
        d.get(person)
        sleepr(2,4)
      
        # * Unsubscribe
        try:
            # * first
            button = '//span/span[1]/button' # first button
            button = d.element_by_xpath(button, 3)
            if button != None:
                # button check
                if (button.text == 'Follow') or (button.text == 'Подписаться'):
                    print('You are not following this person')
                    continue
            else: # for requested button
                button = '//button[text()="Requested"]' # first button
                button = d.element_by_xpath(button)
            # click first button
            if button != None:
                d.driver.execute_script("arguments[0].click();", button)
            else:
                print('Button not found')
                continue

            # * second
            button = '//button[text()="Unfollow"]' # second eng button
            button = d.element_by_xpath(button)
            if button == None:
                button = '//button[text()="Отписаться"]' # second ru button
                button = d.element_by_xpath(button)
            # click second button
            if button != None:
                d.driver.execute_script("arguments[0].click();", button)
                print('Unsubscribed')
            else:
                print('Button not found')
                continue

            # * Rewrite urls file
            for i in range(len(all_persons)):
                temp = all_persons[i]
                if temp.rfind(person) != -1:
                    now_date = datetime.now()
                    now_time = str(now_date.time())
                    now_time = now_time[:now_time.rfind('.')]
                    all_persons[i] = temp[:temp.rfind('/')+1] + '\tОтписался\t' + str(now_date.date()) + ' ' + now_time
                    break

            write_file('urls.txt', all_persons, 'w')

        except:
            # terminal.print_except() # ! only for test
            continue

        sleepr(pause_time-2,pause_time)

    terminal.ok('\nDone\n')
    d.driver.quit()

if __name__ == "__main__":
    try:
        terminal = Terminal()
        main()
    except:
        terminal.print_except()

# 3. лайки и подписки
# берет из специального файла url акк, заходит на них, 
# лайкает (крайние x постов с проверкой
# лайкали ли мы их ранее), подписывается (если выбрано и на них не подписан) 
# ? исходя из лимитов.
# ? если не успел, запоминает где остановился и продолжает снова через паузу.

# напротив отработанных url ставит пометку о том что делал лайк/подписку
#  через табуляцию и время тоже через табуляцию.