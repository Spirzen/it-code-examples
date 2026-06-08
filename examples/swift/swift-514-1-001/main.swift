   @propertyWrapper
   struct UserDefault<T> {
       let key: String
       let defaultValue: T
       init(key: String, default defaultValue: T) {
           self.key = key
           self.defaultValue = defaultValue
       }
       var wrappedValue: T {
           get { UserDefaults.standard.value(forKey: key) as? T ?? defaultValue }
           set { UserDefaults.standard.setValue(newValue, forKey: key) }
       }
   }

   class Settings {
       @UserDefault(key: "theme", default: "light") var theme: String
   }
