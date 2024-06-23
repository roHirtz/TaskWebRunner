ssh-keygen -t rsa       获取ssh令牌在github绑定
ssh -T git@github.com   测试绑定
git clone -b <分支名> --single-branch <ssh远程库名>

git config --global user.name "roHirtz"
git config --global user.email "490489027@qq.com"

git init
git remote add origin https://github.com/roHirtz/TaskWebRunner.git
gid add .
git commit -m "版本号"
git push

git pull

检测版本号