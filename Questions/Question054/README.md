Question054 - PyCharm 中的 Too broad exception clause 好煩好煩怎麼辦 ?
=====
```
try:
    ...
except Exception:  # <= causes warning: Too broad exception clause
    ...
```
* ### use ```# noinspection PyBroadException``` to tell PyCharm that you're OK with this exception clause. 
```
# noinspection PyBroadException
try:
    ...
except Exception:
    ...
```
<br />
