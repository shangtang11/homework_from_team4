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
- reports/：数据质量报告、查新报告
- paper/：课程综述、论文稿件
- docs/：字段说明、规范文档
## 检索表达式：
 TS=("RISC-V" OR "RISC V" OR "RISC_V" OR "RV32" OR "RV64") AND TS=("CPU" OR "central processing unit" OR "processor" OR "microprocessor" OR "core") AND TS=("design" OR "architecture" OR "implementation" OR "microarchitecture") NOT TS=("GPU" OR "graphics processing unit" OR "DSP" OR "digital signal processor" OR "FPGA" OR "ASIC" OR "accelerator")
