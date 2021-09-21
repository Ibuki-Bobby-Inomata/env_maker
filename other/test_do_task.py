import gym
from do_task import GoRight

# 環境の生成
env = GoRight()

# １エピソードのループ
state = env.reset()

i = 0

while True:
    # ランダム行動の取得
    action = env.action_space.sample()
    # １ステップの実行
    state, reward, done, info = env.step(action)
    # 環境の描画
    env.render()
    i += 1
    print(i)
    print('reward:', reward)
    # エピソード完了
    if done:
        print('done')
        break