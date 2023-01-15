import csv
from bs4 import BeautifulSoup
import requests


def main():
    date = input("PLS enter the Date MM/DD/YYYY : ")
    page = requests.get(
        f"https://www.yallakora.com/Match-Center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A"
        f"%D8%A7%D8%AA?date={date}#days")

    src = page.content
    soup = BeautifulSoup(src, "lxml")
    matchdetils = []
    tournments = soup.findAll("div", {'class': 'matchesList'})
    number_tour = len(tournments)
    # print(tournments)
    for i in range(number_tour):
        def match_details_title(tournments):
            tournment_title = tournments.contents[1].find('h2').text.strip()
            all_matchs = tournments.contents[3].find_all("li")
            number_match = len(all_matchs)
            # if i==0:()
            # else:(
            # print("--------------------------------------")
            # )
            # print(tournment_title)
            for x in range(number_match):
                team_A = all_matchs[x].find("div", {'class': 'teamA'}).text.strip()
                team_B = all_matchs[x].find("div", {'class': 'teamB'}).text.strip()
                match_score = all_matchs[x].find("div", {'class': 'MResult'}).find_all("span", 'score')
                match_time = all_matchs[x].find("div", {'class': 'MResult'}).find("span",{'class': 'time'}).text.strip()
                score = f"'{match_score[0].text.strip()} - {match_score[1].text.strip()}'"
                #  print(team_A, score, team_B)
                # print("-----", match_time, "-----")
                matchdetils.append(
                    {"نوع البطوله": tournment_title, "الفريق الاول": team_A, "النتيجه": score.strip(), "الفريق الثاني": team_B,
                     "وقت المباره": match_time, "تاريخ": date})
                #print(matchdetils)

        match_details_title(tournments[i])

    keys = matchdetils[0].keys()
    with open("C:/Users/Yehia/Desktop/match_calender.csv", 'w',encoding='utf-8-sig') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matchdetils)
    output_file.close()
    q = input("IF you want to countuie press Y : ")
    if q == "y":
        main()
    else:
        return 0


main()
