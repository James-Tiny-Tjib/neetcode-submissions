class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Create Position and Speed Tuple Pair
        cars = list(zip(position, speed))

        # Sort the cars by position in descending order
        sorted_cars = sorted(cars, reverse = True)

        # Define Monotonic Decreasing Stack (The result will be the length)
        car_fleets = []

        # Iterate Through the cars in descending order by speed
        for p,s in sorted_cars:
            
            # Calculate Time
            arrival_time = (float)(target - p) / s

            if (not car_fleets) or car_fleets[-1] < arrival_time:
                car_fleets.append(arrival_time)
                    
        return len(car_fleets)





        