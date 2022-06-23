import heapq


def scheduleCourse(courses):
    ret, sum_of_duration = [], 0
    tmp = sorted(courses, key=lambda course:course[1])
    
    #if prev_duration + duration <= deadline   --->  maintain order && both class can be taken
    #else --> you need to choose one class -> less duration -> need to delete maximum duration class
    for duration, deadline in tmp:
        heapq.heappush(ret, -duration)
        sum_of_duration += duration
        if sum_of_duration > deadline:
            delet_course = -heapq.heappop(ret)
            sum_of_duration -= delet_course
    return len(ret)






courses = [[5,5],[4,6],[2,6]]
print(scheduleCourse(courses))