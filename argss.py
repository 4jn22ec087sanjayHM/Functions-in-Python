def calculate_total(*prices):
    total=0

    for price in prices:
        total+=price
    return total
total=calculate_total(100,200,300)
print(total)

def display_subjects(*subjects):
    counter=0
    for subject  in subjects:
        print(subject)
        counter+=1
    print(counter)

counter=display_subjects("Python","Html","SQL","javascript")
