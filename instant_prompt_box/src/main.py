from typing import Dict, List, Optional

from instant_prompt_box.prompts.zoltraak.zoltraak import Zoltraak
from instant_prompt_box.src.utils.file_util import FileUtil


class _InstantPromptBox:
    def __init__(self):
        self._zoltraak = Zoltraak()

    @property
    def zoltraak(self):
        return self._zoltraak


# For comvinience, we create an instance of the class.
InstantPromptBox = _InstantPromptBox()

if __name__ == "__main__":
    prompt = InstantPromptBox.zoltraak.zoltraak_prompt_fix_code(
        code="test_code", error_message="test_error_message"
    )
    print("prompt:", prompt)
