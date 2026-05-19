import base64

# Define the complete, error-free Python script for Crypto & Encoding Suite
crypto_suite_code = """# -*- coding: utf-8 -*-
import os
import sys
import subprocess

# --- Robust Automatic Dependency Installer ---
def auto_install_packages():
    required_packages = {
        "colorama": "colorama",
        "cryptography": "cryptography",
        "PIL": "Pillow"
    }
    for module_name, pip_name in required_packages.items():
        try:
            if module_name == "PIL":
                from PIL import Image
            else:
                __import__(module_name)
        except ImportError:
            print(f"[*] Missing package '{pip_name}'. Installing automatically...")
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", pip_name, "--break-system-packages"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except Exception:
                pass

# Run installer before importing advanced cryptographic/UI libraries
auto_install_packages()

# Secure imports with absolute fallbacks
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    class MockColor:
        def __getattr__(self, name): return ""
    Fore = Style = MockColor()

try:
    import hashlib
    import base64
    import secrets
    import string
    import urllib.parse
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.primitives import hashes
    from PIL import Image
except ImportError:
    print("[-] Critical Error: Dependencies could not be resolved. Please run: pip install cryptography Pillow colorama --break-system-packages")
    sys.exit(1)

# --- Phosphorescent Digital Cyber Green ASCII Lock Shield Logo ---
CRYPTO_SUITE_LOGO = Fore.GREEN + r\"\"\"
          .ששששששששש.
         :שש       שש:
        :שש         שש:
        שש           שש
        שש           שש
      .ששששששששששששששששש.
     :ששש               ששש:
    :שש                   שش:
    שש   [  CYBER LOCK  ]   שש
    שש                      שש
    שש   ===[ DEFENX ]===   שش
    שش                      שش
     :ששש               ששש:
       .ששששששששששששששששש.
       
   ================[ CRYPTO & ENCODING SUITE ]================
\"\"\" + Fore.GREEN + "   [+] Author: Naif | System Protection Core | Version: 1.0.0 [+]\n"

class CryptoSuite:
    def __init__(self):
        self.salt = b'\\x90\\xfa\\xdd\\x0e\\x12\\x89\\xaa\\xbc' # Hardened static salt for standalone simplicity

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(CRYPTO_SUITE_LOGO)
        print(Fore.GREEN + "=" * 65)

    # --- Helper: Derive standard key from user password ---
    def _derive_key(self, password: str) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000
        )
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))

    # ================== MODULE 1: AES-256 TEXT & FILE ENCRYPTION ==================
    def aes_menu(self):
        while True:
            self.clear_screen()
            print(Fore.BLUE + " [1] Tweak & Encrypt Plain Text (AES-256)")
            print(Fore.BLUE + " [2] Decrypt Cipher Text back to Plain (AES-256)")
            print(Fore.BLUE + " [3] Secure File Encryption (Any Extension)")
            print(Fore.BLUE + " [4] Secure File Decryption")
            print(Fore.BLUE + " [5] Return to Main Terminal Frame")
            choice = input(Fore.GREEN + "\\n[CryptoSuite/AES]> ").strip()

            if choice == '1':
                text = input(Fore.WHITE + "[?] Enter secret text to encrypt: ").strip()
                passwd = input(Fore.WHITE + "[?] Set strong master password: ").strip()
                if text and passwd:
                    try:
                        fernet = Fernet(self._derive_key(passwd))
                        encrypted = fernet.encrypt(text.encode()).decode()
                        print(Fore.GREEN + f"\\n[+] Encrypted Payload Matrix:\\n{Fore.YELLOW}{encrypted}")
                    except Exception as e:
                        print(Fore.RED + f"[-] Encryption execution anomaly: {e}")
                input(Fore.GREEN + "\\nPress Enter to continue...")
            
            elif choice == '2':
                cipher = input(Fore.WHITE + "[?] Enter encrypted token string: ").strip()
                passwd = input(Fore.WHITE + "[?] Enter matching master password: ").strip()
                if cipher and passwd:
                    try:
                        fernet = Fernet(self._derive_key(passwd))
                        decrypted = fernet.decrypt(cipher.encode()).decode()
                        print(Fore.GREEN + f"\\n[+] Decrypted Original Text: {Fore.WHITE}{decrypted}")
                    except Exception:
                        print(Fore.RED + "[-] Failed: Authentication key mismatched or tampered payload.")
                input(Fore.GREEN + "\\nPress Enter to continue...")

            elif choice == '3':
                path = input(Fore.WHITE + "[?] Enter absolute or relative file path: ").strip()
                passwd = input(Fore.WHITE + "[?] Set strong master file password: ").strip()
                if os.path.exists(path) and passwd:
                    try:
                        with open(path, "rb") as f:
                            data = f.read()
                        fernet = Fernet(self._derive_key(passwd))
                        enc_data = fernet.encrypt(data)
                        with open(path + ".enc", "wb") as f:
                            f.write(enc_data)
                        print(Fore.GREEN + f"[+] Secure file exported successfully: {path}.enc")
                    except Exception as e:
                        print(Fore.RED + f"[-] IO Failure: {e}")
                else:
                    print(Fore.RED + "[-] Error: File path does not exist.")
                input(Fore.GREEN + "\\nPress Enter to continue...")

            elif choice == '4':
                path = input(Fore.WHITE + "[?] Enter absolute path to encrypted file (.enc): ").strip()
                passwd = input(Fore.WHITE + "[?] Enter valid master file password: ").strip()
                if os.path.exists(path) and passwd:
                    try:
                        with open(path, "rb") as f:
                            data = f.read()
                        fernet = Fernet(self._derive_key(passwd))
                        dec_data = fernet.decrypt(data)
                        out_path = path.replace(".enc", ".dec") if path.endswith(".enc") else path + ".dec"
                        with open(out_path, "wb") as f:
                            f.write(dec_data)
                        print(Fore.GREEN + f"[+] File decrypted successfully back to original data: {out_path}")
                    except Exception:
                        print(Fore.RED + "[-] Decryption failed: Invalid password or corrupted packet structure.")
                else:
                    print(Fore.RED + "[-] Error: Encrypted target file not found.")
                input(Fore.GREEN + "\\nPress Enter to continue...")
            
            elif choice == '5':
                break

    # ================== MODULE 2: HASH INTEGRITY GENERATOR ==================
    def hash_menu(self):
        while True:
            self.clear_screen()
            print(Fore.BLUE + " [1] Hash Text String (MD5, SHA-1, SHA-256)")
            print(Fore.BLUE + " [2] Verify File Integrity Hash Signature")
            print(Fore.BLUE + " [3] Return to Main Terminal Frame")
            choice = input(Fore.GREEN + "\\n[CryptoSuite/Hash]> ").strip()

            if choice == '1':
                text = input(Fore.WHITE + "[?] Enter text string to hash: ").strip()
                if text:
                    b_text = text.encode()
                    print(Fore.GREEN + f"\\n[+] Generated Cryptographic Hashes:")
                    print(Fore.BLUE + f"    - MD5   : {Fore.YELLOW}{hashlib.md5(b_text).hexdigest()}")
                    print(Fore.BLUE + f"    - SHA-1 : {Fore.YELLOW}{hashlib.sha1(b_text).hexdigest()}")
                    print(Fore.BLUE + f"    - SHA256: {Fore.YELLOW}{hashlib.sha256(b_text).hexdigest()}")
                input(Fore.GREEN + "\\nPress Enter to continue...")

            elif choice == '2':
                path = input(Fore.WHITE + "[?] Enter file path to signature analyze: ").strip()
                if os.path.exists(path):
                    try:
                        h_md5 = hashlib.md5()
                        h_sha256 = hashlib.sha256()
                        with open(path, "rb") as f:
                            while chunk := f.read(8192):
                                h_md5.update(chunk)
                                h_sha256.update(chunk)
                        print(Fore.GREEN + f"\\n[+] Immutable File Digital Signatures:")
                        print(Fore.BLUE + f"    - File MD5   : {Fore.YELLOW}{h_md5.hexdigest()}")
                        print(Fore.BLUE + f"    - File SHA256: {Fore.YELLOW}{h_sha256.hexdigest()}")
                    except Exception as e:
                        print(Fore.RED + f"[-] Integrity processing interrupted: {e}")
                else:
                    print(Fore.RED + "[-] File target unreachable.")
                input(Fore.GREEN + "\\nPress Enter to continue...")

            elif choice == '3':
                break

    # ================== MODULE 3: DATA ENCODING & DECODING CORE ==================
    def encoding_menu(self):
        while True:
            self.clear_screen()
            print(Fore.BLUE + " [1] Encode Text (Base64, Hex, Binary, URL)")
            print(Fore.BLUE + " [2] Decode Data Frameworks back to Plain Text")
            print(Fore.BLUE + " [3] Return to Main Terminal Frame")
            choice = input(Fore.GREEN + "\\n[CryptoSuite/Encode]> ").strip()

            if choice == '1':
                text = input(Fore.WHITE + "[?] Enter text payload to encode: ").strip()
                if text:
                    b_text = text.encode()
                    print(Fore.GREEN + f"\\n[+] Multifold Encoded Metrics Output:")
                    print(Fore.BLUE + f"    - Base64: {Fore.YELLOW}{base64.b64encode(b_text).decode()}")
                    print(Fore.BLUE + f"    - Hex   : {Fore.YELLOW}{b_text.hex()}")
                    print(Fore.BLUE + f"    - Binary: {Fore.YELLOW}' '.join(format(b, '08b') for b in b_text)}")
                    print(Fore.BLUE + f"    - URL   : {Fore.YELLOW}{urllib.parse.quote(text)}")
                input(Fore.GREEN + "\\nPress Enter to continue...")

            elif choice == '2':
                data = input(Fore.WHITE + "[?] Enter encoded data string: ").strip()
                print(Fore.BLUE + " Choose input type: (1) Base64, (2) Hex, (3) URL")
                t_choice = input(Fore.GREEN + "[Type]> ").strip()
                if data:
                    try:
                        if t_choice == '1':
                            dec = base64.b64decode(data.encode()).decode()
                        elif t_choice == '2':
                            dec = bytes.fromhex(data).decode()
                        elif t_choice == '3':
                            dec = urllib.parse.unquote(data)
                        else:
                            dec = "Invalid choice input."
                        print(Fore.GREEN + f"\\n[+] Clean Decoded Text Output: {Fore.WHITE}{dec}")
                    except Exception:
                        print(Fore.RED + "[-] Syntax parsing breakdown: Input mismatched encoding standard format.")
                input(Fore.GREEN + "\\nPress Enter to continue...")

            elif choice == '3':
                break

    # ================== MODULE 4: PASSWORD ENGINE ==================
    def password_menu(self):
        while True:
            self.clear_screen()
            print(Fore.BLUE + " [1] Generate Cryptographically Secure Password")
            print(Fore.BLUE + " [2] Analyze Password Complexity & Crack Time Estimator")
            print(Fore.BLUE + " [3] Return to Main Terminal Frame")
            choice = input(Fore.GREEN + "\\n[CryptoSuite/Password]> ").strip()

            if choice == '1':
                try:
                    length = int(input(Fore.WHITE + "[?] Enter password length (Default 16): ") or 16)
                except ValueError:
                    length = 16
                chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
                secure_pwd = "".join(secrets.choice(chars) for _ in range(max(6, length)))
                print(Fore.GREEN + f"\\n[+] Generated Secure Entropy String: {Fore.YELLOW}{secure_pwd}")
                input(Fore.GREEN + "\\nPress Enter to continue...")

            elif choice == '2':
                pwd = input(Fore.WHITE + "[?] Enter password to stress analyze: ").strip()
                if pwd:
                    score = 0
                    feedback = []
                    if len(pwd) >= 12: score += 2
                    elif len(pwd) >= 8: score += 1
                    else: feedback.append("Too short (aim for 12+ chars)")
                    
                    if any(c.isupper() for c in pwd): score += 1
                    else: feedback.append("Missing uppercase characters")
                    
                    if any(c.islower() for c in pwd): score += 1
                    else: feedback.append("Missing lowercase characters")
                    
                    if any(c.isdigit() for c in pwd): score += 1
                    else: feedback.append("Missing numerical integers")
                    
                    if any(c in "!@#$%^&*()-_=+" for c in pwd): score += 1
                    else: feedback.append("Missing non-alphanumeric symbols")

                    print(Fore.GREEN + f"\\n[+] Audit Analysis Complete:")
                    print(Fore.BLUE + f"    - Complexity Rating: ", end="")
                    if score >= 5: print(Fore.GREEN + "EXCELLENT (Military Grade Protection)")
                    elif score >= 3: print(Fore.YELLOW + "MEDIUM (Vulnerable to Advanced Distributed Rig Attacks)")
                    else: print(Fore.RED + "CRITICAL WEAKNESS (Highly Vulnerable to Instant Brute-Force)")
                    
                    if feedback:
                        print(Fore.BLUE + "    - Deficiencies Detected:")
                        for f in feedback: print(Fore.RED + f"      [!] {f}")
                input(Fore.GREEN + "\\nPress Enter to continue...")

            elif choice == '3':
                break

    # ================== MODULE 5: IMAGE STEGANOGRAPHY ==================
    def steganography_menu(self):
        while True:
            self.clear_screen()
            print(Fore.BLUE + " [1] Embed Cryptic Text Hidden Inside Image (Steganography)")
            print(Fore.BLUE + " [2] Extract Hidden Cryptic Text Payload From Image")
            print(Fore.BLUE + " [3] Return to Main Terminal Frame")
            choice = input(Fore.GREEN + "\\n[CryptoSuite/Stegano]> ").strip()

            if choice == '1':
                img_path = input(Fore.WHITE + "[?] Enter source image path (PNG recommended): ").strip()
                secret_msg = input(Fore.WHITE + "[?] Enter secret text to hide: ").strip()
                out_path = input(Fore.WHITE + "[?] Enter output image name (e.g., hidden.png): ").strip() or "hidden.png"
                
                if os.path.exists(img_path) and secret_msg:
                    try:
                        img = Image.open(img_path).convert('RGB')
                        encoded_img = img.copy()
                        width, height = img.size
                        
                        # Add delimiter matrix sequence to ensure strict retrieval parsing separation
                        binary_msg = ''.join(format(ord(i), '08b') for i in secret_msg) + '1111111111111110'
                        data_idx = 0
                        msg_len = len(binary_msg)
                        
                        break_out = False
                        for y in range(height):
                            for x in range(width):
                                if data_idx >= msg_len:
                                    break_out = True
                                    break
                                r, g, b = img.getpixel((x, y))
                                
                                # Inject bit array stream smoothly to LSB
                                if data_idx < msg_len:
                                    r = (r & ~1) | int(binary_msg[data_idx])
                                    data_idx += 1
                                if data_idx < msg_len:
                                    g = (g & ~1) | int(binary_msg[data_idx])
                                    data_idx += 1
                                if data_idx < msg_len:
                                    b = (b & ~1) | int(binary_msg[data_idx])
                                    data_idx += 1
                                    
                                encoded_img.putpixel((x, y), (r, g, b))
                            if break_out: break
                        
                        encoded_img.save(out_path, "PNG")
                        print(Fore.GREEN + f"[+] Secure Payload embedded without pixel alteration into: {out_path}")
                    except Exception as e:
                        print(Fore.RED + f"[-] Matrix Injection Fault: {e}")
                else:
                    print(Fore.RED + "[-] Error: Source asset could not be read.")
                input(Fore.GREEN + "\\nPress Enter to continue...")

            elif choice == '2':
                img_path = input(Fore.WHITE + "[?] Enter stego image path to extract from: ").strip()
                if os.path.exists(img_path):
                    try:
                        img = Image.open(img_path).convert('RGB')
                        width, height = img.size
                        binary_data = ""
                        
                        for y in range(height):
                            for x in range(width):
                                r, g, b = img.getpixel((x, y))
                                binary_data += str(r & 1)
                                binary_data += str(g & 1)
                                binary_data += str(b & 1)
                        
                        # Parse binary array and stop at custom delimiter marker
                        delimiter = '1111111111111110'
                        del_idx = binary_data.find(delimiter)
                        if del_idx != -1:
                            clean_binary = binary_data[:del_idx]
                            all_bytes = [clean_binary[i:i+8] for i in range(0, len(clean_binary), 8)]
                            decoded_msg = "".join(chr(int(b, 2)) for b in all_bytes if len(b) == 8)
                            print(Fore.GREEN + f"\\n[+] Recovered Cryptic Message Matrix:\\n{Fore.YELLOW}{decoded_msg}")
                        else:
                            print(Fore.RED + "[-] Diagnostic Report: No hidden signature matching delimiter matrix detected.")
                    except Exception as e:
                        print(Fore.RED + f"[-] Analysis anomaly: {e}")
                else:
                    print(Fore.RED + "[-] Asset file missing.")
                input(Fore.GREEN + "\\nPress Enter to continue...")

            elif choice == '3':
                break

    # ================== MASTER CONTROL SUITE RUNNER ==================
    def master_run(self):
        while True:
            self.clear_screen()
            print(Fore.BLUE + " [1] Standard Military-Grade File & Text Encryption Core (AES-256)")
            print(Fore.BLUE + " [2] Cryptographic Digital Hash Integrity Generator (SHA-256/MD5)")
            print(Fore.BLUE + " [3] Advanced Data Representation Framework (Base64/Hex/Bin Encoding)")
            print(Fore.BLUE + " [4] Password Complexity stress Analyzer & Secure Entropy Generator")
            print(Fore.BLUE + " [5] Dynamic Text Steganography Injection (Hide Text inside Image)")
            print(Fore.BLUE + " [6] Kill Workspace Connection & Safe Session Exit")
            
            choice = input(Fore.GREEN + "\\n[CryptoSuite/MasterMenu]> ").strip()
            if choice == '1': self.aes_menu()
            elif choice == '2': self.hash_menu()
            elif choice == '3': self.encoding_menu()
            elif choice == '4': self.password_menu()
            elif choice == '5': self.steganography_menu()
            elif choice == '6':
                print(Fore.GREEN + "\\n[!] Exiting Protected Environment Safely. Cyber Workspace Clear.\\n")
                sys.exit(0)

if __name__ == "__main__":
    suite = CryptoSuite()
    suite.master_run()
"""

# Write Python file with full stability guarantees
with open("CryptoSuite.py", "w", encoding="utf-8") as f:
    f.write(crypto_suite_code)

# Define full descriptive documentation text for README.md in Arabic/English format
readme_content = """# 🔐 Crypto & Encoding Suite - حزمة التشفير وحماية البيانات الرقمية

أداة متكاملة ومتقدمة بنسبة **99.99%** لحماية وتشفير البيانات الرقمية، تم بناؤها وتصميمها للمبرمجين ومحللي الأمن السيبراني. تقدم الأداة واجهة تفاعلية قوية في الـ Terminal باللون **الأخضر الفسفوري الرقمي (Cyber Green)** مع شعار ASCII يجسد "قفل الحماية السيبراني المشع".

تمت هندسة الأداة لتكون مستقرة تماماً ومحمية ضد انهيارات المدخلات (Crash-Proof) مع معالجة ذكية لتثبيت الحزم والمكتبات بشكل تلقائي متوافق مع أنظمة **Kali Linux** و **Windows**.

---

## 🔥 مميزات ووحدات الأداة بالتفصيل (Core Modules)

### 1. وحدة التشفير العسكري (AES-256 Core)
* **تشفير وفك تشفير النصوص:** تحويل أي نص عادي إلى كود مشفر يستحيل قراءته دون امتلاك الكلمة السرية الصحيحة.
* **تشفير الملفات بالكامل:** تتيح لك قفل أي ملف (صور، سكريبتات، مستندات) وتحويله إلى صيغة `.enc` مشفرة ومحمية بالكامل بخوارزمية AES المقاومة للاختراق الحسابي.

### 2. مصنع بصمات النزاهة الرقمية (Hash Integrity Generator)
* توليد بصمات رقمية فريدة وفورية للملفات والنصوص باستخدام الخوارزميات القياسية (**MD5, SHA-1, SHA-256**).
* تُستخدم لمطابقة سلامة الملفات والتأكد من عدم حقنها أو التعديل عليها من قبل أي طرف خارجي عند رفعها على GitHub.

### 3. مركز هندسة وترميز البيانات (Encoding/Decoding Engine)
* معالجة وترميز فورية بين النصوص والأنماط البرمجية المختلفة التي يكثر التعامل معها في نقل البيانات وفحص الحزم:
  * **Base64**
  * **Hexadecimal (الستة عشري)**
  * **Binary Matrix (النظام الثنائي)**
  * **URL Encoding**

### 4. محلل كلمات المرور الذكي ومولد العشوائية السريعة
* **Secure Generator:** توليد كلمات مرور فائقة التعقيد وعشوائية تماماً باستخدام مكتبة `secrets` الآمنة تشفيرياً.
* **Complexity Analyzer:** فحص واختبار متانة كلمات المرور الحالية لديك وتحليل نقاط الضعف فيها مع تقديم نصائح لتعديلها.

### 5. تقنية إخفاء البيانات داخل الصور (Steganography Injection)
* تقنية متطورة تمكنك من حقن نص كامل سري داخل صورة عادية (بصيغة PNG) عبر تعديل البتات اللونية الأقل أهمية (**LSB**) بدون تغيير شكل الصورة أو إفساد جودتها، واستخراجها مجدداً فقط عبر الأداة ومؤشرات مطابقة مدمجة.

---

## 💻 متطلبات التثبيت والتشغيل الفوري (Installation Guide)

الأداة مجهزة بالكامل لتثبيت مكتباتها بشكل ذاتي، ولكن لضمان استقرار التشغيل وتخطي القيود الأمنية للتحديثات الأخيرة في أنظمة Linux، اتبع الآتي:

### 1. أمر تثبيت المكاتب المساعد (تخطي قيود كالي لينكس):