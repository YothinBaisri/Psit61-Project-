import csv
import matplotlib
import matplotlib.pyplot as plt



""" All varible """
game_rank = {}
game_style = []
game_plat = []


""" """

  
def keep(varible, style, plat):
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
keep(game_rank, game_style, game_plat)



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
    plt.title("Top")
    plt.xticks(lis_x, rotation=45)
    plt.show()
      
top_rank_flag(game_rank)


def top_style(style, lis_x=[], lis_y=[]):
    for i in set(style):
        
        print(style.count(i), i)
        
    plt.plot(lis_x, lis_y, 'ro-')
    plt.xlabel("Year")
    plt.ylabel("Average")
    plt.title("Top")
    plt.xticks(lis_x, rotation=50)
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


