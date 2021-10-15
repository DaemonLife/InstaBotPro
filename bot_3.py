from lib import *
from superdriver import SuperDriver

def main(post_num=2, subscribe_on=True, max_users=50, pause_time=4, device=None):
    terminal = Terminal()
    d = SuperDriver(driver_start(device))

    persons = read_file('urls.txt')
    for i in range(len(persons)):
        temp = persons[i]
        temp = temp[:temp.rfind('/')+1]
        persons[i] = temp
        print(persons[i])

    authorization(d)

    iteration = 0

    for person in persons:
        print(f'\nOpen user {person}')
        # d.get(person) # ! only for tests, enable (or not...)
        d.get(person+'feed/')
        liked = False # for rewriting urls file
        followed = False
        iteration += 1
        sleepr(2,4)

        # * checking if there were already subscribed
        follow_button = d.element_by_xpath('//button[text()="Follow"]', 1)
        if follow_button == None:
            follow_button = d.element_by_xpath('//button[text()="Подписаться"]', 1)
        if follow_button == None:
            print(f'Iteration {i+1}: Subscribe button not found. Passing user')
            sleepr(pause_time-2,pause_time)
            continue

        # * Likes
        # checking if there were already likes
        if (d.element_by_xpath('//*[name()="svg"][@aria-label="Не нравится"]') != None) or (d.element_by_xpath
        ('//*[name()="svg"][@aria-label="Unlike"]') != None):
            print(f'Iteration {i+1}: You have already liked this user.')
        else:

            like_buttons = d.elements_by_xpath('//article//span[1]/button') # like button
            if like_buttons == None:
                print('Empty profile. I will not like')
            else:
                i = 0
                while (i < post_num) and (i < len(like_buttons)):
                    el = like_buttons[i]
                    try:
                        d.driver.execute_script("arguments[0].click();", el)
                        print(f'Iteration {i+1}: liked')
                        timer(random.uniform(pause_time-2, pause_time+2))
                        liked = True
                    except:
                        # terminal.print_except() # ! for tests
                        pass
                    i += 1 
        
        # * Subscribe
        try:
            d.driver.execute_script("arguments[0].click();", follow_button)
            print('Subscribed')
            followed = True
        except:
            # terminal.print_except() # ! for tests
            continue

        sleepr(pause_time-2,pause_time)

        # * Rewrite urls file
        if (followed == True) or (liked == True):
            links = read_file('urls.txt')
            temp = links[iteration-1]
            links[iteration-1] = temp[:temp.rfind('/')+1]
            now_date = datetime.now()
            now_time = str(now_date.time())
            now_time = now_time[:now_time.rfind('.')]
            if liked == True:
                links[iteration-1] += '\tЛайкнул'
            if followed == True:
                links[iteration-1] += '\tПодписался'
            links[iteration-1] += '\t' + str(now_date.date()) + ' ' + now_time

            write_file('urls.txt', links, 'w')

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