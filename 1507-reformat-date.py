1507	Reformat Date	https://leetcode.com/problems/reformat-date/	String

class Solution:
    def reformatDate(self, date: str) -> str:
        hashmap_months = {
            "Jan":"01", 
            "Feb":"02", 
            "Mar":"03", 
            "Apr":"04", 
            "May":"05", 
            "Jun":"06", 
            "Jul":"07", 
            "Aug":"08", 
            "Sep":"09", 
            "Oct":"10", 
            "Nov":"11", 
            "Dec":"12"}
        
        split_date = date.split(" ")
        day = split_date[0][:-2]
        month = split_date[1]
        month = hashmap_months[month]
        year = split_date[2]
        
        
        #if len(day) > 1:
            #day.zfill(2)
            
        new_day = day.zfill(2)
        
        output_date = year + "-" + month + "-" + new_day
        
        return output_date
        
