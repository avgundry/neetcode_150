from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        # if n == 1:
        #     return 1

        # Hm. We can think of this as...each car will reach the end by
        # some time. If another car with a lower position would reach 
        # the end before the time of the first, they form a fleet...
        # I think.

        # This looks like we need a monotonic stack: we want the top of
        # the stack to store the fleet that will arrive *latest*.
        # Then at each new car, if that car would arrive after the 
        # current one...it becomes part of that fleet? Hm.

        # Brute force to start might be to make a new array and sort it
        # by car position.
        # For each car, it either overtakes the car ahead of it or it
        # doesn't. If it doesn't, it cannot be used to form any further
        # fleets, so we pop it and increment our total.
        car_times = sorted([((target - pos) / sp, pos) for pos, sp in zip(position, speed)],)
                        
        print(car_times)
        total = 0
        curr = car_times.pop()
        while car_times:
            # guaranteed that curr[0] < car_times[-1][0], i.e. that
            # our current car will take longer to reach the destination
            # than the next car.
            # Thus just check if the next car is in front of or behind
            # the current one; if it's behind it will form a fleet with
            # it.
            if curr[1] > car_times[-1][1]:
                curr2 = car_times.pop()
                car_times.append((max(curr[1], curr2[1]),min(curr[0], curr2[0])))
            else:
                total += 1
            curr = car_times.pop()

        return total + 1



if __name__ == "__main__":
    s = Solution()
    print(s.carFleet(10, [3], [3]))
    print(s.carFleet(13, [10,2,5,7,4,6,11], [7,5,10,5,9,4,1]))
    print(s.carFleet(100, [0, 2, 4], [4, 2, 1]))
    print(s.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))

        