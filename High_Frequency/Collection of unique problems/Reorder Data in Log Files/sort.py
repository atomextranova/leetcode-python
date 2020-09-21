class Solution:
    # Key
    # First divide into digts/alphas
    # for alphas, sort key = x[1:0] + x[0]
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        alphas = []

        for log in logs:
            log = log.split()
            if log[1].isdigit():
                digits.append(log)
            else:
                alphas.append(log)

        alphas.sort(key=lambda x: x[1:] + [x[0]])
        results = alphas + digits

        for i in range(len(results)):
            results[i] = " ".join(results[i])

        return results