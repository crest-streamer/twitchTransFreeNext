import os
import sys
import subprocess
import shutil

def get_version():
    try:
        # UTF-8エンコーディングでファイルを読み込む
        with open("twitchTransFN.py", "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("version ="):
                    return line.split("'")[1]
    except UnicodeDecodeError:
        # UTF-8で読み込めない場合は、他のエンコーディングを試す
        try:
            with open("twitchTransFN.py", "r", encoding="shift-jis") as f:
                for line in f:
                    if line.startswith("version ="):
                        return line.split("'")[1]
        except Exception as e:
            print(f"Error reading file with shift-jis encoding: {e}")
    except Exception as e:
        print(f"Error reading file: {e}")
    
    # バージョン情報が取得できない場合は、環境変数から取得を試みる
    if "VERSION" in os.environ:
        return os.environ["VERSION"]
    
    return "unknown"

def build_for_os(os_name, arch, add_data_option):
    version = get_version()
    print(f"Building for {os_name} ({arch})...")
    
    # distフォルダを削除
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    
    # 必要なモジュールを明示的に指定
    include_modules = [
        "--include-package=async_google_trans_new",  # AsyncTranslatorとconstant用
        "--include-package=gtts",                    # gTTS用
        "--include-package=playsound",               # playsound用（macOSでは代替手段あり）
        "--include-package=deepl",                   # deepl用
        "--include-package=twitchio",                # twitchio用
        "--include-package=emoji",                   # emoji用
        "--include-module=tts",                      # カスタムモジュール
        "--include-module=sound",                    # カスタムモジュール
        "--include-module=database_controller",      # カスタムモジュール
    ]

    # Windowsの場合、pywin32を追加
    if os_name == "windows":
        include_modules.append("--include-module=win32api")
        include_modules.append("--include-module=win32con")
        include_modules.append("--include-module=win32com.client")
        include_modules.append("--include-module=pythoncom")

    # macOSの場合、AppKitを試す（必要に応じて）
    if os_name == "macos":
        os.environ["CC"] = "/usr/bin/clang"
        os.environ["CXX"] = "/usr/bin/clang++"
        #include_modules.append("--include-module=AppKit")

    # コマンド構築
    if os_name == "windows":
        command = [
            sys.executable,
            "-m", "nuitka",
            "--standalone",
            "--onefile",
            "--output-dir=dist",
            "--assume-yes-for-downloads",
            "--windows-icon-from-ico=icon.ico",
            add_data_option,
        ] + include_modules + ["twitchTransFN.py"]
    elif os_name == "macos":
        if arch == "arm64":
            command = [
                "nuitka",
                "--standalone",
                "--onefile",
                "--output-dir=dist",
                "--macos-app-icon=icon.icns",
                add_data_option,
            ] + include_modules + ["twitchTransFN.py"]
        elif arch == "x86_64":
            command = [
                "nuitka",
                "--standalone",
                "--onefile",
                "--output-dir=dist",
                "--macos-app-icon=icon.icns",
                "--macos-create-app-bundle",
                add_data_option,
            ] + include_modules + ["twitchTransFN.py"]
    elif os_name == "linux":
        command = [
            "nuitka",
            "--standalone",
            "--onefile",
            "--output-dir=dist",
            "--linux-icon=icon.ico",
            add_data_option,
        ] + include_modules + ["twitchTransFN.py"]
    
    print("Running command:", " ".join(command))
    subprocess.run(command, check=True)

    # ファイル名の変更
    if os_name == "windows":
        os.rename("dist/twitchTransFN.exe", f"dist/twitchTransFN_{version}_win.exe")
    elif os_name == "linux":
        os.rename("dist/twitchTransFN", f"dist/twitchTransFN_{version}_linux")
    elif os_name == "macos":
        if arch == "arm64":
            os.rename("dist/twitchTransFN", f"dist/twitchTransFN_{version}_macos_M1.command")
        elif arch == "x86_64":
            os.rename("dist/twitchTransFN", f"dist/twitchTransFN_{version}_macos_Intel.command")

    print(f"Build for {os_name} ({arch}) completed.")

def main(target_os):
    # cacert.pemが存在することを確認
    if not os.path.exists("cacert.pem"):
        print("Error: cacert.pem not found. Downloading...")
        try:
            import urllib.request
            urllib.request.urlretrieve("https://curl.se/ca/cacert.pem", "cacert.pem")
            print("cacert.pem downloaded successfully.")
        except Exception as e:
            print(f"Failed to download cacert.pem: {e}")
            return

    # distフォルダの準備
    if not os.path.exists("dist"):
        os.makedirs("dist")

    # 各OS向けにビルド
    if target_os == "windows":
        build_for_os("windows", "", "--include-data-file=cacert.pem=cacert.pem")
    elif target_os == "linux":
        build_for_os("linux", "", "--include-data-file=cacert.pem=cacert.pem")
    elif target_os == "macos_M1" or target_os == "macos_Intel":
        add_data_option = "--include-data-file=cacert.pem=cacert.pem"
        if target_os == "macos_M1":
            build_for_os("macos", "arm64", add_data_option)
        else:
            build_for_os("macos", "x86_64", add_data_option)

    print("Build process completed.")

if __name__ == "__main__":
    main(sys.argv[1])
