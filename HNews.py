from csv import reader
import datetime as dt
opened_file = open('hacker_news.csv')
read_file = reader(opened_file)
hn = list(read_file)

ask_posts = []
show_posts = []
other_posts = []

#In this step we're going to separated the publications
for row in hn:
    title = row[1].lower()
    if title.startswith('ask hn'):
        ask_posts.append(row)
    elif title.startswith('show hn'):
        show_posts.append(row)
    else:
        other_posts.append(row)
        
# here we add the comments by each publication
def totalComments(lista, indice):
    total_comments = 0
    for row in lista:
        num_comments = int(row[indice])
        total_comments += num_comments
    return total_comments

total = totalComments(ask_posts, 4)
avg_ask_comments = total / len(ask_posts)
print(avg_ask_comments)

total_show = totalComments(show_posts, 4)
avg_show_comments = total_show / len(show_posts)
print(avg_show_comments)

result_list = []
for row in ask_posts:
    created_at = row[6]
    num_comments = int(row[4])
    result_list.append([created_at, num_comments])
counts_by_hour = {}
comments_by_hour = {}
for row in result_list:
    date, time = row[0].split()
    #print(time) #here is the hour
    #print(date) #8/28/2016
    date = dt.datetime.strptime(date, '%m/%d/%Y')
    if time not in counts_by_hour:
        counts_by_hour[time] = 1
        comments_by_hour[time] = row[1]
    else:
        counts_by_hour[time] += 1
        comments_by_hour[time] += row[1]

avg_by_hour = []
for row in counts_by_hour:
    avg_by_hour.append([row, comments_by_hour[row] / counts_by_hour[row]])

swap_avg_by_hour = []
for element in avg_by_hour:
    swap_avg_by_hour.append([element[1], element[0]])
sorted_swap = swap_avg_by_hour.sort(reverse = True)
#print(swap_avg_by_hour)
sorted_swap = swap_avg_by_hour
print(sorted_swap[:3])

for lista in sorted_swap:
    date = dt.datetime.strptime(lista[1], '%H:%M')
    date = dt.datetime.strftime(date, '%H:%M')
    string = "{} {:.2f} average comments per post".format(date, lista[0])
    print(string)