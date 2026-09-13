class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # The idea goes like this:
        # With the position and speed, we can tell when the car will reach the destination. So if we start with car closest to the end, and if that time is longer than the car behind it, the car behind it will join up with the current. We can put this in a stack, but we won't have to monotonically pop off a car that was already on the list if the current car will arrive slower. We actually count the number of cars in the stack to determin the car fleet. We only pop ones off that get held up by the car on top of the stack.

        # Zip to get position, speed
        car_fleet = zip(position, speed)

        # Sort the car_fleet by position in descending order, so we process the car that is closest to the end
        car_fleet = sorted (car_fleet, reverse=True)

        # Make a stack
        stack = []

        for (pos, s) in car_fleet:

            time = float(target-pos) / s

            if not stack or time > stack[-1]:
                stack.append(time)

        # Return the length of the stack
        return len(stack)





          






    