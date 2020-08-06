import random, string, csv

used_nirc = []
batch_count = 50

grades_template = ["F", "D", "D+", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"]

headers = ["NAME","NIRC","IS200", "IS103", "IS101", "WRIT001"]

f = open("names.txt", "r")
names = []

line = f.readline()
while line:
    names.append(line.strip())
    line = f.readline()

random.shuffle(names)

def export_batch(batch_name):
    f = open(batch_name + '.csv', 'w')
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    students = generate_batch()
    for student in students:
        writer.writerow(student)

def generate_batch():
    students = []
    for i in range(50):
        students.append(generate_student())
    return students

def generate_student():
    generate_nirc_check = False
    nirc = ""
    while nirc == "":
        nirc = generate_nirc()
        if nirc not in used_nirc:
            generate_nirc_check = True
        else:
            nirc = ""
    return {headers[0]: nirc, headers[1]: names.pop(), headers[2]: random.choice(grades_template), headers[3]: random.choice(grades_template), headers[4]: random.choice(grades_template), headers[5]: random.choice(grades_template)}

def generate_nirc():
    return random.choice(['S','T']) + ''.join(random.choice(string.digits) for i in range(7)) + random.choice(string.ascii_uppercase)

if __name__ == "__main__":
    export_batch("fy2016-17")
    export_batch("fy2017-18")
    export_batch("fy2018-19")
    export_batch("fy2019-20")