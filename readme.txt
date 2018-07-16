
前面讲了我们把文件往Git版本库
第一步是用git add把文件添加进去，实际上就是把文件修改添加到暂存区；

第二步是用git commit提交更改，实际上就是把暂存区的所有内容提交到当前分支。

此后，每次本地提交后，只要有必要，就可以使用命令git push origin master推送最新修改 

现在，远程库已经准备好了，下一步是用命令git clone克隆一个本地库
$ git clone git@github.com:heronghua008/gitskills.git
注意把Git库的地址换成你自己的，然后进入gitskills目录看看，已经有README.md文件了。





