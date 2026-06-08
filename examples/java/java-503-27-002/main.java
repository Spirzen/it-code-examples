  @Component
  public class LoggingBeanPostProcessor implements BeanPostProcessor {
      @Override
      public Object postProcessAfterInitialization(Object bean, String beanName) {
          if (bean.getClass().isAnnotationPresent(Loggable.class)) {
              return Proxy.newProxyInstance(
                  bean.getClass().getClassLoader(),
                  bean.getClass().getInterfaces(),
                  (proxy, method, args) -> {
                      log.info("Calling {} with {}", method.getName(), args);
                      return method.invoke(bean, args);
                  }
              );
          }
          return bean;
      }
  }
