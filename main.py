import Matrix

score_board = Matrix.build_up()
student_mx = []


def highest_average_score():

    mx = 0
    avg_score = 0

    for row in range(1, 100):
        avg_score = 0

        for column in range(1, 6):
            avg_score += int(score_board[row, column])

        avg_score /= 5
        if avg_score > mx:
            mx = avg_score
            student_mx.clear()
            student_mx.append(score_board[row, 0])

        elif avg_score == mx:
            student_mx.append(score_board[row, 0])

    for each in student_mx:
        print(f"{each}, ", end="")

    print(f"საშუალო ქულა = {avg_score}")
    print("___________________________")


def best_and_worst():
    mx = 0
    mn = 101
    student_low = []

    for row in range(1, 100):
        score = int(score_board[row, 2])
        
        if score > mx:
            student_mx.clear()
            student_mx.append(score_board[row, 0])
            mx = score

        elif score == mx:
            student_mx.append(score_board[row, 0])
        
        elif score < mn:
            student_low.clear()
            student_low.append(score_board[row, 0])
            mn = score

        elif score == mn:
            student_low.append(score_board[row, 0])

    for each in student_mx:
        print(f"{each}, ", end="")
    print(f"მაქსიმალური ქულა მათემატიკაში = {mx}")
    print("__________________________________")

    for each in student_low:
        print(f"{each}, ", end="")
    print(f"მინიმალური ქულა მატემატიკაში = {mn}")


def above_average():
    avg_score = 0

    for row in range(1, 100):
        avg_score += int(score_board[row, 3])

    avg_score //= 100

    for row in range(1, 100):
        if int(score_board[row, 3]) > avg_score:
            print(score_board[row, 0])

# highest_average_score()
# best_and_worst()
# above_average()
