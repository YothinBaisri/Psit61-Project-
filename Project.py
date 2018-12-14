import csv
import matplotlib
import matplotlib.pyplot as plt



""" All varible """
game_rank = {}
game_style = []


""" """

  
def keep(varible, style):
    """ keep data """
    for year in range(2000, 2019):
        file = csv.reader(open(r"C:\Users\GGG\Desktop\PYTHON\Project\list GOY\%s.csv" %year))
        varible[year] = list(file)
    for key, item in varible.items():
        for top in range(10):
            game_style.append(item[top][2])
keep(game_rank, game_style)



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
        lis_x.append(i)
        lis_y.append(style.count(i))
        print(style.count(i), i)
        
    plt.plot(lis_x, lis_y, 'ro-')
    plt.xlabel("Year")
    plt.ylabel("Average")
    plt.title("Top")
    plt.xticks(lis_x, rotation=50)
    plt.show()

top_style(game_style)


        
