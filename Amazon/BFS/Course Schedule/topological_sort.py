class Solution:
    # Topological Sort
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        pre_requisite_list = [0 for _ in range(numCourses)]
        pre_dict = {i: [] for i in range(numCourses)}
        finish_count = 0
        # pre_dict = {}

        for pair in prerequisites:
            # if not pair:
            #     continue
            pre, post = pair
            pre_dict[pre].append(post)
            pre_requisite_list[post] += 1

        course_queue = []
        for i, count in enumerate(pre_requisite_list):
            if count != 0:
                continue
            course_queue.append(i)

        while course_queue:
            finished_course = course_queue.pop()
            finish_count += 1
            # if finished_course not in pre_dict:
            #     continue
            for post in pre_dict[finished_course]:
                pre_requisite_list[post] -= 1
                if pre_requisite_list[post] != 0:
                    continue
                course_queue.append(post)
            # print(pre_requisite_list)
            # print(course_queue)

        return finish_count == numCourses