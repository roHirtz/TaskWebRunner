电脑绑定连接github令牌：

    ssh-keygen -t rsa       获取ssh令牌在github绑定
    ssh -T git@github.com   测试绑定
    git clone -b <分支名> --single-branch <ssh远程库名>

设置git环境变量：

    git config --global user.name "roHirtz"
    git config --global user.email "490489027@qq.com"

当前目录添加.git和关联：

    git init
    git remote add origin https://github.com/roHirtz/TaskWebRunner.git

提交流程：

    gid add .
    git commit -m "版本号"
    git push

git pull

检测版本号

sudo apt install python3-pytest
