def solution(experience, threshold, reward):
    # Calculate total points
    points = experience + reward
    # Check if after killing the monster points are equal or greater than the threshold to pass to the next level
    if points >= threshold:
        return True # pass to next level   
    else:
        return False # unable to pass to next level
    

"""
You are playing an RPG game. Currently your experience points (XP) total is equal to experience. To reach the next level your XP should be at least at threshold. If you kill the monster in front of you, you will gain more experience points in the amount of the reward.

Given values experience, threshold and reward, check if you reach the next level after killing the monster.

Example

For experience = 10, threshold = 15, and reward = 5, the output should be
solution(experience, threshold, reward) = true;
For experience = 10, threshold = 15, and reward = 4, the output should be
solution(experience, threshold, reward) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer experience

Guaranteed constraints:
3 ≤ experience ≤ 250.

[input] integer threshold

Guaranteed constraints:
5 ≤ threshold ≤ 300.

[input] integer reward

Guaranteed constraints:
2 ≤ reward ≤ 65.

[output] boolean

true if you reach the next level, false otherwise.
"""