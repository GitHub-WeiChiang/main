Question034 - Python 中的編譯、解譯與鏈接各為何意 ?
=====
* ### 何为 "链接" ?
    * ### "链接" 是一个 "打包" 的过程，将所有的目标文件及系统组件组合成可执行文件。
    * ### 因为程序通常需要和系统提供的组件 (比如标准库) 结合，这些组件都是程序运行所必须的 (例如我们要在屏幕中输出字符，这必须调用系统提供的库才能够实现)。
    * ### 经过 "链接" 才会生成可执行程序。
* ### 运行一个高级语言程序的时候，就需要一个 "翻译机" 来从事把高级语言转变成计算机能读懂的机器语言的过程，这个过程分成两类，第一种是编译，第二种是解释。
* ### 编译型语言在程序执行之前，先会通过编译器对程序执行一个编译的过程，把程序转变成机器语言，运行时就不需要翻译，而直接执行就可以了，最典型的例子就是 C 语言。
* ### 解释型语言就没有这个编译的过程，而是在程序运行的时候，通过解释器对程序逐行作出解释，然后直接运行，最典型的例子是 Ruby。
* ### Java 首先是通过编译器编译成字节码文件，然后在运行时通过解释器给解释成机器文件，所以 Java 是一种先编译后解释的语言。
* ### C# 首先是通过编译器将 C# 文件编译成 "中繼語言 (IL, Intermediate Language)" 文件，然后在通过 "通用執行環境 (CLR, Common Language Runtime)" 将 IL 文件编译成机器文件，所以 C# 是一门纯编译语言，但是 C# 是一门需要二次编译的语言。
* ### Python 是一门先编译后解释的语言 !!
    * ### 当我们在命令行中输入 ```python xxx.py``` 时，其实是激活了 Python 的 "解释器"，告诉 "解释器": 要开始工作了。可是在 "解释" 之前，其实执行的第一项工作和 Java 一样，是编译。
    * ### 在硬盘上看到的 pyc 自然不必多说，而其实 PyCodeObject 则是 Python 编译器真正编译成的结果，也就是字节码。
    * ### 当 Python 程序运行时，编译的结果则是保存在位于内存中的 PyCodeObject 中，当 Python 程序运行结束时，Python 解释器则将 PyCodeObject 写回到 pyc 文件中。
    * ### 当 Python 程序第二次运行时，首先程序会在硬盘中寻找 pyc 文件，如果找到，则直接载入，否则就重复上面的过程。
    * ### pyc 文件其实是 PyCodeObject 的一种持久化保存方式。
    * ### pyc 文件是由 .py 文件经过编译后生成的字节码文件，其加载速度相对于之前的 py 文件有所提高，而且还可以实现源码隐藏，以及一定程度上的反编译。
* ### 需要编译成 pyc 文件的应该是那些可以重用的模块，所以 Python 的解释器认为: 只有 import 进来的模块，才是需要被重用的模块。
* ### 可以这样理解 Python 解释器的意图，Python 解释器只把可能重用到的模块持久化成 pyc 文件。
* ### 一次性的脚本文件，解释器是不会保存编译 + 解释的结果，也就是没有 .pyc 文件。
<br />