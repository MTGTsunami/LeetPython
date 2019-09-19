"""
Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.



Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation:
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.


Note:

1 <= items.length <= 1000
items[i].length == 2
The IDs of the students is between 1 to 1000
The score of the students is between 1 to 100
For each student, there are at least 5 scores
"""


class MySolution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        items.sort(key=lambda x: (x[0], -x[1]))
        total, count = 0, 0
        end = False
        curr_id = items[0][0]
        res = []
        for item in items:
            Id = item[0]
            if curr_id == Id:
                if not end:
                    total += item[1]
                    count += 1
                    if count >= 5:
                        end = True
                        average = total / 5
                        res.append([curr_id, average])
                        count, total = 0, 0
            else:
                curr_id = Id
                end = False
                total += item[1]
                count += 1
        return res


# 可以将每个人的成绩存储在dict中，像存储图（adjacent matrix）一样
