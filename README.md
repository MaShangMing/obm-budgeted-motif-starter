# 设备诊断模式放置起始程序

此程序使用Python标准库，读取设备、诊断角色、候选位置、链路与区域容量。起始solver枚举候选组合，仅检查模板存在边并返回首个匹配，还未实现诱导关系、共享容量和全映射结果归约。

| 文件 | 用途 |
| --- | --- |
| app/solver.py | 小规模首解探测，是精确匹配和搜索优化的修改入口。 |
| app/cli.py | 文件CLI，读取JSON输入并将solve返回值写入输出文件。 |
| app/workload.py | 两类公开合成输入生成器，不包含期望结果或求解逻辑。 |
| data/devices.json | 合成设备示例，含内部干扰链路和外部邻居。 |
| Dockerfile | 固定摘要的Python3.12 Linux标准库环境，不安装第三方包。 |
| README.md | 文件用途、启动方式和公开输入说明。 |

在本目录运行python app/cli.py data/devices.json /tmp/result.json。输入与输出路径应不同。也可将app加入PYTHONPATH，再from solver import solve并传入解析后的JSON字典。默认没有持久缓存和文件外状态。

cycle_case(width, depth, seed)生成分层定向环，每层width台设备、depth个角色，边具有层次标签；候选域按同类设备逆序排列，成本由seed确定，容量按角色数配置。capacity_case使用同样的设备与候选域，去掉边，将唯一共享区域容量减一。公开负载使用width为24、32、40，depth为8，seed为0、1、2、3。这些函数只生成输入。data/devices.json与workload.py保持不改，solver、cli与新增标准库辅助模块可用于实现所需行为。
