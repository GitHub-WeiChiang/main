Question052 - 遇到問題 error: externally-managed-environment 要如何解決 ?
=====
```
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.

    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.

    See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
```
* ### This is due to your distribution adopting PEP 668 – Marking Python base environments as "externally managed".
* ### 这个错误是因为其在一个 "externally-managed (外部管理的)" Python 环境中尝试安装 Python 包，这种环境通常由操作系统的包管理器管理，如 apt，以避免系统包被破坏。
* ### 解決法: ```使用虚拟环境 (venv) 安装 Python 包```。
<br />
