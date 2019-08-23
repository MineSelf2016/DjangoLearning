# DjangoLearning
Django学习记录

<hr>
8月23日：
1、完成bootstrap studio 的下载与getting started；
2、复习bootstrap，使用studio 临摹苹果与特斯拉官网；
3、Azure 学生身份认证，挑选云服务器；
4、vscode <a href="https://code.visualstudio.com/docs/remote/remote-overview">remote</a>模块的使用，连接阿里云服务器，搭建nodeJS Demo；
5、完善zhizhe 前端页面。

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




<hr>
