.. -*- coding: utf-8 -*-
.. URL: https://www.terraform.io/intro/vs/chef-puppet.html
.. SOURCE: https://github.com/hashicorp/terraform/blob/master/website/source/intro/vs/chef-puppet.html.markdown
     https://github.com/hashicorp/terraform/commits/master/website/source/intro/vs/chef-puppet.html.markdown
.. check date: 2016/06/07
.. Commits on Oct 22, 2014 073a0f76c51e966232f5c8b66e3ce78b0eec87be
.. -----------------------------------------------------------------------------

.. Terraform vs. Chef, Puppet, etc

.. _terraform-vs-chef-puppet-etc:

=======================================
Terraform vs Chef、Puppet等
=======================================

.. Configuration management tools install and manage software on a machine that already exists. Terraform is not a configuration management tool, and it allows existing tooling to focus on their strengths: bootstrapping and initializing resources.

構成管理ツール（Configuration management tool）は、ソフトウェアを既存のマシン上にインストールまたは管理します。Terraform は構成管理ツールではありません。既存ツールとの比較に焦点をあてると、リソースの環境構築（ブートストラッピング）と初期化が強み強みです。

.. Using provisioners, Terraform enables any configuration management tool to be used to setup a resource once it has been created. Terraform focuses on the higher-level abstraction of the datacenter and associated services, without sacrificing the ability to use configuration management tools to do what they do best. It also embraces the same codification that is responsible for the success of those tools, making entire infrastructure deployments easy and reliable.

Terraform はリソース作成のセットアップ時に、あらゆる構成管理ツールをプロビジョナとして使えます。Terraform が集中するのはデータセンタとそこに関連付けられたサービスに対しての、高レベル抽象化です。そのため、構成管理ツールを使うのがベストであれば、そこは犠牲にしません。また、同様にコード化も包括しており、これらのツールの活躍にも責任を持つので、インフラ全体のデプロイを簡単かつ信頼できるものとします。

.. seealso:: 
   Terraform vs. Chef, Puppet, etc
      https://www.terraform.io/intro/vs/chef-puppet.html
