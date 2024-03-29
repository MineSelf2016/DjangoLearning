# Remote Deploy Tutorial
从0开始搭建云端python、nodejs 开发环境，实现前后端分离、ML与DL 模型的部署。

## VSCode Remote 使用教程
1. 环境准备
    申请Linux x64 远程服务器；
    vs code中安装Remote development 插件；
2. SSH-Key配置
通过ssh 登录服务器，存在两种方案：
    2.1 账号和密码登录，但导致每次登录都需要验证密码；
    2.2 使用ssh-key 的方式登录则是更好的选择，
SSH-key 基本原理为：在local host上创建（生成）两个Key文件，一个是私钥（id_rsa），一个是公钥（id_rsa.pub），私钥放在本地，公钥放在远程服务器。<br>
当用户通过ssh-key登录到远程服务器时，远程服务器使用公钥创建了一个加密的随机消息，然后发送到本地机器，本地机器使用私钥解密消息，发送解密的消息到远程服务器。远程服务器验证这个解密后的消息，然后授权访问。实际过程比这个复杂，这里理解大概就可以了。<br>
    ssh-key 生成过程：<br>
    在local host 的~/.ssh 文件中使用命令
```bash
ssh-keygen -t rsa -b 4096
```
    生成id_rsa 私钥文件与id_rsa.pub 公钥文件。
3. 分发公钥至remote host
    3.1 将id_rsa.pub 文件内容拷贝至remote host 的~/.ssh/authorized_keys 文件（没有则创建）中；
    3.2 修改权限，使得当前用户具备验证权限
```bash
chown -R feiffy:feiffy ~/.ssh
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```
4. 配置本地ssh config 文件
local host进入~/.ssh/config 文件，配置remote host 信息：
```bash
# Read more about SSH config files: https://linux.die.net/man/5/ssh_config
Host AliECS
    HostName 120.78.130.250
    User root
    IdentityFile /Users/mineself2016/.ssh/id_rsa
```
5. vscode remote 连接
vscode 中F1 键进入command pattle 选择remote connect 与配置完成的remote host。

配置完成

## zsh 配置
1. 查看当前shell 环境
```bash
$ cat /etc/shells
$ echo $SHELL
```
Linux 的默认shell 是/bin/bash

2. 安装zsh 并升级为oh my zsh
```bash
$ yum install zsh
$ sudo yum install wget
$ sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

3. 更换默认shell 为zsh
```bash
$ chsh -s /bin/zsh
```
或使用$ chsh 依照步骤完成更改。

4. 重启shell，当前用户shell 环境完成了更改。

## 远程服务器配置python3、pip3与Django
1. 至python 官网选择python3 版本，此处选择python3.7 的tar 压缩包；

2. 上传至服务器解压，将解压文件移动至/usr/local；

3. 编译前需安装python3.7 额外依赖（坑）：
```bash
yum -y groupinstall "Development tools"
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
yum -y install libffi-devel
```

4. 进入/usr/local/Python3.7.4 目录，输入以下命令cmake 编译源文件
```bash
./configure --prefix=/usr/local/python3 --enable-optimizations --enable-loadable-sqlite-extensions

make

make install
```
等待编译完成。。。。。。

5. 软链接至系统命令
```bash
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
```
测试python3 是否安装成功：
```bash
python --version
```

6. 使用get-pip.py安装pip3
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```
软链接至系统命令
```bash
ln -s /usr/local/python3/bin/pip3.7 /usr/bin/pip3
```
测试pip3 是否安装成功
```bash
pip3 --version
```

7. 安装Django
```bash
pip3 install Django==2.0
```

8. 将django-admin 命令添加至环境变量
```bash
vi /etc/profile

export PATH=$PATH:/usr/local/python3.7/bin
```
测试Django 是否安装成功
```bash
django-admin
```

## 远程服务器配置nodeJS 环境

### 配置npm -g 全局安装路径：
1、查看全局安装路径
```bash
npm config get prefix
```
一般显示为系统目录：/usr/local

2、修改默认全局安装路径
```bash
//1. 新建一个全局安装的路径
mkdir ~/.npm_global 
//2. 配置npm使用新的路径
npm config set prefix '~/.npm_global'
//3. 编辑 /etc/profile，加入
export PATH=~/.npm-global/bin:$PATH
//4、更新系统环境变量
source /etc/profile
```


<hr>
