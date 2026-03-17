# source="travduxtechnologies"
# target="vridautx"


class Containerword:
    def solution(self,source:str,target:str):
        present=True
        for ch in target:
            if ch not in source:
                present= False
                break
            return present
        
Container_word_instance=Containerword()
print(Container_word_instance.solution("traviduxtechnology","vridautx"))


# method 2
class Containerword:
    def solution(self,source:str,target:str):
        present=True
        present=set(target).issubset(set(source))
        return present
        
Container_word_instance=Containerword()
print(Container_word_instance.solution("traviduxtechnology","vridautx"))





