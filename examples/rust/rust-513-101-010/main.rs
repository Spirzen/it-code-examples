trait State {
    fn handle(&self, context: &mut Context) -> Result<(), Error>;
}

struct DraftState;
struct PublishedState;

impl State for DraftState {
    fn handle(&self, context: &mut Context) -> Result<(), Error> {
        // логика для черновика
        context.state = Box::new(PublishedState);
        Ok(())
    }
}

struct Context {
    state: Box<dyn State>,
}

impl Context {
    fn request(&mut self) -> Result<(), Error> {
        self.state.handle(self)
    }
}
