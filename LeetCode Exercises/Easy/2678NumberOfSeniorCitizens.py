#2678

def get_num_senior_citizens(details):
    count = 0
    for passanger in details:
        if int(passanger[11]) >= 6:
            count += 1

    
    return count


print(get_num_senior_citizens(["1234567890M3210", "1134568290M6010", "1334536890M7210"]))