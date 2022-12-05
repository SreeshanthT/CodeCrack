class Solution:
    def get_sum(self,my_dict:dict)->dict:
        b = sorted(my_dict, key=lambda x : x['department'])
        i, t = 0, []
    
        while i < len(b) -1:
            if b[i]['department'] not in [i['department'] for i in t if i]:
                t += [{'department':b[i]['department'],'amount':b[i]['amount']}]
            
            if b[i]['department'] == b[i+1]['department']:
                t[-1]['amount'] += b[i+1]['amount']
                
            if b[-1]['department'] not in [i['department'] for i in t if i]:
                t += [{'department':b[-1]['department'],'amount':b[-1]['amount']}]
                
                
            i += 1
            
        return t
        
        
            
    
if __name__ == "__main__":
    my_dict = [
        {'project':1,"department":"land","amount":5000},
        {'project':1,"department":"drone","amount":6000},
        {'project':3,"department":"gps","amount":6000},
        {'project':2,"department":"drone","amount":6000},
        {'project':1,"department":"gps","amount":2000},
        {'project':2,"department":"gps","amount":2000},
    ]
    solution = Solution()
    a = solution.get_sum(my_dict)
    print(a)