# PyLaTeX研究

## 测试代码

- p001.py：
- p002.py: List/Itemize/Enumerate/Description
- p003.py: Head/Foot
- p004.py: SubFigure
- p005.py: SubFigure

## 模块

pylatex/figure.py中包含Figure，StandAloneGraphic等类，在引用时：

```
from pylatex import Figure, StandAloneGraphic
```

# 疑问

- 见`headfoot.py`：
```
    _latex_name = "fancypagestyle"

    packages = [Package('fancyhdr')]
``` 