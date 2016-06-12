.. -*- coding: utf-8 -*-
.. URL: https://www.terraform.io/intro/getting-started/install.html
.. SOURCE: https://github.com/hashicorp/terraform/blob/master/website/source/intro/getting-started/install.html.markdown
     https://github.com/hashicorp/terraform/commits/master/website/source/intro/getting-started/install.html.markdown
.. check date: 2016/06/0
.. Commits on Mar 5, 2016 b7008babd7e31c5a153648d481216beafdaa5dcf
.. -----------------------------------------------------------------------------

.. Install Terraform

.. _install-terraform:

=======================================
Terraform のインストール
=======================================

.. sidebar:: 目次

   .. contents:: 
       :depth: 3
       :local:

.. Terraform must first be installed on your machine. Terraform is distributed as a binary package for all supported platforms and architecture. This page will not cover how to compile Terraform from source.

Terraform を使うには、まず第一に自分のマシン上にインストールします。Terraform はサポート対象のプラットフォームとアーキテクチャごとに :doc:`バイナリ・パッケージ </downloads>` を配布しています。このページではソースから Terraform をコンパイルする手法を扱いません。

.. Installing Terraform

.. _installing-terraform:

Terraform のインストール作業
==============================

.. To install Terraform, find the appropriate package for your system and download it. Terraform is packaged as a zip archive.

Terraform をインストールするには、自分のシステム用の :doc:`適切なパッケージ </downloads>` を探してダウンロードします。Terraform は zip アーカイブにパッケージ化されています。

.. After downloading Terraform, unzip the package into a directory where Terraform will be installed. The directory will contain a set of binary programs, such as terraform, terraform-provider-aws, etc. The final step is to make sure the directory you installed Terraform to is on the PATH. See this page for instructions on setting the PATH on Linux and Mac. This page contains instructions for setting the PATH on Windows.

Terraform をダウンロードしたら、Terraform をインストールするディレクトリの中に、パッケージを unzip （展開）します。ディレクトリ内には ``terraform`` 、 ``terraform-provider-aws`` などのバイナリ・プログラム群が入ります。最後のステップは Terraform をインストールしたディレクトリを環境変数 PATH に追加します。Linux と Mac で PATH を設定する手順は `こちら <https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux>`_ のページをご覧ください。Windows で PATH を指定するには `こちら <https://stackoverflow.com/questions/1618280/where-can-i-set-path-to-make-exe-on-windows>`__ の手順をご覧ください。

.. Example for Linux/Mac - Type the following into your terminal:

Linux/mac の例 - ターミナル上で以下のコマンドを実行：

.. code-block:: bash

   PATH=/usr/local/terraform/bin:/home/your-user-name/terraform:$PATH

.. Example for Windows - Type the following into Powershell:

Windows の例 - Powershell 上で以下のコマンドを実行：

.. code-block:: bash

   set PATH=%PATH%;C:\terraform

.. Verifying the Installation

.. _veritying-the-installation:

インストールの確認
====================

.. After installing Terraform, verify the installation worked by opening a new terminal session and checking that terraform is available. By executing terraform you should see help output similar to that below:

Terraform のインストール後、新しいターミナル・セッションを開き、 ``terraform`` コマンドが動作するか確認します。

.. code-block:: bash

   $ terraform
   usage: terraform [--version] [--help] <command> [<args>]
   
   Available commands are:
       apply       Builds or changes infrastructure
       destroy     Destroy Terraform-managed infrastructure
       get         Download and install modules for the configuration
       graph       Create a visual graph of Terraform resources
       init        Initializes Terraform configuration from a module
       output      Read an output from a state file
       plan        Generate and show an execution plan
       push        Upload this Terraform module to Atlas to run
       refresh     Update local state file against real resources
       remote      Configure remote state storage
       show        Inspect Terraform state or plan
       taint       Manually mark a resource for recreation
       validate    Validates the Terraform files
       version     Prints the Terraform version

.. If you get an error that terraform could not be found, then your PATH environment variable was not setup properly. Please go back and ensure that your PATH variable contains the directory where Terraform was installed.

``terraform`` が見つからないとエラーが出る場合は、環境変数 PATH の値を適切に設定したかを確認します。前の手順に戻り、環境変数 PATH に Terraform をインストールしたディレクトリがあるかどうか確認します。

.. Otherwise, Terraform is installed and ready to go! Nice!

エラーがでなければ Terraform はインストール完了しています。準備が整いました。素晴らしい！

.. Next Step

次のステップ
====================

.. Time to build infrastructure using a minimal Terraform configuration file. You will be able to examine Terraform's execution plan before you deploy it to AWS.

最小限の Terraform 設定ファイルを使い :doc:`インフラを構築 <build>` する時間です。AWS へデプロイする前に、Terraform の実行計画を調べましょう。



.. seealso:: 
   Install Terraform
      https://www.terraform.io/intro/getting-started/install.html

