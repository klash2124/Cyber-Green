# -*- coding: utf-8 -*-
import os
import sys

# استيراد المكتبات الأساسية والتأكد من وجودها
try:
    from colorama import Fore, Style, init
    import hashlib
    import base64
    import secrets
    import string
    import urllib.parse
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.primitives import hashes
    from PIL import Image
    init(autoreset=True)
except ImportError as e:
    print("[-] خطأ في الاستيراد: المكاتب غير مثبتة بالكامل على نظامك.")
    print("[-] تفاصيل الخطأ:", e)
    print("[*] فضلاً نفذ الأمر التالي في التيرمنال أولاً للتثبيت:")
    print("pip3 install cryptography Pillow colorama --break-system-packages --force-reinstall")
    sys.exit(1)

# الشعار الفسفوري الرقمي الآمن
CRYPTO_SUITE_LOGO = Fore.GREEN + r"""
          .שששששששش.
         :שש      שש:
        :שש        שש:
        שش          שش
        שش          שش
      .ששששشששشششششششش.
     :שש                 שش:
    :שש                   שش:
    שش   [  CYBER LOCK  ]   שش
    שش                      שش
    שش   ===[ DEFENX ]===   שش
    שش                      שش
     :שש                 שش:
       .שששشששששششششششش.
       
   ================[ CRYPTO & ENCODING SUITE ]================
""" + Fore.GREEN + "   [+] Author: Naif | System Protection Core | Version: 1.0.0 [+]\n"

class CryptoSuite:
    def __init__(self):
        # ملح ثابت لعملية اشتقاق المفاتيح
        self.salt = b'\x90\xfa\xdd\x0e\x12\x89\xaa\xbc'

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(CRYPTO_SUITE_LOGO)
        print(Fore.GREEN + "=" * 65)

    def _derive_key(self, password: str) -> bytes:
        # اشتقاق مفتاح آمن متوافق مع Fernet (AES-256) من كلمة المرور
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000
        )
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))

    def aes_menu(self):
        while True:
            self.clear_screen()
            print(Fore.BLUE + " [1] تشفير نصوص عادية (AES-256)")
            print(Fore.BLUE + " [2] fك تشفير النصوص المشفرة")
            print(Fore.BLUE + " [3] تشفير ملف بالكامل (أي امتداد)")
            print(Fore.BLUE + " [4] فك تشفير ملف محمى")
            print(Fore.BLUE + " [5] العودة للقائمة الرئيسية")
            choice = input(Fore.GREEN + "\n[CryptoSuite/AES]> ").strip()

            if choice == '1':
                text = input(Fore.WHITE + "[?] أدخل النص السري لتشفيره: ").strip()
                passwd = input(Fore.WHITE + "[?] حدد كلمة مرور قوية للتشفير: ").strip()
                if text and passwd:
                    try:
                        fernet = Fernet(self._derive_key(passwd))
                        encrypted = fernet.encrypt(text.encode()).decode()
                        print(Fore.GREEN + f"\n[+] البيانات المشفرة الناتجة:\n{Fore.YELLOW}{encrypted}")
                    except Exception as e:
                        print(Fore.RED + f"[-] فشلت العملية: {e}")
                input(Fore.GREEN + "\nاضغط Enter للمتابعة...")
            
            elif choice == '2':
                cipher = input(Fore.WHITE + "[?] أدخل النص المشفر (الكود): ").strip()
                passwd = input(Fore.WHITE + "[?] أدخل كلمة المرور المطابقة: ").strip()
                if cipher and passwd:
                    try:
                        fernet = Fernet(self._derive_key(passwd))
                        decrypted = fernet.decrypt(cipher.encode()).decode()
                        print(Fore.GREEN + f"\n[+] النص الأصلي بعد فك التشفير: {Fore.WHITE}{decrypted}")
                    except Exception:
                        print(Fore.RED + "[-] فشل: كلمة المرور خاطئة أو البيانات تم التلاعب بها.")
                input(Fore.GREEN + "\nاضغط Enter للمتابعة...")

            elif choice == '3':
                path = input(Fore.WHITE + "[?] أدخل مسار الملف المراد قفله: ").strip()
                passwd = input(Fore.WHITE + "[?] حدد كلمة مرور حماية الملف: ").strip()
                if os.path.exists(path) and passwd:
                    try:
                        with open(path, "rb") as f:
                            data = f.read()
                        fernet = Fernet(self._derive_key(passwd))
                        enc_data = fernet.encrypt(data)
                        with open(path + ".enc", "wb") as f:
                            f.write(enc_data)
                        print(Fore.GREEN + f"[+] تم تشفير وتصدير الملف المحمي بنجاح باسم: {path}.enc")
                    except Exception as e:
                        print(Fore.RED + f"[-] خطأ في معالجة الملف: {e}")
                else:
                    print(Fore.RED + "[-] خطأ: مسار الملف غير صحيح أو غير موجود.")
                input(Fore.GREEN + "\nاضغط Enter للمتابعة...")

            elif choice == '4':
                path = input(Fore.WHITE + "[?] أدخل مسار الملف المشفر (.enc): ").strip()
                passwd = input(Fore.WHITE + "[?] أدخل كلمة مرور فك القفل: ").strip()
                if os.path.exists(path) and passwd:
                    try:
                        with open(path, "rb") as f:
                            data = f.read()
                        fernet = Fernet(self._derive_key(passwd))
                        dec_data = fernet.decrypt(data)
                        out_path = path.replace(".enc", ".dec") if path.endswith(".enc") else path + ".dec"
                        with open(out_path, "wb") as f:
                            f.write(dec_data)
                        print(Fore.GREEN + f"[+] تم فك قفل واستعادة الملف بنجاح باسم: {out_path}")
                    except Exception:
                        print(Fore.RED + "[-] فشل: كلمة المرور خاطئة أو هيكل الملف تالف.")
                else:
                    print(Fore.RED + "[-] خطأ: لم يتم العثور على الملف المشفر المستهدف.")
                input(Fore.GREEN + "\nاضغط Enter للمتابعة...")
            
            elif choice == '5':
                break

    def hash_menu(self):
        while True:
            self.clear_screen()
            print(Fore.BLUE + " [1] توليد الهاش (Hash) لنص معين")
            print(Fore.BLUE + " [2] استخراج وتحليل بصمة ملف (النزاهة)")
            print(Fore.BLUE + " [3] العودة للقائمة الرئيسية")
            choice = input(Fore.GREEN + "\n[CryptoSuite/Hash]> ").strip()

            if choice == '1':
                text = input(Fore.WHITE + "[?] أدخل النص لتوليد البصمات: ").strip()
                if text:
                    b_text = text.encode()
                    print(Fore.GREEN + f"\n[+] البصمات الرقمية المولدة:")
                    print(Fore.BLUE + f"    - MD5   : {Fore.YELLOW}{hashlib.md5(b_text).hexdigest()}")
                    print(Fore.BLUE + f"    - SHA-1 : {Fore.YELLOW}{hashlib.sha1(b_text).hexdigest()}")
                    print(Fore.BLUE + f"    - SHA256: {Fore.YELLOW}{hashlib.sha256(b_text).hexdigest()}")
                input(Fore.GREEN + "\nاضغط Enter للمتابعة...")

            elif choice == '2':
                path = input(Fore.WHITE + "[?] أدخل مسار الملف لاستخراج بصمته: ").strip()
                if os.path.exists(path):
                    try:
                        h_md5 = hashlib.md5()
                        h_sha256 = hashlib.sha256()
                        with open(path, "rb") as f:
                            while chunk := f.read(8192):
                                h_md5.update(chunk)
                                h_sha256.update(chunk)
                        print(Fore.GREEN + f"\n[+] البصمات الرقمية الثابتة للملف:")
                        print(Fore.BLUE + f"    - File MD5   : {Fore.YELLOW}{h_md5.hexdigest()}")
                        print(Fore.BLUE + f"    - File SHA256: {Fore.YELLOW}{h_sha256.hexdigest()}")
                    except Exception as e:
                        print(Fore.RED + f"[-] حدث خطأ أثناء المعالجة: {e}")
                else:
                    print(Fore.RED + "[-] خطأ: لم يتم العثور على الملف المطلوب.")
                input(Fore.GREEN + "\nاضغط Enter للمتابعة...")

            elif choice == '3':
                break

    def encoding_menu(self):
        while True:
            self.clear_screen()
            print(Fore.BLUE + " [1] ترميز وتحويل نص (Base64, Hex, Binary, URL)")
            print(Fore.BLUE + " [2] فك الترميز والعودة إلى النص المقروء")
            print(Fore.BLUE + " [3] العودة للقائمة الرئيسية")
            choice = input(Fore.GREEN + "\n[CryptoSuite/Encode]> ").strip()

            if choice == '1':
                text = input(Fore.WHITE + "[?] أدخل النص لتحويل ترميزه: ").strip()
                if text:
                    b_text = text.encode()
                    print(Fore.GREEN + f"\n[+] نواتج التحويل للأنظمة البرمجية المختلفة:")
                    print(Fore.BLUE + f"    - Base64: {Fore.YELLOW}{base64.b64encode(b_text).decode()}")
                    print(Fore.BLUE + f"    - Hex   : {Fore.YELLOW}{b_text.hex()}")
                    print(Fore.BLUE + f"    - Binary: {Fore.YELLOW}" + " ".join(f"{byte:08b}" for byte in b_text))
                    print(Fore.BLUE + f"    - URL   : {Fore.YELLOW}{urllib.parse.quote(text)}")
                input(Fore.GREEN + "\nاضغط Enter للمتابعة...")

            elif choice == '2':
                data = input(Fore.WHITE + "[?] أدخل الكود/النص المرمز المراد فكه: ").strip()
                print(Fore.BLUE + " اختر نوع الترميز المدخل: (1) Base64, (2) Hex, (3) URL")
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
                            dec = "اختيار غير صحيح."
                        print(Fore.GREEN + f"\n[+] النص المفكوك والجاهز للقراءة: {Fore.WHITE}{dec}")
                    except Exception:
                        print(Fore.RED + "[-] خطأ في الهيكلة: المدخلات لا تطابق معايير هذا الترميز.")
                input(Fore.GREEN + "\nاضغط Enter للمتابعة...")

            elif choice == '3':
                break

    def password_menu(self):
        while True:
            self.clear_screen()
            print(Fore.BLUE + " [1] توليد كلمة مرور معقدة وآمنة تشفيرياً")
            print(Fore.BLUE + " [2] فحص متانة كلمة المرور الحالية وتحليلها")
            print(Fore.BLUE + " [3] العودة للقائمة الرئيسية")
            choice = input(Fore.GREEN + "\n[CryptoSuite/Password]> ").strip()

            if choice == '1':
                try:
                    length = int(input(Fore.WHITE + "[?] حدد طول كلمة المرور (الافتراضي 16 حرف): ") or 16)
                except ValueError:
                    length = 16
                chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
                secure_pwd = "".join(secrets.choice(chars) for _ in range(max(6, length)))
                print(Fore.GREEN + f"\n[+] كلمة المرور العشوائية المولدة بأمان: {Fore.YELLOW}{secure_pwd}")
                input(Fore.GREEN + "\nاضغط Enter للمتابعة...")

            elif choice == '2':
                pwd = input(Fore.WHITE + "[?] أدخل كلمة المرور المراد فحصها: ").strip()
                if pwd:
                    score = 0
                    feedback = []
                    if len(pwd) >= 12: score += 2
                    elif len(pwd) >= 8: score += 1
                    else: feedback.append("قصير جداً (يُفضل أن تكون 12 خانة أو أكثر)")
                    
                    if any(c.isupper() for c in pwd): score += 1
                    else: feedback.append("تفتقد للأحرف الكبيرة (Uppercase)")
                    
                    if any(c.islower() for c in pwd): score += 1
                    else: feedback.append("تفتقد للأحرف الصغيرة (Lowercase)")
                    
                    if any(c.isdigit() for c in pwd): score += 1
                    else: feedback.append("تفتقد للأرقام والرموز العددية")
                    
                    if any(c in "!@#$%^&*()-_=+" for c in pwd): score += 1
                    else: feedback.append("تفتقد للرموز والرموز الخاصة المشفرة")

                    print(Fore.GREEN + f"\n[+] تقرير التحليل والتدقيق الأمني:")
                    print(Fore.BLUE + f"    - مستوى القوة: ", end="")
                    if score >= 5: print(Fore.GREEN + "ممتاز (حماية على مستوى عسكري ومقاومة للتخمين)")
                    elif score >= 3: print(Fore.YELLOW + "متوسطة (قابلة للكسر عن طريق كروت الشاشة الموزعة الكبيرة)")
                    else: print(Fore.RED + "ضعيفة جداً (سهلة الاختراق الفوري وعبر هجمات القوة العنيفة)")
                    
                    if feedback:
                        print(Fore.BLUE + "    - الثغرات المكتشفة في كلمة المرور:")
                        for f in feedback: print(Fore.RED + f"      [!] {f}")
                input(Fore.GREEN + "\nاضغط Enter للمتابعة...")

            elif choice == '3':
                break

    def steganography_menu(self):
        while True:
            self.clear_screen()
            print(Fore.BLUE + " [1] حقن وإخفاء نص سري داخل صورة (Steganography)")
            print(Fore.BLUE + " [2] استخراج النص المخفي من الصورة")
            print(Fore.BLUE + " [3] العودة للقائمة الرئيسية")
            choice = input(Fore.GREEN + "\n[CryptoSuite/Stegano]> ").strip()

            if choice == '1':
                img_path = input(Fore.WHITE + "[?] أدخل مسار الصورة المصدر (يُفضل PNG): ").strip()
                secret_msg = input(Fore.WHITE + "[?] أدخل الرسالة المراد كتمها داخل الصورة: ").strip()
                out_path = input(Fore.WHITE + "[?] حدد اسم الصورة الجديدة الناتجة (مثال secret.png): ").strip() or "secret.png"
                
                if os.path.exists(img_path) and secret_msg:
                    try:
                        img = Image.open(img_path).convert('RGB')
                        encoded_img = img.copy()
                        width, height = img.size
                        
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
                        print(Fore.GREEN + f"[+] تم حقن الرسالة بنجاح دون إفساد بكسلات الصورة وتم الحفظ باسم: {out_path}")
                    except Exception as e:
                        print(Fore.RED + f"[-] خطأ أثناء حقن الصورة: {e}")
                else:
                    print(Fore.RED + "[-] خطأ: الملف المصدر غير موجود أو لم يتم كتابة رسالة.")
                input(Fore.GREEN + "\nاضغط Enter للمتابعة...")

            elif choice == '2':
                img_path = input(Fore.WHITE + "[?] أدخل مسار الصورة لاستخراج البيانات منها: ").strip()
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
                        
                        delimiter = '1111111111111110'
                        del_idx = binary_data.find(delimiter)
                        if del_idx != -1:
                            clean_binary = binary_data[:del_idx]
                            all_bytes = [clean_binary[i:i+8] for i in range(0, len(clean_binary), 8)]
                            decoded_msg = "".join(chr(int(b, 2)) for b in all_bytes if len(b) == 8)
                            print(Fore.GREEN + f"\n[+] تم استخراج النص السري من الصورة بنجاح:\n{Fore.YELLOW}{decoded_msg}")
                        else:
                            print(Fore.RED + "[-] تقرير الفحص: لم يتم العثور على أي بيانات مشفرة أو مخفية في هذه الصورة.")
                    except Exception as e:
                        print(Fore.RED + f"[-] فشل فحص الصورة: {e}")
                else:
                    print(Fore.RED + "[-] خطأ: الصورة غير موجودة في هذا المسار.")
                input(Fore.GREEN + "\nاضغط Enter للمتابعة...")

            elif choice == '3':
                break

    def master_run(self):
        while True:
            self.clear_screen()
            print(Fore.BLUE + " [1] وحدة التشفير العسكري المتناظر للنصوص والملفات (AES-256)")
            print(Fore.BLUE + " [2] مصنع بصمات النزاهة والتحقق الرقمي (Hash Generator)")
            print(Fore.BLUE + " [3] centre ترميز البيانات والتحويل السريع (Base64 / Hex / Binary)")
            print(Fore.BLUE + " [4] مولد ومحلل متانة كلمات المرور العشوائية والآمنة")
            print(Fore.BLUE + " [5] تقنية إخفاء وحقن النصوص داخل عمق بكسلات الصور (Steganography)")
            print(Fore.BLUE + " [6] إغلاق الجلسة والخروج الآمن من بيئة التشفير")
            
            choice = input(Fore.GREEN + "\n[CryptoSuite/MasterMenu]> ").strip()
            if choice == '1': self.aes_menu()
            elif choice == '2': self.hash_menu()
            elif choice == '3': self.encoding_menu()
            elif choice == '4': self.password_menu()
            elif choice == '5': self.steganography_menu()
            elif choice == '6':
                print(Fore.GREEN + "\n[!] تم إغلاق الجلسة بأمان يا نايف. في أمان الله.\n")
                sys.exit(0)

if __name__ == "__main__":
    suite = CryptoSuite()
    suite.master_run()