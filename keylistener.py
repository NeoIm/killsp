from pynput import keyboard

from killsp import Kill

class KeyListener:

    # 定义三个标志位
    def __init__(self):
        self.flag_alt = False
        self.flag_ctrl = False
        self.flag_start = False

        self.killsp = Kill()

    # 当某一个键被按下时触发
    def on_press(self, key):
        try:
            # alt被按下时改变标志位
            if key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
                self.flag_alt = True
                print(key, '  pressed')

            # ctrl被按下时改变标志位
            if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                self.flag_ctrl = True
                print(key, '  pressed')

            # 确定alt + ctrl + c 被按下时触发动作
            # 在这里处理剪贴板的内容
            if key.char == 'c' and self.flag_alt and self.flag_ctrl:
                self.flag_start = True
                self.flag_alt = False
                self.flag_ctrl = False
                print(key, '  pressed')
                print('==== kill sp ====')
                self.killsp.kill_sp()

        # 没被处理的其他功能键按下时触发
        except AttributeError:
            print(key, "other functional pressed")

    def start(self):
        # 开始进程
        with keyboard.Listener(
                on_press=self.on_press) as listener:
            listener.join()


if __name__ == "__main__":
    keyListener = KeyListener()
    keyListener.start()
