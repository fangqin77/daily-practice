# git的基本操作

```
PS D:\myCode\dailyPractice> git
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     克隆已有远程仓库
   init      初始化一个空仓库

work on the current change (see also: git help everyday)
   add       添加文件到缓存区
   mv        移动或者重命名一个文件或者文件夹或文件链接
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       查看提交记录
   show      Show various types of objects
   status    查看当前git的工作树状态

grow, mark and tweak your common history
   branch    查看分支列表、创建新分支、删分支
   commit    提交记录到仓库
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      从远程仓库拉取提交
   push      推送变化到远程仓库
```

## git的基本概念

![](https://www.runoob.com/wp-content/uploads/2015/02/1352126739_7909.jpg)

## .gitgnore

用来记录忽略提交的文件

## git add [options]

表示将目标内容添加到缓存区 如

- `git add . ` 表示添加当前目录下的所有文件
- `git add CSS笔记.md`  表示添加某个文件到缓存区

## git commit -m "描述"

用来提交内容的。-m 表示 message


## 拉取和推送

git pull 拉取远程更改

git push 推送本地提交
