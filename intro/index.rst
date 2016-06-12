.. -*- coding: utf-8 -*-
.. URL: https://www.terraform.io/intro/index.html
.. SOURCE: https://github.com/hashicorp/terraform/blob/master/website/source/intro/index.html.markdown
     https://github.com/hashicorp/terraform/commits/master/website/source/intro/index.html.markdown
.. check date: 2016/06/06
.. Commits on Oct 22, 2014 073a0f76c51e966232f5c8b66e3ce78b0eec87be
.. -----------------------------------------------------------------------------

.. INTRODUCTION TO TERRAFORM

.. _introduction-to-terraform:

=======================================
Terraform 入門
=======================================

.. sidebar:: 目次

   .. contents:: 
       :depth: 3
       :local:

.. Welcome to the intro guide to Terraform! This guide is the best place to start with Terraform. We cover what Terraform is, what problems it can solve, how it compares to existing software, and contains a quick start for using Terraform.

Terraform 入門ガイドへようこそ！　このガイドは Terraform を始めるのに最適です。ここで扱うのは Terraform とは何か、どのような問題を解決するのか、既存のソフトウェアとの違いについて、そして Terraform のクイック・スタートです。

.. If you are already familiar with the basics of Terraform, the documentation provides a better reference guide for all available features as well as internals.

既に Terraform の基本について慣れているのであれば、 :doc:`ドキュメント </docs/index>` をご覧ください。利用可能な全機能に対するファレンス・ガイドだけでなく、内部実装についても扱います。

.. What is Terraform?

Terraform とは？
====================

.. Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently. Terraform can manage existing and popular service providers as well as custom in-house solutions.

Terraform はインフラを安全かつ効率的に構築、変更、バージョン管理するためのツールです。Terraform は既存かつ有名なサービス・プロバイダを管理できるだけでなく、社内でのカスタム・ソリューションも管理できます。

.. Configuration files describe to Terraform the components needed to run a single application or your entire datacenter. Terraform generates an execution plan describing what it will do to reach the desired state, and then executes it to build the described infrastructure. As the configuration changes, Terraform is able to determine what changed and create incremental execution plans which can be applied.

設定ファイルに記述するのは、単一アプリケーションまたはデータセンタ全体の実行に必要な Terraform のコンポーネント（構成部品）です。Terraform が実行計画（execution plan）の生成で表示するのは、目的とする状態に到達するには何が必要なのかです。それから、目的とするインフラの構築を実行します。設定ファイルを変更したら、Terraform は実行計画を適用するため、何を変更するか、あるいは、何を追加作成するかを決定できます。

.. The infrastructure Terraform can manage includes low-level components such as compute instances, storage, and networking, as well as high-level components such as DNS entries, SaaS features, etc.

Terraform が管理できるインフラとは、計算インスタンス、ストレージ、ネットワークのような低レベルのコンポーネントだけではありません。DNS エントリ、SasS 機能など高レベルのコンポーネントも管理できます。

.. Examples work best to showcase Terraform. Please see the use cases.

Terraform が効果を発揮する場面の例は、 :doc:`使用例 <use-cases>` をご覧ください。

.. The key features of Terraform are:

Terraform の主な機能：

..    Infrastructure as Code: Infrastructure is described using a high-level configuration syntax. This allows a blueprint of your datacenter to be versioned and treated as you would any other code. Additionally, infrastructure can be shared and re-used.

* **コードのようなインフラ（Infrastructure as Code）** ：インフラを高レベルの設定構文で記述します。これにより、データセンタの設計図（または青写真）をバージョン管理できるようになり、ほかのコードと同様に扱えます。

..    Execution Plans: Terraform has a "planning" step where it generates an execution plan. The execution plan shows what Terraform will do when you call apply. This lets you avoid any surprises when Terraform manipulates infrastructure.

* **実行計画（Execution Plans）** ：Terraform は実行計画をする「計画（Planning）」ステップがあります。実行計画とはあなたの要求を適用時、Terraform が何を処理するか表示します。これにより、Terraform でインフラを操作時、予期しない動作を起こさないようにします。

..    Resource Graph: Terraform builds a graph of all your resources, and parallelizes the creation and modification of any non-dependent resources. Because of this, Terraform builds infrastructure as efficiently as possible, and operators get insight into dependencies in their infrastructure.

* **リソース・グラフ（Resource Graph）** ：Terraform は全てのリソース・グラフを作成します。並列な作成や、依存関係を持たないリソースの変更もグラフ化します。これにより、Terraform は可能な限り効率的にインフラを構築し、作業者はインフラ上の依存関係を把握します。

..    Change Automation: Complex changesets can be applied to your infrastructure with minimal human interaction. With the previously mentioned execution plan and resource graph, you know exactly what Terraform will change and in what order, avoiding many possible human errors.

* **変更の自動化（Change Automation）** ：インフラに対する複雑な変更を、人間は最小の作業で行えます。先に記載した実行計画とリソース・グラフにより、Terraform に何を命令したら何が変わるかが明確になるため、人現が起こしうる間違いを防ぎます。

.. Next Steps

次のステップ
====================

.. See the page on Terraform use cases to see the multiple ways Terraform can be used. Then see how Terraform compares to other software to see how it fits into your existing infrastructure. Finally, continue onwards with the getting started guide to use Terraform to manage real infrastructure and to see how it works.

:doc:`Terraform 利用例 <use-cases>` では、様々な Terraform の利用例が分かります。そして :doc:`ほかのソフトウェアと Terraform の比較 <vs/index>` では、既存のインフラ上にどのように適用するか分かります。最後は前身のため、 :doc:`導入ガイド <getting-started/install>` で Terraform を実際のインフラ上で使い、どのように動作するかを理解します。


.. seealso:: 
   Introduction
      https://www.terraform.io/intro/index.html

