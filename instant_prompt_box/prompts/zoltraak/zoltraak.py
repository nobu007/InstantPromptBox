import os

from instant_prompt_box.src.utils.file_util import FileUtil

ZOLTRAAK_PPROMPT_DIR = os.path.abspath(os.path.dirname(__file__))


class Zoltraak:
    def zoltraak_prompt_fix_code(self, code: str, error_message: str) -> str:
        prompt_file_path = os.path.join(ZOLTRAAK_PPROMPT_DIR, "zoltraak_prompt_fix_code.md")
        prompt = FileUtil.read_file(prompt_file_path)
        return prompt.format(code=code, error_message=error_message)

    def zoltraak_prompt_fix_code_smart(self, code: str, error_message: str, error_reason: str) -> str:
        prompt_file_path = os.path.join(ZOLTRAAK_PPROMPT_DIR, "zoltraak_prompt_fix_code_smart.md")
        prompt = FileUtil.read_file(prompt_file_path)
        return prompt.format(code=code, error_message=error_message, error_reason=error_reason)
