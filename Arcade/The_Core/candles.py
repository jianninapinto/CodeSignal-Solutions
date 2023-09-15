def solution(candlesNumber, makeNew):
    # Keep track of total num of candles we have burned
    total_burned = 0
    # Keep track of total num of leftovers we have
    leftovers = 0
    # The while loop will run as long as we have candles left to burn
    while candlesNumber > 0:
        # Since we are going to burn all the candles, we add the total
        # num of candles we have to total_burned
        total_burned += candlesNumber
        # Since each burned candle leaves behind a leftover, we add
        # the num of candles we have to leftovers
        leftovers += candlesNumber
        # No candles left, so we set candlesNumber to zero
        candlesNumber = 0
        # Calculate new num of candles we can make using leftovers
        candlesNumber = leftovers // makeNew
        # Update leftovers value with the remainder of the division
        # above, that will be the num of leftovers left after making
        # the new candles
        leftovers = leftovers % makeNew
    # Return the total num of candles burned
    return total_burned

"""
When a candle finishes burning it leaves a leftover. makeNew leftovers can be combined to make a new candle, which, when burning down, will in turn leave another leftover.

You have candlesNumber candles in your possession. What's the total number of candles you can burn, assuming that you create new candles as soon as you have enough leftovers?

Example

For candlesNumber = 5 and makeNew = 2, the output should be
solution(candlesNumber, makeNew) = 9.

Here is what you can do to burn 9 candles:

burn 5 candles, obtain 5 leftovers;
create 2 more candles, using 4 leftovers (1 leftover remains);
burn 2 candles, end up with 3 leftovers;
create another candle using 2 leftovers (1 leftover remains);
burn the created candle, which gives another leftover (2 leftovers in total);
create a candle from the remaining leftovers;
burn the last candle.
Thus, you can burn 5 + 2 + 1 + 1 = 9 candles, which is the answer.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer candlesNumber

The number of candles you have in your possession.

Guaranteed constraints:
1 ≤ candlesNumber ≤ 15.

[input] integer makeNew

The number of leftovers that you can use up to create a new candle.

Guaranteed constraints:
2 ≤ makeNew ≤ 5.

[output] integer

"""