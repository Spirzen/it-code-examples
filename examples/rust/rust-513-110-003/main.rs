use iced::{Application, Settings, Element, Command};

#[derive(Default)]
struct Counter {
    value: i32,
}

#[derive(Debug, Clone)]
enum Message {
    IncrementPressed,
    DecrementPressed,
}

impl Application for Counter {
    type Executor = iced::executor::Default;
    type Message = Message;
    type Flags = ();

    fn new(_flags: ()) -> (Self, Command<Message>) {
        (Counter::default(), Command::none())
    }

    fn title(&self) -> String {
        String::from("Счётчик")
    }

    fn update(&mut self, message: Message) -> Command<Message> {
        match message {
            Message::IncrementPressed => self.value += 1,
            Message::DecrementPressed => self.value -= 1,
        }
        Command::none()
    }

    fn view(&self) -> Element<Message> {
        use iced::widget::{column, button, text};
        column![
            button("+").on_press(Message::IncrementPressed),
            text(self.value).size(50),
            button("-").on_press(Message::DecrementPressed)
        ]
        .into()
    }
}

fn main() -> iced::Result {
    Counter::run(Settings::default())
}
