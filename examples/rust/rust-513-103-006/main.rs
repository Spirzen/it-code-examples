use std::fs;
use std::path::Path;

fn scan(dir: &Path, ext: &str) -> std::io::Result<(usize, u64)> {
    let mut files = 0usize;
    let mut bytes = 0u64;
    for entry in fs::read_dir(dir)? {
        let entry = entry?;
        let path = entry.path();
        if path.is_dir() {
            let (f, b) = scan(&path, ext)?;
            files += f;
            bytes += b;
        } else if path.extension().and_then(|e| e.to_str()) == Some(ext.trim_start_matches('.')) {
            files += 1;
            bytes += entry.metadata()?.len();
        }
    }
    Ok((files, bytes))
}
