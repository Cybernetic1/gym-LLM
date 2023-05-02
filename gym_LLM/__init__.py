from gym.envs.registration import register

# Env registration
# ==========================

register(
    id='LLM-v0',
    entry_point='gym_LLM.LLM_plain:LLMEnv',
    reward_threshold=1000
)
