# 引入 asyncio 库
import asyncio
# 引入 time 库，便于格式化时间输出
import time


# 声明一个异步函数用于运行一个独立的任务
async def task(tag, delay):
    # 循环 6 次执行输出语句
    for i in range(6):
        # 根据 delay 参数休眠，delay 的值以秒为单位
        await asyncio.sleep(delay)
        # 按指定格式输出时间，用以标识本次输出
        print(f"[{time.strftime('%X')}]Task:{tag}, step {i}")


async def main():
    # 创建第 1 个任务，不等待执行结束，
    # 意味着这行代码不阻塞当前的协程，则程序继续走下去
    asyncio.create_task(task("task1", 1))

    # 创建第 2 个任务，并且使用 await 关键字等待该任务完成，
    # 如果这里不等待，程序继续运行下去便走到了程序结尾，
    # 则整个程序在两个任务还未执行完成时便退出，这并非我们的原意
    await asyncio.create_task(task("task2", 2))

if __name__ == '__main__':
    # 启动 asyncio 主程序
    asyncio.run(main())
