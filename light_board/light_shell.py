def light_shell(text):
    command = f"sudo ./rpi-rgb-led-matrix/examples-api-use/scrolling-text-example --led-no-hardware-pulse --led-rows=16 --led-cols=32 -s 4 -f ./rpi-rgb-led-matrix/fonts/helvR12.bdf -C 102,179,22 {text}"
    completed = subprocess.run(command) # commandがコマンド、argumentが引数。必要なだけ並べる。

light_shell('Hello World')