# branch

## git branch 명령어

* 브랜치 `생성`, `삭제`, `조회` 명령어

```bash
# 브랜치 조회
$ git branch

# 원격 저장소의 브랜치 목록 확인
$ git branch -r

# 브랜치 삭제
# 병합된 (수정내역을 합치고 난 후에 삭제 가능)
$ git branch -d {branch name}
#(주의) 병합되지 않은 브랜치 강제 삭제

$git branch -D {branch name}
```



## git switch

* 현재 브랜치에서 다른 브랜치로 HEAD를 이동시키는 명령어
* HEAD는 현재 브랜치를 가리키는 포인터

```bash
# 다른 브랜치로 이동
$ git switch {다른 브랜치를 가리키는 포인터}

# 브랜치를 생성하고 동시에 이동
$ git switch -c{다른 브랜치 이름}
```



* 주의사항

​	git switch 하기 전에 commit 해야됨!!



a생성, 작업 후 master로 돌아가면 a에서 작업한 내용이 없어진다.



## merge

```bash
# dev로 작업 끝난 후 병합
$ git merge dev
이후엔 dev 지워도 됨
```

