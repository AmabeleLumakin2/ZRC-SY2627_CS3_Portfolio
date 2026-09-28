def zodiacSign(birth_year):
    zodiac = (birth_year - 1900) % 12
    
    if zodiac == 0:
        return"Rat (鼠 / Shǔ)"
    elif zodiac == 1:
        return"Ox (牛 / Niú)"
    elif zodiac == 2:
        return"Tiger (虎 / Hǔ)"
    elif zodiac == 3:
        return"Rabbit (兔 / Tù)"
    elif zodiac == 4:
        return"Dragon (龙 / Lóng)"
    elif zodiac == 5:
        return"Snake  (蛇 / Shé)"
    elif zodiac == 6:
        return"Horse  (马 / Mǎ)"
    elif zodiac == 7:
        return"Goat (羊 / Yáng)"
    elif zodiac == 8:
        return"Monkey (猴 / Hóu)"
    elif zodiac == 9:
        return"Rooster (鸡 / Jī)"
    elif zodiac == 10:
        return"Dog (狗 / Gǒu)"
    else:
        return"Pig (猪 / Zhū)",


birth_year = int(input("Enter your birth year: "))

if birth_year < 1900:
        print("Invalid Year, it should not be earlier than 1900.")
else:
    result = zodiacSign(birth_year)

    print("Your Chinese Zodiac Sign is:", result)
