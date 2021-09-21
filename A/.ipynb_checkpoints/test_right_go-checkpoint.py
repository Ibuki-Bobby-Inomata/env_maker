import gym
from go_right import GoRight

# 環境の生成
env = GoRight()

# １エピソードのループ
state = env.reset()

while True:
    # ランダム行動の取得
    action = env.action_space.sample()
    # １ステップの実行
    state, reward, done, info = env.step(action)
    # 環境の描画
    env.render()
    print('reward:', reward)
    # エピソード完了
    if done:
        print('done')
        break