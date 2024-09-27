import msvcrt
import random
import sys
import time

# \b (\x10) - backspace
# \t (\x09) - tab
# \n (\x0A) - new line
# \r (\x0D) - carriage return

ESC = "\x1b"
CSI = ESC + "["  # control sequence introducer
RESET = CSI + "0m"

colors = [
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
    "default",
]


def p(s: str) -> None:
    print(s + RESET, end="", flush=True)


def loading(progress: int) -> None:
    width = progress // 4
    dots = ("." * width).ljust(25, " ")  # ...
    p(f"{CSI}2K{CSI}1GProgress{dots} [{progress}%]")


def main() -> None:
    # p("hello")
    # p(f"{CSI}1mhello")  # 1m - bold mode
    # p(f"{CSI}2mhello")  # 2m - faint mode
    # p(f"{CSI}3mhello")  # 3m - italic mode
    # p(f"{CSI}4mhello")  # 4m - underline mode
    # p(f"{CSI}5mhello")  # 5m - blinking mode (slow)
    # p(f"{CSI}6mhello")  # 6m - blinking mode (rapid)
    # p(f"{CSI}7mhello")  # 7m - inverse mode
    # p(f"{CSI}8mhello")  # 8m - hidden mode
    # p(f"{CSI}9mhello")  # 9m - strikethrough modes
    # p(f"{CSI}21mhello")  # 21m - doubly underlined mode

    # foreground
    # for i, color in enumerate(colors):
    #     p(f"{CSI}{30+i}m{color}")
    # print()
    # # bright colors
    # for i, color in enumerate(colors):
    #     p(f"{CSI}{30+i};1m{color}")
    # print()
    p(f"{CSI}4m{CSI}38;5;82mawesometext\n")
    # # background
    # for i, color in enumerate(colors):
    #     p(f"{CSI}{40+i}m{color}")
    # print()
    # # bright colors
    # for i, color in enumerate(colors):
    #     p(f"{CSI}{40+i};1m{color}")

    # for i in range(255):
    #     if i % 16 == 0:
    #         print()
    #     n = str(i).rjust(4, " ")
    #     p(f"{CSI}38;5;{i}m{n}")
    # print()
    # for i in range(255):
    #     if i % 16 == 0:
    #         print()
    #     n = str(i).rjust(4, " ")
    #     p(f"{CSI}48;5;{i}m{n}")

    # print()
    # fr, fg, fb = 255, 0, 0
    # p(f"{CSI}38;2;{fr};{fg};{fb}mhello")
    # print()
    # br, bg, bb = 0, 255, 0
    # p(f"{CSI}48;2;{br};{bg};{bb}mhello")

    # <n><direction>
    # A - up
    # B - down
    # C - right
    # D - left

    # **
    # **
    # **
    # **
    # **

    # for _ in range(5):
    #     p("\n")
    # p(f"{CSI}5A")
    # for x in range(40):
    #     for y in range(5):
    #         char = "*"
    #         p(f"{char}{CSI}1D{CSI}1B")
    #         time.sleep(0.1)
    #     p(f"{CSI}5A{CSI}1C")
    # p(f"{CSI}4B")

    # for i in range(0, 101):
    #     loading(i)
    #     time.sleep(random.uniform(0.05, 0.03))
    # p(f"{CSI}2K{CSI}1G \u2714\ufe0f  {CSI}38;5;46mThe installation is complete.")

    # x, y = 0, 0
    # p(f"{CSI}?25l")
    # text = [f"hello world {i}" for i in range(5)]
    # mode = "NORMAL"
    # for line in text:
    #     p(f"{line}\n")
    # p(f"{mode}\n")
    # p(f"{CSI}6A")

    # while True:
    #     # LINUX: import tty; tty.setraw(sys.stdin); char = sys.stdin.read(1)
    #     char_code = int.from_bytes(msvcrt.getch())
    #     if char_code == 3:  # Ctrl + c
    #         p(f"{CSI}5B{CSI}?25h")
    #         break
    #     if mode == "NORMAL":
    #         if char_code == 108:  # l
    #             x = min(x + 1, len(text[y]) - 1)
    #         elif char_code == 104:  # h
    #             x = max(0, x - 1)
    #         elif char_code == 107:  # k
    #             y = max(0, y - 1)
    #             x = min(x, len(text[y]) - 1)
    #         elif char_code == 106:  # j
    #             y = min(y + 1, len(text) - 1)
    #             x = min(x, len(text[y]) - 1)
    #         elif char_code == 105:
    #             mode = "INSERT"
    #     elif mode == "INSERT":
    #         if char_code == 27:
    #             mode = "NORMAL"
    #         else:
    #             line = text[y]
    #             new_line = line[:x] + chr(char_code) + line[x:]
    #             text[y] = new_line
    #             x += 1
    #     for idx, line in enumerate(text):
    #         if idx == y:
    #             visual_line = (
    #                 line[:x] + f"{CSI}7m" + line[x] + f"{CSI}0m" + line[x + 1 :]
    #             )
    #             p(f"{CSI}2K{CSI}1G{visual_line}\n")
    #         else:
    #             p(f"{CSI}2K{CSI}1G{line}\n")
    #     p(f"{CSI}2k{CSI}1G{mode}\n")
    #     p(f"{CSI}6A")


if __name__ == "__main__":
    main()
