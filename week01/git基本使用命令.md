



# Git 基本使用

- 查看git版本
- 配置全局用户名
- 配置全局邮箱（真实邮箱）
- 查看当前git配置
- 初始化一个本地仓库
- remote远程仓库（先在github上创建一个仓库）
- 本地创建ssh秘钥对（并且在github中添加公钥）
- 查看当前工作区状态
- 添加（工作区 - > 暂存区）
- 删除（删除暂存区的文件）
- 提交（暂存区 - > 本地仓库）
- 推送（本地仓库 - > github远程仓库）
- 克隆github仓库
- 查看版本提交记录



####  查看git版本

```powershell
$ git --version
git version 2.23.0.windows.1
ppo223@MrXiong MINGW64 /d/python/learn_git
$
```

####  配置全局用户名

```#### 1.3 安装Harbor私有仓库
$ git config --global user.name 'xiongqiang'
ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$
```

####  配置全局邮箱（真实邮箱）

```
$ git config --global user.email 'xiongq1994@163.com'
ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$
```

####  查看当前git配置

```powershell
$ git config --global --list
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
user.name=xiongqiang
user.email=xiongq1994@163.com
winupdater.recentlyseenversion=2.23.0.windows.1
ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$
```

####  初始化一个本地仓库

```powershell
$ git init
Initialized empty Git repository in D:/python/learn_git/.git/

ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$ ls -a
./  ../  .git/

ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$
```

####  remote远程仓库（先在github上创建一个仓库）

```####  查看git版本
$ git remote add origin git@github.com:ppo2233/learn_git.git
ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$
```

####  本地创建ssh秘钥对（并且在github中添加公钥）

```powershell
$ ssh-keygen -t rsa -C "xiongq1994@163.com"
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/ppo223/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /c/Users/ppo223/.ssh/id_rsa.
Your public key has been saved in /c/Users/ppo223/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:BJdNrYyWAMwrXhPNNHDQ1gmDHsiXErnBXRJWCrCGSdY xiongq1994@163.com
The key's randomart image is:
+---[RSA 3072]----+
|.*+BB#Xo.=..     |
|+oBEX+*=+ . .    |
|+. *.= ..+ .     |
|. o =  .+ o      |
| . o . .S        |
|  .              |
|                 |
|                 |
|                 |
+----[SHA256]-----+
ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$ cd /c/Users/ppo223/.ssh && ls
id_rsa  id_rsa.pub  known_hosts
ppo223@MrXiong MINGW64 ~/.ssh
$ cat id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCek/gWmPbL9FdDhms+XiBT9nzfnjQjb4QbD8QUHc1hqVCP+ubDYDzd1Bml+K4TN5KA5tkUIENc+NG0i0mvqfbo1ZIzsm2uhQcntULoAm+zsVXRS/gFE+2pMxxM7L/WnJXv+1S6JQRSdGHVz5mixkurC1LF1OSLSUsaseSag4AWs+PN5HG6hzEi/ER+C9uywrZQ6fg7CYALsmnjmiNRwkEqH22+D6q2K7AmpXfNLatoj5DWage7EGdwzFSCwaW9GN5D4w0I4c1fpMCBpW5HqVwlbqs42lJ+wzYjY5pHVbIrEIuipUEZSY8PS7IghUyRNj9w0ilFoMwIx77pMdG8tj4aY+OdJKjVzFQIkCEECZGLfXf9cYOajBPwS/AbaRzab7pmWq6r5lVGGfUM46+jbHtB7YUdARP4IRYSmp8b8Iu+KdD4giiuEYEXChB/gK88mEBM5CTwDIh6u8D96OasWeRbSRTbTLdLpzSVCU9yp5K/9AAVqjIv2wWX+B7H32qFr/0= xiongq1994@163.com
ppo223@MrXiong MINGW64 ~/.ssh
$
```

####  查看当前工作区状态

```powershell
$ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)

ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$ echo '123' > test.txt

ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$ ls
test.txt

ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        test.txt

nothing added to commit but untracked files present (use "git add" to track)

ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$
```

####  添加（工作区 - > 暂存区）

```powershell
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        test.txt

nothing added to commit but untracked files present (use "git add" to track)

ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$ git add .
warning: LF will be replaced by CRLF in test.txt.
The file will have its original line endings in your working directory

ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   test.txt


ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$
```

#### 删除（删除暂存区的文件）

```
# 查看当前状态
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   test.txt

# 查看本地文件
ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$ ls
test.txt

# 删除缓存区的test.txt文件
ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$ git rm --cache test.txt
rm 'test.txt'

# 删除缓存区的test.txt文件后再次查看状态(缓存区没有了，提示add添加文件)
ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        test.txt

nothing added to commit but untracked files present (use "git add" to track)

# 查看本地文件还在（删除缓存区的文件不会影响本地文件）
ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$ ls
test.txt

ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$
```

#### 提交（暂存区 - > 本地仓库）

```powershell
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   test.txt


ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$ git commit -m 'add a test file'
[master (root-commit) 3332e09] add a test file
 1 file changed, 1 insertion(+)
 create mode 100644 test.txt

ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$ git status
On branch master
nothing to commit, working tree clean

ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$
```

####  推送（本地仓库 - > github远程仓库）

```powershell
ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$ git status
On branch master
nothing to commit, working tree clean

ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$ ls
test.txt

ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$ git push -u origin master
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 215 bytes | 71.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To github.com:ppo2233/learn_git.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.

ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$
```

####  克隆github仓库

```powershell
ppo223@MrXiong MINGW64 /d/python
$ ls

ppo223@MrXiong MINGW64 /d/python
$ git clone git@github.com:ppo2233/Python005-01.git
Cloning into 'Python005-01'...
remote: Enumerating objects: 24, done.
remote: Counting objects: 100% (24/24), done.
remote: Compressing objects: 100% (14/14), done.
remote: Total 24 (delta 5), reused 16 (delta 3), pack-reused 0
Receiving objects: 100% (24/24), 4.67 KiB | 796.00 KiB/s, done.
Resolving deltas: 100% (5/5), done.

ppo223@MrXiong MINGW64 /d/python
$ ls
Python005-01/

ppo223@MrXiong MINGW64 /d/python
$ cd Python005-01/

ppo223@MrXiong MINGW64 /d/python/Python005-01 (main)
$ ls
README.md  week02/  week04/  week06/  week08/  week10/  week12/
week01/    week03/  week05/  week07/  week09/  week11/

ppo223@MrXiong MINGW64 /d/python/Python005-01 (main)
$
```

#### 查看版本提交记录

```powershell
$ git log
commit 3332e0962ae0b4ad30075a82f97c30df44bc2499 (HEAD -> master, origin/master)
Author: xiongqiang <xiongq1994@163.com>
Date:   Tue Nov 24 16:52:25 2020 +0800

    add a test file

ppo223@MrXiong MINGW64 /d/python/learn_git (master)
$
```

