# Gym LLM
---------
Modified from [Gym TicTacToe](https://github.com/ClementRomac/gym-tictactoe) by Clement Romac.

## Installation
1. Install [OpenAi Gym](https://github.com/openai/gym)
```bash
pip install gym
```

2. Download and install `gym-LLM`
```bash
git clone https://github.com/Cybernetic1/gym-LLM.git
cd gym-LLM
python setup.py install
```

## Running
Start by importing the package and initializing the environment
```python
import gym
import gym_LLM
env = gym.make('LLM-v1') 
```

## Settings
You can change the rewards by editing the `settings.xml` placed in your `gym-LLM` installation folder..
