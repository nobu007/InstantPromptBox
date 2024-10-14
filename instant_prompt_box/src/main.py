from instant_prompt_box.prompts.zoltraak.zoltraak import Zoltraak


class _InstantPromptBox:
    def __init__(self):
        self._zoltraak = Zoltraak()

    @property
    def zoltraak(self)->Zoltraak:
        return self._zoltraak


if __name__ == "__main__":
    box = _InstantPromptBox()
    prompt = box.zoltraak.zoltraak_prompt_fix_code(code="", error_message="")
    print("prompt:", prompt)
