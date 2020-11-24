# Rancher2.4.8 高可用部署

@author: liuqingfeng@cewell.com.cn  

@date:2020年10月16日

本节介绍如何使用 RKE 创建和管理集群，然后将 Rancher 安装到该集群上。对于这种类型的架构，您将需要在基础设施提供商中创建节点（通常为虚拟机）。您还需要配置负载均衡器，将前端流量定向到这些节点中。当节点运行起来并满足[节点要求])时，可以使用 RKE  将 Kubernetes 部署到这些节点上，然后使用 Helm 软件包管理器将 Rancher 部署到 Kubernetes 上。

##  RKE 高可用集群推荐架构

- Rancher 的 DNS 应该解析为 4 层负载均衡器
- 负载均衡器应将端口 TCP/80 和 TCP/443 流量转发到 Kubernetes 集群中的所有 3 个节点。
- Ingress 控制器会将 HTTP 重定向到 HTTPS，并在端口 TCP/443 上终止 SSL/TLS。



在 RKE 集群中安装 Rancher 高可用，我们建议为高可用安装配置以下基础设施：

- **3 个 Linux 节点**，通常是虚拟机，**您可以自行选择的基础设施提供商，**例如 Amazon EC2、阿里云、腾讯云或者 vShpere。
- **1 个负载均衡器**，用于将流量转发到这三个节点。

您可以将这些服务器放在不同的可用区里，但这些节点必须位于相同的区域/数据中心。

服务器部署规划

![image-20201124144133293](C:\Users\ppo223\AppData\Roaming\Typora\typora-user-images\image-20201124144133293.png)





##  安装概要

- [1、准备节点和私有镜像仓库](https://docs.rancher.cn/docs/rancher2/installation/other-installation-methods/air-gap/prepare-nodes/_index)
- [2、部署 Kubernetes 集群（Docker 单节点安装请跳过此步骤）](https://docs.rancher.cn/docs/rancher2/installation/other-installation-methods/air-gap/launch-kubernetes/_index)
- [3、安装 Rancher](https://docs.rancher.cn/docs/rancher2/installation/other-installation-methods/air-gap/install-rancher/_index)

建议在 Chrome 或 Firefox 中使用 Rancher UI。

##### 1.1.1  操作系统和容器运行时要求

Rancher 应用可以兼容当前任何流行的 Linux 发行版。

Rancher 官方支持并且已在如下操作系统中测试了 Rancher 和 RKE，它们包括 Ubuntu，CentOS，Oracle Linux，RancherOS 和 RedHat Enterprise Linux

以下操作系统及其这些版本后续的非主要版本中进行了测试：

- Ubuntu 16.04 (amd64)
- Ubuntu 18.04 (amd64)
- Raspbian Buster (armhf)



##### 1.1.2 硬件要求

本节描述安装 Rancher Server 的节点的 CPU、内存和磁盘要求。

- CPU 和 内存

#### 1.3 安装Harbor私有仓库

```powershell
#安装docker-compose
cp docker-compose /usr/bin/
chmod +x /usr/bin/docker-compose 

# 解压安装包
tar -xzvf harbor-offline-installer-v1.9.2.tgz -C /opt
cd /opt/harbor

#修改配置，修改hostname和port
vi harbor.yml
hostname: 10.0.4.123
port: 85

# 镜像数据解压至指定目录
tar -czvf data.tgz -C /
#安装Harbor
./prepare
./install.sh

#启动Harbor
docker-compose up -d 启动
docker-compose stop 停止
docker-compose restart 重新启动

#web访问Harbor
http://10.0.4.123:85
默认账户密码：admin/Harbor12345

#命令行登录Harbor
docker login -u liuqf -p Cewell12345 10.0.4.123:85
```

