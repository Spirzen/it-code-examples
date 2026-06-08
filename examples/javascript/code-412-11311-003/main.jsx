import { FlatList, StyleSheet, Text, View } from 'react-native';

const TASKS = [
  { id: '1', title: 'Купить молоко' },
  { id: '2', title: 'Позвонить в поддержку' },
  { id: '3', title: 'Прочитать главу про RN' },
];

export default function TaskList() {
  return (
    <View style={styles.screen}>
      <FlatList
        data={TASKS}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View style={styles.row}>
            <Text style={styles.rowTitle}>{item.title}</Text>
          </View>
        )}
        ItemSeparatorComponent={() => <View style={styles.separator} />}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  screen: { flex: 1, paddingTop: 48 },
  row: { padding: 16, backgroundColor: '#fff' },
  rowTitle: { fontSize: 16 },
  separator: { height: 1, backgroundColor: '#e5e7eb' },
});
