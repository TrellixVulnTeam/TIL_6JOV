smsraw<-read.csv('./data/sms_spam_ansi.txt')
str(smsraw)
smsraw$type<-factor(smsraw$type)
str(smsraw)

library(tm)
library(stringr)
smsCorpus<-VCorpus(VectorSource(smsraw$text))
inspect(smsCorpus)
class(smsCorpus)


# 1. 수치 데이터 추출 & 제거

#추출
onlydigit<-function(x){
  str_extract_all(x$content,'[[:digit:]]+')
}

table(unlist(lapply(smsCorpus,onlydigit)))


#제거

sms.nodigits<-tm_map(smsCorpus,removeNumbers)

#확인

table(unlist(lapply(sms.nodigits,onlydigit)))



# 2. 대소문자 통일
sms.lower<-tm_map(sms.nodigits,content_transformer(tolower))


# 3. 불용어 제거

stopwords()
sms.clean<-tm_map(sms.nodigits,removeWords,stopwords())


# 4. 특수문자 제거

sms.nopunc<-tm_map(sms.clean,removePunctuation)

#확인
rm.punct<-function(x){
  str_extract_all(x$content,'[[:punct:]]+')
}
table(unlist(lapply(sms.nopunc,rm.punct)))

# ¡     ‘     ’     “     ” \u2030
# 2      2     38     11      6      1


rm<-'¡|‘|’|“|”|\u2030|'

sms.nopunct<-tm_map(sms.nopunc,content_transformer(str_remove_all),rm)



# 5. 단어 길이가 2미만을 제거

sms.word<-tm_map(sms.nopunct,removeWords,'[[:alpha:]]{1}')


# 6. 전체 단어중에서 가장 많이 등장한 단어?
#   내림차순 정렬 10개 추출


res<-tm_map(sms.word, str_extract_all, boundary('word'))
sort(table(unlist(res)),decreasing=T)[1:10]

# words
# call  now  get will  can   Im   ur  You   go know 
# 394  389  336  335  319  314  296  267  255  253 



# ***wordnet 이용하여 동의어/반의어/상위/하위어
# ex) daddy, father,... => father
