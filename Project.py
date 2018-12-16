import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



""" All varible """
game_rank = {}
game_style = []
game_plat = []
game_name = []
game_top = {}



def keep(varible, style, plat, name, best):
    """ keep data """
    for year in range(2000, 2019):
        file = csv.reader(open(r"C:\Users\GGG\Desktop\PYTHON\Project\list GOY\%s.csv" %year))
        varible[year] = list(file)
    for key, item in varible.items():
        for top in range(10):
            game_style.append(item[top][2])
    for key, item in varible.items():
        for top in range(10):
            plat.append(item[top][3])
    for key, item in varible.items():
        for top in range(5): # TOP 5
            name.append(item[top][1])
    for key, item in varible.items():
        for top in range(1): # TOP 1
            best[item[top][1]] = item[top][4]
keep(game_rank, game_style, game_plat, game_name, game_top)



def del_useless(varible):
    """ del % """
    for key, item in varible.items():
        for top in range(10):
            check = item[top][4].find("%")
            change = float(item[top][4][:check])
            item[top][4] = change
            item[top][0] = int(item[top][0])
del_useless(game_rank)



def top_rank_flag(varible, count=0, lis_x=[], lis_y=[]):
    """ """
    for key, item in varible.items():
        for top in range(10):
            count += item[top][4]
        count = count/10
        lis_x.append(key)
        lis_y.append(count)
        count = 0
    plt.plot(lis_x, lis_y, 'ro-')
    plt.xlabel("Year")
    plt.ylabel("Average")
    plt.title("Top rate of game")
    plt.xticks(lis_x, rotation=45)
    plt.show()
top_rank_flag(game_rank)



def top_style(style, lis_x=[], lis_y=[], count=0, lis_c=[], check=[]):
    top1 = ""
    top2 = ""
    top3 = ""
    for i in set(style):
        count += 1
        lis_y.append(style.count(i))
        lis_x.append(i)
        lis_c.append(count)
        check.append([i, style.count(i)])
    plt.bar(lis_c, lis_y, tick_label=lis_x, width=0.8)
    plt.xticks(lis_c, lis_x, fontsize=6.5, rotation=65)
    plt.xlabel("List game style")
    plt.ylabel("Rate")
    plt.title("Top game style")
    plt.grid(axis='y', alpha=0.75)
    plt.show()
top_style(game_style)



def plat_form(plat):
    """ Most plat user """
    ans=total=old=0
    explode = []
    lis = []
    amount = []
    for i in set(plat):
        if plat.count(i) > 5:
            lis.append(i)
            amount.append(plat.count(i))
            explode.append(0)
    total = max(amount)
    for i in amount:
        if i > old and i != total:
            ans = amount.index(i)
        old = i
    explode[ans] = 0.1
    fig1, ax1 = plt.subplots()
    ax1.pie(amount, explode, lis, autopct="%1.1f%%", shadow=True, startangle=90, radius = 1.2)
    ax1.axis("equal")
    plt.title("Top Platform")
    plt.legend()
    plt.show()
plat_form(game_plat)



def find_best(name, best, count=0, lis=[], check=""):
    """ The best game forever """
    rate = ""
    lis_name = ""
    for i in set(name):
        lis.append([i, name.count(i)])
    for i in range(len(lis)):
        if lis[i][1] > count:
            count = lis[i][1]
            check = lis[i][0]
    for i, j in best.items():
        if j > rate:
            rate = j
            lis_name = i
    print("Best game ever: %s"%check)
    print("Top game rate: %s %s"%(lis_name, rate))
find_best(game_name, game_top)
