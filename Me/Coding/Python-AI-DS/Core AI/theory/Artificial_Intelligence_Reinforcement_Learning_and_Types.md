# Reinforcement Learning

- Learn by interacting with an environment — no labels, only reward signals
- Agent takes actions, receives feedback, updates behavior to maximize cumulative reward

**Core setup**
- Agent — the decision-maker
- Environment — the system the agent acts within
- State (s) — current situation observed by the agent
- Action (a) — choice the agent makes
- Reward (r) — scalar feedback signal (positive or negative)
- Policy π(a|s) — learned mapping from state to action

**Goal**
- Maximize cumulative (discounted) reward over time, not just immediate reward

**Process**
1. Observe state s
2. Select action a via policy π
3. Receive reward r
4. Transition to next state s'
5. Update policy → repeat

**Key distinction from other ML types**
- Supervised: correct label provided per input
- Unsupervised: no signal, find structure
- RL: delayed, sparse reward signal — agent must discover what works through trial and error

**Real-world examples**
- Game playing — AlphaGo, AlphaZero, Atari DQN
- Robotics — locomotion, manipulation, sim-to-real transfer
- Recommendation systems — maximize long-term engagement
- Self-driving — sequential decision-making under uncertainty
- RLHF — aligning LLMs using human preference as reward signal

---
# Common algorithms
- Q-Learning / DQN — learn value of state-action pairs
- Policy Gradient (REINFORCE) — directly optimize policy
- PPO (Proximal Policy Optimization) — stable policy gradient, widely used
- Actor-Critic (A3C, SAC) — combine value estimation + policy optimization

---
# Failure modes

| Problem                     | Cause                                                   |
| --------------------------- | ------------------------------------------------------- |
| Credit assignment           | Reward is delayed — hard to know which action caused it |
| Exploration vs exploitation | Too greedy → local optima; too random → no learning     |
| Sparse rewards              | Agent rarely gets feedback → slow or no learning        |
| Reward hacking              | Agent finds unintended ways to maximize proxy reward    |
| Unstable training           | Bootstrapped value estimates → feedback loops           |

---
