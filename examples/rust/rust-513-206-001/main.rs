use eframe::egui;

fn main() -> eframe::Result<()> {
    eframe::run_native(
        "Demo",
        Default::default(),
        Box::new(|_cc| Ok(Box::new(MyApp { clicks: 0 }))),
    )
}

struct MyApp {
    clicks: u32,
}

impl eframe::App for MyApp {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            if ui.button("Нажми").clicked() {
                self.clicks += 1;
            }
            ui.label(format!("Счётчик: {}", self.clicks));
        });
    }
}
