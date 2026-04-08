# homework_from_team4
hnu第四小组的文献计量学作业🤔
# HNU 第四小组 - RISC-V 文献计量学项目

## 团队成员
- 寻锦洲：检索式构建、数据采集
- 金本卓：数据清洗、质量检查
- 胡锦棠：知识图谱构建、可视化
- 卢宏骏：综述撰写、报告整理

## 研究方向
基于文献计量的RISC-V架构处理器设计研究前沿探索

## 项目里程碑
1. M1（第4周）：完成检索式构建 → 数据导出 → 数据清洗
2. M2（第10周）：完成知识图谱、合作网络、共现网络分析
3. M3（第15周）：完成综述论文 + 可复现项目报告

## 仓库结构
- data/：原始数据 + 清洗后数据
- config/：检索式、配置文件
- src/：代码（数据处理、可视化、网络分析）
- outputs/：图表、结果、指标文件
- reports/：数据质量报告、查新报告0
- paper/：课程综述、论文稿件
- docs/：字段说明、规范文档
## 检索表达式：
 ALL=("RISC-V" OR "RISC V" OR "RISC_V" OR RV32 OR RV32I OR RV32M OR RV32A OR RV32F OR RV32D OR RV64 OR RV64I OR RV64M OR RV64A OR RV64F OR RV64D OR "RISC-V core" OR "open source RISC-V" OR "embedded RISC-V")
AND
ALL=(CPU OR processor OR microprocessor OR core OR "processor core" OR "CPU core" OR design OR architecture OR implementation OR microarchitecture OR pipeline OR "branch prediction" OR cache OR ISA OR "instruction set architecture" OR datapath OR "control unit")
NOT TS=(GPU OR "graphics processing unit" OR DSP OR "digital signal processor")

## 数据检索说明
1. 数据来源
本数据集来源于 Web of Science 核心合集（Web of Science Core Collection），为课程文献计量分析指定标准数据源，该数据库引文数据完整度、规范性最高，可支撑共被引分析、文献耦合分析、影响力指标计算等全流程分析需求。
2. 检索式版本（最终锁定版，与 config/query.yaml 完全一致）
plaintext
ALL=("RISC-V" OR "RISC V" OR "RISC_V" OR RV32 OR RV32I OR RV32M OR RV32A OR RV32F OR RV32D OR RV64 OR RV64I OR RV64M OR RV64A OR RV64F OR RV64D OR "RISC-V core" OR "open source RISC-V" OR "embedded RISC-V")
AND
ALL=(CPU OR processor OR microprocessor OR core OR "processor core" OR "CPU core" OR design OR architecture OR implementation OR microarchitecture OR pipeline OR "branch prediction" OR cache OR ISA OR "instruction set architecture" OR datapath OR "control unit")
NOT
TS=(GPU OR "graphics processing unit" OR DSP OR "digital signal processor")
  检索字段说明：ALL= 全字段检索，TS= 主题字段（标题 + 摘要 + 关键词）
  逻辑规则：严格遵循布尔检索优先级，同义词组括号包裹，无逻辑歧义
3. 导出时间戳
分批次导出时间：2026 年 04 月 08 日
检索执行时间：2026 年 04 月 08 日
检索式版本锁定时间：2026 年 04 月 08 日
4. 总批次与总条数
总导出批次：11 个批次
原始文献总条数：10851条
去重后有效文献条数：【请填写基于 DOI 去重后的最终有效条数】 条
去重规则：以 DOI 为唯一标识符，保留首次出现的文献条目，符合课程数据去重标准规范
5. 导出字段清单
（一）作者、标题、来源模块
✅ 作者✅ 标题✅ 资料来源（期刊 / 会议名称）✅ Conf.Info/Sponsors（会议信息 / 赞助方）✅ 被引用次数✅ 作者标识✅ 国际标准连续出版物号（ISSN）
（二）摘要、关键词、地址模块
✅ 摘要✅ 地址（作者单位地址）✅ 隶属关系（作者所属机构全称）✅ 文档类型✅ 关键词（作者关键词）✅ WoS 分类✅ 研究领域✅ 语言
（三）引用参考文献与使用模块
✅ 引用参考文献（Cited References，共被引 / 耦合分析核心必填字段）✅ 热报（Citation Burst，突现检测字段）✅ 高被引（Highly Cited，高影响力文献标识）
