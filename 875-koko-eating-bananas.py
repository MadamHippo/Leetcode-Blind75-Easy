class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        # We know the constraint is: len(p) <= h

        # the least Koko could eat to finish all the bananas
        lowerBound = 1
        # the most Koko could eat to finish all bananas (but she likes eating slowly)
        upperBound = max(piles)

        resultMinimumK= max(piles) # upperBound basically

        # while lowerBound is still smaller than upperBound
        while lowerBound <= upperBound:
            # let's find k (what's the minimum Koko should eat)
            k = (lowerBound + upperBound) // 2

            # count how much for this k, how many hours do we need to eat all bananas...
            totalTime = 0
            for pile in piles:
                # for any pile, we divide by k to get hours and add it to see if crosses max input h
                totalTime += math.ceil(pile / k)

            # if hours calculated is less than input h given...
            if totalTime <= h:
                # update result to the new minimum k...
                resultMinimumK = min(resultMinimumK, k)
                upperBound = k-1
            else:
                lowerBound = k+1
        return resultMinimumK
