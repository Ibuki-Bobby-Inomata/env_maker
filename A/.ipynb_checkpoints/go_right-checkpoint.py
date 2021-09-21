import numpy as np
import gym

# 右への移動を学ぶ環境
class GoRight(gym.Env):
    # 定数定義
    GRID_SIZE = 5
    LEFT = 0
    RIGHT = 1

    # 初期化
    def __init__(self):
        super(GoRight, self).__init__()
        # グリッドのサイズ
        self.grid_size = self.GRID_SIZE
        # 初期位置の指定
        self.agent_pos = self.GRID_SIZE - 1
        # 行動空間と状態空間の定義
        self.action_space = gym.spaces.Discrete(2)
        self.observation_space = gym.spaces.Box(low=0, high=self.GRID_SIZE - 1, shape=(1,), dtype=np.float32)

    # 環境のリセット
    def reset(self):
        # 初期位置の指定
        self.agent_pos = 0
        # 初期位置をfloat32のnumpy配列に変換
        return np.array(self.agent_pos).astype(np.float32).reshape(-1,1)

    # 環境の１ステップ実行
    def step(self, action):
        # 移動
        if action == self.LEFT:
            self.agent_pos -= 1
        elif action == self.RIGHT:
            self.agent_pos += 1
        self.agent_pos = np.clip(self.agent_pos, 0, self.GRID_SIZE)
        # エピソード完了の計算
        done = self.agent_pos == self.GRID_SIZE - 1
        # 報酬の計算
        reward = 1 if done else - 0.1
        return np.array(self.agent_pos).astype(np.float32).reshape(-1,1), reward, done, {}

    # 環境の描画
    def render(self, mode='console', close=False):
        # エージェントはA、他は.で表現する
        print('.' * self.agent_pos, end='')
        print('A', end='')
        print('.' * (self.GRID_SIZE - 1 - self.agent_pos))