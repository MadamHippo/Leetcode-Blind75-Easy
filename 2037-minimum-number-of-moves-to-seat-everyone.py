# O(n) time
# O(1) space

# seat and student same length

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        seats.sort()
        # seats [1, 4, 5, 9]
        students.sort()
        #students [1, 2, 3, 6]
        
        answer = 0
        
        for i in range(len(seats)):
            answer += abs(seats[i] - students[i])
        return answer
