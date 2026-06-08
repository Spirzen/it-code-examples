class ActorCriticAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.actor = self._build_actor()
        self.critic = self._build_critic()
        self.gamma = 0.99
    
    def _build_actor(self):
        inputs = tf.keras.layers.Input(shape=(self.state_size,))
        x = tf.keras.layers.Dense(256, activation='relu')(inputs)
        x = tf.keras.layers.Dense(256, activation='relu')(x)
        outputs = tf.keras.layers.Dense(self.action_size, activation='tanh')(x)
        model = tf.keras.Model(inputs, outputs)
        model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001))
        return model
    
    def _build_critic(self):
        state_input = tf.keras.layers.Input(shape=(self.state_size,))
        action_input = tf.keras.layers.Input(shape=(self.action_size,))
        
        x = tf.keras.layers.Concatenate()([state_input, action_input])
        x = tf.keras.layers.Dense(256, activation='relu')(x)
        x = tf.keras.layers.Dense(256, activation='relu')(x)
        outputs = tf.keras.layers.Dense(1, activation='linear')(x)
        
        model = tf.keras.Model([state_input, action_input], outputs)
        model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='mse')
        return model
    
    def act(self, state):
        state = np.reshape(state, [1, self.state_size])
        action = self.actor.predict(state, verbose=0)[0]
        noise = np.random.normal(0, 0.1, size=self.action_size)
        return np.clip(action + noise, -1, 1)
    
    def train(self, state, action, reward, next_state, done):
        state = np.reshape(state, [1, self.state_size])
        next_state = np.reshape(next_state, [1, self.state_size])
        action = np.reshape(action, [1, self.action_size])
        
        target = reward
        if not done:
            next_action = self.actor.predict(next_state, verbose=0)
            target += self.gamma * self.critic.predict([next_state, next_action], verbose=0)[0][0]
        
        target_value = np.array([[target]])
        self.critic.fit([state, action], target_value, epochs=1, verbose=0)
