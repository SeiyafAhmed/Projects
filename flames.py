def flames(boy="", girl=""):
    f = """
---------------------------------[ FLAMES ]---------------------------------
            _____ ____   _______    ________   _        ____
           |      |   \\     |      |          | \\   |  |    \\
           |----  |___/     |      |------    |  \\  |  |     |
           |      |   \\  ___|___   |________  |   \\_|  |____/
    """
    l = """
-----------------------[ FLAMES ]-----------------------
                    ____           ________
           |       /    \\  \\    / |
           |      |      |  \\  /  |------
           |_____  \\____/    \\/   |________
           """
    a = """
----------------------------------------------------[ FLAMES ]----------------------------------------------------
              _     _______  _______  ____      _      _____   _______  _______   ____   _
             / \\       |        |     |   \\    / \\    /     \\     |        |     /    \\  | \\   |
            /---\\      |        |     |___/   /---\\  |            |        |    |      | |  \\  |
           /     \\     |        |     |   \\  /     \\  \\_____/     |     ___|___  \\____/  |   \\_|
           """

    m = """
------------------------------------------[ FLAMES ]------------------------------------------
            _      _      _    ____   ____   _______    _      ____     ________
           | \\    / |    / \\   |   \\  |   \\     |      / \\    /    \\   |
           |   \\_/  |   /---\\  |___/  |___/     |     /---\\  |   __    |-------
           |        |  /     \\ |   \\  |   \\  ___|___ /     \\  \\____|   |________"""
    e = """
-------------------------------[ FLAMES ]-------------------------------
            ________    _        ________   _     _    
           |           | \\   |  |          | \\   / |  \\   /
           |------     |  \\  |  |------    |  \\_/  |   \\_/
           |________   |   \\_|  |________  |       |    |
        """
    s = """
------------------------------------[ FLAMES ]------------------------------------
            _______   _______   ____           _______   ____     _______
           |             |     |    )  |          |     /    \\   |
            -------      |     |---<   |          |    |    __    -------
            _______|  ___|___  |____)  |_____  ___|___  \\____|    _______|
           """

    if boy == "":
        boy = list(input("Enter the boy name   :").lower())
    else:
        boy = list(boy)
    if girl == "":
        girl = list(input("Enter the girl name  :").lower())
    else:
        girl = list(girl)
    while " " in boy:
        boy.remove(" ")
    while " " in girl:
        girl.remove(" ")
    for i in boy:
        if i in girl:
            boy.remove(i)
            girl.remove(i)
    for i in girl:
        if i in boy:
            boy.remove(i)
            girl.remove(i)
    num = len(boy) + len(girl)
    t = ["f", "l", "a", "m", "e", "s"]
    x = 0
    b = 0
    while len(t) > 1:
        x = num % len(t) - 1
        t.pop(x)
        for i in range(x):
            t.append(t[0])
            t.pop(0)
    if "f" in t:
        print(f)
        
    elif "l" in t:
        print(l)
        
    elif "a" in t:
        print(a)
        
    elif "m" in t:
        print(m)
        
    elif "e" in t:
        print(e)

    elif "s" in t:
        print(s)


while True:
    flames()
    d = input("""
Do you wish to continue (Y/N) : """).lower()
    if 'n' in d:
        break
