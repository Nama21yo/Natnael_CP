from collections import defaultdict


class Solution:
    """ 
    This class contains various methods for solving problems using the line sweep algorithm.
    """

    def maximum_population_year(self, logs):
        """ 
        Problem 1854: Maximum Population Year [Easy]
        Given birth and death years of persons, determine the year with the maximum population.
        """
        from collections import defaultdict
        
        line = defaultdict(int)
        for birth, death in logs:
            line[birth] += 1
            line[death] -= 1
        
        max_population = 0
        current_population = 0
        result_year = 0
        
        for year in sorted(line.keys()):
            current_population += line[year]
            if current_population > max_population:
                max_population = current_population
                result_year = year
        
        return result_year

    def min_meeting_rooms(self, intervals):
        """ 
        Problem 253: Meeting Rooms II [Medium]
        Return the minimum number of conference rooms required for the meetings.
        """
        from collections import defaultdict
        
        line = defaultdict(int)
        for interval in intervals:
            line[interval[0]] += 1
            line[interval[1]] -= 1
        
        max_rooms = 0
        current_rooms = 0
        
        for time in sorted(line.keys()):
            current_rooms += line[time]
            max_rooms = max(max_rooms, current_rooms)
        
        return max_rooms

    def book(self, start, end):
        """ 
        Problem 731: My Calendar II [Medium]
        Check if the booking can be made without triple booking.
        """
        self.m = defaultdict(int)
        self.m[start] += 1
        self.m[end] -= 1
        
        count = 0
        for time in sorted(self.m.keys()):
            count += self.m[time]
            if count >= 3:
                self.m[start] -= 1
                self.m[end] += 1
                return False
        
        return True

    def count_positions(self, brightness_thresholds):
        """ 
        Problem 2237: Count Positions on Street With Required Brightness [Medium]
        Count the positions where the brightness meets the required threshold.
        """
        brightness = defaultdict(int)
        
        for threshold in brightness_thresholds:
            brightness[threshold[0]] += 1
            brightness[threshold[1] + 1] -= 1
        
        ans = 0
        current_brightness = 0
        
        for position in range(1, 51):  # Assuming the range is [1, 50]
            current_brightness += brightness[position]
            if current_brightness >= threshold:
                ans += 1
        
        return ans

    def min_arrows(self, points):
        """ 
        Problem 452: Minimum Number of Arrows to Burst Balloons [Medium]
        Determine the minimum number of arrows needed to burst all balloons.
        """
        points.sort(key=lambda x: x[1])
        prev_end = points[0][1]
        arrows = 1
        
        for i in range(1, len(points)):
            if points[i][0] > prev_end:
                arrows += 1
                prev_end = points[i][1]
        
        return arrows

    def find_non_overlapping_intervals(self, intervals):
        """ 
        Problem 435: Non-overlapping Intervals [Medium]
        Find the maximum number of non-overlapping intervals.
        """
        intervals.sort(key=lambda x: x[1])
        prev_end = float('-inf')
        count = 0
        
        for interval in intervals:
            if interval[0] >= prev_end:
                count += 1
                prev_end = interval[1]
        
        return count

    def insert_interval(self, intervals, new_interval):
        """ 
        Problem 57: Insert Interval [Medium]
        Insert a new interval into a set of non-overlapping intervals, merging if necessary.
        """
        intervals.append(new_interval)
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged

    def remove_interval(self, intervals, to_be_removed):
        """ 
        Problem 1272: Remove Interval [Medium]
        Remove intervals that overlap with a specified interval.
        """
        result = []
        for interval in intervals:
            if interval[1] <= to_be_removed[0] or interval[0] >= to_be_removed[1]:
                result.append(interval)
            else:
                if interval[0] < to_be_removed[0]:
                    result.append([interval[0], to_be_removed[0]])
                if interval[1] > to_be_removed[1]:
                    result.append([to_be_removed[1], interval[1]])
        
        return result

    def meeting_scheduler(self, person1, person2, duration):
        """ 
        Problem 1229: Meeting Scheduler [Medium]
        Find a meeting time that works for both persons.
        """
        # Convert available time intervals to a suitable format
        events = []
        for start, end in person1 + person2:
            events.append((start, 1))  # Start of an interval
            events.append((end, -1))    # End of an interval
        
        events.sort()
        
        count = 0
        last_time = None
        for time, change in events:
            if count == 2 and last_time is not None and time - last_time >= duration:
                return [last_time, last_time + duration]
            count += change
            last_time = time
        
        return []

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Example for maximum_population_year
    print(solution.maximum_population_year([[1993, 1999], [2000, 2010]]))  # Example output
    
    # Example for min_meeting_rooms
    print(solution.min_meeting_rooms([[0, 30], [5, 10], [15, 20]]))  # Example output
    
    # Example for My Calendar II booking
    print(solution.book(10, 20))  # Example output for booking
    print(solution.book(15, 25))  # Example output for booking
    
    # Example for count_positions
    print(solution.count_positions([(1, 5), (2, 3), (4, 8)]))  # Example output
    
    # Example for min_arrows
    print(solution.min_arrows([[10, 16], [2, 8], [1, 6], [7, 12]]))  # Example output
    
    # Example for find_non_overlapping_intervals
    print(solution.find_non_overlapping_intervals([[1,2], [2,3], [3,4], [1,3]]))  # Example output
    
    # Example for insert_interval
    print(solution.insert_interval([[1,3], [6,9]], [2,5]))  # Example output
    
    # Example for remove_interval
    print(solution.remove_interval([[1, 2], [3, 4], [5, 6]], [2, 3]))  # Example output
    
    # Example for meeting_scheduler
    print(solution.meeting_scheduler([[10, 12]], [[11, 13]], 1))  # Example output
