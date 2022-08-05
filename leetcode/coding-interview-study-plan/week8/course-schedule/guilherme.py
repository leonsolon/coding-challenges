class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if len(prerequisites) == 0:
            return True

        courses_done = set()
        courses_to_be_done = set(range(0, numCourses))
        courses_to_be_done_next = set()

        last_len = -1

        prerequisites_course = {}
        for p in prerequisites:
            p = p[::-1]
            # print(p)
            while len(p) > 0:
                prereq = p.pop()
                # print(prereq)
                if prereq not in prerequisites_course:
                    prerequisites_course[prereq] = set(p)
                else:
                    prerequisites_course[prereq] = prerequisites_course[prereq].union(set(p))

        print(prerequisites_course)

        while courses_to_be_done or courses_to_be_done_next:
            if not courses_to_be_done:
                if last_len == len(courses_to_be_done_next):
                    return False
                last_len = len(courses_to_be_done_next)
                courses_to_be_done = courses_to_be_done_next
                courses_to_be_done_next = set()
            course = courses_to_be_done.pop()
            # print(course)

            if course not in prerequisites_course or len(prerequisites_course[course]) == 0 or set(
                    prerequisites_course[course]).issubset(courses_done):
                courses_done.add(course)
            else:
                courses_to_be_done_next.add(course)
        return True