import sys
import math

def S_total(score_list):
    quiz = score_list[:-1]
    score_list.remove(min(quiz))
    return sum(score_list)

def S_adjusted(S_total, max_S):
    return math.ceil((S_total/max_S)*100)

def letter(S_grade):
    if 90 <= S_grade <= 100:
        return "A"
    elif 80 <= S_grade < 90:
        return "B"
    elif 70 <= S_grade < 80:
        return "C"
    elif 60 <= S_grade < 70:
        return "D"
    else:
        return "F"

def main():
    contents = sys.stdin.readlines()

    contents = contents[1:]

    grade_book = []
    max_total = 0
    
    for line in contents:
        line = line.split()
        name = line[0]
        total = S_total([int(score) for score in line[1:]])
        if max_total < total:
            max_total = total
        data = []
        data.append(name)
        data.append(total)
        grade_book.append(data)

    for student in grade_book:
        adjust = S_adjusted(student[1], max_total)
        letter_grade = letter(adjust)
        student.append(adjust)
        student.append(letter_grade)
        print("{} {} {} {}".format(student[0], student[1], student[2], student[3]))

if __name__ == "__main__":
    main()

# first = contents[0]
    # num_student, num_tests = [int(num) for num in first.split()]

    # print(grade_book)
    # grade_book = {}
    # for line in contents:
    #     line = line.split()
    #     grade_book[line[0]] = S_total([int(score) for score in line[1:]])
    
    # max_S = max([value for value in grade_book.values()])
    
    # for key, value in grade_book.items():
    #     S_adjust = S_adjusted(value, max_S)
    #     letter_grade = letter(S_adjust)
    #     l = []
    #     l.append(value)
    #     l.append(S_adjust)
    #     l.append(letter_grade)
    #     value = l
    #     print("{} {} {} {}".format(key, value[0], value[1], value[2]))