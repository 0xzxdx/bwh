# BWH

搬瓦工面板 API SDK

## 安装

使用pip安装

```
$ pip install turbotools
```

或者从源码包安装

```
$ git clone https://github.com/anshengme/turbotools
$ cd turbotools
$ python setup.py install
```

## 示例

- 创建实例

```
>>> from bwh import BwhSdk
>>> bwh = BwhSdk(veid=598375,api_key='private_YJuvhyLXL5RwLJ2q9pVxlqi9')
```

- 获取服务器信息

```
>>> bwh.get_service_info()
```

- 获取可以安装的OS列表

```
>>> bwh.get_available_os()
{'error': 0, 'installed': 'centos-6-x86-bbr', 'templates': ['centos-6-x86', 'centos-6-x86-bbr', 'centos-6-x86_64', 'centos-6-x86_64-bbr', 'centos-7-x86_64', 'centos-7-x86_64-bbr', 'debian-7-x86', 'debian-7-x86_64', 'debian-8-x86', 'debian-8-x86_64', 'debian-9-x86', 'debian-9-x86_64', 'ubuntu-12.04-x86', 'ubuntu-12.04-x86_64', 'ubuntu-14.04-x86', 'ubuntu-14.04-x86_64', 'ubuntu-16.04-x86', 'ubuntu-16.04-x86_64', 'ubuntu-18.04-x86_64']}
```