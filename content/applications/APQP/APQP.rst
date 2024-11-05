APQP模块
========

简介
----

APQP全称Advanced Product Quality Planning，产品质量先期策划。是一种结构化方法，用于定义和建立必要的步骤，以确保产品满足客户设定的所有性能和质量要求。它旨在通过精心策划产品开发和生产的每个阶段，确保产品满足客户的期望。

功能模块概述
------------

Odoo 17 APQP模块的主要功能包括：

1. **项目**：创建项目任务，设置任务前提。
2. **任务**：管理由我发起和由我审批任务。
3. **产品**：管理与新增所有产品信息。
4. **客户**：管理与新增所有客户信息。

功能详细描述
------------

项目
----

在 **APQP模块 > 项目** 页面可以对项目总览，点击“新建”可以新增项目：

.. image:: APQP/img.png
  :align: center
  :alt: 项目

填写完下图信息后，点击“添加行”，在弹窗中选择审批人，确认无误后点击“Save&Close”：

.. image:: APQP/img_1.png
  :align: center
  :alt: 编辑

.. image:: APQP/img_2.png
  :align: center
  :alt: 选择审批人

填写完所有信息后点击Document处的Submit后再将这个项目Submit：

.. image:: APQP/img_3.png
  :align: center

.. image:: APQP/img_4.png
  :align: center

任务
----

由我发起
~~~~~~~~

在 **APQP模块 > 任务 > 由我发起** 页面可以看到由我创建的项目，点击一条进入：

.. image:: APQP/img_5.png
  :align: center

此处点击“Send Email”，可以通知审批人，在弹窗中还可以增添留言和附件：

.. image:: APQP/img_6.png
  :align: center

.. image:: APQP/img_7.png
  :align: center

由我审批
~~~~~~~~

在 **APQP模块 > 任务 > 待我审批** 页面可以看到自己被任务发起人指派审批的任务，点击进入：

.. image:: APQP/img_8.png
  :align: center

在右侧聊天框中可以收到发起人的邮件通知，在顶部点击“Approve”或“Reject”来处理此任务，处理完后点击“Send Email”可以邮件通知任务发起人任务审核进度：

.. image:: APQP/img_9.png
  :align: center

当任务通过审批，在 **APQP模块 > 任务 > 由我审批** 页面找到已经审批通过的任务，点击箭头处进入，点击“Done”完成任务：

.. image:: APQP/img_10.png
  :align: center

.. image:: APQP/img_11.png
  :align: center

当任务审批不通过，在 **APQP模块 > 任务 > 由我审批** 页面找到被拒绝的任务，点击此处进入需要修改的文档或信息，点击箭头处进入APQP Project修改信息或直接进入Documents修改文档：

.. image:: APQP/img_12.png
  :align: center

.. image:: APQP/img_13.png
  :align: center

.. image:: APQP/img_14.png
  :align: center

修改完成之后，点击文档明细处的Submit，返回上一级，可以重新发送邮件通知，之后在 **APQP模块 > 任务 > 待我审批** 页面，审批人可以重新对该任务发起审批。

产品
----

在 **APQP模块 > 产品 > 新建** 页面，填写要新增的产品信息，保存后展示在 **APQP模块 > 产品** 页面上：

.. image:: APQP/img_15.png
  :align: center

.. image:: APQP/img_16.png
  :align: center

客户
----

在 **APQP模块 > 客户 > 新建** 页面，填写要新增的产品信息，保存后展示在 **APQP模块 > 客户** 页面上：

.. image:: APQP/img_17.png
  :align: center

.. image:: APQP/img_18.png
  :align: center