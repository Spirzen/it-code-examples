
import { StatusBar } from 'expo-status-bar';
import { useState } from 'react';
import { Pressable, StyleSheet, Text, View } from 'react-native';

export default function App() {
  const [clicks, setClicks] = useState(0);

  return (
    <View style={styles.root}>
      <Text style={styles.h1}>Expo Hello</Text>
      <Text>Нажатий: {clicks}</Text>
      <Pressable style={styles.btn} onPress={() => setClicks((n) => n + 1)}>
        <Text style={styles.btnLabel}>Нажми</Text>
      </Pressable>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  root: { flex: 1, alignItems: 'center', justifyContent: 'center' },
  h1: { fontSize: 24, marginBottom: 12 },
  btn: { marginTop: 16, paddingHorizontal: 20, paddingVertical: 12, backgroundColor: '#10b981', borderRadius: 8 },
  btnLabel: { color: '#fff' },
});
