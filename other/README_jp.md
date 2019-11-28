# Auto-C-Execution

![Python3.6](https://img.shields.io/badge/Python-3.6-brightgreen)
![size](https://img.shields.io/github/repo-size/yuto51942/Auto-C-Execution)
![lastcommit](https://img.shields.io/github/last-commit/yuto51942/Auto-C-Execution)
![twitter](https://img.shields.io/twitter/follow/cateiru?style=social)

## languages

[English](../README.md)

## 説明

大学、高校などのC言語の授業でのプログラム作成のお手伝いをします。

* 必要なソフトフェアが存在しない場合自動的にインストールします。
* `gcc`により自動的にC言語で書かれたプログラムをコンパイルします。
* 正常にコンパイルできた場合`.out`を実行します。
* 正常に実行ができたら結果logを画像として出力します。
* 生成画像の例  
    [image1](Images/test.c.png)  
    [image2](Images/test2.c.png)  
    [image3](Images/test3.c.png)

## 動作環境

OS: MacOS  
Font: Menlo.ttc

## 注意

* 複数ファイルのコンパイルは未対応です。
* 入力がある場合、その前の出力はterminalに表示されません。

## 使用方法

1. pipを使用しGithubのリポジトリからインストールする。

    ```bash
    pip install git+https://github.com/yuto51942/Auto-C-Execution
    ```

2. このリポジトリの`main.py`をダウンロード、または下のコードをコピーアンドペーストし新しいファイルを作成。
3. `.c`が入ったディレクトリに移動し、そこに`main.py`を移動させる。
4. Terminalでそのディレクトリに移動する。
5. その`main.py`を実行する。

    ```bash
    # Homebrew, gccのインストールを確認する。PC内にない場合はインストールする。
    python main.py --install

    # コンパイルとその結果を画像化する。
    python main.py --create
    ```

## `main`のソースコード

```py
import sys
import os
from autoce import create, check


def main(args: list) -> None:
    if args[1] == '--install':
        check.brew_install()
        check.gcc_install()
        return
    elif args[1] == '--create':
        create.execution(os.getcwd())


if __name__ == "__main__":
    main(sys.argv)
```

## テストについて

* TDDで開発をしています。テストを実行する際はTerminalで`tox`と入力します。

## 更新履歴

### v1.2.0

* 出力結果によって画像サイズが変更されるようにした。

### v1.2.5

* 生成する画像のバックカラーとフォント、フォントサイズを変更しより見やすくした。

![follow](https://img.shields.io/github/followers/yuto51942?label=Follow&style=social)
