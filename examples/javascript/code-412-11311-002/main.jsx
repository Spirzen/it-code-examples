import { useState } from 'react';
import { StyleSheet, Text, View, Pressable, TextInput } from 'react-native';

export default function App() {
  const [name, setName] = useState('');
  const [count, setCount] = useState(0);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Привет, React Native</Text>
      <TextInput
        style={styles.input}
        placeholder="Ваше имя"
        value={name}
        onChangeText={setName}
      />
      {name ? <Text style={styles.greet}>Привет, {name}!</Text> : null}
      <Text style={styles.counter}>Счётчик: {count}</Text>
      <Pressable style={styles.button} onPress={() => setCount((c) => c + 1)}>
        <Text style={styles.buttonText}>+1</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', padding: 24 },
  title: { fontSize: 22, fontWeight: '600', marginBottom: 16 },
  input: { borderWidth: 1, borderColor: '#ccc', padding: 12, borderRadius: 8 },
  greet: { marginTop: 12, fontSize: 18 },
  counter: { marginTop: 24, fontSize: 18 },
  button: {
    marginTop: 12,
    backgroundColor: '#2563eb',
    padding: 14,
    borderRadius: 8,
    alignItems: 'center',
  },
  buttonText: { color: '#fff', fontWeight: '600' },
});
