class Solution:
    """
    @param logs: the logs
    @return: the log after sorting
    """
    # O(nlogn)
    def logSort(self, logs):
        # Write your code here
        str_content_logs = []
        num_content_logs = []
        for log in logs:
            index = log.index(" ")
            if log[index + 1].isdigit():
                num_content_logs.append(log)
            if log[index + 1].isalpha():
                str_content_logs.append(log)

        return sorted(str_content_logs, key=self.log_key) + num_content_logs

    def log_key(self, log):
        index = log.index(" ")
        return (log[index + 1:], log[:index])