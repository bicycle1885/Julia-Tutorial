# -*- coding: utf-8 -*-

c = get_config()

c.NbConvertApp.export_format = "html"

c.Exporter.preprocessors = [
    "IPython.nbconvert.preprocessors.ExecutePreprocessor",
]

c.NbConvertApp.notebooks = [
    u"./Julia高速チュートリアル.ipynb"
]
