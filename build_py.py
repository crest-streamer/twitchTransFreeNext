import os
import sys
import subprocess
import shutil
import zipfile

def get_version():
    try:
        with open("twitchTransFN.py", "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("version ="):
                    return line.split("'")[1]
    except UnicodeDecodeError:
        try:
            with open("twitchTransFN.py", "r", encoding="shift-jis") as f:
                for line in f:
                    if line.startswith("version ="):
                        return line.split("'")[1]
        except Exception as e:
            print(f"Error reading file with shift-jis encoding: {e}")
    except Exception as e:
        print(f"Error reading file: {e}")
    
    if "VERSION" in os.environ:
        return os.environ["VERSION"]
    
    return "unknown"

def build_for_os(os_name, arch, add_data_option):
    version = get_version()
    print(f"Building for {os_name} ({arch})...")

    if os.path.exists("dist"):
        shutil.rmtree("dist")
    
    include_modules = [
        "--include-package=async_google_trans_new",
        "--include-package=gtts",
        "--include-package=playsound",
        "--include-package=deepl",
        "--include-package=twitchio",
        "--include-package=emoji",
        "--include-module=tts",
        "--include-module=sound",
        "--include-module=database_controller",
    ]

    if os_name == "windows":
        include_modules += [
            "--include-module=win32api",
            "--include-module=win32con",
            "--include-module=win32com.client",
            "--include-module=pythoncom",
        ]
        command = [
            sys.executable, "-m", "nuitka",
            "--standalone", "--onefile",
            "--output-filename=twitchTransFN.exe",
            "--nofollow-import-to=config",
            "--output-dir=dist",
            "--assume-yes-for-downloads",
            "--disable-ccache",
            "--windows-icon-from-ico=icon.ico",
            "--include-data-file=cacert.pem=cacert.pem",
        ] + include_modules + ["twitchTransFN.py"]
    else:
        command = [
            "pyinstaller",
            "--onefile",
            "--icon=icon.ico",
            "--runtime-tmpdir=.",
            add_data_option,
            "twitchTransFN.py",
        ]

    subprocess.run(command, check=True)

    if os_name == "windows":
        output_name = f"twitchTransFN_{version}_win.exe"
        shutil.move("dist/twitchTransFN.exe", f"dist/{output_name}")
    elif os_name == "linux":
        output_name = f"twitchTransFN_{version}_linux"
        shutil.move("dist/twitchTransFN", f"dist/{output_name}")
    elif os_name == "macos":
        suffix = "macos_M1" if arch == "arm64" else "macos_Intel"
        output_name = f"twitchTransFN_{version}_{suffix}.command"
        shutil.move("dist/twitchTransFN", f"dist/{output_name}")

    create_zip_archive(version, output_name)
    print(f"Build for {os_name} ({arch}) completed.")

def create_zip_archive(version, filename):
    zip_name = f"twitchTransFN_{version}_{filename.split('_')[-1].replace('.exe','').replace('.command','')}.zip"
    zip_path = os.path.join("dist", zip_name)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(os.path.join("dist", filename), filename)
        if os.path.exists("config.py"):
            zipf.write("config.py", "config.py")
    print(f"Archive created: {zip_name}")

def main(target_os):
    if not os.path.exists("cacert.pem"):
        print("cacert.pem not found. Downloading...")
        try:
            import urllib.request
            urllib.request.urlretrieve("https://curl.se/ca/cacert.pem", "cacert.pem")
            print("cacert.pem downloaded.")
        except Exception as e:
            print(f"Failed to download cacert.pem: {e}")
            return

    if not os.path.exists("dist"):
        os.makedirs("dist")

    if target_os == "windows":
        build_for_os("windows", "", "")
    elif target_os == "linux":
        build_for_os("linux", "", "--add-data=cacert.pem:.")
    elif target_os == "macos_M1":
        build_for_os("macos", "arm64", "--add-data=cacert.pem:.")
    elif target_os == "macos_Intel":
        build_for_os("macos", "x86_64", "--add-data=cacert.pem:.")
    else:
        print("Invalid target_os. Choose: windows | linux | macos_M1 | macos_Intel")
        return

    print("Build process completed.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python build.py [windows|linux|macos_M1|macos_Intel]")
    else:
        main(sys.argv[1])
