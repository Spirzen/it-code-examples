jlink \
  --module-path $JAVA_HOME/jmods:libs \
  --add-modules com.example.app,java.logging \
  --output runtime \
  --strip-debug \
  --compress 2

mkdir -p package/{app,bin}
cp app.jar package/app/
cp -r runtime/* package/bin/

jpackage \
  --type deb \
  --input package/app \
  --main-jar app.jar \
  --runtime-image package/bin \
  --name myapp \
  --app-version 1.0.0 \
  --vendor "Example" \
  --description "My App" \
  --linux-shortcut
