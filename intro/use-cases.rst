.. -*- coding: utf-8 -*-
.. URL: https://www.terraform.io/intro/use-cases.html
.. SOURCE: https://github.com/hashicorp/terraform/blob/master/website/source/intro/use-cases.html.markdown
     https://github.com/hashicorp/terraform/commits/master/website/source/intro/use-cases.html.markdown
.. check date: 2016/06/06
.. Commits on Jan 15, 2016 8dbc43639d8cd418ed87c4c16d2e3abeb0e610ec
.. -----------------------------------------------------------------------------

.. USE CASES

.. _use-cases:

=======================================
使用例
=======================================

.. sidebar:: 目次

   .. contents:: 
       :depth: 3
       :local:

.. Before understanding use cases, it's useful to know what Terraform is. This page lists some concrete use cases for Terraform, but the possible use cases are much broader than what we cover. Due to its extensible nature, providers and provisioners can be added to further extend Terraform's ability to manipulate resources.

利用例を理解する前に、 :doc:`Terraform とは何か <index>` を知っておけば有益でしょう。このページでは Terraform の具体的な使用例を列挙しますが、可能性としての利用例はここ以外にも広範囲にわたります。拡張性を備えている プロバイダ（provider）とプロビジョナ（provisioner）によって、Terraform のリソース管理能力をさらに追加拡張できます。

.. Heroku App Setup

.. _heroku-app-setup:

Heroku App のセットアップ
==============================

.. Heroku is a popular PaaS for hosting web apps. Developers create an app, and then attach add-ons, such as a database, or email provider. One of the best features is the ability to elastically scale the number of dynos or workers. However, most non-trivial applications quickly need many add-ons and external services.

Heroku はウェブ・アプリケーションをホスティングする有名な PaaS です。開発者はアプリケーションを作成し、それからデータベースや電子メール・プロバイダなどのアドオンを追加します。素晴らしい機能の１つに、 Heroku の dyno やワーカを伸縮自在にスケールできます。しかしながら、重要なアプリケーションの大部分は、多くのアドオンや外部サービスが迅速に必要です。

.. Terraform can be used to codify the setup required for a Heroku application, ensuring that all the required add-ons are available, but it can go even further: configuring DNSimple to set a CNAME, or setting up CloudFlare as a CDN for the app. Best of all, Terraform can do all of this in under 30 seconds without using a web interface.

Heroku アプリケーションがセットアップで必要なものを、Terraform は確実にコード化します。コード化できるのは必要な利用可能アドオンすべてだけではなく、その他のもの、例えば DNSimple の CNAME 設定や、アプリケーションの CDN として CloudFlare のセットアップも含みます。とりわけ、ウェブ・インターフェースを使わなくても、Terraform であれば 30 秒以下で実行できます。

.. Multi-Tier Applications

.. _multi-tier-application:

複数階層（multi-tier）アプリケーション
========================================

.. A very common pattern is the N-tier architecture. The most common 2-tier architecture is a pool of web servers that use a database tier. Additional tiers get added for API servers, caching servers, routing meshes, etc. This pattern is used because the tiers can be scaled independently and provide a separation of concerns.

非常に一般的なパターンは N 階層構造（アーキテクチャ）です。最も一般的な２階層構造とは、ウェブサーバのプール（集まり）と、これを使うデータベース層です。ほかに、 API サーバ、キャッシュ・サーバ、ルーティング・メッシュ等の依存に応じて層を追加します。このパターンが用いられるのは、各層が独立してスケール可能であり、各々の分離をもたらすからです。

.. Terraform is an ideal tool for building and managing these infrastructures. Each tier can be described as a collection of resources, and the dependencies between each tier are handled automatically; Terraform will ensure the database tier is available before the web servers are started and that the load balancers are aware of the web nodes. Each tier can then be scaled easily using Terraform by modifying a single count configuration value. Because the creation and provisioning of a resource is codified and automated, elastically scaling with load becomes trivial.

このようなインフラの構築・管理のためには、Terraform は理想的なツールです。各層をリソースの集合として記述でき、各リソース間の依存関係を自動的に扱います。たとえば、Terraform はウェブサーバを開始する前にデータベース層を準備できますし、ロードバランサは各ウェブ用ノードを把握できます。各層のスケールは Terraform の ``count`` （カウント）という設定値を変更するだけであり、とても簡単です。リソースの作成やプロビジョニング（自動設定）をコード化・自動化しているため、伸縮自在なスケール作業など取るに足りません。

.. Self-Service Clusters

.. _self-service-clusters:

セルフ・サービスのクラスタ
==============================

.. At a certain organizational size, it becomes very challenging for a centralized operations team to manage a large and growing infrastructure. Instead it becomes more attractive to make "self-serve" infrastructure, allowing product teams to manage their own infrastructure using tooling provided by the central operations team.

ある規模の組織において、大きく成長するインフラ管理を運用チームに集約するのは、大きなチャレンジとなります。それよりもプロダクトチームとしては、中央運用チームが提供するツールを使い、自身で管理できる「セルフ・サービス」インフラを作る方が魅力的になるでしょう。

.. Using Terraform, the knowledge of how to build and scale a service can be codified in a configuration. Terraform configurations can be shared within an organization enabling customer teams to use the configuration as a black box and use Terraform as a tool to manage their services.

Terraform を使えば、サービスをどのように構築・スケールするかの知識を、設定（configuration）としてコード化できます。Terraform の設定は組織内で共有可能なため、カスタマー・チームはブラック・ボックスとして設定を使うことができ、彼ら音サービスを管理するツールとして Terraform を使うのです。

.. Software Demos

.. _software-demos:

ソフトウェアのデモ
====================

.. Modern software is increasingly networked and distributed. Although tools like Vagrant exist to build virtualized environments for demos, it is still very challenging to demo software on real infrastructure which more closely matches production environments.

最近のソフトウェアは、ますますネットワーク化・分散化されつつあります。デモ要に仮想化環境を構築するには `Vagrant <https://www.vagrantup.com/>`_ のようなツールがあります。しかしながら、デモ環境のインフラをプロダクション環境に極めて近づけるのは大変です。

.. Software writers can provide a Terraform configuration to create, provision and bootstrap a demo on cloud providers like AWS. This allows end users to easily demo the software on their own infrastructure, and even enables tweaking parameters like cluster size to more rigorously test tools at any scale.

ソフトウェア開発者は Terraform の設定を提供することにより、AWS のようなクラウド・プロバイダ上にデモの構築・プロビジョン・ブートストラップ（起動）ができるようになります。これにより、エンドユーザは簡単にソフトウェアのデモを自身のインフラ上で可能となります。それだけでなく、あらゆる規模にスケール可能な厳密な試験ツール用の、クラスタ・サイズのパラメータのような細かな調整さえも可能とします。

.. Disposable Environments

.. _disposable-environments:

ディスポーザブル（使い捨て）な環境
========================================

.. It is common practice to have both a production and staging or QA environment. These environments are smaller clones of their production counterpart, but are used to test new applications before releasing in production. As the production environment grows larger and more complex, it becomes increasingly onerous to maintain an up-to-date staging environment.

プロダクションと、ステージングまたは QA 環境の両方を準備するのは一般的です。これらの環境はプロダクションと類似する小さな複製です。とはいえ、プロダクションで新しいアプリケーションのリリース前にテストするために使われます。プロダクション環境が大きく成長して複雑になれば、ステージング環境の更新や維持の煩雑さも増えるでしょう。

.. Using Terraform, the production environment can be codified and then shared with staging, QA or dev. These configurations can be used to rapidly spin up new environments to test in, and then be easily disposed of. Terraform can help tame the difficulty of maintaining parallel environments, and makes it practical to elastically create and destroy them.

Terraform を使ってプロダクション環境をコード化すると、それをステージング、QA あるいは開発で共有できます。これらの設定はテスト用の新しい環境を迅速にスピンアップし（立ち上げ）、終わったら簡単に破棄できます。Terraform は並列環境の難しい管理を緩和し、環境作成と破棄といった扱いを伸縮自在にします。

.. Software Defined Networking

.. _software-defined-networing:

ソフトウェア定義ネットワーク
==============================

.. Software Defined Networking (SDN) is becoming increasingly prevalent in the datacenter, as it provides more control to operators and developers and allows the network to better support the applications running on top. Most SDN implementations have a control layer and infrastructure layer.

ソフトウェア定義ネットワーク（Software Defined Networking; SDN）はデータセンタにおいてますます広まりつつあります。それは、この環境上で作業者や開発者がアプリケーション実行を管理しやすくなるからです。SDN 実装の多くはコントロール・レイヤとインフラ・レイヤを持ちます。

.. Terraform can be used to codify the configuration for software defined networks. This configuration can then be used by Terraform to automatically setup and modify settings by interfacing with the control layer. This allows configuration to be versioned and changes to be automated. As an example, AWS VPC is one of the most commonly used SDN implementations, and can be configured by Terraform.

Terraform はソフトウェア定義ネットワークの設定をコード化して使えます。Terraform はこの設定を使い、自動セットアップとコントロール・レイヤの設定変更をします。設定はバージョン化と変更を自動的に行えます。たとえば、 `AWS VPC <https://aws.amazon.com/vpc/>`_ は最も一般的に使われている SDN 実装であり、 :doc:`Terraform によって設定可能 </docs/providers/aws/r/vpc>` です。

.. Resource Schedulers

.. _resource-schedulers:

リソース・スケジューラ
==============================

.. In large-scale infrastructures, static assignment of applications to machines becomes increasingly challenging. To solve that problem, there are a number of schedulers like Borg, Mesos, YARN, and Kubernetes. These can be used to dynamically schedule Docker containers, Hadoop, Spark, and many other software tools.

大規模なインフラでマシンにアプリケーションを静的に割り振るのは、負荷になりがちです。この問題を解決するために、Borg、Mesos、YARN、Kubernetes のようなスケジューラがたくさんあります。動的にスケジュールするものとしては、Docker コンテナ、Hadoop、Spark そしてその他のソフトウェア・ツールがあります。

.. Terraform is not limited to physical providers like AWS. Resource schedulers can be treated as a provider, enabling Terraform to request resources from them. This allows Terraform to be used in layers: to setup the physical infrastructure running the schedulers as well as provisioning onto the scheduled grid.

Terraform は AWS のような物理プロバイダのみに限定されません。リソース・スケジューラをプロバイダとして扱うことで、Terraform はそれらにリソースのリクエストを可能とします。これにより、Terraform を様々なレイヤで利用出来ます。たとえば、スケジューラを物理インフラで実行するようセットアップするだけでなく、スケジュール化されたグリッドへのプロビジョニングも可能です。

.. Multi-Cloud Deployment

.. _multi-cloud-deployment:

マルチ・クラウドのデプロイ
==============================

.. It's often attractive to spread infrastructure across multiple clouds to increase fault-tolerance. By using only a single region or cloud provider, fault tolerance is limited by the availability of that provider. Having a multi-cloud deployment allows for more graceful recovery of the loss of a region or entire provider.

多くの場合で魅力があるのは、障害耐性（fault-tolerance）を高めるため、複数のクラウドに渡るインフラの展開です。１つのリージョンやクラウド・プロバイダで実現しようとしても、障害耐性はプロバイダの有効範囲に限定されます。複数のクラウドにデプロイできれば、プロバイダの一部や全体が失われても、スムーズに復旧できるでしょう。

.. Realizing multi-cloud deployments can be very challenging as many existing tools for infrastructure management are cloud-specific. Terraform is cloud-agnostic and allows a single configuration to be used to manage multiple providers, and to even handle cross-cloud dependencies. This simplifies management and orchestration, helping operators build large-scale multi-cloud infrastructures.

複数クラウドへのデプロイを実現するために、多くの既存のインフラ管理ツールがあります。しかし、どれも特定のクラウド向けです。Terraform はクラウド不可知論（cloud-agnostic；訳者注、何らかの本質を、人が認識するのは不可能であるという考え）であり、そのため、簡単な設定が複数のプロバイダの管理に使えるだけでなく、クラウドを交差する依存関係も扱えます。このシンプルな管理とオーケストレーションは、作業者が大規にスケールする複数クラウド・インフラの構築を助けます。

.. seealso:: 
   Use Cases
      https://www.terraform.io/intro/use-cases.html

