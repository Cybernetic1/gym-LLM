# Gym LLM
---------

## Installation

Install [OpenAi Gym](https://github.com/openai/gym)
```bash
pip install gym
```

Download and install `gym-LLM`
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


## Acknowledgement

Modified from [Gym TicTacToe](https://github.com/ClementRomac/gym-tictactoe) by Clement Romac.
