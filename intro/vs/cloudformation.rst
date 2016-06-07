.. -*- coding: utf-8 -*-
.. URL: https://www.terraform.io/intro/vs/cloudformation.html
.. SOURCE: https://github.com/hashicorp/terraform/blob/master/website/source/intro/vs/cloudformation.html.markdown
     https://github.com/hashicorp/terraform/commits/master/website/source/intro/vs/cloudformation.html.markdown
.. check date: 2016/06/07
.. Commits on Oct 22, 2014 073a0f76c51e966232f5c8b66e3ce78b0eec87be
.. -----------------------------------------------------------------------------

.. Terraform vs. Cloudformation, Heat, etc

.. _terraform-vs-cloudformation-heat-etc:

=======================================
Terraform vs CloudFormation、Heat等
=======================================

.. Tools like CloudFormation, Heat, etc. allow the details of an infrastructure to be codified into a configuration file. The configuration files allow the infrastructure to be elastically created, modified and destroyed. Terraform is inspired by the problems they solve.

CloudFormation や Heat 等のツールは、インフラの詳細を設定ファイル内にコード化します。設定ファイルにより、インフラの柔軟な作成・変更・破棄を行います。つまり Terraform はこの種の問題解決に影響を受けています。

.. Terraform similarly uses configuration files to detail the infrastructure setup, but it goes further by being both cloud-agnostic and enabling multiple providers and services to be combined and composed. For example, Terraform can be used to orchestrate an AWS and OpenStack cluster simultaneously, while enabling 3rd-party providers like CloudFlare and DNSimple to be integrated to provide CDN and DNS services. This enables Terraform to represent and manage the entire infrastructure with its supporting services, instead of only the subset that exists within a single provider. It provides a single unified syntax, instead of requiring operators to use independent and non-interoperable tools for each platform and service.

インフラのセットアップ詳細に設定ファイルを使うのは、Terraform と似ています。しかし Terfarom が推進するのは、クラウド不可知論、および、複数のプロバイダとサービスを連結してまとめることです。たとえば、Terraform を AWS と OpenStack のクラスタを擬似的にオーケストレート可能です。他にもサードパーティー・プロバイダである CloudFlare や DNSimple といった、CDN や DNS サービスとの統合も可能とします。これにより、既存のプロバイダ内にあるインフラのサブネットだけでなく、インフラがサポートするサービス全体を Terraform で表示・管理可能にします。各プラットフォームやサービスで互換性がないツールを作業者は使う必要がありません。Terraform は１つの統一された構文のみ必要とします。

.. Terraform also separates the planning phase from the execution phase, by using the concept of an execution plan. By running terraform plan, the current state is refreshed and the configuration is consulted to generate an action plan. The plan includes all actions to be taken: which resources will be created, destroyed or modified. It can be inspected by operators to ensure it is exactly what is expected. Using terraform graph, the plan can be visualized to show dependent ordering. Once the plan is captured, the execution phase can be limited to only the actions in the plan. Other tools combine the planning and execution phases, meaning operators are forced to mentally reason about the effects of a change, which quickly becomes intractable in large infrastructures. Terraform lets operators apply changes with confidence, as they know exactly what will happen beforehand.

また、Terraform は実行計画（execution plan）という概念を使い、計画フェーズ（plan phase）を実行フェーズ（execution phase）から分離します。 ``terraform plan`` を実行することで、現在の状況を更新し、設定情報を参考に行動計画（action plan）を生成します。計画には作業範囲の全てを含みます。範囲に含まれるのは、リソースの作成・更新・破棄といった情報です。これにより、作業者は実際に何をしようとしているか確認可能です。 ``terraform graph`` を使えば、依存関係に従って計画を可視化します。計画を把握した後の実行フェーズでは、勝利は計画した行動のみに限定されます。計画および実行フェーズで他のツールと組みあわせると、大きなインフラでも作業者は迅速に変更対象のみに集中できます。作業者が Terraform で適用するのは事前に何を行うか把握していること、つまり、信頼している作業作業内容のみです。

.. seealso:: 
   Terraform vs. Cloudformation, heat, etc
      https://www.terraform.io/intro/vs/cloudformation.html
