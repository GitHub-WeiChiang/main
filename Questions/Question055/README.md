Question055 - 如何解決 Python 中的 Circular Import 問題 ?
=====
* ### 修改前
    ```
    # Foo/foo.py

    from Bar.bar import bar_func


    def foo_func():
        ...
    ```
    ```
    # Bar/bar.py

    from Foo.foo import foo_func


    def bar_func():
        foo_func()
    ```
* ### 解决方案 1：只引用当前的包，不引用具体的模块。
    ```
    # Foo/foo.py

    from Bar.bar import bar_func


    def foo_func():
        ...
    ```
    ```
    # Bar/bar.py

    import Foo


    def bar_func():
        Foo.foo.foo_func()
    ``` 
* ### 解决方案 2：将引用放到函数内部。
    ```
    # Foo/foo.py

    from Bar.bar import bar_func


    def foo_func():
        ...
    ```
    ```
    # Bar/bar.py

    def bar_func():
        from Foo.foo import foo_func
        
        foo_func()
    ``` 
<br />
