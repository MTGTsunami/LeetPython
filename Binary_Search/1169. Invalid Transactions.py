"""
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.

Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.



Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]


Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.
"""

from collections import defaultdict
import bisect


class MySolution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = set()
        trans = defaultdict(dict)
        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            if int(amount) > 1000:
                res.add(transaction)
            if name not in trans or city not in trans[name]:
                trans[name][city] = []
            bisect.insort_left(trans[name][city], (int(time), int(amount)))

            for k in trans[name].keys():
                if k != city:
                    i = bisect.bisect_left(trans[name][k], (int(time), int(amount)))
                    p1 = p2 = i
                    while p1 >= 0 and abs(trans[name][k][p1 - 1][0] - int(time)) <= 60:
                        res.add(transaction)
                        res.add(str(name) + "," + str(trans[name][k][p1 - 1][0]) + "," + str(
                            trans[name][k][p1 - 1][1]) + "," + str(k))
                        p1 -= 1
                    while p2 < len(trans[name][k]) and abs(trans[name][k][p2][0] - int(time)) <= 60:
                        res.add(transaction)
                        res.add(
                            str(name) + "," + str(trans[name][k][p2][0]) + "," + str(trans[name][k][p2][1]) + "," + str(
                                k))
                        p2 += 1
        return list(res)

