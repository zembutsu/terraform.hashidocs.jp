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
Terraform と Boto や Fog との比較
=======================================

.. Libraries like Boto, Fog, etc. are used to provide native access to cloud providers and services by using their APIs. Some libraries are focused on specific clouds, while others attempt to bridge them all and mask the semantic differences. Using a client library only provides low-level access to APIs, requiring application developers to create their own tooling to build and manage their infrastructure.

Boto や Fig などのライブラリは、クラウド・プロバイダやサービスに対して、それぞれの API でネイティブなアクセスを提供します。全てを接続して差違を埋めるのではなく、あるライブラリは特定のクラウドに焦点をあてています。クライアント・ライブラリは API で低レベルのアクセスのみ提供するため、アプリケーション開発者は自信でインフラを構築・管理するツールを作成する必要があります。

.. Terraform is not intended to give low-level programmatic access to providers, but instead provides a high level syntax for describing how cloud resources and services should be created, provisioned, and combined. Terraform is very flexible, using a plugin-based model to support providers and provisioners, giving it the ability to support almost any service that exposes APIs.

Terraform では、プロバイダに対する低レベルなプログラミング的なアクセスを提供する意図を持ちません。しかし、そのかわりに高レベルな記述構文を提供します。ここで記述するのは、クラウドのリソースやサービスを、どのように作成・プロビジョン・連携するかです。Terraform はプラグインをベースとしたモデルでプロバイダやプロビジョナをサポートするため、非常に柔軟です。そして、公開 API を通して、様々なサービスをサポートできます。

.. seealso:: 
   Terraform vs. Boto, 
      https://www.terraform.io/intro/vs/boto.html
