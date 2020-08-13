'''
https://py.checkio.org/en/mission/multiply-intro/

This is an intro mission, the purpose of which is to explain how to solve
missions on CheckiO and how to get the most out of solving them. When the
mission is solved, one more station become available for you, containing more
complex missions.

So this mission is the easiest one. Write a function that will receive 2
numbers as input and it should return the multiplication of these 2 numbers.

Input: Two arguments. Both are int

Output: Int.

How does it work?:

When you start solving the initial code is always consists of an “empty”
function (which you need to fill in as the solution) and asserts under this
function. You should pay attention to is that your function should return
values, and not to print them. That is, use the return command instead of the
print function. Check this short explanation.

The asserts after your function you can use in order to check yourself by
pressing the “Run” button (). CheckiO also uses several additional tests in
order to check your solution when you click the “Check” button ().

If the solution didn’t pass the internal tests, the right panel will display an
error message containing 3 items.

Fail: - shows how your function was called. Your Result: - shows what it
returned. Right Result: - what it should’ve returned. To solve the task the
“empty” function must be replaced with the following code.

def mult_two(a: int, b: int) -> int: return a*b Try to click “Check” button now

If the solution passes all the tests, the congratulations should appear on the
right panel along with a suggestion for the following action. (Yes, this is not
the end of the story).

View other solutions - when the task is solved, you can access the solutions of
other players, which are divided into categories. Publish your solution -
publish your own solution. Next Mission - go to the next mission. I’d recommend
to go through the solutions of other players before publishing your own.

The last but not the least, some tasks at the end have a list of hints for
solving. But since in this task we’ve already described how to solve, then in
hints we’ll add some interesting facts about CheckiO
'''


def mult_two(a, b):
    return a * b


if __name__ == '__main__':
    print("Example:")
    print(mult_two(3, 2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
