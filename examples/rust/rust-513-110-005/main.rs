use dioxus::prelude::*;

fn app(cx: Scope) -> Element {
    let mut count = use_state(cx, || 0);

    cx.render(rsx! {
        div {
            h1 { "Счётчик: {count}" }
            button { onclick: move |_| count += 1, "+" }
            button { onclick: move |_| count -= 1, "-" }
        }
    })
}

fn main() {
    dioxus::desktop::launch(app);
}
