class Solution:
    def romanToInt(self, s: str) -> int:
        s_c= s[::-1]
        listed= list(s_c)
        previouslisted=[0]
        var= 0
        while len(listed):
            
            for l in listed:
                if l=="M" :
                    previouslisted.append(listed[0])
                    listed.remove(listed[0])
                    if previouslisted[-2]  == "C":
                        var-=100
                    else:
                        var+=1000
                    break

                elif l=="D" :
                    previouslisted.append(listed[0])
                    listed.remove(listed[0])
                    if previouslisted[-2]  == "C":
                        var-=100
                    else:
                        var+=500
                    break
                elif l=="C" :
                    previouslisted.append(listed[0])
                    listed.remove(listed[0])
                    if previouslisted[-2]  == "X":
                        var-=10
                    else:
                        var+=100
                    break
                
                elif l=="L" :
                    previouslisted.append(listed[0])
                    listed.remove(listed[0])
                    if previouslisted[-2]  == "X":
                        var-=10
                    else:
                        var+=50
                    break
                                
                elif l=="X" :
                    previouslisted.append(listed[0])
                    listed.remove(listed[0])
                    if previouslisted[-2]  == "I" :
                        var-=1
                    else:
                        var+=10
                    break

                elif l=="V" :
                    previouslisted.append(listed[0])
                    listed.remove(listed[0])
                    if previouslisted[-2]  == "I":
                        var-=1
                    else:
                        var+=5
                    break
                
                if l=="I" :
                    var+=1
                    previouslisted.append(listed[0])
                    listed.remove(listed[0])
                    break
        
        return var
        
numero=Solution()
print(numero.romanToInt("XL"))
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        listed= list(str(s))
        var= 0
        i = 0
        while listed != "" and i < len(listed):
            if listed[0] == "I":
                var+=1
                listed.remove(listed[0])
            elif listed[0] == "V":
                var+= 5
                listed.remove(listed[0])
            elif listed[0] == "X":
                var+= 10
                listed.remove(listed[0])
            elif listed[0] == "L":
                var+= 50
                listed.remove(listed[0])
            elif listed[0] == "C":
                var+= 100
                listed.remove(listed[0])
            elif listed[0] == "D":
                var+= 500
                listed.remove(listed[0])
            elif listed[0] == "M":
                var+= 1000
                listed.remove(listed[0])
        return var

numero=Solution()
print(numero.romanToInt("MV"))
"""