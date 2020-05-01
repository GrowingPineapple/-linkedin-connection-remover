from linkedin_api import Linkedin, client

import csv
with open('input.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    login = "YourUserName"
    password = "YourPassword"
    try:
        linkedin = Linkedin(login, password, refresh_cookies=True)
    except client.ChallengeException:
        print("Login to LinkedIn in browser, then press any key")
        input()
        linkedin = Linkedin(login, password, refresh_cookies=True)
        reader.read()
    next(reader, None)
    for row in reader:
        if row[0] == '':
            continue
        url = row[0].split("/")
        user_id = url[-1] if url[-1] else url[-2]
        while 1:
            try:
                removed = not linkedin.remove_connection(user_id, timeout=10)
                break
            except:
                print("Error on", user_id)
                continue
        if removed:
            print(user_id, "removed")
        else:
            print(user_id, "didn't removed")

        with open('processed.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow([user_id])
