---
name: init-notion-project
description: Create or repair a Notion project home and its document framework before planning; reserve Issues and Milestones positions for later to-pm setup.
disable-model-invocation: true
---

# Init Notion Project

为新项目建立简洁的团队入口，默认位于「项目总览」下。通常在需求澄清后、to-notion 前使用；已有项目复用原入口。只执行用户请求的初始化，不自动启动其他显式技能。

## 1. 定位项目

读取项目名称、稳定标识、已有 README 与用户指定位置；搜索并读取已有主页，避免按相似标题另建副本。读取 [记录写入](../_shared/record-writing.md) 与 [Notion 项目布局](../_shared/notion-project.md)。

优先使用指定父页，否则定位「项目总览」。存在多个无法区分的目标时集中询问，同时准备框架。告知实际目标和操作；已明确的位置直接沿用。

## 2. 建立或补齐框架

按顺序保留 Issues、里程碑、项目文档、记录与归档四个区域。前两区各用一条简短占位，说明由 toPM 在组织执行时建立；本步不创建数据库、任务、里程碑或虚构进度。

文档区域按已有内容安排，尚无文档时只保留标题。不为预设类别创建空子页。记录与归档按需使用折叠区域；不放教程、重复摘要、试验或迁移说明。

已有数据库和视图原位保留，已有文档直接引用，已有人工布局优先沿用。重复调用只补缺项；不要把已填充区域恢复成占位。数据库创建与执行管理交由 toPM。

## 3. 核对与交付

检查主页父级、唯一入口、区域顺序、原有子页和数据库保留情况，区分已完成写入与待补内容。返回项目主页链接，简述框架及下一步可用 to-notion 沉淀方案。API 结构检查不等同视觉检查。
