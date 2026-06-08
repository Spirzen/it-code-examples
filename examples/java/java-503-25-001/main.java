> @Named
> @ViewScoped
> public class UserController implements Serializable {
>     @Inject private UserService userService;
>     
>     private String name;
>     private User user;
>
>     @PostConstruct
>     public void init() {
>         user = new User();
>     }
>
>     public String save() {
>         userService.persist(user);
>         return "profile?faces-redirect=true";
>     }
>
>     // геттеры/сеттеры
> }
> 