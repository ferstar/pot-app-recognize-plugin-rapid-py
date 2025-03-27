# Pot-App RapidOCR 文字识别插件 Python 版

## 为什么要弄这个插件

因为官方 [pot-app-recognize-plugin-rapid](https://github.com/pot-app/pot-app-recognize-plugin-rapid) 插件依赖的 [RapidOcrOnnx](https://github.com/RapidAI/RapidOcrOnnx) 更新太慢，我又需要使用他家更新更强的模型，刚好会点 Python，所以就照猫画虎写了这个插件。

本插件支持 RapidOCR 的四种模型：ONNXRuntime/OpenVINO/PaddlePaddle/PyTorch，可以自行配置使用。

更多模型详情见：https://rapidai.github.io/RapidOCRDocs/main/model_list/

## 使用方法

1. 安装 Python 包管理工具`uv`：https://docs.astral.sh/uv/getting-started/installation

2. 打开 Pot-偏好设置-服务设置-翻译-添加外部插件-安装外部插件

3. 选择`plugin.com.pot-app.rapid-py.potext`文件，安装成功

4. 进入本插件目录，如 Linux 路径为`~/.config/com.pot-app.desktop/plugins/recognize/plugin.com.pot-app.rapid-py`

5. 在当前目录打开终端，执行初始化 Python 运行环境命令：`uv sync`

6. Pot-偏好设置-服务设置-添加外部插件-选择`Rapid OCR Python Version`-配置需要的模型-保存即可使用

## 鸣谢

1. https://github.com/pot-app/pot-desktop

2. https://github.com/RapidAI/RapidOCR

3. https://docs.astral.sh/uv
