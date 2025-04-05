# Pot-App RapidOCR 文字识别插件 Python 版

## 为什么要弄这个插件

因为官方 [pot-app-recognize-plugin-rapid](https://github.com/pot-app/pot-app-recognize-plugin-rapid) 插件依赖的 [RapidOcrOnnx](https://github.com/RapidAI/RapidOcrOnnx) 更新太慢，我又需要使用他家更新更强的模型，刚好会点 Python，所以就照猫画虎写了这个插件。

本插件支持 RapidOCR 的四种模型：ONNXRuntime（默认）/OpenVINO/PaddlePaddle/PyTorch，可以自行配置使用。使用非默认模型需要安装对应的运行时环境，请自行研究，这里不做说明。

更多模型详情见：https://rapidai.github.io/RapidOCRDocs/main/model_list/

## 使用方法

1. 安装 Python 包管理工具`uv`，确保配好 Python 环境：https://docs.astral.sh/uv/getting-started/installation

2. [下载插件](https://github.com/ferstar/pot-app-recognize-plugin-rapid-py/releases)，解压出`plugin.com.pot-app.rapid-py.potext`文件

3. 打开 Pot-偏好设置-服务设置-翻译-添加外部插件-安装外部插件-选中`plugin.com.pot-app.rapid-py.potext`文件即可

4. Pot-偏好设置-服务设置-添加外部插件-选择`Rapid OCR Python Version`-配置需要的模型-保存即可使用

> 注意：首次使用因后台需要配置 Python 环境及下载模型，可能会比较慢，请确保网络连接顺畅并耐心等待，初始化完成后即可完全离线使用。

## 鸣谢

1. https://github.com/pot-app/pot-desktop

2. https://github.com/RapidAI/RapidOCR

3. https://docs.astral.sh/uv
