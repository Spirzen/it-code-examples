
import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            Text("Привет, мир!")
                .font(.largeTitle)
                .padding()
            
            Button(action: {
                print("Кнопка нажата")
            }) {
                Text("Нажми меня")
                    .frame(width: 200, height: 50)
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
