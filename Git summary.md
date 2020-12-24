## git 이란?



## git 설치



1. Git-scm.com 에서 다운로드
2. 계속 next 로 설치



## git 사용법

### 최초설정

처음 컴퓨터에 git을 설치하면, 사용자의 이메일과 이름을 적어준다. 이는 앞으로 일어나는 커밋에 서명을 하기 위해서 필요하다. 



```
git config --global user.name "<당신의 이름>"
git config --gloabl user.email "<당신의>@<이메일>"
```



잘 설정되었나 확인하려면 

```
git config user.name 이름출력
git config user.email 이메일 출력
```









### 상태 점검



### 초기화

초기화는 'git init'을 통해 진행한다. 

```
git init
```



### add하기



### commit 하기



### log 보기





### 원격 저장소 등록하기

git remote add origin <URL> #등록하기 

git remote -v 

### summary 

| 명령어         | 설명                                                         |
| -------------- | ------------------------------------------------------------ |
| Git init       | 빈 디렉토리(폴더)를 git 저장소(repo)로 초기화한다.(처음 파일들을 인식하도록) |
| Git status     | 파일이 어떤 상태에 있는지 확인한다.                          |
| Ls -a          | 로컬파일과 깃에 있는 파일을 삭제한다.                        |
| Gid add 파일명 | 파일을 깃이 추적가능한 상태로 만든다.(사진찍기)              |
| Git commit     |                                                              |
| :q!            | 저장하지 않고 강제 종료한다.                                 |
| :wq            | 저장하고 나간다.                                             |
|                |                                                              |
|                |                                                              |







