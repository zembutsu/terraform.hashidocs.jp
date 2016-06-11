.. -*- coding: utf-8 -*-
.. URL: https://www.terraform.io/intro/vs/custom.html
.. SOURCE: https://github.com/hashicorp/terraform/blob/master/website/source/intro/vs/custom.html.markdown
     https://github.com/hashicorp/terraform/commits/master/website/source/intro/vs/custom.html.markdown
.. check date: 2016/06/11
.. Commits on Oct 22, 2014 073a0f76c51e966232f5c8b66e3ce78b0eec87be
.. -----------------------------------------------------------------------------

.. Terraform vs. Custom Solutions

.. _terraform-vs-custom-solutions:

=======================================
Terraform と カスタム・ソリューションの比較
=======================================

.. Most organizations start by manually managing infrastructure through simple scripts or web-based interfaces. As the infrastructure grows, any manual approach to management becomes both error-prone and tedious, and many organizations begin to home-roll tooling to help automate the mechanical processes involved.

多くの組織はインフラの管理を手動で始めます。管理はシンプルなスクリプトを通してか、あるいは、ウェブをベースとしたインターフェースを通してです。インフラが大きくなると、あらゆる手動の管理手法はミスを起こしがちであり、かつ、退屈な傾向があります。そして多くの組織では、手順の改善のため、手製のツールで自動化の仕組みに役立てようとします。

.. These tools require time and resources to build and maintain. As tools of necessity, they represent the minimum viable features needed by an organization, being built to handle only the immediate needs. As a result, they are often hard to extend and difficult to maintain. Because the tooling must be updated in lockstep with any new features or infrastructure, it becomes the limiting factor for how quickly the infrastructure can evolve.

これらのツールは構築と維持のために、時間とリソースを必要です。必要なツールとは、組織で必要とする最小限の機能であり、必要な時にすぐ構築できるものです。そして、今すぐ必要なものだけを構築することです。ですが、結果としては拡張性が大変であり、維持が難しいものによくなりがちです。

.. Terraform is designed to tackle these challenges. It provides a simple, unified syntax, allowing almost any resource to be managed without learning new tooling. By capturing all the resources required, the dependencies between them can be resolved automatically so that operators do not need to remember and reason about them. Removing the burden of building the tool allows operators to focus on their infrastructure and not the tooling.

これらの課題に対応するよう Terraform は設計されています。Terraform はシンプルで、統一された構文なので、新しいツールについて学ぶ必要なく大くのリソースを管理可能にします。必要なリソースを把握しており、リソースの依存関係を自動的に処理します。そのため、作業者は依存関係や理由を覚えておく必要はありません。ツール導入の負担を減らしますので、作業者はインフラに集中できるのです。ツールではありません。

.. Furthermore, Terraform is an open source tool. In addition to HashiCorp, the community around Terraform helps to extend its features, fix bugs and document new use cases. Terraform helps solve a problem that exists in every organization and provides a standard that can be adopted to avoid reinventing the wheel between and within organizations. Its open source nature ensures it will be around in the long term.

さらに付け加えると、Terraform はオープンソースのツールです。HashiCorp だけでなく、Terraform のコミュニティが機能の拡張、バグ対応、新しい使い方のドキュメントに取り組んでいます。あらゆる既存の組織がかかえる問題を Terraform が解決し、標準化をもたらします。そのため、組織内における車輪の再発明を防げます。オープンソースの性質上、長期間にわたって使えます。

.. seealso:: 
   Terraform vs. Custom Solutions
      https://www.terraform.io/intro/vs/custom.html
