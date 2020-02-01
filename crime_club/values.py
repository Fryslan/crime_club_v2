class Values:
    # parameters
    running = True
    crush_cars = True
    sell_cars = False
    trade_in_weapon_experience = True
    break_out_players_when_idle = True
    bank_cash = True
    finished_weapon_training = False
    jail_breakout_only = False

    garage_count = -1
    weapon_experience = "0"
    weapon_training = "0"
    player_rank = 'scum'

    # pages
    login_page = 'https://www.crime-club.nl/login.php'
    base_page = 'https://www.crime-club.nl/'
    index_page = 'https://www.crime-club.nl/index.php'
    crime_page = 'https://www.crime-club.nl/nav.php?p=crimes'
    carjack_page = 'https://www.crime-club.nl/nav.php?p=stealvehicles'
    delivery_boy_page = 'https://www.crime-club.nl/nav.php?p=deliveryboy'
    gym_page = 'https://www.crime-club.nl/nav.php?p=gym'
    weapon_training_page = 'https://www.crime-club.nl/nav.php?p=murdering&tab=weapontraining'
    hookers_page = 'https://www.crime-club.nl/nav.php?p=redlightdistrict'
    player_list_page = 'https://www.crime-club.nl/nav.php?p=members&tab=memberlist&x=0&page='

    # xpaths
    timer_light_crime_x_path = '/html/body/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td[1]'
    timer_heavy_crime_x_path = '/html/body/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td[2]'
    timer_weapon_experience_x_path = '/html/body/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td[3]'
    timer_hookers_x_path = '/html/body/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td[4]'

    timer_light_carjack_x_path = '/html/body/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td[1]'
    timer_heavy_carjack_x_path = '/html/body/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td[2]'
    timer_safe_cracking_x_path = '/html/body/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td[3]'
    timer_land_attack_x_path = '/html/body/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td[4]'

    timer_family_crime_x_path = '/html/body/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td[1]'
    timer_family_robbery_x_path = '/html/body/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td[2]'
    timer_delivery_boy_x_path = '/html/body/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td[3]'
    timer_gym_x_path = '/html/body/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td[4]'

    player_list_data_x_path = '/html/body/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/table/tbody/tr[3]/td/table[1]/tbody'
    jail_x_path = '/html/body/table/tbody/tr/td[1]/table/tbody/tr[8]/td/a'
    jail_all_x_path = '/html/body/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td[2]/b[1]'
    rank_status_x_path = '/html/body/table/tbody/tr/td[3]/form/table/tbody/tr[6]/td/b'