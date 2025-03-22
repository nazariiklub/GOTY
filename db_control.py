
# import sqlite3

# conn = sqlite3.connect('rating.db')
# c = conn.cursor()

# def convert_to_binary_data(filename):
#     with open(filename, 'rb') as file:
#         blob_data = file.read()
#     return blob_data

# # Оновлене створення таблиці з додаванням стовпця link_more
# c.execute('''CREATE TABLE IF NOT EXISTS rating (
#           id INTEGER PRIMARY KEY,
#           year INTEGER,
#           name VARCHAR,
#           developers VARCHAR,
#           rating INTEGER,
#           genre VARCHAR,
#           description VARCHAR,
#           image BLOB,        
#           link_more VARCHAR
#           )''')

# # Створення інших таблиць, якщо потрібно
# c.execute('''CREATE TABLE IF NOT EXISTS cart (
#           id INTEGER PRIMARY KEY,
#           id_product INTEGER
#           )''')

# c.execute('''CREATE TABLE IF NOT EXISTS card_product (
#           id INTEGER PRIMARY KEY,
#           id_card INTEGER,
#           id_rating INTEGER,
#           quantity INTEGER,
#           FOREIGN KEY(id_card) REFERENCES cart(id),
#           FOREIGN KEY(id_rating) REFERENCES rating(id)
#           )''')


# serials_list = [
    # ['2024', 'Astro Bot', 'Japan Studio', '90/100', 'Платформер, пригоди', 'Віртуальна реальність із веселими пригодами робота в чудовому світі.', convert_to_binary_data(r'yasrobot.jpg'), 'https://store.steampowered.com/app/994010/Astro_Bot_Rescue_Mission/'],
    # ['2023', 'Baldur\'s Gate 3', 'Larian Studios', '93/100', 'RPG, дії, пригоди', 'Рольова гра у світі Dungeons & Dragons з глибокою сюжетною лінією та складною механікою бою.', convert_to_binary_data(r'ybg3.jpg'), 'https://store.steampowered.com/app/1086940/Baldurs_Gate_3/'],
    # ['2022', 'Elden Ring', 'FromSoftware', '96/100', 'Action RPG, відкритий світ, пригоди', 'Епічна рольова гра з відкритим світом і складною механікою бою, створена компанією FromSoftware.', convert_to_binary_data(r'yed.jpg'), 'https://store.steampowered.com/app/1245620/Elden_Ring/'],
    # ['2021', 'Resident Evil Village', 'Capcom', '84/100', 'Action, Horror, Survival', 'Четверта частина "Resident Evil" з новими героями та переживаннями в холодному і темному світі.', convert_to_binary_data(r'yrev.jpg'), 'https://store.steampowered.com/app/1196590/Resident_Evil_Village/'],
    # ['2020', 'The Last of Us Part II', 'Naughty Dog', '93/100', 'Action, Adventure', 'Продовження гри The Last of Us, знову слідуючи за персонажами Еллі і Джоелом в постапокаліптичному світі.', convert_to_binary_data(r'ytlou2.jpg'), 'https://store.steampowered.com/app/1222680/The_Last_of_Us_Part_II/'],
    # ['2019', 'Sekiro: Shadows Die Twice', 'FromSoftware', '90/100', 'Action, Adventure', 'Гра з елементами бойових мистецтв, яка переносить гравців у феодальний Японський період з механікою смертельних боїв.', convert_to_binary_data(r'ysekiro.jpg'), 'https://store.steampowered.com/app/814380/Sekiro_Shadows_Die_Twice/'],
    # ['2018', 'Red Dead Redemption 2', 'Rockstar Games', '97/100', 'Action, Adventure', 'Історія Артура Моргана та його банди в США, відкритий світ, насичений сюжет і захоплюючі пригоди.', convert_to_binary_data(r'yrdr2.jpg'), 'https://store.steampowered.com/app/1174180/Red_Dead_Redemption_2/'],
    # ['2017', 'Horizon Zero Dawn', 'Guerrilla Games', '89/100', 'Action RPG', 'Історія про дівчину на ім\'я Елой, яка бореться з роботизованими істотами в постапокаліптичному світі.', convert_to_binary_data(r'yhzd.jpg'), 'https://store.steampowered.com/app/1151640/Horizon_Zero_Dawn_Complete_Edition/'],
    # ['2016', 'Overwatch', 'Blizzard Entertainment', '91/100', 'FPS, командний шутер', 'Мультиплеєрна командна гра, де гравці обирають героїв з унікальними здібностями для боротьби проти інших команд.', convert_to_binary_data(r'yo.jpg'), 'https://store.steampowered.com/app/356980/Overwatch/'],
    # ['2015', 'The Witcher 3: Wild Hunt', 'CD Projekt Red', '93/100', 'RPG, Action', 'Епічна рольова гра з відкритим світом, в якій гравці виступають у ролі відьмака Геральта в пошуках своєї прийомної дочки.', convert_to_binary_data(r'ygeralt.jpg'), 'https://store.steampowered.com/app/292030/The_Witcher_3_Wild_Hunt/'],
    # ['2014', 'Dragon Age: Inquisition', 'BioWare', '89/100', 'RPG', 'Рольова гра з відкритим світом, де гравець виступає в ролі інквізитора, який повинен врятувати світ від злих сил.', convert_to_binary_data(r'ydei.jpg'), 'https://store.steampowered.com/app/1222700/Dragon_Age_Inquisition/'],
    # ['2013', 'Bioshock Infinite', 'Irrational Games', '94/100', 'Action, Adventure, FPS', 'Шутер від першої особи, де гравець досліджує хмарне місто Колумбія і рятує дівчину, що володіє надзвичайними здібностями.', convert_to_binary_data(r'ybi.jpg'), 'https://store.steampowered.com/app/8870/BioShock_Infinite/'],
    # ['2012', 'The Walking Dead', 'Telltale Games', '92/100', 'Adventure', 'Інтерактивна історія в світі "The Walking Dead", де гравець вибирає, як розвиватиметься сюжет і взаємодіє з іншими персонажами.', convert_to_binary_data(r'ytwdjpg.jpg'), 'https://store.steampowered.com/app/207610/The_Walking_Dead/'],
    # ['2011', 'The Elder Scrolls V: Skyrim', 'Bethesda', '94/100', 'RPG, відкритий світ', 'Відкрите світоутворююче RPG, де гравець грає за драконорожденного в фентезійному світі Скайрім.', convert_to_binary_data(r'yskyrim.jpg'), 'https://store.steampowered.com/app/489830/The_Elder_Scrolls_V_Skyrim_Special_Edition/'],
    # ['2010', 'Mass Effect 2', 'BioWare', '94/100', 'RPG, шутер, наукова фантастика', 'Продовження науково-фантастичної гри, в якій гравець виступає в ролі командора Шепарда, рятуючи галактику від знищення.', convert_to_binary_data(r'yme2.jpg'), 'https://store.steampowered.com/app/17460/Mass_Effect_2/'],
    # ['2009', 'Uncharted 2: Among Thieves', 'Naughty Dog', '96/100', 'Action, Adventure', 'Пригодницький шутер, що стежить за пригодами Нейтана Дрейка в пошуках артефактів по всьому світу.', convert_to_binary_data(r'yu2.jpg'), 'https://store.steampowered.com/app/119860/Uncharted_2_Among_Thieves/'],
    # ['2008', 'Fallout 3', 'Bethesda Game Studios', '91/100', 'RPG, відкритий світ', 'Постапокаліптичне RPG, де гравець досліджує пост-апокаліптичний Вашингтон.', convert_to_binary_data(r'yf3.jpg'), 'https://store.steampowered.com/app/22370/Fallout_3/'],
    # ['2007', 'The Orange Box', 'Valve', '95/100', 'Action, Puzzle, Shooter', 'Компільований набір з ігор, включаючи Half-Life 2, Team Fortress 2, Portal і інші.', convert_to_binary_data(r'ytob.jpg'), 'https://store.steampowered.com/app/380/The_Orange_Box/'],
    # ['2006', 'The Elder Scrolls IV: Oblivion', 'Bethesda', '94/100', 'RPG, відкритий світ', 'Рольова гра з відкритим світом, де гравець досліджує континент Тамріель і бореться з темними силами.', convert_to_binary_data(r'yoblivion.jpg'), 'https://store.steampowered.com/app/22330/The_Elder_Scrolls_IV_Oblivion/'],
    # ['2005', 'God of War', 'Santa Monica Studio', '94/100', 'Action, Adventure', 'Гра про Кратоса, антигероя грецької міфології, який бореться з богами та монстрами.', convert_to_binary_data(r'ygow.jpg'), 'https://store.steampowered.com/app/414620/God_of_War/'],
    # ['2004', 'Half-Life 2', 'Valve', '96/100', 'Action, Shooter', 'Гравець керує Гордоном Фріменом, щоб боротися з інопланетянами у постапокаліптичному світі.', convert_to_binary_data(r'yhl2.jpg'), 'https://store.steampowered.com/app/220/HalfLife_2/'],
    # ['2003', 'Star Wars: Knights of the Old Republic', 'BioWare', '93/100', 'RPG', 'Рольова гра, що відбувається в світі Зоряних Війн, де гравець може вибирати між темною та світлою стороною сили.', convert_to_binary_data(r'ysw.jpg'), 'https://store.steampowered.com/app/32370/Star_Wars_Knights_of_the_Old_Republic/'],
    # ['2002', 'The Elder Scrolls III: Morrowind', 'Bethesda', '93/100', 'RPG, відкритий світ', 'Рольова гра з відкритим світом, де гравець досліджує місто Морровінд, з боротьбою за королівську владу.', convert_to_binary_data(r'ymoro.jpg'), 'https://store.steampowered.com/app/22320/The_Elder_Scrolls_III_Morrowind/'],
    # ['2001', 'Grand Theft Auto III', 'Rockstar Games', '90/100', 'Action, відкритий світ', 'Класична гра в жанрі відкритого світу, де гравець бере на себе роль злочинця в місті Ліберті-Сіті.', convert_to_binary_data(r'ygta3.jpg'), 'https://store.steampowered.com/app/12260/Grand_Theft_Auto_III/'],
    # ['2000', 'Deus Ex', 'Ion Storm', '92/100', 'Action RPG', 'Класичний шутер з елементами RPG, який дозволяє гравцям вибирати різні шляхи для досягнення мети в кіберпанковому світі.', convert_to_binary_data(r'ydesus.jpg'), 'https://store.steampowered.com/app/6910/Deus_Ex/']


# ]

# # Додаємо серіали в таблицю
# for rating in serials_list:
#     c.execute('''INSERT INTO rating (year, name, developers, rating, genre, description, image, link_more)
#                  VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', rating)

# # Перевіряємо, чи було додано все в базу
# c.execute('''SELECT * FROM rating''')
# rows = c.fetchall()

# print(rows)

# conn.commit()
# conn.close()










