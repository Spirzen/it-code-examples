import { StyleSheet, Text, View, Pressable } from 'react-native';

export default function CardScreen() {
  return (
    <View style={styles.screen}>
      <View style={styles.card}>
        <Text style={styles.title}>Задача</Text>
        <Text style={styles.body}>Описание карточки</Text>
        <Pressable style={styles.button}>
          <Text style={styles.buttonLabel}>Готово</Text>
        </Pressable>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  screen: { flex: 1, padding: 16, backgroundColor: '#f3f4f6' },
  card: {
    flex: 1,
    backgroundColor: '#fff',
    borderRadius: 12,
    padding: 20,
    justifyContent: 'space-between',
  },
  title: { fontSize: 20, fontWeight: '600' },
  body: { fontSize: 16, color: '#4b5563' },
  button: {
    backgroundColor: '#2563eb',
    padding: 14,
    borderRadius: 8,
    alignItems: 'center',
  },
  buttonLabel: { color: '#fff', fontWeight: '600' },
});
