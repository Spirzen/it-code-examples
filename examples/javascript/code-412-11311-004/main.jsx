import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { Pressable, StyleSheet, Text, View } from 'react-native';

const Stack = createNativeStackNavigator();

function HomeScreen({ navigation }) {
  return (
    <View style={styles.center}>
      <Text style={styles.h1}>Главная</Text>
      <Pressable
        style={styles.btn}
        onPress={() => navigation.navigate('Details', { taskId: '42' })}
      >
        <Text style={styles.btnText}>Открыть детали</Text>
      </Pressable>
    </View>
  );
}

function DetailsScreen({ route, navigation }) {
  const { taskId } = route.params;
  return (
    <View style={styles.center}>
      <Text>Задача #{taskId}</Text>
      <Pressable style={styles.btn} onPress={() => navigation.goBack()}>
        <Text style={styles.btnText}>Назад</Text>
      </Pressable>
    </View>
  );
}

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} options={{ title: 'Список' }} />
        <Stack.Screen name="Details" component={DetailsScreen} options={{ title: 'Детали' }} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  center: { flex: 1, alignItems: 'center', justifyContent: 'center', gap: 16 },
  h1: { fontSize: 22, fontWeight: '600' },
  btn: { backgroundColor: '#2563eb', paddingHorizontal: 20, paddingVertical: 12, borderRadius: 8 },
  btnText: { color: '#fff' },
});
