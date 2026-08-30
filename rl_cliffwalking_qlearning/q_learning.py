"""
Off-Policy Q-Learning Algorithm for CliffWalking
"""
import numpy as np
from cliff_environment import CliffWalkingEnv

def train_q_learning(episodes=500, alpha=0.1, gamma=0.99):
    env = CliffWalkingEnv()
    Q = np.zeros((env.rows, env.cols, 4))
    rewards = []

    for ep in range(episodes):
        s = env.reset()
        ep_reward = 0
        eps = max(0.01, 1.0 - ep / 300)
        done = False

        while not done:
            if np.random.rand() < eps:
                a = np.random.randint(4)
            else:
                a = np.argmax(Q[s[0], s[1]])

            ns, r, done = env.step(a)
            ep_reward += r
            best_next_a = np.max(Q[ns[0], ns[1]])
            Q[s[0], s[1], a] += alpha * (r + gamma * best_next_a - Q[s[0], s[1], a])
            s = ns
            if ep_reward < -1000:
                break
        rewards.append(ep_reward)

    return Q, rewards

if __name__ == '__main__':
    Q, rewards = train_q_learning()
    print(f"Trained Q-learning across {len(rewards)} episodes. Final 10-ep average reward: {np.mean(rewards[-10:]):.1f}")
