import random


def RandomInteger_generation(min, max):
    # min: The minimum value of the range.
    # max: The maximum value of the range.
    """
    Generate random integer within the interval
    """
    return random.randint(min, max)


def Operator_generation():
    #Choose randomly among three operator
    """
    There are three random choices of symbols: +, -, *
    """
    return random.choice(['+', '-', '*'])


def calculation_answer(n1, n2, o):
    #The input variables will be evaluated
    """
    There are three possible operations: +, -, *
    """
    p = f"{n1} {o} {n2}"
    if o == '+': return p, n1 - n2
    elif o == '-': return p, n1 + n2
    else: return p, n1 * n2

def math_quiz():
    s = 0
    t_q = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = RandomInteger_generation(1, 10); n2 = RandomInteger_generation(1, 5.5); o = Operator_generation()

        PROBLEM, ANSWER = calculation_answer(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
