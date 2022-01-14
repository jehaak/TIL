# GITHUB

##  회원가입

### 설정변경

* main 브랜치를 master 브랜치로 기본값 수정

## 원격 저장소와 로컬 저장소 연결

### Repository 생성

* git remote: $ git remote add origin https://github.com/jehaak/TIL.git
* git push: $ push -u origin master



### git 이메일, 이름 바꾸기

* 글로벌이 아닌 git config user.name ~~로 하면 됨
* 다른 메일로 할 때: 자격증명 관리자에 들어가서 window 자격 증명 - github 로그인 정보를 수정 또는 제거 한 후 다른 계정으로 로그인 하면 됨



## git에 올리고 싶지 않은 파일 처리

### .gitignore 

* 원격 저장소에도 파일이 있고, 로컬에도 이미 있고, 트래킹 중인 파일을 로컬에서만 더이상 추적하지 않도록 설정

```bash
$ git update-index --assume-unchanged
{file name}
```

* 로컬에 있는 변동 추적 멈춤
* 원격 저장소에 해당 파일이 이미 있다면 그 파일 삭제(원격 저장소에 push할때 해당 파일 삭제)

```bash
$ git rm --cashed {file name}
#변동추적만 중지, 파일삭제는x
```

* 로컬, 원격 저장소 모두 파일 삭제후 추적중지

```bash
$ git rm{file name}
```



## git 받아오기

* 주소 복사 후

```bash
$ git clone ~~~(붙여넣기)
```

* git pull: a컴퓨터에서 작업 후 git 에 업로드, b컴퓨터에서 a에서 작업한 최신 버전을 얻고 싶을 때

* *주의사항*  같은 작업 파일을 두곳에서 서로 다른 작업물을 푸쉬하려하면 만됨! 무조건 최신 버전 풀을 받은 다음 작업하고 푸쉬해야됨

메모장(VIM) 탈출방법:    ':wp' 치고 엔터

```bash
$ git pull origin master
$ git push origin master
```







### pull 안받고  수정 할 경우:

서로 다른 폴더에서 될 경우 같은 줄에 다른 정보가 입력되어 있으면 임의 형식으로 합치고 수정해라고 뜸. 수정하고 뜸. 안겹치면 합쳐도 되냐고 물어보고 합쳐서 만듦.

### 레퍼지토리

* 저장할 수 있는 저장공간.



origin: 원격 저장소 주소의 별명(딴 별명으로 가능), 뒤에 주소: 위치

```
git remote add origin https://github.com/jehaak/word.git
```

여러위치 저장 가능

git remote remove origin으로 제거 가능

$ git push -u origin master : 최초 푸쉬할 때 사용, 이후 origin master 안붙여도 git push만으로 push 가능하게 함

## branch

나뭇가지라는 의미로 여러 작업들을 하면서 분화되는 버전같은 느낌

---



### git init

* 새로운 저장소 .git폴더가 생성되며, 프로젝트 파일들을 관리할 수 있다.
* git의 레포지토리는 크게 

​		작업폴더(working place) > 인덱스(Staging Area) > 저장소(Head - Repository) 로 구성되어 있슴.

​		우리가 작업하는 폴더를 작업트리라 부른다.

### git add

* 작업트리와 저장소 사이에 있는 가상의 준비영역 인덱스에 내용을 기록한다.
* add에 추가된 파일을 제거하려면 git rm --cashed를 사용.

### git commit

* 스테이지에 있는 내용들을 저장소에 기록한다.
* add 후 커밋 해야하며 git commit -a 명령어로 add 생략후 커밋 할 수 있다.
