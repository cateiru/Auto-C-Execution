# Auto-C-Execution

## languages

[English](../README.md)

## 説明

大学、高校などのC言語の授業でのプログラム作成のお手伝いをします。

## 動作環境

Macのみ。

## 詳細

* 必要なソフトフェア。が存在しない場合自動的にインストールします。
* `gcc`により自動的にC言語で書かれたプログラムをコンパイルします。
* 正常にコンパイルできた場合`.out`を実行します。
* 正常に実行ができたら結果logを画像として出力します。

## 使用方法

1. pipを使用しGithubのリポジトリからインストールする。

    ```bash
    pip install git+https://github.com/yuto51942/Auto-C-Execution
    ```

2. このリポジトリの`main.py`をダウンロード、または下のコードをコピーアンドペーストし新しいファイルを作成。
3. `.c`が入ったディレクトリに移動し、そこに`main.py`を移動させる、
4. Terminalでそのディレクトリに移動する。
5. その`main.py`を実行する。

    ```bash
    # Homebrew, gccのインストールを確認する。PC内にない場合はインストールする。
    python main.py --install

    # コンパイルとその結果を画像化する。
    python main.py --create
    ```

## mainのソースコード

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

## 静的解析、テストについて

* Google Python Style Guideに基づいています。
* TDDで開発をしています。テストを実行する際はTerminalで`tox`と入力します。
