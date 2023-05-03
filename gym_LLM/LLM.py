import gym
import numpy
from gym import spaces, error
import os

class LLMEnv(gym.Env):

	def __init__(self):
		super(LLMEnv, self).__init__()

		# Action space = space of words in vocabulary (default = 50432)
		self.vocab_size = 50432
		self.action_space = spaces.Discrete(self.vocab_size)

		# State space = sequence of prior tokens (dim = d_model each)
		self.d_model = 96

		self.observation_space = spaces.Sequence( spaces.Box( -1.0, 1.0, shape = (self.d_model,) ))
		# print("state space test sample:", self.observation_space.sample())

		self.rewards = {
			'wrong_word': -1.0,
			'right_word': 5.0
			}

	def reset(self):
		self.state = ()		# empty sequence
		return self.state

	# ------------------ ACTIONS --------------------
	def step(self, action):

		# State update
		# append new token to obs sequence
		self.state = self.state + (action,)

		# Determine reward
		if self.is_win():
			reward_type = 'win'
			done = True
		elif self.is_draw():
			reward_type = 'draw'
			done = True
		else:
			reward_type = 'still_in_game'
			done = False

		return self.state, self.reward, done

	def render(self, mode=None, close=False):
		print("[display sentence?]")

	def close(self):
		return None
