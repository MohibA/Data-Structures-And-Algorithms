class Solution:
    
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = list()
        digit_logs = list()
        for log in logs:    
            if log[-1].isnumeric():
                digit_logs.append(log)
            else: 
                letter_logs.append(log)
        
        
        letter_logs = sorted(letter_logs, key = lambda x: [x.split(" ")[1:], x.split(" ")[:1]])
        
        return letter_logs + digit_logs

   