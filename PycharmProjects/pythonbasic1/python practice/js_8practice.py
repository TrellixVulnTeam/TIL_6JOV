# # 1.
# # 현우는 축구를보다가 우리나라선수들의몸값을 알고싶었다
# # 그래서 검색을해서 메모장에 적는데 키보드가 조그만하고 안좋은지라
# # 자꾸 숫자가아닌 문자를 같이입력해버린다
# # ex: xxx : 1627000000 > xxx : 1w627r00o00p00 만 (특수문자제외)
# # 현우는 왜인지모르지만 뜻대로안되는것에
# # 너무화가나서 자신이수량을입력하면 문자열만 딱빼서 숫자만 반환하는 코드를 만들고싶어한다
# # 화가난 현우를위해 코드를 만들어보자!
#
# # import re
# # num= input("입력하세요 : ")
# #
# # numonly= re.compile('[0-9]')
# # print(''.join(numonly.findall(num)))
#
#
#
# #
# # 2.
# # 회원가입페이지 수정 및 추가
# # 1)signup버튼 클릭시 검증 작업 목록
# # - id는 6글자 이상 12글자 이하(숫자 문자 조합 가능, 반드시 문자로 시작)
# # - pw와 pw확인에서 동일한지 확인
# # - 취미가 몇개 선택되었는지 확인
# # (4개가 모두 선택된 경우에는 3개 이하로 선택하라는 경고메시지 출력->재체크)
# # -생년월일 입력한 뒤에 현재 나이에 마우스 포커스가 들어오면 자동으로 나이를 계산
# # 하여 출력
# # - 이메일 아이디 작성 규칙 검증(일반적인 규칙)
# # ex) 아이디에 올 수 없는 문자 :
# # @,#...특수문자가 올 수 없음, 길이를 12글자로 제한
# # - 전화번호 작성 규칙 검증
# # - 자기소개는 최소 10글자 이상 작성해야 함(10글자 미만인 경우 메시지 출력)
# #
# # 3. (매우 어려움)
# #
# # 데이터 처리 전문가가 되고 싶은 “어피치”는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다. 최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데, 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다. 간단한 예로 “aabbaccc”의 경우 “2a2ba3c”(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데, 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다. 예를 들면, “abcabcdede”와 같은 문자열은 전혀 압축되지 않습니다. “어피치”는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.
# # 예를 들어, “ababcdcdababcdcd”의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 “2ab2cd2ab2cd”로 표현할 수 있습니다. 다른 방법으로 8개 단위로 잘라서 압축한다면 “2ababcdcd”로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.
# # 다른 예로, “abcabcdede”와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 “abcabc2de”가 되지만, 3개 단위로 자른다면 “2abcdede”가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다. 이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.
# # 압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.
# #
# # 제한사항
# # s의 길이는 1 이상 1,000 이하입니다.
# # s는 알파벳 소문자로만 이루어져 있습니다.
# # 입출력 예
# # s				result
# # "aabbaccc"			7
# # "ababcdcdababcdcd"		9   #2ababcdcd
# # "abcabcdede"			8
# # "abcabcabcabcdededededede"	14
# # "xababcdcdababcdcd"		17
# #
# # 입출력 예에 대한 설명
# # 입출력 예 #1 문자열을 1개 단위로 잘라 압축했을 때 가장 짧습니다.
# # 입출력 예 #2 문자열을 8개 단위로 잘라 압축했을 때 가장 짧습니다.
# # 입출력 예 #3 문자열을 3개 단위로 잘라 압축했을 때 가장 짧습니다.
# # 입출력 예 #4 문자열을 2개 단위로 자르면 “abcabcabcabc6de” 가 됩니다. 문자열을 3개 단위로 자르면 “4abcdededededede” 가 됩니다. 문자열을 4개 단위로 자르면 “abcabcabcabc3dede” 가 됩니다. 문자열을 6개 단위로 자를 경우 “2abcabc2dedede”가 되며, 이때의 길이가 14로 가장 짧습니다.
# # 입출력 예 #5 문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다. 따라서 주어진 문자열을 x / ababcdcd / ababcdcd 로 자르는 것은 불가능 합니다. 이 경우 어떻게 문자열을 잘라도 압축되지 않으므로 가장 짧은 길이는 17이 됩니다.
# #
# #"ababcdcd//ababcdcd"   #2ababcdcd
def solution(s):
    length = []
    result = ""

    if len(s) == 1:
        return 1

    for cut in range(1, len(s) // 2 + 1):    #cut=2
        count = 1
        tempStr = s[:cut]
        for i in range(cut, len(s), cut):  #(2,10,2)
            if s[i:i + cut] == tempStr:    #s[2:4]
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + tempStr
                tempStr = s[i:i + cut]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + tempStr
        length.append(len(result))
        result = ""

    return min(length)
print(solution("aabbaccc"))
#7







#ababcdcd
def solution(s):
    leng=[]
    for n in range(1,len(s)//2+1):
        ss=[s[i:i+n] for i in range(0,len(s)-(n-1),n)]

        cnt=1
        res=""
        for i in range(len(ss)-1):
            if ss[i]==ss[i+1]:
                cnt+=1
            else:
                res+=str(cnt)+ss[i]
                cnt=1
        res+=str(cnt)+ss[i+1]

        try:
            res+=s[n*(len(s)//n):]
        except: pass

        res=res.replace("1","")
        leng.append(len(res))
    print(min(leng))

solution("aabbaccc")
solution("ababcdcdababcdcd")
solution("abcabcdede")
solution("abcabcabcabcdededededede")
solution("xababcdcdababcdcd")
#
#
#
#
#
# #################################
#
#
# # a, b = map(int, input().split())
# # if a != 0:
# #     if b >= 45:
# #         print(a, b-45)
# #     else:
# #         print(a - 1, 60 - (45-b))
# # else:
# #     if b >= 45:
# #         print(a, b-45)
# #     else:
# #         print(23, 60 - (45-b))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# #
# # 4. (매우 어려움)
# #
# # 친구들로부터 천재 프로그래머로 불리는 “프로도”는 음악을 하는 친구로부터 자신이
# 좋아하는 노래 가사에 사용된 단어들 중에 특정 키워드가 몇 개 포함되어 있는지 궁금하니
# 프로그램으로 개발해 달라는 제안을 받았습니다. 그 제안 사항 중, 키워드는 와일드카드 문자 중 하나인 ‘?’가
# 포함된 패턴 형태의 문자열을 뜻합니다. 와일드카드 문자인 ‘?’는 글자 하나를 의미하며, 어떤 문자에도 매치된다고
# 가정합니다. 예를 들어 "fro??"는 "frodo", "front", "frost" 등에 매치되지만 "frame", "frozen"에는
# 매치되지 않습니다.
# # 가사에 사용된 모든 단어들이 담긴 배열 words와 찾고자 하는 키워드가 담긴 배열 queries가 주어질 때,
# 각 키워드 별로 매치된 단어가 몇 개인지 순서대로 배열에 담아 반환하도록 solution 함수를 완성해 주세요.
# #
# # 가사 단어 제한사항
# # words의 길이(가사 단어의 개수)는 2 이상 100,000 이하입니다.
# # 각 가사 단어의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
# # 전체 가사 단어 길이의 합은 2 이상 1,000,000 이하입니다.
# # 가사에 동일 단어가 여러 번 나올 경우 중복을 제거하고 words에는 하나로만 제공됩니다.
# # 각 가사 단어는 오직 알파벳 소문자로만 구성되어 있으며, 특수 문자나 숫자는 포함하지 않는 것으로 가정합니다.
# # 검색 키워드 제한사항
# # queries의 길이(검색 키워드 개수)는 2 이상 100,000 이하입니다.
# # 각 검색 키워드의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
# # 전체 검색 키워드 길이의 합은 2 이상 1,000,000 이하입니다.
# # 검색 키워드는 중복될 수도 있습니다.
# # 각 검색 키워드는 오직 알파벳 소문자와 와일드카드 문자인 '?' 로만 구성되어 있으며, 특수 문자나 숫자는 포함하지 않는 것으로 가정합니다.
# # 검색 키워드는 와일드카드 문자인 '?'가 하나 이상 포함돼 있으며, '?'는 각 검색 키워드의 접두사 아니면 접미사 중 하나로만 주어집니다.
# # 예를 들어 "??odo", "fro??", "?????"는 가능한 키워드입니다.
# # 반면에 "frodo"('?'가 없음), "fr?do"('?'가 중간에 있음), "?ro??"('?'가 양쪽에 있음)는 불가능한 키워드입니다.
# # 입출력 예
# # words	queries	result
# # ["frodo", "front", "frost", "frozen", "frame", "kakao"]	["fro??", "????o", "fr???", "fro???", "pro?"]	[3, 2, 4, 1, 0]
# # 입출력 예에 대한 설명
# # "fro??"는 "frodo", "front", "frost"에 매치되므로 3입니다.
# # "????o"는 "frodo", "kakao"에 매치되므로 2입니다.
# # "fr???"는 "frodo", "front", "frost", "frame"에 매치되므로 4입니다.
# # "fro???"는 "frozen"에 매치되므로 1입니다.
# # "pro?"는 매치되는 가사 단어가 없으므로 0 입니다.
# #


#1번풀이

import re
def solution(words,queries):
    res=[]
    for i in queries:
        pat=i.replace("?","[a-z]")
        cnt=0
        for j in words:
            if re.match(pat,j):
                cnt+=1
            res.append(cnt)
    print(res)



#2번풀이
import re
def keyWord(words,queries):
    queryList=[x.replace("?",".") for x in queries]

    result=[]
    for q in queryList:
        count=len([w for w in words if re.match(q,w) and len(q)==len(w)])
        result.append(count)
        print(result)
        keyWord(words,queries)

#다른 분 풀이
def cnt_match(words,q):
    import re
    cnt = 0
    for w in words:
        if re.match(q, w):
            cnt += 1
    return cnt

def num_match(words, queries):
    import re
    res = []
    for q in queries:
        if re.search("^\?+[a-z]*$",q):
            idx = re.match("\?+",q).span()
            q = "^[a-z]{"+str(idx[1])+"}"+q[idx[1]:]+"$"
            res.append(cnt_match(words,q))

        elif re.search("^[a-z]*\?+$",q):
            idx = re.search("\?+",q).span()
            q = "^"+q[:idx[0]]+"[a-z]{"+str(idx[1]-idx[0])+"}$"
            res.append(cnt_match(words, q))
        else:
            res.append(q + ": 불가능한 키워드")
    return res

print(num_match(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?", "fr?do"]))
# [3, 2, 4, 1, 0, 'fr?do: 불가능한 키워드']


#(main) num_match 함수 :
#
# - queries 요소 q를 정규표현식으로 변환 (?가 앞에 있는 경우, ?가 뒤에 있는 경우 분리하여 진행)
#
#     ex) fro?? >>> ^fro[a-z]{2}$
#
#           ????o >>> ^[a-z]{4}o$
#
# - 변환한 요소 q를 cnt_match​ 함수에 넣은 결과(cnt)를 res에 추가
#
# - 결과로 res를 리턴
#
# ​
#
# (sub) cnt_match 함수 :
#
# - words에 있는 단어 w가 num_match에서 가공한 q 패턴과 match되면 cnt+1 해줌
#
# - 결과로 cnt를 리턴

