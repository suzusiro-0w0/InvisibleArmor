# This resource-pack contains Invisible Armor texture.

# Minecraft Mod Armor Texture Extractor & Transparency Tool

This tool extracts armor textures from `.jar` files located in the `mods` directory (commonly Minecraft mod files) and then makes these textures transparent.

## Overview

1. Scans the `.jar` files in the `mods` folder for images (`.png`, `.jpg`, `.jpeg`) located in paths containing `textures/models/armor/`.
2. Extracts these armor texture files to the `assets` directory located at the same level as the script.
   - If it cannot determine the `modid` (e.g., no recognizable `assets/<modid>` structure), it falls back to placing them under `unknown_mod`.
3. After extraction, it processes all extracted images in the `assets` directory, making them fully transparent.
   - Each processed image is backed up with a `.bak` extension before being overwritten with the transparent version.

## Prerequisites

- Python 3.x  
- `Pillow` library for image processing  
  Install via:  
  ```bash
  pip install Pillow

## How to Setup and Run
1. Download or clone the code.
2. Extract the code to the resourcepacks folder. (e.g., resourcepacks/InvisibleArmor/replace.py)
3. Open a command prompt and navigate to the directory where the script is located.
4. Run `python replace.py`.


## 日本語

このツールは、`mods` ディレクトリ内にある `.jar` ファイル(主にMinecraftのMod)から、`textures/models/armor/` 以下に配置されているアーマーテクスチャを抽出し、その後、それらのテクスチャ画像を透過化するための Python スクリプトです。

## 機能概要

1. `mods` フォルダにある `.jar` ファイルを走査し、`assets/textures/models/armor/` を含むパス配下の画像(`.png`, `.jpg`, `.jpeg`)を検出します。
2. 検出した画像ファイルをスクリプト実行ディレクトリ直下の `assets` ディレクトリに展開します。
   - もし `assets/<modid>/textures/models/armor/` のような構造が取得できない場合、`unknown_mod` ディレクトリ以下に展開されます。
3. 抽出完了後、`assets` ディレクトリ内を走査して、該当する画像ファイルを透過化します。
   - 透過化処理は元画像を `*.bak` としてバックアップし、上書き保存します。

## 前提条件

- Python 3.x がインストールされていること
- `Pillow` ライブラリがインストールされていること
  - `pip install Pillow`
- `mods` ディレクトリがスクリプトと同じ階層（例：`../mods`）に存在していること

## セットアップと実行方法

1. コードをダウンロードまたはクローンします。
2. resourcepacksフォルダーに展開します。（resourcepacks/InvisibleArmor/replace.pyなどのファイルとなるように）
3. コマンドプロンプトを開き、スクリプトがあるディレクトリに移動します。
4. `python replace.py` を実行します。