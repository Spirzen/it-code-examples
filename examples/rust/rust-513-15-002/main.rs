use clap::Parser;

#[derive(Parser)]
#[command(name = "kb-tool", about = "Rust CLI example")]
struct Cli {
    /// Путь к входному файлу
    #[arg(short, long)]
    input: String,

    /// Включить подробный вывод
    #[arg(short, long)]
    verbose: bool,
}

fn main() {
    let args = Cli::parse();
    if args.verbose {
        println!("reading {}", args.input);
    }
}
