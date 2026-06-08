require 'find'

def scan_dir(root, extensions = [])
  stats = { files: 0, bytes: 0 }
  Find.find(root) do |path|
    next unless File.file?(path)
    ext = File.extname(path)
    next if extensions.any? && !extensions.include?(ext)
    stats[:files] += 1
    stats[:bytes] += File.size(path)
  end
  stats
end

p scan_dir('.', ['.rb', '.md'])
