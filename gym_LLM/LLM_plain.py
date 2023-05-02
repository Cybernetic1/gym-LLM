import gym
import numpy
from gym import spaces, error
import xml.etree.ElementTree as ET
import os

class LLMEnv(gym.Env):

	def __init__(self):
		super(LLMEnv, self).__init__()

		# Action space = space of words in vocabulary (default = 50432)
		self.vocab_size = 50432
		self.action_space = spaces.Discrete(self.vocab_size)

		# State space = sequence of prior tokens (dim = d_model each)
		self.d_model = 512
		self.state_space = spaces.Sequence( spaces.Box( -1.0, 1.0, shape = (self.d_model,) ))
		# print("state space test sample:", self.state_space.sample())

		self.observation_space = spaces.Sequence( spaces.Box( -1.0, 1.0, shape = (self.d_model,) ))

		self.rewards = {
			'wrong_word': -1.0,
			'right_word': 5.0
			}

	def reset(self):
		self.state_vector = (self.d_model) * [0]
		return numpy.array(self.state_vector)

	# ------------------ GAME STATE CHECK ----------------
	def is_win(self):
		if self.win == 1:
			return True
		return False

	def is_draw(self):
		for i in range(self.board_size * self.board_size):
			if self.state_vector[i] == 0:
				return False
		return True

	# ------------------ ACTIONS --------------------
	def step(self, action, symbol):
		is_position_already_used = False

		if self.state_vector[action] != 0:
			is_position_already_used = True

		if is_position_already_used:
			self.state_vector[action] = "Bad"
			reward_type = 'bad_position'
			done = True
		else:
			self.state_vector[action] = symbol

			if self.is_win():
				reward_type = 'win'
				done = True
			elif self.is_draw():
				reward_type = 'draw'
				done = True
			else:
				reward_type = 'still_in_game'
				done = False

		return numpy.array(self.state_vector), self.rewards[reward_type], done, {'already_used_position': is_position_already_used}

	def render(self, mode=None, close=False):
		print("Display sentence")

	def close(self):
		return None

	def seed(self, seed=None):
		self.action_space.np_random.seed(seed)
		return [seed]
