from pydantic import BaseSettings

class EnvivonmentSettings(BaseSettings):
    # grid size
    x_size: int = 5
    y_size: int = 5
    # number of agents
    n_agents: int = 2
    # agents capacity
    fov_x: int = 3
    fov_y: int = 3
    # performance evaluation
    coverage_threshold: float = 0.9

class QTableSettings(BaseSettings):
    # policy type
    e_greedy: bool = True
    softmax: bool = False
    # Q-table update
    gamma: float = 0.9 # discount factor
    lr: float = 0.1 # learning rate
    # epsilon
    eps_start: float = 1
    eps_end: float = 0
    r: float = 0.99 # decay
    # stuck threshold
    max_stuck: int = 100000

class TrainingSettings(BaseSettings):
    train_episodes: int = 200000
    max_steps: int = 10 * 10 * 2


