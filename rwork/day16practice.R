# 패키지와 파일 불러오기 ####
library(tm)
library(stringr)
library(dplyr)

smsraw <- read.csv('sms_spam_ansi.txt')
smsCorpus <- VCorpus(VectorSource(smsraw$text))
# 수치 데이터, 불용어, 특수문자 제거 / 대소문자 통일 / 단어 길이 2미만 제거 ####
tm_map(smsCorpusClean, str_replace_all, '[^\\w\\t\\d\\s]*')

smsCorpusClean<- smsCorpus %>% 
  tm_map(removeNumbers) %>% 
  tm_map(removeWords, stopwords()) %>% 
  tm_map(str_replace_all, '[^[:alpha:]\\t\\d\\s]{1,}', ' ') %>% 
  tm_map(tolower) %>% 
  tm_map(removeWords, '[[:alpha:]{,2}]')
smsCorpusClean
# comments
# punct는 통화 기호 같은 특수문자들 없어지지 않아서 '[^[:alpha:]\\t\\d\\s]{1,}' <- 이 표현식 작성 
# 2번째 데이터 K..give 같은 경우에서 remove하면 Kgive로 되는 것 방지 위해 replace_all 사용
#전체 단어중에서 가장 많이 등장한 단어? ####
#내림차순 정렬 10개 추출

smsCorpusWords <- tm_map(smsCorpusClean, str_extract_all, boundary('word'))
smsCorpusWords <- as.vector(unlist(smsCorpusWords))
sort(table(smsCorpusWords), decreasing = T)[1:10]
# call now  can  get   ur will just  you   ok   go 
# 595  502  418  393  390  387  375  344  293  289




#wordnet을 이용하여 동의어/반의어/상위/하위어 
#ex) daddy, father,....=>father
