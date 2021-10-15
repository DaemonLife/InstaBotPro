from lib import *
from superdriver import SuperDriver

def main(post_num=4, pause_time=2, max_users=50, mod='all', device=None):
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
        iteration += 1
        d.get(person+'feed/')
        sleepr(2,4)
      

        try:
            likes_elements = '//section/div//a'
            likes_elements = d.elements_by_xpath(likes_elements)
            # while by posts
            i = 0
            while (i < len(likes_elements)) and (i < post_num):
                print(f'Parsing {i+1} post likes/comments')

                # * PARSING LIKES
                if (mod == 'likes') or (mod == 'all'): 
                    # open likes post
                    likes_elements = '//section/div//a'
                    likes_elements = d.elements_by_xpath(likes_elements)
                    print(f'len of comment elements is {len(likes_elements)}')

                    if (likes_elements == None):
                        print('Посты не найдены')
                        continue

                    d.driver.execute_script("arguments[0].click();", likes_elements[i])
                    # scroll
                    sleepr(2,3)

                    # check if the site is loaded, checking the visibility of users
                    if d.elements_by_xpath('//a[@title]') == None:
                        d.driver.refresh()
                        sleepr(3,5)
                        if d.elements_by_xpath('//a[@title]') == None:
                            terminal.warning('\nInstagram blocked you!')
                            input('Press <Enter> to exit. . . ')
                            return 0

                    scroll_page(d, pause_time, max_users)
                    # users likes parsing
                    users_links = []
                    users = d.elements_by_xpath('//a[@title]')
                    current_url = d.driver.current_url
                    for user in users:
                        str_ = user.get_attribute('href') + '\t' + current_url + '\t' + person
                        users_links.append(str_)
                        print(users_links[-1])
                    write_file('Активная аудитория.txt', users_links)

                    # back
                    el = '//header//button' # back button
                    el = d.element_by_xpath(el)
                    if el == None:
                        print('Кнопка вернуться назад не найдена')
                        continue
                    d.driver.execute_script("arguments[0].click();", el)

                # * PARSING COMMENTS
                if (mod == 'comments') or (mod == 'all'): 
                    # users comments parsing
                    comment_elements = '//span[2]/button[@type="button"]'
                    comment_elements = d.elements_by_xpath(comment_elements)
                    print(f'len of comment elements is {len(comment_elements)}')
                    el = comment_elements[i] # open comments
                    d.driver.execute_script("arguments[0].click();", el)

                    # check if the site is loaded, checking the visibility of any comments (author and users)
                    if d.elements_by_xpath('//li') == None:
                        d.driver.refresh()
                        sleepr(3,5)
                        if d.elements_by_xpath('//li') == None:
                            terminal.warning('\nInstagram blocked you!')
                            input('Press <Enter> to exit. . . ')
                            return 0

                    scroll_block(d, pause_time, max_users) # * not quite right, but works well! :)
                    comments = []
                    els = '//h3' # user case
                    els = d.elements_by_xpath(els)
                    current_url = d.driver.current_url
                    if els != None:
                        for el in els:
                            msg = el.find_element_by_xpath('div/a')
                            msg = msg.get_attribute('href')
                            temp = el.find_element_by_xpath('..')
                            temp = temp.find_element_by_xpath('span')
                            msg += '\t' + temp.text
                            msg = msg.replace('\n','')
                            msg += '\t' + current_url + '\t' + person
                            print(msg)
                            comments.append(msg)

                        write_file('Активная аудитория.txt', comments)
                    
                    # back
                    d.get(person+'feed/')
                    sleepr(4,6)
                    terminal.ok(f'\nParsing {i+1} post likes and comments is complited\n')
                    i+=1 # parsing post likes and comments is complited. Next cycle

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

# это будет 5й парсер :)
# заходим на акк по списку и лезем не в его подписчиков, 
# а в крайние x-его постов (задаем в интерфейсе) и парсим всех, кто поставил лайки :)
# таким образом получим вовлеченную аудиторию
# также собираем и тех, кто прокомментировал
# тоже из админки задаем: что собирать - оставивших лайки/комменты или все вместе
# разумеется с пометкой что именно оставил подписчик