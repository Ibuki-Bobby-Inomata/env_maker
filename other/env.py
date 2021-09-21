import gym

class MyEnv(gym.Env):
    def __init__(self):
        ACTION_NUM=3 #アクションの数が3つの場合
        self.action_space = gym.spaces.Discrete(ACTION_NUM) 
        
        #状態が3つの時で上限と下限の設定と仮定
        LOW=[0,0,0]
        HIGH=[1,1,1]
        self.observation_space = gym.spaces.Box(low=LOW, high=HIGH)

    def reset(self):
        return observation

    def step(self, action_index):
        return observation, reward, done, {}

    def render(self):
        pass