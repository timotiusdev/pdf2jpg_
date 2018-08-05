convert.py is simple tool to convert your multiple pages pdf into three channel jpg files.

<h1>Requirements</h1>
```
pip install wand
pip install Pillow
```

<h1>How To Use</h1>

For single files just import convert to your code
```
import convert
filename = "1.pdf"
convert.pdf2jpg (filename)
```

For check and convert a single file use inputCheck
```
import convert
filename = "1.pdf"
convert.inputCheck (filename)
```

For whole directory check use dirCheck
```
import convert
DIR = "./pdfs/"
convert.dirCheck (DIR)
```
