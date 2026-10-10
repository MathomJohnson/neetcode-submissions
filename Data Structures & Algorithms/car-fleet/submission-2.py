class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for car in cars:

            if not stack: 
                stack.append(car)
                continue

            time = (target - car[0]) / car[1]
            nextTime = (target - stack[-1][0]) / stack[-1][1]

            if time <= nextTime:
                continue
            elif time > nextTime:
                stack.append(car)

        return len(stack)