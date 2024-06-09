import gym
import numpy as np
import  time
# 创建 CarRacing-v0 环境
env = gym.make('CarRacing-v0')

# 初始化环境
env.reset()

# 设置渲染模式
env.render()
time.sleep(10)
env.close()
