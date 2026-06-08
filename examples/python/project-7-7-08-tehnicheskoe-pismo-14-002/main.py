  # ep_validator.py
  import subprocess
  import hashlib

  def verify_cades(pdf_path: str, expected_hash: str) -> bool:
      # Извлекаем подпись из PDF (BPM embedded)
      sig_data = extract_signature_from_pdf(pdf_path)
      # Сохраняем во временный .sig
      with open("temp.sig", "wb") as f:
          f.write(sig_data)
      # Проверяем через КриптоПро
      result = subprocess.run(
          ["cpverify", "-verify", "temp.sig", "-content", pdf_path],
          capture_output=True, text=True
      )
      return "Verified successfully" in result.stdout and \
             hashlib.sha256(open(pdf_path, 'rb').read()).hexdigest() == expected_hash
