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
- src/：代码（数据处理）
- outputs/：图表、结果、指标文件
- reports/：答辩ppt
- paper/：课程综述、论文稿件
- docs/：AI使用说明
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
去重后有效文献条数：7682 条
去重规则：以 DOI 为唯一标识符，保留首次出现的文献条目，符合课程数据去重标准规范
5. 导出字段清单
（一）作者、标题、来源模块
✅ 作者✅ 标题✅ 资料来源（期刊 / 会议名称）✅ Conf.Info/Sponsors（会议信息 / 赞助方）✅ 被引用次数✅ 作者标识✅ 国际标准连续出版物号（ISSN）
（二）摘要、关键词、地址模块
✅ 摘要✅ 地址（作者单位地址）✅ 隶属关系（作者所属机构全称）✅ 文档类型✅ 关键词（作者关键词）✅ WoS 分类✅ 研究领域✅ 语言
（三）引用参考文献与使用模块
✅ 引用参考文献（Cited References，共被引 / 耦合分析核心必填字段）✅ 热报（Citation Burst，突现检测字段）✅ 高被引（Highly Cited，高影响力文献标识）

## 技术栈 
1. 文献计量学工具：CiteSpace 6.1.R6、VOSviewer 
2. 编程语言：Python 3.10+ 
3. AI辅助：详见 `docs/AI_usage_disclosure_RISC-V_bibliometrics `

## 核心产出
### 一、 VOSviewer共被引网络图解释
RQ1：该领域的知识基础由哪些核心文献和研究方向构成？
<img width="771" height="532" alt="image" src="https://github.com/user-attachments/assets/a7802900-1a81-4bb9-ae8e-50146c504fb2" />

研究问题
本图为VOSviewer生成的RISC-V处理器领域文献共被引网络，旨在回答RISC-V处理器架构领域的知识基础是什么这一核心问题。通过文献间的共被引关联，识别该领域的核心奠基文献、关键知识集群以及不同研究方向的内在联系，明确支撑整个领域发展的学术根基。
 
主要发现 
网络中节点代表被引文献，大小反映被引频次，颜色区分不同知识聚类，连线代表文献间的共被引关系。本领域知识基础主要由四大核心板块构成： 
1. 黄色聚类：以Hills G 2019年《Nature》论文为绝对核心，该节点尺寸最大、被引频次最高，奠定了RISC-V与碳基半导体、存算一体等新型计算架构融合的研究基础。
2. 红色聚类：以He KM 2016、Hamilton WL 2017等论文为核心，构成了RISC-V处理器微架构优化、指令集扩展与硬件加速技术的知识体系。
3. 绿色聚类：以Costan V 2016年USENIX Security论文为核心，提供了RISC-V可信执行环境、安全扩展与侧信道防御的核心理论支撑。
4. 蓝色聚类：以Carlini N 2015、Bisheh-Niasar M 2021等论文为核心，对应RISC-V处理器的形式化验证、漏洞检测与可靠性设计方向。
四大板块相互关联，共同支撑了RISC-V处理器领域后续的技术演进与应用拓展。
 
局限性
本图仅展示了被引频次排名靠前的核心文献，大量低被引的细分领域研究成果未被呈现；节点标签仅显示作者、年份与部分来源信息，完整文献内容需结合原始数据核对；共被引关系无法区分引用性质，可能高估部分争议性文献的学术价值。

### 二、CiteSpace共被引时间线图解释
　　RQ2：该领域的研究主题如何随时间演化，经历了哪些关键发展阶段？
<img width="771" height="489" alt="image" src="https://github.com/user-attachments/assets/010bdff8-0adf-44d7-b41f-3492bc09a4e9" />

研究问题 
本图为CiteSpace生成的RISC-V处理器领域共被引时间线图，旨在回答RISC-V处理器架构领域的研究趋势如何演化这一问题。通过将共被引网络按时间维度展开，清晰呈现不同研究主题的出现时间、发展周期与演变脉络，识别领域发展的关键转折点与未来走向。
 
主要发现 
图中横轴为时间轴（2016-2026年），节点代表被引文献，大小反映被引频次，不同横向条带对应不同研究聚类，标签为CiteSpace自动生成的主题关键词。该领域的研究演化可分为三个清晰阶段：
1. 基础构建期（2013-2015年）：对应#0 using verification和#6 data-oriented attack聚类，研究聚焦于RISC-V指令集的形式化验证、基础安全漏洞分析，为后续架构发展奠定了可靠性与安全性基础。
2. 技术爆发期（2016-2019年）：对应#2 carbon nanotube和#3 carbon nanotube聚类，研究热点转向RISC-V与新型半导体材料的结合，Hills G 2019年的碳纳米管RISC-V处理器论文成为这一阶段的标志性成果，推动了领域向异构计算方向发展。
3. 应用拓展期（2020年至今）：对应#4 multispectral riemannian classification聚类，研究开始向嵌入式、边缘计算等具体应用场景延伸，探索RISC-V在多模态处理、低功耗设备中的实现方案。
 
局限性
聚类标签为软件自动生成，部分标签语义与RISC-V主题的关联性需结合文献内容进一步人工修正；2020年之后的文献数量较少，无法完整反映近三年的最新研究动态；时间线图仅能体现主题的时间分布，难以直观展示不同主题间的交叉融合关系。

### 三、 VOSviewer作者合作网络图解释
RQ3：谁是该领域的核心学者，全球合作格局呈现何种特征？
<img width="771" height="532" alt="image" src="https://github.com/user-attachments/assets/4ec75e65-d59f-49ac-91ad-be22522a8d41" />

研究问题
本图为VOSviewer生成的RISC-V处理器领域作者合作网络，旨在回答谁在推动RISC-V处理器架构领域的发展这一问题。通过分析作者间的合作关系，识别该领域的核心学者、主要研究团队以及全球合作格局，明确不同团队的研究特色与影响力。
 
主要发现
网络中节点代表作者，大小反映发文量，颜色区分不同合作团队，连线代表作者间的合作关系。该领域形成了四大核心研究阵营，呈现出"多中心、强区域合作"的特点：
1. 欧洲核心阵营：以Benini Luca为核心（节点尺寸最大，发文量最高），联合Magno Michele、Atienza David等学者，主导了嵌入式RISC-V与低功耗设计方向的研究。
2. 美国起源阵营：以Asanovic Krste（RISC-V联合创始人）为核心，包括Wentzlaff David、Malik Sharad等学者，奠定了RISC-V基础架构与开源生态的发展方向。
3. 中国研究阵营：以Wei Shaojun、Shi Longxing、Li Xiaowei、Yang Huazhong等学者为核心，在高性能RISC-V处理器设计、安全扩展与产业化应用方面成果显著。
4. 安全研究阵营：以Karri Ramesh、Sinanoglu Ozgur为核心，专注于RISC-V硬件安全、侧信道攻击与防御技术的研究。
各阵营内部合作紧密，但跨阵营的国际合作相对较少。
 
局限性
本图仅展示了发文量较高的核心作者，大量参与合作的次要作者未被呈现；未区分第一作者与通讯作者，无法准确衡量每位作者的具体贡献；仅反映了基于论文发表的正式合作关系，无法体现项目合作、学术会议交流等非正式学术互动。

### 四、Top10里程碑候选论文列表
RQ4： 该领域的知识基础由哪些核心文献和研究方向构成？
| 排名 | 作者            | 年份   | 被引频次 | 中心性  | 突现强度  | Sigma 值 | 半衰期 (年) | 来源出版物             | DOI                       |
|----|---------------|------|------|------|-------|---------|---------|-------------------|---------------------------|
| 1  | Costan V      | 2016 | 104  | 0.07 | 32.03 | 9.18    | 3.5     | USENIX Security   | -                         |
| 2  | Jouppi NP     | 2017 | 50   | 0.12 | 17.12 | 7.42    | 4.5     | ISCA 2017         | 10.1145/3079856.3080246   |
| 3  | Costan Victor | 2016 | 56   | 0.10 | 16.89 | 4.73    | 3.5     | Cryptology ePrint | 10.1159/000088809         |
| 4  | Sebastian A   | 2020 | 37   | 0.10 | 15.62 | 4.28    | 3.5     | Nature Nanotech   | 10.1038/s41565-020-0655-z |
| 5  | Paszke A      | 2019 | 67   | 0.05 | 26.26 | 3.45    | 4.5     | NeurIPS           | -                         |
| 6  | Xu YZ         | 2015 | 29   | 0.09 | 13.42 | 3.26    | 3.5     | IEEE S&P 2015     | 10.1109/SP.2015.45        |
| 7  | Krizhevsky A  | 2017 | 33   | 0.09 | 13.07 | 3.03    | 3.5     | Commun ACM        | 10.1145/3065386           |
| 8  | Amid A        | 2020 | 66   | 0.06 | 18.17 | 2.75    | 3.5     | IEEE Micro        | 10.1109/MM.2020.2996616   |
| 9  | Hu H          | 2016 | 19   | 0.06 | 9.35  | 1.79    | 2.5     | IEEE S&P 2016     | 10.1109/SP.2016.62        |
| 10 | Hills G       | 2019 | 364  | 0.04 | 19.06 | 2.05    | 2.5     | Nature            | 10.1038/s41586-019-1493-8 |


• 计量证据：Top10 文献中有 6 篇属于安全领域，平均中心性 = 0.08，高于其他领域的平均中心性（0.05）。
• 文献证据：Van Bulck J 2018 年的 "Foreshadow" 攻击论文（中心性 = 0.13）连接了微架构优化与安全两个聚类，是知识网络中最重要的桥梁文献。
• 边界提醒：被引频次和 Sigma 值仅反映文献的学术影响力，不能直接等同于学术质量；部分高被引文献可能因争议性而非创新性获得高引用。
（详细内容见小组课程论文）





