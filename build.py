import os
import sys
import subprocess
import shutil

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
        "--nofollow-import-to=config",
        "--include-package=twitchio",
        "--include-package=emoji",
        "--include-module=tts",
        "--include-module=sound",
        "--include-module=database_controller",
    ]

    if os_name == "windows":
        include_modules.append("--include-module=win32api")
        include_modules.append("--include-module=win32con")
        include_modules.append("--include-module=win32com.client")
        include_modules.append("--include-module=pythoncom")

    if os_name == "macos":
        os.environ["CC"] = "/usr/bin/clang"
        os.environ["CXX"] = "/usr/bin/clang++"
        include_modules.append("--include-module=AppKit")

    if os_name == "windows":
        command = [
            sys.executable,
            "-m", "nuitka",
            "--standalone",
            "--onefile",
            "--output-filename=twitchTransFN.exe",
            "--nofollow-import-to=config",
            "--output-dir=dist",
            "--assume-yes-for-downloads",
            "--disable-ccache",
            "--windows-icon-from-ico=icon.ico",
            add_data_option,
        ] + include_modules + ["twitchTransFN.py"]
    elif os_name == "macos":
        if arch == "arm64":
            command = [
                "nuitka",
                "--standalone",
                "--onefile",
                "--output-filename=twitchTransFN",
                "--macos-create-app-bundle",
                "--nofollow-import-to=config",
                "--output-dir=dist",
                "--disable-ccache",
                "--macos-app-icon=icon.icns",
                add_data_option,
            ] + include_modules + ["twitchTransFN.py"]
        elif arch == "x86_64":
            command = [
                "nuitka",
                "--standalone",
                "--onefile",
                "--output-filename=twitchTransFN",
                "--macos-create-app-bundle",
                "--nofollow-import-to=config",
                "--output-dir=dist",
                "--disable-ccache",
                "--macos-app-icon=icon.icns",
                "--macos-create-app-bundle",
                add_data_option,
            ] + include_modules + ["twitchTransFN.py"]
    elif os_name == "linux":
        command = [
            "nuitka",
            "--standalone",
            "--onefile",
            "--output-filename=twitchTransFN.bin",
            "--nofollow-import-to=config",
            "--output-dir=dist",
            "--disable-ccache",
            "--linux-icon=icon.ico",
            add_data_option,
        ] + include_modules + ["twitchTransFN.py"]

    print("Running command:", " ".join(command))
    subprocess.run(command, check=True)

    if os_name == "windows":
        os.rename("dist/twitchTransFN.exe", f"dist/twitchTransFN_{version}_win.exe")
    elif os_name == "linux":
        os.rename("dist/twitchTransFN.bin", f"dist/twitchTransFN_{version}_linux")
    elif os_name == "macos":
        if arch == "arm64":
            os.rename("dist/twitchTransFN", f"dist/twitchTransFN_{version}_macos_M1.app")
        elif arch == "x86_64":
            os.rename("dist/twitchTransFN", f"dist/twitchTransFN_{version}_macos_Intel.app")

    archive_name = None
    output_name = None

    if os_name == "windows":
        output_name = f"twitchTransFN_{version}_win.exe"
        archive_name = f"twitchTransFN_{version}_win.zip"
        shutil.copy("config.py", "dist/config.py")
        shutil.make_archive(archive_name.replace(".zip", ""), 'zip', root_dir="dist", base_dir=".")
    elif os_name == "linux":
        output_name = f"twitchTransFN_{version}_linux"
        archive_name = f"twitchTransFN_{version}_linux.tar.gz"
        shutil.copy("config.py", "dist/config.py")
        subprocess.run(["tar", "-czvf", f"dist/{archive_name}", "-C", "dist", output_name, "config.py"], check=True)
    elif os_name == "macos":
        if arch == "arm64":
            output_name = f"twitchTransFN_{version}_macos_M1.app"
            archive_name = f"twitchTransFN_{version}_macos_M1.tar.gz"
        elif arch == "x86_64":
            output_name = f"twitchTransFN_{version}_macos_Intel.app"
            archive_name = f"twitchTransFN_{version}_macos_Intel.tar.gz"
        shutil.copy("config.py", "dist/config.py")
        subprocess.run(["tar", "-czvf", f"dist/{archive_name}", "-C", "dist", output_name, "config.py"], check=True)

    print(f"Build for {os_name} ({arch}) completed.")

    # 成果物と config.py をリリースディレクトリに移動
    release_dir = "release"
    if not os.path.exists(release_dir):
        os.makedirs(release_dir)

    #shutil.move(f"dist/{output_name}", f"{release_dir}/{output_name}")
    shutil.move(f"dist/config.py", f"{release_dir}/config.py")

    if archive_name:
        shutil.move(f"dist/{archive_name}", f"{release_dir}/{archive_name}")

def main(target_os):
    if not os.path.exists("cacert.pem"):
        print("Error: cacert.pem not found. Downloading...")
        try:
            import urllib.request
            urllib.request.urlretrieve("https://curl.se/ca/cacert.pem", "cacert.pem")
            print("cacert.pem downloaded successfully.")
        except Exception as e:
            print(f"Failed to download cacert.pem: {e}")
            return

    if not os.path.exists("dist"):
        os.makedirs("dist")

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
